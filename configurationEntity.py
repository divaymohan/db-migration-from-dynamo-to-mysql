from numbers import Integral
from sqlite3 import IntegrityError
import string
from db_connection.JsonObject import JsonObj
from db_connection.db_connection import Base
from db_connection.db_connection import Column


class ConfigurationEntity(Base):
    __tablename__ = 'configuration'

    id = Column(IntegrityError, primary_key=True)
    body_type = Column(string(100))
    body_wrapper = Column(Integral)
    formData = Column(list(JsonObj))
    formUrlEncoded = Column(list(JsonObj))
    headers = Column(list(JsonObj))
    jsonBody = Column(list(JsonObj))
    queryParams = Column(list(JsonObj))
    category = Column(Integral)
    is_credit_free = Column(Integral)
    method = Column(Integral)
    type = Column(Integral)
    url = Column(Integral)
    created_at = Column(Integral)
    updated_at = Column(Integral)

