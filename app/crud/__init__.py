"""
crudパッケージ

CRUD操作をまとめたパッケージです。
各モデルのCRUD操作をモジュールとしてインポートできます。

使用例:
    from app.crud import user as user_crud
    user_crud.get_user(db, user_id=1)
"""

# 将来的に他のモデルのCRUDを追加する場合は、ここにインポートを追加します
# 例:
# from app.crud import user, line, delay
