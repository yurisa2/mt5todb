import mysql.connector
from dotenv import load_dotenv


class Dal:
    def __init__(self):
        load_dotenv()

        self.db = mysql.connector.connect(
          host=MYSQL_SRV,
          user=MYSQL_USR,
          password=MYSQL_PW
        )

    def insert_rates(self, rates):
        sqlString = '''insert into marketdata ('symbol', 'market', 'time',
                                                'open', 'high', 'low', 'close',
                                                'tick_volume', 'spread',
                                                'real_volume', 'period',
                                                'provider') values
        '''
        for rate in rates:
            sqlString += symbolName
            sqlString += "', "
            sqlString += "'B3', '"
            sqlString += str(row[0])
            sqlString += "', '"
            sqlString += str(row[1])
            sqlString += "', '"
            sqlString += str(row[2])
            sqlString += "', '"
            sqlString += str(row[3])
            sqlString += "', '"
            sqlString += str(row[4])
            sqlString += "', '"
            sqlString += str(row[5])
            sqlString += "', '"
            sqlString += str(row[6])
            sqlString += "', '"
            sqlString += str(row[7])
            sqlString += "', 'TIMEFRAME_M5', 'Rico')"


            conn.commit()
