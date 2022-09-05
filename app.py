from flask import Flask, render_template, request, url_for

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/answer')
def answer():
    return render_template('answer.html',
        name= yourName)

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        yourName = request.form['your_name']
        return render_template('answer.html',
            name = yourName)
    else:
        return render_template('question.html')