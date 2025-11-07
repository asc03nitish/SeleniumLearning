# test_string_operations.py
import requests

def test_string_operations_on_example_dot_com():
    # Fetch the webpage
    response = requests.get("https://example.com", verify=False)

    # Ensure request was successful
    assert response.status_code == 200

    # Get the page text
    page_text = response.text

    # ✅ 1. Extract and verify page title
    assert "<title>Example Domain</title>" in page_text

    # ✅ 2. Check if specific text exists on the page (updated to match real text)
    assert "This domain is for use in documentation examples without needing permission." in page_text

    # ✅ 3. Verify string length constraints
    assert len(page_text) > 100
    assert len(page_text) < 10000

    # ✅ 4. Test case sensitivity
    assert "example domain" not in page_text  # lowercase should fail
    assert "Example Domain" in page_text      # correct case should pass
