import json
from copy import deepcopy
from pathlib import Path

from llama_index.core import ChatPromptTemplate
from llama_index.core.base.llms.types import TextBlock
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential


class AIDungeonMaster:
    """
    Class to manage the AI Dungeon Master.
    """

    def __init__(self, system_prompt: Path | None = None, chat_history: ChatPromptTemplate | None = None):
        self.llm_client = OpenAI()

        self.user_message_template = ChatMessage("```{user_message}```", role=MessageRole.USER)

        if system_prompt is not None:
            # set up prompt
            with open(system_prompt, "r") as fh:
                system_prompt_text = fh.read()

            message_templates = [
                ChatMessage(content=system_prompt_text, role=MessageRole.SYSTEM),
                self.user_message_template,
            ]

            self.chat_template = ChatPromptTemplate(message_templates=message_templates)

        elif chat_history is not None:
            self.chat_template = chat_history

        else:
            raise ValueError("Either a system prompt or chat history must be provided.")

    def format_user_message(self, message: str) -> list[ChatMessage]:
        """
        Format a user message to be consumed by LLM.

        Args:
            message (str): The user message.

        Returns:
            list[ChatMessage]: The formatted list of messages.
        """
        return self.chat_template.format_messages(user_message=message)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def query_model(self, message: str) -> str:
        """
        Query the model with a user message and return the AI's response.
        """
        formatted_messages = self.format_user_message(message)

        chat_response = self.llm_client.chat(messages=formatted_messages)
        chat_resp_message = chat_response.message

        # get the response text for return
        text_blocks = [block for block in chat_resp_message.blocks if isinstance(block, TextBlock)]
        chat_resp_text = text_blocks[0].text

        # cycle the chat template to prepare for the next message
        formatted_messages.append(chat_resp_message)

        message_templates = deepcopy(formatted_messages)
        message_templates.append(self.user_message_template)

        self.chat_template = ChatPromptTemplate(message_templates=message_templates)

        return chat_resp_text

    def save_message_history(self, save_file: Path):
        """
        Save the message history to a file.

        Args:
            save_file (Path): A `.json` filepath.
        """

        json_chat_messages = [cm.model_dump_json() for cm in self.chat_template.message_templates]

        with open(save_file, "w") as fh:
            json.dump(json_chat_messages, fh)

    @classmethod
    def construct_from_history(cls, history_path: Path) -> "AIDungeonMaster":
        """
        Construct an AIDungeonMaster instance from a message history file.
        """
        with open(history_path, "r") as fh:
            json_chat_messages = json.load(fh)

        chat_template = ChatPromptTemplate.from_messages(
            [ChatMessage.model_validate_json(cm) for cm in json_chat_messages]
        )

        return cls(chat_history=chat_template)
