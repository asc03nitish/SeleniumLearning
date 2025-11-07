# Experiments/tests/test_file_utils.py
import os
import pytest
from nov4_lab.srclab.file_utils import (
    create_file, delete_file, read_file, write_file,
    has_read_permission, has_write_permission,
    write_binary_file, read_binary_file
)

# --- File Creation & Deletion ---
def test_file_creation_and_deletion(tmp_path):
    file_path = tmp_path / "test.txt"
    created = create_file(file_path, "Hello World")
    assert created
    assert file_path.exists()

    deleted = delete_file(file_path)
    assert deleted
    assert not file_path.exists()

def test_delete_non_existing_file(tmp_path):
    fake_path = tmp_path / "missing.txt"
    assert not delete_file(fake_path)


# --- Read/Write Operations ---
def test_file_read_write(tmp_path):
    file_path = tmp_path / "sample.txt"
    content = "Pytest File Handling!"
    create_file(file_path, content)

    assert read_file(file_path) == content

    new_content = "Updated Content"
    write_file(file_path, new_content)
    assert read_file(file_path) == new_content


# --- Permission Checks ---
@pytest.mark.skipif(os.name == "nt", reason="Permission test skipped on Windows")
def test_read_write_permissions(tmp_path):
    file_path = tmp_path / "perm.txt"
    create_file(file_path, "data")

    # Remove all permissions
    os.chmod(file_path, 0o000)

    assert not has_read_permission(file_path)
    assert not has_write_permission(file_path)

    # Restore permissions
    os.chmod(file_path, 0o600)
    assert has_read_permission(file_path)
    assert has_write_permission(file_path)


# --- File Content Validation ---
def test_file_content_validation(tmp_path):
    file_path = tmp_path / "content.txt"
    expected = "This is test content"
    create_file(file_path, expected)
    content = read_file(file_path)

    assert isinstance(content, str)
    assert expected in content
    assert len(content) == len(expected)


# --- Binary File Operations ---
def test_binary_file_operations(tmp_path):
    file_path = tmp_path / "binary.dat"
    data = b"\xDE\xAD\xBE\xEF"

    write_binary_file(file_path, data)
    read_data = read_binary_file(file_path)

    assert read_data == data
    assert len(read_data) == 4
