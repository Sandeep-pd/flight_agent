from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types

from agent import (
    flight_agent,
    hotel_agent,
    location_agent
)

from model import TravelResponse, TravelRequest


# --------------------------------
# FastAPI App
# --------------------------------

app = FastAPI(
    title="Travel Agent API",
    description="AI Travel Agent for flights, hotels and locations",
    version="1.0"
)


# --------------------------------
# Gemini Client
# --------------------------------

client = genai.Client()


# --------------------------------
# Travel Agent
# --------------------------------

def travel_agent(source, destination, date):

    # --------------------------------
    # 1. Flight Agent
    # --------------------------------

    flights = flight_agent(
        source,
        destination,
        date
    )

    # --------------------------------
    # 2. Hotel Agent
    # --------------------------------

    hotels = hotel_agent(
        destination
    )

    # --------------------------------
    # 3. Location Agent
    # --------------------------------

    locations = location_agent(
        destination
    )

    # --------------------------------
    # 4. Combine Results
    # --------------------------------

    final_prompt = f"""
    You are the main travel agent.

    Create a final travel plan.

    Source:
    {source}

    Destination:
    {destination}

    Travel Date:
    {date}

    FLIGHT SEARCH RESULTS:
    {flights}

    HOTEL SEARCH RESULTS:
    {hotels}

    LOCATION SEARCH RESULTS:
    {locations}

    Convert these results into the required structured format.

    Do not invent information.
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=final_prompt,

        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=TravelResponse
        )
    )

    return response.parsed


# --------------------------------
# Home API
# --------------------------------

@app.get("/")
def home():

    return {
        "message": "Travel Agent API is running"
    }


# --------------------------------
# Travel API
# --------------------------------

@app.post(
    "/travel",
    response_model=TravelResponse
)
def search_travel(request: TravelRequest):

    try:

        result = travel_agent(
            source=request.source,
            destination=request.destination,
            date=request.date
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )