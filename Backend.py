import numpy as np
from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch as a

app = Flask(__name__)
model_path = "Lustyrobo/llama-2-7b-robo"
tokenizer = AutoTokenizer.from_pretrained("Lustyrobo/llama-2-7b-robo")
model = AutoModelForQuestionAnswering.from_pretrained(model_path)


@app.route('/')
def home():
    return render_template('C:\\Users\\solan\\OneDrive\\Desktop\\St.Clair\\sem_3\\Project\\index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = request.form['text']
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = logits.argmax(dim=1)

    output = prediction.item()

    return render_template('index.html', prediction_text='Prediction results are :{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
