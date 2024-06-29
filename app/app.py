from flask import Flask
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    # Return a simple message
    return 'Hello, World!'

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)