## AI-Product-Suggester

AI Product Recommendation System (Flask Web App)  An intelligent AI-powered product recommendation web application built using Python Flask. This project fetches real-time product data from an API and uses smart filtering, category detection, and budget-based recommendations to display the most relevant products to users.

## Tech Stack

Python (Flask)
HTML, CSS, JavaScript
DummyJSON API (for product data)
Jinja2 templating

## How It Works

1.User enters a product query (e.g., “phone”, “laptop”)
2.System detects intent and maps it to correct category
3.API fetches relevant products
4.Results are filtered by budget and sorted by rating
5.Clean UI displays product cards with images, price, and rating

## Challenges & Solutions
Building a web-based recommendation engine introduced new complexities, particularly in handling external data and ensuring a smooth user experience.

1. Mapping User Intent to API Categories

The Problem: The API requires specific category slugs (e.g., smartphones), but users might type "mobile" or "phone." A direct search often returned zero results if the keywords didn't match the API's strict taxonomy.

The Solution: I implemented a Keyword Mapping Layer. I created a dictionary that maps common user aliases to official API categories. If a user types "cellphone," the system automatically translates it to smartphones before making the fetch request.

2. Handling API Latency and Failures
   
The Problem: Depending on network speed or API downtime, the app would sometimes hang or crash with a 500 Internal Server Error if the external data didn't load.

The Solution: I added Robust Exception Handling and Loading States.
Used try-except blocks around the requests call to catch connection timeouts.
Implemented a fallback mechanism where the UI displays a "Service Temporarily Unavailable" message instead of a broken page.

3. Dynamic Data Filtering (Budget & Ratings)

The Problem: The API returns a large JSON object with various products, but not all fit the user's budget. Filtering this data efficiently in the backend without slowing down the response time was a challenge.

The Solution: I utilized Python's List Comprehensions for high-speed filtering.
Once the data is fetched, the system instantly parses the list to keep only items where price <= user_budget.
I then used the sorted() function with a lambda key to prioritize the highest-rated products first, ensuring the "AI" feels like it's picking the best options.

4. UI/UX: Handling Broken Product Images

The Problem: External APIs sometimes provide image URLs that are broken or slow to load, leading to "empty" product cards in the UI.

The Solution: I used a JavaScript fallback listener. I added an onerror attribute to the HTML <img> tags that automatically replaces a broken image with a local "placeholder" image, maintaining the professional look of the dashboard.

