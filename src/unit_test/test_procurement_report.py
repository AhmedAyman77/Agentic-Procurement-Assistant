"""
Test file to verify the agent crew workflow.
This test calls the API endpoint and checks for any issues with the agent crew execution.
"""

import os
import pytest
import requests

def test_agent_crew():
    """
    Calls the procurement agent API and verifies the response.
    Ensures the agent crew runs without errors and the API is reachable.
    """
    
    # Prepare the API endpoint and test payload
    api_url = "http://0.0.0.0:5000/api/get_procurement_review"
    test_payload = {
        "product_name": "Gaming Laptop",
        "websites_list": ["amazon.com"],
        "country_name": "Egypt",
        "no_keywords": 3,
        "language": "English"
    }
    
    try:
        # Send a POST request to the API endpoint
        response = requests.post(api_url, data=test_payload, timeout=300)
        
        # Assert that the API call was successful
        assert response.status_code == 200, f"API call failed with status: {response.status_code}"
        print("API call returned status 200")
        
    except requests.exceptions.ConnectionError:
        # Skip the test if the API server is not running
        pytest.skip("API server not running")
    except requests.exceptions.Timeout:
        # Fail the test if the agent crew takes too long to respond
        pytest.fail("Agent crew timed out after 5 minutes")
    except Exception as e:
        # Fail the test for any other unexpected errors
        pytest.fail(f"Test failed: {str(e)}")

if __name__ == '__main__':
    """Allows running the test directly from the command line."""
    test_agent_crew()