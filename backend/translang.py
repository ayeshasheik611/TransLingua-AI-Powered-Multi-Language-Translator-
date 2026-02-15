from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Gemini API
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)


def translate_text(text, source_language, target_language):
    """
    Translate text from source language to target language using Gemini AI
    
    Args:
        text (str): The text to be translated
        source_language (str): The language of the input text
        target_language (str): The language to translate to
    
    Returns:
        str: The translated text
    """
    prompt = (
        f"Translate the following text from {source_language} to {target_language}. "
        f"Provide only the translation without any additional explanation or context.\n\n"
        f"Text: {text}"
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    return response.text


@app.route('/api/translate', methods=['POST'])
def translate():
    """
    API endpoint for text translation
    
    Expected JSON payload:
    {
        "text": "Hello, world!",
        "source_language": "English",
        "target_language": "Spanish"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        text = data.get('text')
        source_language = data.get('source_language')
        target_language = data.get('target_language')
        
        if not all([text, source_language, target_language]):
            return jsonify({
                'error': 'Missing required fields: text, source_language, target_language'
            }), 400
        
        # Perform translation
        translated_text = translate_text(text, source_language, target_language)
        
        return jsonify({
            'success': True,
            'original_text': text,
            'translated_text': translated_text,
            'source_language': source_language,
            'target_language': target_language
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'TransLingua Translation API'
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
