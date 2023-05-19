# Подготовка тестовых классов Pydantic для проверки структур данных запросов и ответов

from pydantic import BaseModel, Field


class AuthBody(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

        
class AuthResponse(BaseModel):
    token: str = Field(...)


class BookingDates(BaseModel):
    checkin: str = Field(...)
    checkout: str = Field(...)


class Booking(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: BookingDates = Field(...)
    additionalneeds: str = Field(...)


class BookingReduced(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: BookingDates = Field(...)
    additionalneeds: str = Field(None)


class BookingIdsResponse(BaseModel):
    bookingid: int = Field(...)
