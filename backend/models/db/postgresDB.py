from dotenv import load_dotenv
from logger import get_module_logger
import logging
import pandas as pd
from sqlalchemy import create_engine, select, Table, update
from sqlalchemy.orm import registry


load_dotenv()
logger = get_module_logger(mod_name=__name__,log_path='./logs/logs.log', lvl=logging.INFO)

class PostgresDB():
    def __init__(self, db_host, db_port, db_name, db_user, db_password):
        self.db_host=db_host
        self.db_port=db_port
        self.db_name=db_name
        self.db_user=db_user
        self.db_password=db_password

        self.engine = create_engine(
            'postgresql://' + str(db_user) + ':' + str(db_password) + '@' + str(db_host) + ':' + str(db_port) + '/' + str(db_name))
        self.mapper_registry = registry()

    def get_table(self,table_name: str):
        try:
            return Table(table_name,
                         self.mapper_registry.metadata,
                         autoload=True,
                         autoload_with=self.engine)
        except:
            logger.error("Could not get table")
            raise Exception

    def send_df_to_db(self, table_name: str,df: pd.DataFrame):
        try:
            logger.info("Try send df to db")
            df.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)

            logger.info("Wrote data to database")
        except Exception as error:
            logger.error("Can not write data to database " + str(error))

    def get_df_from_sql(self, query: str):
        conn = self.engine.connect()
        return pd.read_sql(query, conn)

    def get_by_id(self, table_name:str, id:str):
        try:
            table = self.get_table(table_name=table_name)
            query = select(table).where(table.c.id == id)
            return self.get_df_from_sql(query=query)
        except Exception as ex:
            logger.exception(ex)

    def create(self,  table_name: str, df: pd.DataFrame):
        df.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)

    def update(self, table_name: str, id : str, data: dict):
        table = self.get_table(table_name=table_name)
        query = update(table).where(table.c.id == id).values(data)
        with self.engine.connect() as conn:
            conn.execute(query)

    def delete(self, table_name: str, id: str, id_column):

        table=self.get_table(table_name=table_name)

        query=table.delete().where(id_column == id)
        with self.engine.connect() as conn:
            conn.execute(query)

