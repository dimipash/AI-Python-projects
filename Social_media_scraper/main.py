from bs4 import BeautifulSoup
import csv

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def extract_posts(soup):
    posts = []
    post_elements = soup.find_all("div", class_="post")
    for post in post_elements:
        username = post.find("h2", class_="username").text.strip()
        content = post.find("p", class_="content").text.strip()
        timestamp = post.find("span", class_="timestamp").text.strip()
        posts.append({"username": username, "content": content, "timestamp": timestamp})
    return posts

def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "content", "timestamp"])
        writer.writeheader()
        writer.writerows(posts)  

def main():
    print("This is a module for extracting social media posts. Please import and use the functions as needed.")
    hrml_content = load_html("social_media.html")
    soup = BeautifulSoup(hrml_content, "html.parser")
    posts = extract_posts(soup)
    save_posts_to_csv(posts, "social_media_posts.csv")
    print("Posts saved to social_media_posts.csv")

if __name__ == "__main__":
    main()

# html_content = load_html("social_media.html")
# soup = BeautifulSoup(html_content, "html.parser")
# posts = extract_posts(soup)
# save_posts_to_csv(posts, "social_media_posts.csv")
# print("Posts saved to social_media_posts.csv")