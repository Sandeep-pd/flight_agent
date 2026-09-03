from pydantic import BaseModel
from typing import List


class TravelRequest(BaseModel):
    source: str
    destination: str
    date: str


class Flight(BaseModel):
    airline: str
    departure: str
    arrival: str
    price: str


class Hotel(BaseModel):
    name: str
    location: str
    price_per_night: str
    rating: str


class Location(BaseModel):
    name: str
    type: str
    description: str


class TravelResponse(BaseModel):
    source: str
    destination: str
    flights: List[Flight]
    hotels: List[Hotel]
    locations: List[Location]