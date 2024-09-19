from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Retrieve values from form
            first_number = float(request.form['firstNumber'])
            second_number = float(request.form['secondNumber'])
            # Calculate sum
            result = first_number + second_number
        except ValueError:
            result = 'Invalid input. Please enter valid numbers.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
