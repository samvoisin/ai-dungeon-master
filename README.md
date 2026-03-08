# AI Dungeon Master

This project implements an AI-powered game master that you and your party can interact with through discord.

## The Problem
In order to play most tabletop role-playing games ("TTRPGs"), someone has to take on the role of Game Master. This means that one of your friends doesn't get to experience the world as a player character ("PC"). Some groups have a member who wants to act as game master, but there are a lot of groups where everyone prefers to take on the role of a PC. In those cases, someone has to compromise for everyone else to enjoy the game.

## A Solution
With the advent of widely available generative AI systems and specifically large language models ("LLMs"), it's now possible to use high quality text generation models that can take on the role of Game Master in TTRPGs. AI-DM uses state-of-the-art LLMs to create immersive storylines, manage game mechanics, and interact with players.

## Key Features
* Dynamic Storytelling: Generates and adapts storylines on-the-fly based on PC actions, so every session is as unique as your party.
* NPC Interaction: Characters in the game world are brought to life with realistic and varied dialogues, making each interaction feel genuine.
* Rules Management: Understands and applies the rules for many TTRPG systems.
* Discord Integration: Integrates with Discord, allowing players to interact with the AI-DM through a familiar interface.

## How It Works
The AI-DM is built on top of OpenAI's chat interface to [GPT-4](https://openai.com/gpt-4) and the suite of LLM tools provided by [LlamaIndex](https://docs.llamaindex.ai/en/stable/). Players can then interact with the LLM chatbot through text in a channel on their discord server. When players input their actions, AI-DM interprets these actions and responds appropriately within the scope of the rules and the current adventure. Whether it's describing a new scene, managing combat, or engaging in dialogue with NPCs, the AI-DM handles it all.

## Limitations
This project is at an early state of it's development. It works as intended (and is a ton of fun!), but it currently has some limitations:
* You must have your own OpenAI API token. You can create an API account and get an API key by following the directions in OpenAI's [API documentation](https://openai.com/product).
* You must have your own discord API token and invite a bot to your discord server. You can do that by following the directions on [discord's developer documentation](https://discord.com/developers/docs/intro). The relevant channel in you discord server should be titled `aidm`.

## Getting Started

### Prerequisites

Before setting up AI-DM, make sure you have the following:

- **Python 3.12 or higher** — [Download Python](https://www.python.org/downloads/)
- **git** — [Download git](https://git-scm.com/downloads)
- **uv** (Python package manager) — Install with `pip install uv` or see the [uv documentation](https://github.com/astral-sh/uv)
- **An OpenAI account** with API access — [Sign up at OpenAI](https://platform.openai.com/signup)
- **A Discord account** with permission to create a bot and add it to a server — [Discord](https://discord.com)

---

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/samvoisin/ai-dungeon-master.git
cd ai-dungeon-master
```

---

### Step 2: Set Up the Python Environment

Use the provided `Makefile` target to create a virtual environment and install all dependencies:

```bash
make init
```

This will:
1. Create a virtual environment using `uv venv`
2. Install all required packages from `requirements/requirements.txt` and `requirements/requirements-dev.txt`
3. Install the `aidm` CLI tool in editable mode

> **Note:** All subsequent commands assume you are running from the root directory of this repository with the virtual environment activated (e.g., `source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\activate` in Windows Command Prompt, or `.\.venv\Scripts\Activate.ps1` in Windows PowerShell).

---

### Step 3: Obtain an OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/) and sign in or create an account.
2. Navigate to **API Keys** in your account settings.
3. Click **Create new secret key**, give it a name, and copy the key — you won't be able to view it again.

---

### Step 4: Create a Discord Bot and Obtain Its Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in.
2. Click **New Application**, give it a name (e.g., "AI Dungeon Master"), and click **Create**.
3. In the left sidebar, select **Bot**, then click **Add Bot** and confirm.
4. Under the **Token** section, click **Reset Token**, confirm, and copy the bot token — store it somewhere safe.
5. Scroll down to **Privileged Gateway Intents** and enable **Message Content Intent**.
6. In the left sidebar, select **OAuth2 → URL Generator**.
   - Under **Scopes**, check `bot`.
   - Under **Bot Permissions**, check at minimum: `Read Messages/View Channels`, `Send Messages`, and `Read Message History`.
7. Copy the generated URL, paste it into your browser, and follow the prompts to invite the bot to your Discord server.

> **Note:** The bot reads from and writes to a Discord channel named **`aidm`**. Create a channel with exactly this name in your server before starting the bot.

---

### Step 5: Set the Required Environment Variables

AI-DM requires two environment variables to be set:

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key from Step 3 |
| `AI_DM_BOT_KEY` | Your Discord bot token from Step 4 |

**On macOS/Linux**, add these to your shell profile (e.g., `~/.bashrc` or `~/.zshrc`) or export them for the current session:

```bash
export OPENAI_API_KEY="your-openai-api-key-here"
export AI_DM_BOT_KEY="your-discord-bot-token-here"
```

**On Windows (Command Prompt):**

```cmd
set OPENAI_API_KEY=your-openai-api-key-here
set AI_DM_BOT_KEY=your-discord-bot-token-here
```

**On Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY = "your-openai-api-key-here"
$env:AI_DM_BOT_KEY = "your-discord-bot-token-here"
```

---

### Step 6: (Optional) Customize the System Prompt

The system prompt defines the rules and persona of your AI Dungeon Master. The default prompt uses **D&D 5th Edition** rules.

To customize:

1. Open `prompts/aidm-system-prompt.txt` in a text editor.
2. Modify the contents to describe the ruleset, setting, or style you want for your campaign.
3. Save the file.

You can also point the bot to a different prompt file at startup using the `--system-prompt-path` option (see Step 7).

---

### Step 7: Start the AI Dungeon Master Bot

From the root of the repository, run:

```bash
aidm run
```

To use a custom system prompt file:

```bash
aidm run --system-prompt-path /path/to/your-prompt.txt
```

The bot will connect to Discord and begin listening in the `aidm` channel of your server.

---

### Step 8: Invite Your Friends and Start Playing

1. Make sure all players have access to the `aidm` channel in your Discord server.
2. In the `aidm` channel, introduce your characters and describe the type of adventure you want to have.
3. The AI-DM will guide your party through the story — enjoy your adventure!

---

If you are having trouble getting things to work please don't hesitate to reach out. I'll do everything I can to get your party adventuring!

## Contribution
This is a labor of love. I'm currently working on this project in my spare time because I think it is a lot of fun. If you would like to contribute to this project I would greatly appreciate it! Just submit a PR, and we will work together to make AI-DM everything it can be.
