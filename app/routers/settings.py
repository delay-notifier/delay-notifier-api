from fastapi import APIRouter, HTTPException
import app.schemas.settings as settings_schema
from app.dependencies.lines import get_line

router = APIRouter()

@router.post("")
async def set_delaynotifier(
    request: settings_schema.DelayNotifierRequest
):
    if request.end_time <= request.start_time:
          raise HTTPException(
              status_code=400,
              detail="end_timeはstart_timeより後の時刻である必要があります"
          )
    line = await get_line(request.line_id)
    return settings_schema.DelayNotifierResponse(
        line_id=line.line_id,
        line_name=line.line_name,
        day_of_the_week=request.day_of_the_week,
        start_time=request.start_time,
        end_time=request.end_time,
        message="通知設定が完了しました"
    )

@router.get("/v1/commute-profiles")
async def get_commute_profiles():
    pass


@router.delete("/v1/commute-profiles/{profile_id}")
async def delete_commute_profile(profile_id: int):
    pass