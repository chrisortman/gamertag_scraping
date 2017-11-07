import urllib.request
from urllib.parse import urlparse

def generate_urls():
    url_template = "https://www.xboxgamertag.com/leaderboards/"
    urls = []
    for page in range(1720,1800):
        new_url = url_template + str(page) + "/"
        urls.append(new_url)
    return urls

def download_url(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')

def save_file(filename, contents):
   the_file = open(filename,"w")
   the_file.write(contents)
   the_file.close()

def filename_for(url):
   parsed = urlparse(url)
   return parsed.path.split("/")[-2] + ".html"

def main():
    urls = generate_urls()
    for url in urls:
        contents = download_url(url)
        filename = filename_for(url)
        save_file(filename, contents)
main()
