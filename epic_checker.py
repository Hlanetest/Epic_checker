from bs4 import BeautifulSoup
import requests
import re
import time
import yaml
import random

# Function to extract stock details from webpage text
def get_stock_details(webpage_text):
    paragraphsplit = re.split("(?<=[.!?]) +", webpage_text)
    paragraphsplit = [p.replace(',', '\n') for p in paragraphsplit]

    stock_details = {}  # Dictionary to store extracted data
    for line in paragraphsplit:
        if 'Total In Stock' in line:
            stockline1 = re.findall(r'\d+', line)
            # Create formatted date string
            whdate = stockline1[0][0] + stockline1[0][-1] + '-' + stockline1[1] + '-' + stockline1[2]
            whdate = ('    ETA: ' + whdate)
            merged_string1 = stockline1[0][0:-1]
            if len(merged_string1) == 7:
                backorder = merged_string1[:4]
                totalincoming = merged_string1[3:]
                infoline1 = ('    Back Ordered Amount: ' + backorder[-3:])
                infoline2 = ('    Total Incoming: ' + totalincoming[-3:])

                stock_details = {
                    "whdate": whdate,
                    "infoline1": infoline1,
                    "infoline2": infoline2,
                    "stockline1": stockline1
                }
                break

    return stock_details

# Load data from YAML file
with open("shoplist.yml", "r") as file:
    data = yaml.safe_load(file)

# Create a session and set User-Agent header
web_session = requests.Session()
web_session.headers.update({"User-Agent": "Mozilla/5.0 ... "})

while True:
    for url_list in data["url"]:
        if "link" in url_list:
            url = url_list["link"]
            webhook_url = $DISCORDURLHERE  # Replace with your Discord webhook URL

            # Send GET request to the URL and parse HTML
            response = web_session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            stock_details = get_stock_details(soup.text)

            if stock_details:
                print('Stock Availability Details - ', url_list["name"])
                print(stock_details["whdate"])
                print(stock_details["infoline1"])
                print(stock_details["infoline2"])
                print('-----Stock Line Raw:' + str(stock_details["stockline1"]))

                # Prepare payload for Discord webhook
                payload = {
                    "content": f"\n{url_list['name']}\nStock Availability Details\n{stock_details['whdate']}\n{stock_details['infoline1']}\n{stock_details['infoline2']}\n-----Stock Line Raw: {stock_details['stockline1']}"
                }
                headers = {
                    "Content-Type": "application/json"
                }

                # Send POST request to Discord webhook
                response = requests.post(webhook_url, json=payload)

                if response.status_code != 204:
                    print(f"Failed to post to Discord with error code {response.status_code}")

    # Sleep for a random time between 30 minutes to an hour
    sleep_time = random.randint(30 * 60, 60 * 60)
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)  # Sleep for the specified time
