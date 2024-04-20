from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route('/') #first page
def hello():
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        height = request.form['height']
        model = pickle.load(open('model.pkl','rb'))
        weight = model.predict([[float(height)]])
        print(height)
        print(weight[0])
    return render_template('prediction.html', weight = round(weight[0], 2))

if  __name__ == '__main__':
    app.run()
# to run python app.py
#ctrl +C to stop running