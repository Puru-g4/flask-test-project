# app.py
# This file sets up the basic server logic using the Flask framework.

# 1. Import the necessary components from the Flask library
from flask import Flask, render_template
print("debug")
# 2. Create the Flask application instance
# The argument __name__ tells Flask where to look for resources like templates.
app = Flask(__name__)

# 3. Define a route for the home page ('/')
# This decorator links the URL '/' (the root of your website) to the function below.
@app.route('/')
def home():
    # The render_template function looks for the file inside the 'templates' folder.
    # It passes the title variable to the HTML template for display.
    page_title = "Welcome to Flask Starter App"
    return render_template('index.html', title=page_title)

# 4. Define another route for an 'about' page
@app.route('/about')
def about():
    page_title = "About Our Flask Project"
    # This renders a second, simple template
    return render_template('about.html', title=page_title)


# 5. Run the application
# This block ensures the server only runs when you execute this script directly (e.g., python app.py)
if __name__ == '__main__':
    # Setting debug=True is useful for development as it reloads the server on code changes
    # By default, it runs on http://127.0.0.1:5000/
    app.run(debug=True)