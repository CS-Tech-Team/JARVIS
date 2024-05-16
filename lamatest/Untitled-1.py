import requests
from bs4 import BeautifulSoup

res=requests.get("https://www.google.com/search?gs_ssp=eJzj4tLP1TcwqypITzIyYPTiTk_MSSxJLE4sSqwEAGJwCDs&q=galatasaray&oq=glatasa&gs_lcrp=EgZjaHJvbWUqDwgCEC4YChiDARixAxiABDIGCAAQRRg5MgYIARBFGEAyDwgCEC4YChiDARixAxiABDIMCAMQABgKGLEDGIAEMgkIBBAAGAoYgAQyDAgFEAAYChixAxiABDISCAYQABgKGIMBGLEDGIAEGIoFMg8IBxAuGAoYgwEYsQMYgATSAQgyOTE4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
soup=BeautifulSoup(res.content,"html.parser")
soup2=soup
print(soup2)
print(soup2.find("div",class_="search"))