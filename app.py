import os
import sys
from flask import Flask, request, jsonify
import re
from collections import Counter

app = Flask(__name__)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_text():
    if request.method == 'GET':
        return jsonify({'message': 'Use POST with JSON: {"text": "your text"}'})
    
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json(silent=True)
        
        if data is None:
            return jsonify({'error': 'Invalid JSON format'}), 400
            
        if 'text' not in data:
            return jsonify({'error': 'Missing "text" field in JSON'}), 400
        
        text = data['text']
        
        if not isinstance(text, str):
            return jsonify({'error': '"text" must be a string'}), 400
        
        words = re.findall(r'\b\w+\b', text.lower())
        total_words = len(words)
        word_counts = Counter(words)
        top_words = word_counts.most_common(5)
        
        port = os.environ.get('PORT', '5000')
        
        return jsonify({
            'total_words': total_words,
            'top_words': dict(top_words),
            'server_port': port
        })
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Безопасные настройки по умолчанию
    port = int(os.environ.get('PORT', '5000'))
    host = os.environ.get('HOST', '127.0.0.1')
    
    print(f"🚀 Starting Flask server on {host}:{port}")
    app.run(host=host, port=port, debug=False)