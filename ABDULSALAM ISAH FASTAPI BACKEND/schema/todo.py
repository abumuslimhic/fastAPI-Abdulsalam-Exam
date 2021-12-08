from pydantic import BaseModel, validator

class Todo(BaseModel):
        title : str
        description : str
        priority : int = 0

        @validator('priority')
        def validate_priority(cls, value):
                if not value in [0, 1, 2]:
                        raise ValueError("Priority values must be 0(low), 1(medium), 2(high)")
                
                return value