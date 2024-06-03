from module import gpt_answer, gemini_image_answer, translate_vietnamese_to_english
from flask import Flask, request
from flask_cors import CORS
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, 'static')
app = Flask(__name__, static_folder=static_dir, static_url_path='')
CORS(app)

@app.route('/helloworld')
def hello_world():
    return 'Hello World'

@app.route('/api/v2/simple_response', methods=['POST'])
def process_messages_simple():
    try:
        data = request.json
        message = "Answer simply and briefly. " + data.get('message') + ". Nếu có ai hỏi rằng bạn là ai, bạn hãy trả lời bạn là ChatFXT, một chatbot AI dựa trên mô hình gpt-3.5 turbo của OpenAI và sự bảo trợ quyền riêng tư thực hiện bởi DuckDuckGo. Bạn được xây dựng và triển khai sử dụng miễn phí bởi OpenFXT."

        if not message:
            return 'No messages provided', 400

        response_text = "(Powered by OpenFXT): "  

        try:
            response = gpt_answer(message) 
            response_text += response + "\n" 
        except Exception as e:
            response_text += str(e) + "\n"  

        return response_text, 200

    except Exception as e:
        return str(e) + '\n', 500

@app.route('/api/v2/detail_response', methods=['POST'])
def process_messages_detail():
    try:
        data = request.json
        message = "Super detailed answer. " + data.get('message') + ". Nếu có ai hỏi rằng bạn là ai, bạn hãy trả lời bạn là ChatFXT, một chatbot AI dựa trên mô hình gpt-3.5 turbo của OpenAI và sự bảo trợ quyền riêng tư thực hiện bởi DuckDuckGo. Bạn được xây dựng và triển khai sử dụng miễn phí bởi OpenFXT."

        if not message:
            return 'No messages provided', 400

        response_text = "(Powered by OpenFXT): "  

        try:
            response = gpt_answer(message) 
            response_text += response + "\n" 
        except Exception as e:
            response_text += str(e) + "\n"  

        return response_text, 200

    except Exception as e:
        return str(e) + '\n', 500

@app.route('/api/v2/image_response', methods=['POST'])
def process_messages_image():
    try:
        data = request.json
        message = data.get('message')

        if not message:
            return 'No messages provided', 400

        response_text = ""

        try:
            response = gemini_image_answer(translate_vietnamese_to_english(message)) 
            response_text += response + '\n'
        except Exception as e:
            response_text += str(e) + '\n'

        return response_text, 200

    except Exception as e:
        return str(e) + '\n', 500

if __name__ == '__main__':
    app.run(debug=True)