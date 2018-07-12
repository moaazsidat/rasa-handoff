# Starter Pack for Rasa Stack

This starter pack helps you build a bot faster with [Rasa Stack](http://rasa.com/products/rasa-stack/). Apart from a basic file and folder structure, it gives you some initial training data. Clone this repo and start building your bot.

For more information on the Rasa Stack, please visit the docs here:
- [Rasa Core](https://core.rasa.com/)
- [Rasa NLU](https://nlu.rasa.com/)

## Setup

To install the necessary requirements, run:

```
pip install -r requirements.txt
```

## Usage

To train the NLU model, run ``make train-nlu``

To train the Core model, run ``make train-core``

To run the bot on the command line run ``make cmdline``

## What now?

To continue developing your bot, you can start by adding some NLU data for intents/entities relevant to your use case. These then need to be added to your domain file. From there you can add more utterances for the bot, or custom actions you've written in `actions.py` and then write stories using these. 
