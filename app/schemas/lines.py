from pydantic import BaseModel, Field

class LineBase(BaseModel):
    id: int = Field(..., description="路線ID")
    name: str = Field(..., description="路線名")
    operator_id: int = Field(..., description="鉄道会社ID")
