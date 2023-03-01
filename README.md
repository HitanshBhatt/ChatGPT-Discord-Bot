# ChatGPT-Discord-Bot

## Functionality
The discord bot is powered by the openAI API. It queries user input as ChatGPT would and produces an output

## Running the Code

### requirements.txt file
Contains all the libraries needed to build the bot. To install all the libraries in the file, run `pip install -r requirements.txt`. If not already insalled, you will also have to include `requests = version` or alternatively, you need to run the command `pip install requests`

### .env file
Make sure there is a `.env` file present in the root directory with a valid `cohere-token` so the API calls will work.

### Using the openAI API
Under the root directory, run `python nlp.py -embed` to convert all the description into embedings. This will modify the files in the `data` folder.

### Running the code

## Examples
![image](https://user-images.githubusercontent.com/74229658/222205182-306372f1-25ae-4b0c-8b1a-03ae1ceba2bc.png)

