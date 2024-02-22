# Stackshop

## Introduction
#### StackShop is an e-commerce platform designed to offer a personalized shopping experience. Leveraging the secure data handling capabilities of Affinidi Vault, we ensure that user preferences and sensitive information are managed with the utmost care.

## Setup for Developers
### 1. For developers who wish to test the application locally, here are the prerequisites and steps to get started.

- Visit [Affinidi Portal](portal.affinidi.com) and login, Once done go to Services -> Affinidi Login.
- Create a New Configuration with the name you like and in Allowed Redirect URIs enter `localhost:5000` in-case you are running it locally, Once done Copy CLIENT_ID and CLIENT_SECRET somewhere safe as they will be only shown once, Finally Copy the ISSUER.
- Now click on Presentation Definition and Paste the `pex.json` Code over there, In the Next Step Click on Re-generate from Presentation Definition.
- Click on Save -> Scroll down to the bottom and click Save again.

### 2. Fork and Clone the Repository
Begin by forking the StackShop repository into your GitHub account:

- Click on the "Fork" button at the top right.
- Once forked, clone your repository to your local machine using:
```bash
git clone https://github.com/YOUR-USERNAME/stackshop.git
cd stackshop
```

### 3. Initialize the Flask Application
After cloning the repo, set up your Python environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Setup Environment Variables

- Depending Upon your System add PROVIDER_CLIENT_ID, PROVIDER_CLIENT_SECRET, PROVIDER_ISSUER, FLASK_SECRET as .env Variables.

### 5. Run the Application using:

```bash
flask --debug run
```

## Features
### Product Recommendation
The product recommendation feature is a way to personalize the shopping experience by suggesting items that align with the user's gender and demographics.

How it Works in Code:
User Demographics: I retrieved the user's country and gender from the session data in Flask. This data is typically obtained during the login process and stored securely in the session (app.py).
```python
user_info = {
    ...
    'country': user_data['custom'][3]['country'],
    'gender': user_data['custom'][21]['gender'],
}
```

- Recommendations by Country: If the user is from India, we display traditional products by manipulating the DOM elements in the home.html file. This is done using a JavaScript function that filters products based on their data attributes.
```js
function showRecommendations() {
  // Clear any existing filters
  filterProducts('all');

  document.querySelectorAll('.product-card').forEach(function (product) {
    if (product.dataset.category === 'traditionals') {
      product.style.display = '';
    }
    else {
      product.style.display = 'none';
    }
  });
}
```

- Recommendations by Gender: We tailor the recommendations further by gender. The JavaScript function filterProductsByGender checks the data-gender attribute and filters the products accordingly.
```js
function filterProductsByGender(gender) {
  // Get all product cards
  var products = document.querySelectorAll('.product-card');
  products.forEach(function (product) {
    var productGender = product.getAttribute('data-gender');

    if (productGender === gender) {
      product.style.display = ''; // Show the product
    } else {
      product.style.display = 'none'; // Hide the product
    }
  });
}
```

### Free Delivery on Birthday
Make birthdays special for users by offering free delivery.

How it Works in Code:
Birthday Check: In app.py, I compared the user's birthdate with the current date. If it's their birthday, set the shipping fee to zero and flag a birthday discount.
```python
if birthdate.month == datetime.today().month and birthdate.day == datetime.today().day:
    shipping_fee = 0
    birthday_discount = True
```

Also, a message is sent on the front-end wishing them Happy Birthday along with Telling them the offer.
```html
{% if birthday_discount %}
<div class="alert alert-success mt-2">Happy Birthday! You get 100% off on shipping charges today!</div>
{% endif %}
```

### Product Filtering
This feature enhances the user experience by allowing them to filter products based on categories.

How it Works in Code:
Filter Function: The filterProducts JavaScript function in home.html receives a category parameter. It then loops through all products and compares their data-category attribute to the parameter. If there's a match, the product is shown; otherwise, it's hidden.

```js
function filterProducts(category) {
  // Get all product cards
  var products = document.querySelectorAll('.product-card');
  products.forEach(function (product) {
    // Check the data-category attribute of the product
    var productCategory = product.getAttribute('data-category');
    if (category === 'all' || productCategory === category) {
      product.style.display = ''; // Show the product
    } else {
      product.style.display = 'none'; // Hide the product
    }
  });
}
```


## Screenshots
