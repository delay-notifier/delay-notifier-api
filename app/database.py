from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# PostgreSQL用の設定
import os
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://delay_user:delay_password@localhost:5432/delay_notifier"
)

# SQLite用の設定（動作確認用）
# DATABASE_URL = "sqlite:///./delay_notifier.db"

engine = create_engine(
    DATABASE_URL,
    # SQLiteの場合のみ必要な設定
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    データベースセッションを取得する関数
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
