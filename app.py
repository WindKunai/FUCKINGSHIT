from flask import Flask, render_template, session

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    if session.get('username') != None:
        return render_template('index.html', username = session.get('username'))
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
