from datetime import timezone, time, timedelta
from pydantic import BaseModel, Field, model_validator
from typing import List

JST = timezone(timedelta(hours=9), "JST")

class DelayNotifierRequest(BaseModel):
    line_id: int = Field(..., description="路線ID")
    day_of_the_week: List[int] = Field(
        ..., 
        description="通知曜日 (0=月曜, 1=火曜, 2=水曜, 3=木曜, 4=金曜, 5=土曜, 6=日曜)",
        example=[0,1,2,3,4]
    )
    start_time: time = Field(..., description="通知開始時間（日本時間 HH:MM形式）", example="07:30")
    end_time: time = Field(..., description="通知終了時間（日本時間 HH:MM形式）", example="09:30")

class DelayNotifierResponse(DelayNotifierRequest):
    line_name: str = Field(..., description="路線名")
    is_enabled: bool = Field(True, description="通知有効フラグ")
    message: str = Field(..., description="登録結果メッセージ")

    class Config:
        orm_mode = True