from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BASE_URL = "https://dummyjson.com/products/category"
USD_TO_INR = 83


# INTENT MAP
def get_category(user_input):
    user_input = user_input.lower()

    if any(x in user_input for x in ["phone", "mobile", "smartphone"]):
        return "smartphones"

    if any(x in user_input for x in ["laptop", "computer", "pc"]):
        return "laptops"

    if any(x in user_input for x in ["headphone", "earphone", "headset"]):
        return "headphones"

    if any(x in user_input for x in ["ram", "memory"]):
        return "laptops"

    if any(x in user_input for x in ["drive", "ssd", "storage"]):
        return "laptops"

    if any(x in user_input for x in ["perfume", "fragrance"]):
        return "fragrances"

    if any(x in user_input for x in ["shirt", "tshirt", "pant"]):
        return "mens-shirts"

    return None


# FETCH PRODUCTS 
def get_products(category, budget=None):
    try:
        url = f"{BASE_URL}/{category}"
        response = requests.get(url)

        if response.status_code != 200:
            return []

        data = response.json()
        products = data.get("products", [])

        results = []

        for p in products:

            # PRICE CONVERT
            price_inr = int(p.get("price", 0) * USD_TO_INR)

            # BUDGET FILTER (MAIN FIX)
            if budget is not None and price_inr > budget:
                continue

            # SAFE IMAGE HANDLING
            image = (
                p.get("thumbnail")
                or (p.get("images")[0] if p.get("images") else None)
                or "https://via.placeholder.com/300"
            )

            results.append({
                "title": p.get("title", "No Title"),
                "price_inr": price_inr,
                "rating": p.get("rating", 0),
                "image": image,
                "description": p.get("description", "No description")
            })

        # SORT BY RATING (BEST FIRST)
        results = sorted(results, key=lambda x: x["rating"], reverse=True)

        return results

    except Exception as e:
        print("Error:", e)
        return []


# ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    top_product = None

    if request.method == "POST":
        user_input = request.form.get("query", "")
        budget = request.form.get("budget", "")

        # convert budget safely
        budget = int(budget) if budget and budget.isdigit() else None

        category = get_category(user_input)

        if category:
            results = get_products(category, budget)  # IMPORTANT FIX
        else:
            results = []

        if results:
            top_product = results[0]

    return render_template("index.html", results=results, top_product=top_product)


if __name__ == "__main__":
    app.run(debug=True)
