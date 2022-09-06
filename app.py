from flask import Flask, render_template, request, url_for

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=5000)

@app.route('/')
def start():
    variable = "Welcome friends!"
    return render_template('start.html',
        greeting = variable)

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        yourName = request.form['your_name']
        return render_template('answer.html',
            name = yourName)
    else:
        return render_template('question.html')

@app.route('/answer')
def answer():
    return render_template('answer.html',
        name = yourName)