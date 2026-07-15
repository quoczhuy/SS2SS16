from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    department_id: Optional[int] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department_id: Optional[int] = None

    class Config:
        from_attributes = True