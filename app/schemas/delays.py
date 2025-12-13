from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DelayBase(BaseModel):
    id: int = Field(..., description="遅延情報ID")
    line_id: int = Field(..., description="路線ID")
    delay_minutes: int = Field(..., description="遅延分数（分）")
    reason: Optional[str] = Field(None, description="遅延理由")
    occurred_at: datetime = Field(..., description="遅延発生時刻")
    resolved_at: Optional[datetime] = Field(None, description="遅延解消時刻")

    class Config:
        orm_mode = True 

class DelayResponse(DelayBase):
    """遅延情報のレスポンススキーマ"""
    pass
