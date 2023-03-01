# ChatGPT-Discord-Bot

## Functionality
The discord bot is powered by the openAI API. It queries user input as ChatGPT would and produces an output

## Running the Code

### requirements.txt file
Contains all the libraries needed to build the bot. To install all the libraries in the file, run `pip install -r requirements.txt`. If not already insalled, you will also have to include `requests = *version*` or alternatively, you need to run the command `pip install requests`

### .env file
Make sure there is a `.env` file present in the root directory. The file should cointain the Discord bot token and the OpenAI API token. The file should simply contain:
```
DISCORD_BOT_TOKEN = *discord bot token*
API_KEY = *OpenAI API key*
```

Note: This file is not included in the repository

### Using the OpenAI API
The documentation provided by OpenAI is very useful and straightforward to follow. Find the documentation [here](https://platform.openai.com/docs/api-reference?lang=python)

### Running the code
Execute and run `run.py` and the bot will show an online status on Discord.

## Examples
![image](https://user-images.githubusercontent.com/74229658/222205182-306372f1-25ae-4b0c-8b1a-03ae1ceba2bc.png)

