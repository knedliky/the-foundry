from pydantic.dataclasses import dataclass


@dataclass
class PropertyListing:
    agency_id: int
    property_id: int
    property_url: str
    agency_name: str
    agency_url: str
    agent: str
    bathrooms: int
    bedrooms: int
    carspaces: int
    geolocation: dict
    postcode: int
    price: str
    property_type: str
    result: str
    state: str
    street_name: str
    street_number: str
    street_type: str
    suburb: str = None
    unit_number: str = None
