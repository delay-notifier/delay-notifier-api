from fastapi import APIRouter
import app.schemas.lines as lines_schema

router = APIRouter()

#全鉄道会社の一覧を取得する
@router.get("/operators", response_model=lines_schema.OperatorsResponse)
async def list_operators():
    return lines_schema.OperatorsResponse(
        operators=[
            lines_schema.OperatorBase(
                    operator_id=1,
                    operator_name="JR東日本"
            ),
            lines_schema.OperatorBase(
                    operator_id=2,
                    operator_name="小田急電鉄"
            ),
            lines_schema.OperatorBase(
                    operator_id=3,
                    operator_name="西武鉄道"
            )
        ]
    )

#ある鉄道会社の路線一覧を取得する
@router.get("/operators/{operator_id}", response_model=lines_schema.OperatorResponse)
async def list_lines(operator_id: int):
    return lines_schema.OperatorResponse(
            operator_id=operator_id,
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

#特定の路線の情報を取得する
@router.get("/{line_id}")
async def get_lines(line_id: int):
    pass