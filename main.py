import requests
import bs4
import io


# appends the chapter from the url to the text file.
def append_chapter(file, url):
    try:
        novel_site_req = requests.get(url)
        novel_site_req.raise_for_status()
        html = novel_site_req.text
        entry_content = bs4.BeautifulSoup(html, features="lxml").select(".entry-content")[0]
        novel_text = entry_content.select('p')
        for i in range(len(novel_text)):
            file.write(str(novel_text[i].text) + "\n")
        file.write("\n\n\n")
        print("Successfully appended {}".format(url))
        list_of_links = entry_content.select("a")
        for link in list_of_links:
            if link.text.strip() == 'Next Chapter':
                return link.get("href")
        return None
    except Exception as error_message:
        print("There was a problem. {}".format(error_message))


f = io.open("weakestMage.txt", "a", encoding="utf-8")
current_url = "https://isekailunatic.com/2020/02/12/wm-prologue-1-a-class-stranded/"
while current_url is not None:
    current_url = append_chapter(f, current_url)