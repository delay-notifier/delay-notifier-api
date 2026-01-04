"""
modelsパッケージ

このファイルは、modelsディレクトリ内のモデルをまとめてインポートしやすくするためのものです。

使用例:
    from app.models import User
    # app.models.user.User と書かなくても良くなります
"""

from app.models.user import User

# __all__ は「このモジュールから公開するもの」のリスト
# from app.models import * とした時に、ここに書かれたものだけがインポートされます
__all__ = ["User"]
