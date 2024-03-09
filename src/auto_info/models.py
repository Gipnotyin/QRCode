from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, Boolean, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()


auto = Table(
    "auto",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("vin", String, nullable=False),
    Column("mark", String, nullable=False),
    Column("model", String, nullable=False),
    Column("modelYear", String, nullable=False),
    Column("year", Integer, nullable=False),
    Column("date", TIMESTAMP, nullable=False),
    Column("equipment", String, nullable=False),
    Column("bodywork", String, nullable=False),
    Column("package", String, nullable=False),
    Column("color", String, nullable=False),
    Column("department", String, nullable=False)
)
