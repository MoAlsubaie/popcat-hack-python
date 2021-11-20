from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def open():
    num = 0 
    while True :
        driver = webdriver.Chrome()
        driver.get('https://popcat.click/')
        button = driver.find_element_by_id('app')
        for i in range(400):
            num=num+1
            button.click()
            print(num)
        driver.close()
    


if __name__ == '__main__':
    open()
