import app.schemas.lines as lines_schema

async def get_line(line_id: int):
    return lines_schema.LineResponse(
            line_id=line_id,
            line_name="中央線"
        )