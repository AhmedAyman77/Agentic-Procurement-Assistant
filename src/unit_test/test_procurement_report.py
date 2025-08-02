"""
Test file to verify procurement agent creates HTML report.
Calls the API endpoint and checks if procurement_report.html file is generated.
"""

import os
import time
import pytest
import requests


def test_agent_creates_procurement_report():
    """
    Test that calls procurement agent API and verifies HTML report creation.
    """
    
    # Set up file path where report should be created
    current_directory = os.path.dirname(os.path.abspath(__file__))
    src_directory = os.path.dirname(current_directory)
    report_file_path = os.path.join(src_directory, 'agent_output', 'procurement_report.html')
    
    # Remove old report file if exists
    if os.path.exists(report_file_path):
        os.remove(report_file_path)
        print("Removed old report file")
    
    # API request setup
    api_url = "http://0.0.0.0:5000/api/get_procurement_review"
    test_payload = {
        "product_name": "Gaming Laptop",
        "websites_list": ["amazon.com"],
        "country_name": "Egypt",
        "no_keywords": 3,
        "language": "English"
    }
    
    print("Starting agent test")
    
    try:
        # Call the API
        response = requests.post(api_url, data=test_payload, timeout=300)
        
        # Check API response
        assert response.status_code == 200, f"API call failed with status: {response.status_code}"
        print("API call successful")
        
        # Wait for file creation
        time.sleep(2)
        
        # Check if report file exists
        assert os.path.exists(report_file_path), f"Report file not found at: {report_file_path}"
        print("Report file created")
        
        # Check file has content
        file_size = os.path.getsize(report_file_path)
        assert file_size > 0, "Report file should not be empty"
        print(f"Report file size: {file_size} bytes")
        
        
        print("Test passed")
        
    except requests.exceptions.ConnectionError:
        pytest.skip("API server not running")
    except requests.exceptions.Timeout:
        pytest.fail("Agent timeout after 5 minutes")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")

if __name__ == '__main__':
    """Run test directly."""
    test_agent_creates_procurement_report()