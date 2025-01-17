import singlestoredb as s2
import bcrypt
from decouple import config

class DatabaseConnection():
    def __init__(self):
        """Connecting to database
        and Execute some neccessary Scripts"""

        # Connect to Database
        self.conn = s2.connect(config("connection"))
        try:
            with self.conn as conn:
                with conn.cursor() as cur:
                    self.flag = cur.is_connected()
        except Exception as e:
            print(e)
        
        # Create Tabel if not Exist
        
        


if __name__ == "__main__":
    app = DatabaseConnection()
    if app.flag == True:
        print("Connection Success")
    else:
        print(Exception)