# TransLingua Backend API

Python Flask backend for the TransLingua AI translation application using Google's Gemini API.

## Setup Instructions

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure API Key

1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in the backend directory:

```bash
cp .env.example .env
```

3. Edit `.env` and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### POST /api/translate

Translate text from one language to another.

**Request Body:**
```json
{
  "text": "Hello, world!",
  "source_language": "English",
  "target_language": "Spanish"
}
```

**Response:**
```json
{
  "success": true,
  "original_text": "Hello, world!",
  "translated_text": "¡Hola, mundo!",
  "source_language": "English",
  "target_language": "Spanish"
}
```

### GET /api/health

Health check endpoint to verify the API is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "TransLingua Translation API"
}
```

## Testing the API

You can test the API using curl:

```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "source_language": "English",
    "target_language": "French"
  }'
```
