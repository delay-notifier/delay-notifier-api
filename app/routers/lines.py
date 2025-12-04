from fastapi import APIRouter

router = APIRouter()

#ある鉄道会社の路線一覧を取得する
@router.get("/lines")
async def get_lines(operator_id: int):
    pass

#特定の路線の情報を取得する
@router.get("/v1/lines/{line_id}")
async def get_lines(line_id: int):
    pass

#test