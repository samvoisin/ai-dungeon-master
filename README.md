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
The AI-DM is built on top of OpenAI's chat interface to the powerful [GPT-4](https://openai.com/gpt-4) LLM. Players can then interact with the LLM chatbot through text in a channel on their discord server. When players input their actions, AI-DM interprets these actions and responds appropriately within the scope of the rules and the current adventure. Whether it's describing a new scene, managing combat, or engaging in dialogue with NPCs, the AI-DM handles it all.

## Limitations
This project is at an early state of it's development. It works as intended (and is a ton of fun!), but it currently has some limitations:
* You must have your own OpenAI API token. You can create an API account and get an API key by following the directions in OpenAI's [API documentation](https://openai.com/product).
* You must have your own discord API token and invite a bot to your discord server. You can do that by following the directions on [discord's developer documentation](https://discord.com/developers/docs/intro). The relevant channel in you discord server should be titled `aidm`.

## Getting Started
1. You need to add two environment variables to your system: `AI_DM_BOT_KEY` is the discord API key. `OPENAI_API_KEY` is the OpenAI API key.
2. Install the Bot: Add AI-DM bot to your Discord server.
3. Set Up Your Game: Choose your TTRPG system and establish basic game settings. Currently there is a file in the `prompts` directory titled `aidm-system-prompt.txt`. You can modify this file to fit the rules you want. The default rule system is the fifth edition of D&D.
4. Initialize AI-DM through the CLI with `aidm run`. The CLI assumes you are working from the root directory of this repository.
5. Invite Your Friends: Bring your party together in your Discord server.
6. Start Playing: Begin your adventure with the AI-DM guiding your journey. Just describe your characters in the discord channel and the type of adventure you want to have.

If you are having trouble getting things to work please don't hesitate to reach out. I'll do everything I can to get your party adventuring!

## Contribution
This is a labor of love. I'm currently working on this project in my spare time because I think it is a lot of fun. If you would like to contribute to this project I would greatly appreciate it! Just submit a PR, and we will work together to make AI-DM everything it can be.
