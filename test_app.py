import unittest
import json
import os
import sys

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(__file__))

from app import app

class TestTextAnalysis(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_analyze_text_success(self):
        """Тест успешного анализа текста"""
        response = self.app.post('/analyze',
            json={'text': 'hello world hello test'}
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertEqual(data['total_words'], 4)
        self.assertEqual(data['top_words']['hello'], 2)
        self.assertEqual(data['top_words']['world'], 1)
    
    def test_analyze_empty_text(self):
        """Тест с пустым текстом"""
        response = self.app.post('/analyze',
            json={'text': ''}
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['total_words'], 0)
    
    def test_no_text_field(self):
        """Тест без поля text"""
        response = self.app.post('/analyze',
            json={'message': 'no text here'}
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Missing "text" field', data['error'])
    
    def test_invalid_json(self):
        """Тест с невалидным JSON"""
        response = self.app.post('/analyze',
            data='invalid json',
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_wrong_content_type(self):
        """Тест с неправильным Content-Type"""
        response = self.app.post('/analyze',
            data=json.dumps({'text': 'hello'}),
            content_type='text/plain'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()