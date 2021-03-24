from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mars_scrape import scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def home(): 
     # Find data
    mars_info = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_info)

@app.route('/scrape')
def scrape_all():
    # Create mars info collection
    mars_info = mongo.db.mars
    mars_data = scrape()
    mars_info.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=False)



