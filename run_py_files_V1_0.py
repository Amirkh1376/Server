import requests
import io
import sys

def fetch_contentÙ€py_files(url):
    
    response = requests.get(url) # Send a GET request to fetch the content
    if response.status_code == 200: # Check if the request was successful (status code 200)
        script_content = response.text # Access the content of the response
        stdout_capture = io.StringIO() # Capture stdout to a string
        sys.stdout = stdout_capture
        exec(script_content, globals()) # Execute the script
        sys.stdout = sys.__stdout__ # Restore stdout
        output = stdout_capture.getvalue() # Get the captured output as a string
    else:
        print("Failed to fetch the content. Status code:", response.status_code)
        output = ""

    return output

# # Raw GitHub URL of the .py file
# url = "https://raw.githubusercontent.com/Amirkh1376/Server/Test/sum.py"

# # Call the function to fetch the content
# fetch_contentÙ€py_files(url)