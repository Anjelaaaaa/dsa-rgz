from flask import Flask, request, jsonify
import re
from collections import Counter
import sys
import json

app = Flask(__name__)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_text():
    if request.method == 'GET':
        return jsonify({'message': 'Use POST with JSON: {"text": "your text"}'})
    
    try:
        # Проверяем Content-Type
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        # Пробуем получить JSON
        try:
            data = request.get_json()
        except:
            return jsonify({'error': 'Invalid JSON format'}), 400
        
        # Проверяем что data не None
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        # Проверяем наличие поля text
        if 'text' not in data:
            return jsonify({'error': 'Missing "text" field in JSON'}), 400
        
        text = data['text']
        
        # Проверяем тип text
        if not isinstance(text, str):
            return jsonify({'error': '"text" must be a string'}), 400
        
        # Обрабатываем текст
        words = re.findall(r'\b\w+\b', text.lower())
        
        total_words = len(words)
        word_counts = Counter(words)
        top_words = word_counts.most_common(5)
        
        # Получаем порт
        port = sys.argv[1] if len(sys.argv) > 1 else '5000'
        
        return jsonify({
            'total_words': total_words,
            'top_words': dict(top_words),
            'server_port': port
        })
        
    except Exception as e:
        # Логируем ошибку для отладки
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(f"🚀 Starting Flask server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)