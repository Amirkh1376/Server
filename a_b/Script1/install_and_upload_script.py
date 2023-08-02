
try:
    subprocess.call(['python', '-m', 'pip', 'install', '--quiet', '--upgrade', 'pip']) # Update pip to the latest version
    current_version = pip.__version__ # Check the installed version of pip
    # Fetch the latest version of pip from PyPI
    url = 'https://pypi.org/pypi/pip/json'
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    parsed_data = json.loads(data)
    latest_version = parsed_data['info']['version']

    # Compare installed version with the latest version
    if latest_version == current_version:
        print("pip is up-to-date with the latest version", latest_version)
    else:
        print("pip is not up-to-date. Installed version is", current_version, "and latest version is", latest_version)
       
except Exception as e:
    print("An error occurred:", e)

imports = ['numpy', 'requests']
for module_name in imports:
    try:
        module = __import__(module_name)
        print(f"Module '{module_name}' already imported.")
    except ImportError:
        print(f"Installing and importing module '{module_name}'...")
        try:
            pip.main(['install', module_name])
            module = __import__(module_name)  # Import the module after installation
            print(f"Module '{module_name}' installed and imported successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install and import module '{module_name}': {e}")
        except ImportError as e:
            print(f"Failed to import module '{module_name}': {e}")

    