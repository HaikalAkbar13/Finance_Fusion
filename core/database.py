import singlestoredb as s2
import bcrypt
from decouple import config

class Database:
    def __init__(self):
        try:
            self.conn = s2.connect(config("connection"), autocommit=True, results_format=dict)
        except Exception as e:
            return f"Eror {e}"
        
    def user_info(self):
        result = []
        if self.conn:
            try:
                with self.conn.cursor() as cur:
                    query = 'select * from user_data'
                    cur.execute(query=query)
                    result = cur.fetchall() 
                    return result
            except Exception as e:
                return f"Eror {e}"
        return None



if __name__ == "__main__":
    db = Database()
    result = db.user_info()
    password = next((row['password'] for row in result if row['user_name'] == 'haikal'), None)
    print(password)



"""
# Tips Dict di tampung pada List


# Cari username dengan id = 2
username = next((row["username"] for row in data if row["id"] == 2), None)
print(username)  # Output: JaneDoe

# Ambil semua username
usernames = [row["username"] for row in data]
print(usernames)  # Output: ['JohnDoe', 'JaneDoe']

import pandas as pd

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Akses semua username
print(df["username"].tolist())  # Output: ['JohnDoe', 'JaneDoe']

# Akses username dengan id = 2
username = df.loc[df["id"] == 2, "username"].iloc[0]
print(username)  # Output: JaneDoe


"""