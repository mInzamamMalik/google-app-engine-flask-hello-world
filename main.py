from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('home.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    return render_template('edit.html')


@app.route('/add', methods=["GET", "POST"])
def hello():
    return render_template('classifier.html')

if __name__ == '__main__':
    # app.run() # for google app engine
    app.run(host='0.0.0.0', port=3003) # for google compute engine
