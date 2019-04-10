import time

from selenium import webdriver
from selenium.webdriver import ActionChains

def web_main():
    driver=webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')
    driver.implicitly_wait(10)

    driver.get('https://able.gosafenet.com/')


    driver.find_element_by_css_selector("[type='text']").send_keys('system')
    driver.find_element_by_css_selector("[type='password']").send_keys("1")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='el-button btn-login el-button--primary el-button--small']").click()


    m1=driver.find_element_by_css_selector('.overall-middle-container ul>li:nth-of-type(2)')
    ActionChains(driver).move_to_element(m1).perform()
    time.sleep(1)
    m2=driver.find_element_by_css_selector("body>div li:nth-of-type(6)")
    ActionChains(driver).move_to_element(m2).perform()
    time.sleep(1)
    m3=driver.find_element_by_css_selector("body>div li:nth-of-type(6) ul span")
    ActionChains(driver).move_to_element(m3).perform()

    time.sleep(1)
    m3.click()
    time.sleep(1)

    newm=driver.find_element_by_css_selector('.leftOperate>button:nth-of-type(2)')
    ActionChains(driver).move_to_element(newm).perform()
    time.sleep(1)
    driver.find_element_by_css_selector('.leftOperate>button:nth-of-type(2) span').click()
    input(...)

    driver.quit()




def global_test1():
    global gv
    gv=111
    print(gv)

def global_test2():
    print(gv)

if __name__ == '__main__':
    global_test1()
    global_test2()