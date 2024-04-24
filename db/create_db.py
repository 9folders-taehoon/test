from sqlalchemy import create_engine
from .companylogo_model import Base
from sqlalchemy.orm import sessionmaker

# url = f"{db_engine}://{db_user}@{db_host}:{db_port}/{db_name}"

engine = create_engine("mysql://root@localhost:3306/company_logo")

Base.metadata.create_all(bind=engine)
db_session = sessionmaker(engine)
