'''O seu chefe precisa estar constantemente monitorando alguns sites para saber onde ele pode comprar 
pelo menor preço um determinado produto, sua responsabilidade e de fornecer uma planilha com os preços 
todos os dias, de pelo menos 3 sites para que ela possa decidir de onde comprar aquele determinado produto.
 O produto que preciso saber qual está mais barato é o abacate.'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from time import sleep

# abrir o navegador
opening_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
sleep(5)
# encontrar onde está o abacate no site
#1
opening_browser.get('https://sitepreco1.netlify.app/')
sleep(3)
preco_site1 = opening_browser.find_elements(By.XPATH,'//h6[@class="price_heading"]')
preco_final_site1 = preco_site1[3].text.split(' ')[1]
sleep(3)
#2
opening_browser.get('https://sitepreco2.netlify.app/')
sleep(3)
preco_site2 = opening_browser.find_elements(By.XPATH,'//h5')
preco_final_site2 = preco_site2[3].text.split('$')[1]
sleep(3)
#3
opening_browser.get('https://sitepreco3.netlify.app/')
sleep(3)
preco_site3 = opening_browser.find_elements(By.XPATH,'//div[@class="featured__item__text"]//h5')
preco_final_site3 = preco_site3[2].text.split('$')[1]
with open('PrecoAbacate.csv','w',newline='',encoding='utf-8') as arquivo:
    arquivo.write(f'Site,Valor{os.linesep}')
    arquivo.write(f'https://sitepreco1.netlify.app/,{preco_final_site1}{os.linesep}')
    arquivo.write(f'https://sitepreco2.netlify.app/,{preco_final_site2}{os.linesep}')
    arquivo.write(f'https://sitepreco3.netlify.app/,{preco_final_site3}{os.linesep}')  
  