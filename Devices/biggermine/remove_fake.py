import ctypes

# Constants
MB_OK = 0x0  # OK button only

# First message
ctypes.windll.user32.MessageBoxW(
    None,
    "Deleted Virus",
    "Scan Result",
    MB_OK
)