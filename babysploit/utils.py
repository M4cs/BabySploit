import subprocess


def get_terminal_width(default_size=80):
    """Get terminal width or return `default_size` (80)"""
    try:
        rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
        return rows
    except Exception:
        return default_size
