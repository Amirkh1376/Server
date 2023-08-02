from tkinter import filedialog
import sys
import math 
import numpy as np
import requests
import Matplotlib
from scipy import optimize

# Generate an array of 10 random integers between 1 and 100
random_data = np.random.randint(1, 100, 10)
print("Random Data:", random_data)

# Make a GET request to a public API and retrieve data
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print("\nAPI Response:")
    print("User ID:", data['userId'])
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Failed to fetch data from the API.")