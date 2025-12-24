from pydantic import BaseModel, Field
from typing import List

class LineBase(BaseModel):
    operator_id: int = Field(None, description="鉄道会社ID")
    operator_name: str = Field(None, description="鉄道会社名")

class LineResponse(BaseModel):
    line_id: int = Field(None, description="路線ID")
    line_name: str = Field(None, description="路線名")

    class Config:
        orm_mode = True

class OperatorResponse(LineBase):
    lines: List[LineResponse] = Field([], description="路線一覧")

    class Config:
        orm_mode = True