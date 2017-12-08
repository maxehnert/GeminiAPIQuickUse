# Gemini API Quick Use

I made this so I could easily make trades on Gemini without having to lookup their API calls in the moment.

During high volume swings it's common for exchanges UI to go down but typically their API is still active and will still accept POST requests so interacting through the API is the only method.

I have not tested during an outage so don't blame me if this doesn't work or you lose everything :)

This package only supports buying/selling with existing balances. I do not see a way to deposit or withdrawal from Gemini via the API.

## How To Use

Create an `apiKeys.py` file and past your 2 API keys in there
Depending on whether you're using this for testing or live will determine which API keys and which endpoint you want to use.

For Buy/Sell orders I have variables to enter the amounts into. I wanted to make it very clear and hard to mess up because of the consequences that can come with making btc transactions.

Gemini docs [https://docs.gemini.com/](https://docs.gemini.com/)

Pull Requests Welcome!