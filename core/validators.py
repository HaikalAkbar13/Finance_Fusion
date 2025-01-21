import re
import bcrypt
from .database import Database

class PasswordValidation:
    @staticmethod
    def validate_entry(entry_text):
        """
        This Function to Validate Password Combination of
        Capitalize Word, Number, and Unique Character
        """
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,15}$"
        return bool(re.match(pattern, entry_text))

    @staticmethod    
    def hash_pw(user_input = str):
        user_info = Database.user_info()
        user_password = next((row['password'] for row in user_info if row['username'] == 'haikal'), None)
        user_input_bytes = user_input.encode("utf-8")
        user_password_bytes = user_password.encode("utf-8")
        garam = bcrypt.gensalt()
        hash_input_pw = bcrypt.hashpw(user_input_bytes, garam)
        return bcrypt.checkpw(user_password_bytes, hash_input_pw)





coba = PasswordValidation()
pw = "123"
coba.hash_pw(pw)