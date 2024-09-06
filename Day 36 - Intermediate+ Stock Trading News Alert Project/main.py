import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_THRESHOLD = 5  # Define your threshold for percentage change


def stock_price():
    alphavantage_url = "https://www.alphavantage.co/query"
    api_key = os.getenv("APIKEY")

    if not api_key:
        raise ValueError("APIKEY not set in environment variables.")

    alphavantage_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": api_key
    }

    try:
        alphavantage_response = requests.get(alphavantage_url, params=alphavantage_params).json()
        last_refreshed = alphavantage_response["Meta Data"]["3. Last Refreshed"]
        time_series = alphavantage_response["Time Series (Daily)"][last_refreshed]
        difference = float(time_series["4. close"]) - float(time_series["1. open"])
        percentage_change = (difference * 100) / float(time_series["1. open"])

        return percentage_change

    except KeyError:
        print("Error: Unexpected response from Alpha Vantage.")
        return None
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None


def fetch_news(company_name):
    url = "https://newsapi.org/v2/top-headlines"
    news_api_key = os.getenv("NEWSAPI")

    if not news_api_key:
        raise ValueError("NEWSAPI not set in environment variables.")

    params = {
        "q": company_name,
        "apiKey": news_api_key,
        "pageSize": 5  # Limit the number of articles fetched
    }

    try:
        response = requests.get(url, params=params).json()
        return response.get("articles", [])
    except Exception as e:
        print(f"Error fetching news data: {e}")
        return []


def send_whatsapp_message(msg):
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    to_number = os.getenv("TO")

    if not all([account_sid, auth_token, to_number]):
        raise ValueError("Twilio credentials not set in environment variables.")

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=msg,
            to=f'whatsapp:+{to_number}'
        )
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")


def main():
    price_change = stock_price()

    if price_change is None:
        return  # Stop execution if there's an issue with fetching stock data

    if abs(price_change) >= PERCENTAGE_THRESHOLD:
        articles = fetch_news(COMPANY_NAME)

        for article in articles:
            if article.get("title") != "[Removed]":
                msg = (f"{STOCK}: {'🔻' if price_change < 0 else '🔺'}{abs(round(price_change, 2))}%\n\n"
                       f"Headline: {article.get('title', 'No title')}\n\n"
                       f"Brief: {article.get('description', 'No description')}\n\n"
                       f"URL: {article.get('url', 'No URL')}\n"
                       f"Published At: {article.get('publishedAt', 'No date')}")

                send_whatsapp_message(msg)


if __name__ == "__main__":
    main()
