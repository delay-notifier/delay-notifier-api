from pydantic import BaseModel, Field
from typing import List

class OperatorBase(BaseModel):
    operator_id: int = Field(..., description="鉄道会社ID")
    operator_name: str = Field(..., description="鉄道会社名")

class LineBase(BaseModel):
    line_id: int = Field(..., description="路線ID")
    line_name: str = Field(..., description="路線名")

class LineResponse(LineBase):
    class Config:
        orm_mode = True

class OperatorResponse(OperatorBase):
    lines: List[LineResponse] = Field([], description="路線一覧")

    class Config:
        orm_mode = True

class OperatorsResponse(BaseModel):
    operators: List[OperatorBase] = Field([], description="全鉄道会社")

    class Config:
        orm_mode = True