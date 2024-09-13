from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models import Product, User, CartItem
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main.route('/cart')
def cart():
    # Simplified for demo
    return render_template('cart.html')

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    # Simplified: add logic for adding to the cart
    return redirect(url_for('main.cart'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simplified authentication logic
        return redirect(url_for('main.index'))
    return render_template('login.html')

