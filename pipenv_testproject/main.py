# main.py
import requests

def get_website_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            # <title> etiketi varsa başlığı döndür
            return response.text.split('<title>')[1].split('</title>')[0]
        except IndexError:
            # <title> etiketi yoksa None döndür
            return None
    else:
        # URL'ye erişilemiyorsa None döndür
        return None

if __name__ == "__main__":
    title = get_website_title("https://www.google.com")
    if title:
        print(f"Website title: {title}")
    else:
        print("Could not retrieve website title.")