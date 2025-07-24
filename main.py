from utils import terminal_typing, fake_loading_bar

def login_screen():
    terminal_typing("Welcome to NetHack Terminal v1.0")
    terminal_typing("Accessing secure system...\n")
    username = input("Username: ")
    password = input("Password: ")

    if password == "2431":
        terminal_typing(f"\nAccess granted. Welcome, {username}.")
        fake_loading_bar()
        return True
    else:
        terminal_typing("\nAccess denied. Incorrect password.")
        return False

if __name__ == "__main__":
    success = login_screen()
    if success:
        terminal_typing(">>> Proceeding to Network Scan Stage...\n")
    else:
        terminal_typing("System locked. Try again later.")