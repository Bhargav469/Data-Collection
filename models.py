# models.py

from sqlalchemy import Column, Integer, Float, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)

class NewsHeadlines(Base):
    __tablename__ = 'web_headlines'
    id = Column(Integer, primary_key=True)
    headline = Column(String)
    url = Column(String)
    date = Column(TIMESTAMP)

class WebsiteMetadata(Base):
    __tablename__ = 'website_metadata'
    id = Column(Integer, primary_key=True)
    website_name = Column(String)
    url = Column(String)
    last_scraped = Column(TIMESTAMP)
