import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql://root:''@127.0.0.1/test')


df = pd.read_excel('people.xlsx')
df.to_sql('data', con=engine)
  