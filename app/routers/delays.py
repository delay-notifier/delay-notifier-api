from fastapi import APIRouter
from typing import Optional, List
from datetime import datetime, date
from app.schemas.delays import DelayResponse

router = APIRouter()

@router.get("", response_model=List[DelayResponse])
async def get_delays(line_id: int, date: Optional[str] = None):
    """
    特定の路線の遅延情報を取得する
    
    - **line_id**: 路線ID（必須）
    - **date**: 日付（YYYY-MM-DD形式、オプション）
    """
    # TODO: データベースから実際のデータを取得する実装に置き換える
    # 現在はモックデータを返す
    mock_delays = [
        DelayResponse(
            id=1,
            line_id=line_id,
            delay_minutes=15,
            reason="信号機故障",
            occurred_at=datetime(2024, 1, 15, 8, 30, 0),
            resolved_at=datetime(2024, 1, 15, 8, 45, 0)
        ),
        DelayResponse(
            id=2,
            line_id=line_id,
            delay_minutes=30,
            reason="人身事故",
            occurred_at=datetime(2024, 1, 15, 12, 0, 0),
            resolved_at=datetime(2024, 1, 15, 12, 30, 0)
        )
    ]
    
    if date:
        try:
            filter_date = datetime.strptime(date, "%Y-%m-%d").date()
            mock_delays = [
                delay for delay in mock_delays
                if delay.occurred_at.date() == filter_date
            ]
        except ValueError:
            pass
    
    return mock_delays
