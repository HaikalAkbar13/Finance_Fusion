import re

class PasswordValidation:
    @staticmethod
    def validate_entry(entry_text):
        """
        This Function to Validate Password Combination of
        Capitalize Word, Number, and Unique Character
        """
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,15}$"
        return bool(re.match(pattern, entry_text))