# ChatGPT-Discord-Bot

## Functionality
The discord bot is powered by the openAI API. It queries user input a

## How I Built It
The major component to getting information about existing mental health resources was to scrape websites (Beautiful Soup) that provided such information. We used Python to construct an algorithm to scrape data from websites and store it in our database. The data is fed into our NLP (Natural Language Processing) algorithm to train the chatbot AI to generate responses to specific queries. The AI involves sophisticated NLP techniques to parse through an user input query and take note of keywords for semantic similarity analysis. After training and empirically tuning the AI, we linked the frontend (our website) to the backend (Python scripts) using a server hosted on Flask.

## Running the Code

### requirements.txt file
We currently only pull data from 3 university websites, UofT, Ontario Tech and McMaster. To scrape each site, run each of their respective scrapers under the `scraper` folder. They should then spit the contents of each site into a file under `data`.

### .env file
Make sure there is a `.env` file present in the root directory with a valid `cohere-token` so the API calls will work.

### Using the openAI API
Under the root directory, run `python nlp.py -embed` to convert all the description into embedings. This will modify the files in the `data` folder.

### Running the code

## Examples
![image](https://user-images.githubusercontent.com/74229658/222205182-306372f1-25ae-4b0c-8b1a-03ae1ceba2bc.png = 250 x 250)

