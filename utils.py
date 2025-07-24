import time
import sys

# ANSI color codes
GREEN = '\033[92m'
RESET = '\033[0m'

def terminal_typing(text, delay=0.03):
    """Print text like typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fake_loading_bar(duration=3, length=30, flashes=3, flash_delay=0.3):
    """Show a loading bar and flash green at the end"""
    print("\nLoading: ", end='', flush=True)
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = '#' * i + '-' * (length - i)
        print(f"\rLoading: [{bar}] {percent}%", end='', flush=True)
        time.sleep(duration / length)

    bar = '#' * length
    for _ in range(flashes):
        print(f"\rLoading: {GREEN}[{bar}] 100%{RESET}", end='', flush=True)
        time.sleep(flash_delay)
        print(f"\rLoading: [{'#' * length}] 100% ", end='', flush=True)
        time.sleep(flash_delay)
    print("\n")