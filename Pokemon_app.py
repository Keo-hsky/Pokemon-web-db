from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os
from werkzeug.utils import secure_filename

#App initialiization
'''create a flask app '''
app = Flask(__name__)

#basic route
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Pokebase! :3",
        greeting="Kia ora! The pokebase has connected :3")
        
#List all pizzas in alphabetical order
#Eventually link each one to details page
@app.route("/pokemon")
def pokemon_page():
    #Connection to database/db should be own function
    conn = sqlite3.connect("pokemon.db")
    cur = conn.cursor()
    cur.execute('SELECT ID, pokemon_name, pokemon_type, description, pokemon_image, form, hp, attack, defense, special_attack, special_defense, speed, generation FROM pokemon_info ORDER BY ID ASC;')
    #fetchall return a list of results
    pokemon = cur.fetchall()
    print("pokemon")#debug
    conn.close()#be a tidy kiwi
    return render_template("pokemon.html", 
        pokemon=pokemon_page, 
        page_title="All Pokemon :3 ToT")
# Validate image type
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



@app.route("/items")
def items_page():
    #This route passes the items list into the template
    conn = sqlite3.connect("pokemon.db")
    cur = conn.cursor()
    cur.execute('SELECT ID, item_name, item_type, generation, description, items_image FROM item_info ORDER BY ID ASC;')
    #fetchall return a list of results
    items = cur.fetchall()
    print("items")#debug
    conn.close()#be a tidy kiwi
    return render_template("items.html", 
        items=items_page, 
        page_title="All items :3 ToT")
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)