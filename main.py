# importing libraries
from flask import Flask, session, render_template, request, redirect
import os  


#  How to run flask program reference: https://flask.palletsprojects.com/en/2.2.x/quickstart/#:~:text=To%20run%20the%20application%2C%20use,with%20the%20%2D%2Dapp%20option.&text=As%20a%20shortcut%2C%20if%20the,Line%20Interface%20for%20more%20details
app = Flask(__name__)

app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('home.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    return render_template('edit.html')


@app.route('/add', methods=["GET", "POST"])
def hello():
    return render_template('classifier.html')


# # In[ ]:
# if __name__ == "__main__":
#     app.debug = True
#     app.run()
# else:
#     gunicorn_app = app()
# # https://stackoverflow.com/a/51397334

PORT = os.environ.get('PORT', 3000)

app.run(port=PORT)
