from google import genai
from google.genai import types
from model import TravelResponse


client = genai.Client()


def flight_agent(source: str, destination: str, date: str):

    prompt = f"""
    You are a flight search agent.

    Search the web for flights from {source} to {destination}
    on {date}.

    Find useful flight information such as:
    - airline
    - departure time
    - arrival time
    - price

    Return only relevant flight information.
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text


def hotel_agent(destination: str):

    prompt = f"""
    You are a hotel search agent.

    Search the web for hotels in {destination}.

    Find:
    - hotel name
    - location
    - price per night
    - rating

    Return useful hotel options.
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text


def location_agent(destination: str):

    prompt = f"""
    You are a location search agent.

    Search the web for popular places to visit in {destination}.

    Find:
    - place name
    - type
    - short description

    Return useful tourist locations.
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text