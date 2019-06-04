from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'https://read.qidian.com/chapter/atk0lq-ecYzdjrstIrF5-w2/HQkBFKNYNur4p8iEw--PPw2'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', class_ = 'read-content j_readContent') 
print(texts)