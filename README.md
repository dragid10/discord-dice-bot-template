
# Discord Dice Bot Template

A template for creating a discord bot that can roll dice.


## Tech Stack

**Server:** Python 3.12+

**Libraries:**
- `Py-cord`: The library used to interact with the discord API 

- `python-dotenv`: Library used to load environment variables from a `.env` file  

- `Mypy`: Static type checker for python  

- `ruff`: Library used to lint the codebase


## Environment Variables

To run this project you will need to:
1. Copy the `.env-sample` file and rename it to `.env`
1. Populate the following environment variable to your `.env` file
---
`DISCORD_TOKEN`: The token of your discord bot. This can be found in the [discord developer portal](https://discord.com/developers/applications) in the bot section of your application.

---

## Run Locally

1. Create a new repository from this template, using the button in the top-right corner

1. Clone your new project

    ```bash
      git clone https://github.com/<YOUR_USERNAME>/discord-dice-bot-template
    ```
1. Go to the project directory

    ```bash
      cd discord-dice-bot-template
    ```

1. Install dependencies

    ```bash
      pip install -r requirements.txt
    ```

1. Run the bot

    ```bash
      python main.py
    ```