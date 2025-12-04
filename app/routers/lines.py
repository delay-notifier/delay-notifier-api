from fastapi import APIRouter,  Depends
from app.schemas import line_schema

router = APIRouter()

#ある鉄道会社の路線一覧を取得する
@router.get("/lines", response_model=list[line_schema.Line])
async def get_lines(operator_id: int):
    return [
        line_schema.Line = (
            id=1,
            name="山手線",
            operator_id=operator_id
        )
    ]

#特定の路線の情報を取得する
@router.get("/v1/lines/{line_id}")
async def get_lines(line_id: int):
    pass

#テスト
#test
