from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Location(BaseModel):
    lat: float = Field(default=-38.383494)
    lng: float = Field(default=33.427362)


class Model(BaseModel):
    location: Location = Field(default=Location())
    accuracy: int = Field(default=50)
    name: str = Field(default="Frontline house")
    phone_number: str = Field(default="(+91) 983 893 3937")
    address: str = Field(default="29, side layout, cohen 09")
    types: List[str] = Field(default=["shoe park", "shop"])
    website: str = Field(default="http://google.com")
    language: str = Field(default="French-IN")