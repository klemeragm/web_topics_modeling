from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url='https://www.amazon.com.br/?tag=lomadee0850014813-20&ascsubtag=226536395456z7897z1601958348216&lmdsid=482136395456-7897-1601958348216'
driver.get(url)

driver.get(url)
MaisVendidosemLojaKindle = driver.find_element_by_xpath(
    '//*[@id="dp"]')

SugestaoPromocao= driver.find_element_by_xpath(
    '//*[@id="promoted-suggestion"]/span/span[1]/a[1]')

bookPrice = driver.find_element_by_xpath('//*[@id="stores"]')
        
f = open('mytextfile.txt', 'w')
f.write('Mais Vendidos em Loja Kindle: ' + MaisVendidosemLojaKindle.text +' \n')
f.write('Sugestao: ' + SugestaoPromocao.text +' \n')
f.write('Book Price: ' + f.write('Book Price: ' + bookPrice.text +' \n').text +' \n')
f.close()

pass