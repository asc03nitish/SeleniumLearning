# Experiments/src/file_utils.py
import os

def create_file(path, content=""):
    """Creates a new file with the given content."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return os.path.exists(path)

def delete_file(path):
    """Deletes the specified file."""
    if os.path.exists(path):
        os.remove(path)
        return True
    return False

def read_file(path):
    """Reads text content from a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    """Overwrites a file with new content."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def has_read_permission(path):
    """Checks if file has read permission."""
    return os.access(path, os.R_OK)

def has_write_permission(path):
    """Checks if file has write permission."""
    return os.access(path, os.W_OK)

def write_binary_file(path, data):
    """Writes binary data to a file."""
    with open(path, "wb") as f:
        f.write(data)
    return True

def read_binary_file(path):
    """Reads binary data from a file."""
    with open(path, "rb") as f:
        return f.read()
