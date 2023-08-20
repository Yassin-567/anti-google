from googlesearch import search

query = "breaking bad 360p.mp4"

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)