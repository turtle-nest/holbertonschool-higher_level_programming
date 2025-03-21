from flask import Flask, render_template

app = Flask(__name__)
"""
Flask application that demonstrates conditional logic in Jinja templates.
"""

@app.route('/items')
def items():
    """
    Route that renders a list of items.

    Sends a list of items to the template. You can test this route with different lists,
    including an empty one, to see how the template handles them.
    """
    items_list = ["Apples", "Bananas", "Cherries"]  # Try [] to test empty case
    return render_template('list.html', items=items_list)

if __name__ == '__main__':
    """
    Entry point for running the application.
    """
    app.run(debug=True, port=5000)
