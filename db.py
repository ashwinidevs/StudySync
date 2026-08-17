from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
database_url=os.getenv("DATABASE_URL")
engine=create_engine(database_url,
                    pool_pre_ping=True)
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()