from sqlalchemy import create_engine

engine = create_engine("mysql://root:root@localhost:3306/todos", echo=True)
