import re
from tkinter import StringVar
from ttkbootstrap import Entry








def validate_entry(entry_var: StringVar) -> bool:
    """
    Validate the content of a ttkbootstrap entry.

    The entry must meet the following criteria:
    1. Length must be between 7 to 15 characters.
    2. Must contain at least one uppercase letter.
    3. Must contain at least one digit.
    4. Must contain at least one special character (e.g., @, #, $, etc.).

    Parameters:
    entry_var (StringVar): The StringVar associated with the ttkbootstrap Entry.

    Returns:
    bool: True if the entry is valid according to the criteria, False otherwise.
    """
    entry_value = entry_var.get()

    # Check length
    if not (7 <= len(entry_value) <= 15):
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', entry_value):
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', entry_value):
        return False
    
    # Check for at least one special character
    if not re.search(r'[\W_]', entry_value):
        return False

    return True

# Example usage
# entry_var = StringVar()
# entry = Entry(...)  # Assuming you set up your Entry widget here
# entry_var.trace("w", lambda *args: print(validate_entry(entry_var)))