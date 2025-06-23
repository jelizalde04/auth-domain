from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from config.db import Base

class Responsible(Base):
    __tablename__ = "Responsibles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    contact = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
