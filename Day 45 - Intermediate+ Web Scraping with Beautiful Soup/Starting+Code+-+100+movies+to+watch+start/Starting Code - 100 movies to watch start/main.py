import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

try:
    # Fetch the webpage with a timeout and handle potential errors
    response = requests.get(url=URL, timeout=20)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx/5xx)
except requests.exceptions.RequestException as re:
    print(f"Error fetching the webpage: {re}")
else:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all h3 tags with the class "title" and reverse the list
    title_tags = soup.find_all(name="h3", class_="title")
    titles = [f"{title.get_text()}\n" for title in title_tags[::-1]]

    # Write the movie titles to a text file with UTF-8 encoding
    with open("movies.txt", "w", encoding="UTF-8") as file:
        file.writelines(titles)

    print("Movie titles successfully written to movies.txt")
