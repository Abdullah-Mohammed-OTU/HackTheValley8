from flask import Flask, request, jsonify, render_template
from TrainModel import main

app = Flask(__name__)

model = main()

@app.route('/', methods=['GET', 'POST'])
def index():
    temperature = None
    if request.method == 'POST':
        year = int(request.form['year'])
        temperature = model.predict([[year]])[0]
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)
