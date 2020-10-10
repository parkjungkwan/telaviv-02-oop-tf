from bs4 import BeautifulSoup
from urllib.request import urlopen
 
class Model():
    def exec(self,inputurl):
        url = urlopen(inputurl)
        soup = BeautifulSoup(url, 'lxml')
        cnt_artist = 0
        ctn_title = 0
        artist =[]
        title =[]
        list =[]
        for link1 in soup.find_all(name="p",attrs=({"class":"artist"})):
            cnt_artist += 1
            artist.append(str(cnt_artist)+"위"+link1.find('a').text)
 
        for link2 in soup.find_all(name="p",attrs=({"class":"title"})):
            title.append(link2.text)
        
        for i in range(100):
            list.append(str(artist[i])+" "+str(title[i]))
 
        return list