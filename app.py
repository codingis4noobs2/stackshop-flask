import logging
from datetime import datetime
from authlib.integrations.flask_client import OAuth
from flask import render_template, redirect, send_file
from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)
app.config.from_object('config')

CONF_URL = app.config['PROVIDER_ISSUER'] + '/.well-known/openid-configuration'
app.secret_key = app.config['FLASK_SECRET']

oauth = OAuth(app)
oauth.register(
    name='affinidi',
    client_id=app.config['PROVIDER_CLIENT_ID'],
    client_secret=app.config['PROVIDER_CLIENT_SECRET'],
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid offline_access',
        'token_endpoint_auth_method': 'client_secret_post',
    }
)

@app.route('/')
def homepage():
    user_info = {'is_logged_in': False}
    user_data = session.get('user')
    recommendations = []
    if user_data:
        user_info = {
            'is_logged_in': True,
            'givenName': user_data['custom'][7]['givenName'],
            'picture': user_data['custom'][5]['picture'],
            'country': user_data['custom'][3]['country'],
            'gender': user_data['custom'][21]['gender'],
        }
        if user_info['country'].lower() == 'india':
            recommendations = [{'name': 'Product 1', 'category': 'traditionals'}, {'name': 'Product 2', 'category': 'watches'}]
    return render_template('home.html', user=user_info, recommendations=recommendations)

@app.route('/login')
def login():
    redirect_uri = "https://stackshop.onrender.com/auth"
    logging.info(f'Redirect URI: {redirect_uri}')
    return oauth.affinidi.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = oauth.affinidi.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/cart')
def cart():
    user_info = {'is_logged_in': False}
    user_data = session.get('user')
    if user_data:
        user_info = {
            'is_logged_in': True,
            'givenName': user_data['custom'][7]['givenName'],
            'picture': user_data['custom'][5]['picture'],  # Make sure to replace with the correct key if it's different
        }
    return render_template('cart.html', user=user_info)

@app.route('/checkout')
def checkout():
    if 'user' not in session:
        flash('Please log in to proceed to checkout.')
        return redirect(url_for('login'))
    
    user_info = session['user']
    birthday_discount = False
    shipping_fee = 40  # Default shipping fee
    # Check for birthday and apply discount if applicable
    if user_info['custom'][19]['birthdate']:
        birthdate = datetime.strptime(user_info['custom'][19]['birthdate'], '%Y-%m-%d').date()
        if birthdate.month == datetime.today().month and birthdate.day == datetime.today().day:
            shipping_fee = 0
            birthday_discount = True
    
    return render_template('checkout.html', user=user_info, shipping_fee=shipping_fee, birthday_discount=birthday_discount)


if __name__ == '__main__':
    app.run()
