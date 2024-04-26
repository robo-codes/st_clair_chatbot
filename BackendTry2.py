from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("Lustyrobo/llama-2-7b-robo")

# Load the model
model = AutoModelForCausalLM.from_pretrained("Lustyrobo/llama-2-7b-robo")


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    return jsonify({"response": get_chat_response(msg)})


def get_chat_response(text):
    # Generate response
    input_ids = tokenizer.encode(text, return_tensors="pt")
    output_ids = model.generate(input_ids, max_length=50, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response


if __name__ == '__main__':
    app.run(debug=True)
