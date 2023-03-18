import webbrowser as web

question = input("Enter your question here:  ")

urls = [
            f"https://google.com/search?q={question}",
            f"https://youtube.com/results?search_query={question}",
            f"https://github.com/search?q={question}&type=Respositories",
            f"https://stackoverflow.com/search?q={question}",
            f"https://docs.python.org/3/search.html?q={question}"
            ]

for url in urls:
    web.open(url)
