import json
import os
from pathlib import Path
from typing import Dict, Optional, Union

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential


class AIDungeonMaster:
    """
    Class to manage the AI Dungeon Master.
    """

    def __init__(
        self, system_prompt: Union[str, Path], model_kwargs: Optional[Dict] = None
    ) -> None:
        self._client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model_name = "gpt-4"

        # set up prompt
        if isinstance(system_prompt, Path):
            with open(system_prompt, "r") as fh:
                system_prompt = fh.read()

        self.message_history = [
            {"role": "system", "content": system_prompt},
        ]

        # model parameters
        self.model_kwargs = model_kwargs or dict(
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=0.2,
        )

    def format_user_message(self, message: str) -> str:
        return f"```{message}```"

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def query_model(self, message: str) -> str:
        """
        Query the model with a user message and return the AI's response.
        """
        formatted_message = self.format_user_message(message)
        self.message_history.append({"role": "user", "content": formatted_message})
        response = self._client.chat.completions.create(
            model=self.model_name,
            messages=self.message_history,
            **self.model_kwargs,
        )
        ai_message = response.choices[0].message.content

        if ai_message is None:
            raise ValueError("AI response is None")

        self.message_history.append({"role": "assistant", "content": ai_message})
        return ai_message

    def save_message_history(
        self, save_file: Union[Path, str] = "message_history.json"
    ) -> None:
        """
        Save the message history as JSON.
        """
        # TODO: currently only safe to save the message history in the save_files directory
        save_dir = Path("save_files/")
        save_path = save_dir / save_file
        with open(save_path, "w") as fh:
            json.dump(self.message_history, fh)

    @classmethod
    def construct_from_history(
        cls,
        history_path: Union[str, Path] = "save_files/message_history.json",
        **kwargs,
    ) -> "AIDungeonMaster":
        if isinstance(history_path, str):
            history_path = Path(history_path)

        with open(history_path, "r") as fh:
            message_history = json.load(fh)

        system_prompt = message_history[0]["content"]

        instance = cls(system_prompt=system_prompt, **kwargs)
        instance.message_history = message_history
        return instance
