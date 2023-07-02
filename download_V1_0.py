from urllib.request import urlopen

def download_file(url):
    # Download from URL
    with urlopen(url) as file:
        content = file.read()

    url_parts = url.split("/") # Split the URL by "/"
    url_part1 = url_parts[-1].split(".")[0] # Extract the word between the last "/" and "."
    url_part2 = url_parts[-1].split(".")[1] # Extract the word after "."
    save_as = url_part1 + "." + url_part2
 
    # Save to file
    with open(save_as, 'wb') as download:
        download.write(content)

# url = "https://raw.githubusercontent.com/Amirkh1376/Server/Test/sum.py"
# url = "https://raw.githubusercontent.com/Amirkh1376/Server/Test/Sum_Discription.txt"
# url = "https://raw.githubusercontent.com/Amirkh1376/Server/Test/sum_rar.zip"
# download_file(url)