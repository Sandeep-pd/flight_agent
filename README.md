# Travel Agent API

A FastAPI service that uses Gemini to find flights, hotels, and tourist locations, then combines the results into a structured travel plan.

## Requirements

- Python 3.10+
- A Gemini API key

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn google-genai pydantic
```

Set the Gemini API key before starting the server:

```powershell
$env:GEMINI_API_KEY = "your-api-key"
```

## Run

```powershell
python -m uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

### `GET /`

Returns a simple health message.

### `POST /travel`

Request body:

```json
{
  "source": "New York",
  "destination": "Paris",
  "date": "2026-10-15"
}
```

Example PowerShell request:

```powershell
$body = @{
  source = "New York"
  destination = "Paris"
  date = "2026-10-15"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/travel `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

The response contains structured flight, hotel, and location results.
