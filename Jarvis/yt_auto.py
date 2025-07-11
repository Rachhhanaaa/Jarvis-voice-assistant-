import webbrowser

def music(query):
    """
    This function searches for a song on YouTube and opens it in a browser.
    It takes the query as an argument (song name).
    """
    print(f"Searching for {query} on YouTube...")
    song_query = query.replace("play", "").strip()
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_query}")