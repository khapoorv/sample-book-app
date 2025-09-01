
from pydantic import BaseModel, Field
import uuid

class BaseEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
