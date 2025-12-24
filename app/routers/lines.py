from fastapi import APIRouter
import app.schemas.lines as lines_schema

router = APIRouter()

#ある鉄道会社の路線一覧を取得する
@router.get("/{operator_id}", response_model=list[lines_schema.OperatorResponse])
async def get_lines(operator_id: int):
    return [
        lines_schema.OperatorResponse(
            operator_id=1,
            operator_name="JR東日本",
            lines=[
                lines_schema.LineResponse(
                    line_id=1,
                    line_name="中央線"
                ),
                lines_schema.LineResponse(
                    line_id=2,
                    line_name="山手線"
                )
            ]
        )
    ]
    

#特定の路線の情報を取得する
@router.get("/{line_id}")
async def get_lines(line_id: int):
    pass

#test