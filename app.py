from flask import Flask, request, render_template
import model
from model import generate_summary

# %%

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')




@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        number = request.form['quantity']
        quantity = int(number)
        my_prediction = generate_summary(message, quantity)
    return render_template('result.html', prediction=my_prediction)

# %%

if __name__ == "__main__":
    app.run(debug=True)
