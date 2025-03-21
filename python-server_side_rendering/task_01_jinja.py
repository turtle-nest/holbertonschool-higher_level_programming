from flask import Flask, render_template

app = Flask(__name__)
"""
Flask application instance for serving a simple website with reusable templates.
"""

@app.route('/')
def home():
    """
    Route for the home page.
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Route for the about page.
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Route for the contact page.
    """
    return render_template('contact.html')

if __name__ == '__main__':
    """
    Entry point of the application."
    """
    app.run(debug=True, port=5000)
