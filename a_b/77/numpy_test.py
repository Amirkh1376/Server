# import subprocess
# import json
# import urllib.request
# from importlib import import_module

# # Check and update pip
# try:
#     subprocess.call(['python', '-m', 'pip', 'install', '--quiet', '--upgrade', 'pip'])
# except Exception as e:
#     print("An error occurred while updating pip:", e)

# # Check installed pip version
# try:
#     import pip
#     current_version = pip.__version__
#     url = 'https://pypi.org/pypi/pip/json'
#     response = urllib.request.urlopen(url)
#     data = response.read().decode()
#     parsed_data = json.loads(data)
#     latest_version = parsed_data['info']['version']
#     if latest_version == current_version:
#         print("pip is up-to-date with the latest version", latest_version)
#     else:
#         print("pip is not up-to-date. Installed version is", current_version, "and latest version is", latest_version)
# except ImportError:
#     print("Unable to import pip.")

# # Check and install required modules
# # required_modules = ['numpy', 'requests']
# required_modules = ['numpy']
# for module_name in required_modules:
#     try:
#         import_module(module_name)
#         print(f"Module '{module_name}' already imported.")
#     except ImportError:
#         print(f"Installing and importing module '{module_name}'...")
#         try:
#             subprocess.call(['python', '-m', 'pip', 'install', '--quiet', module_name])
#             import_module(module_name)
#             print(f"Module '{module_name}' installed and imported successfully.")
#         except Exception as e:
#             print(f"Failed to install and import module '{module_name}': {e}")


import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform basic operations
mean_value = np.mean(arr)  # Calculate the mean of the array
sum_value = np.sum(arr)    # Calculate the sum of the array

# Print the results
print("Array:", arr)
print("Mean:", mean_value)
print("Sum:", sum_value)
