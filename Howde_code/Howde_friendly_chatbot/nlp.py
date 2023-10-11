from flask import Flask, render_template, request, jsonify
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

transformers.logging.set_verbosity_error()

model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=0,
        temperature=0.75,
        pad_token_id=tokenizer.eos_token_id
    )
    bot_response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
