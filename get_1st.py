import requests
import lxml
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import warnings
warnings.filterwarnings("ignore")   #忽略警告

cookie=''
def getCode(code_file_name):
    with open(code_file_name, encoding='utf-8') as file_obj:
        return file_obj.read()

def judge(username,password,prob_url):  #操作浏览器自动完成登录并获取cookie与倒计时时间
    global cookie   #改变全局的cookie变量
    url=prob_url
    driver=webdriver.Chrome()
    driver.get(url)
    try:
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.CLASS_NAME, 'accountLogin')))
    except Exception as e:
        print(e)
    account_ele=driver.find_element_by_class_name("accountLogin")
    ActionChains(driver).move_to_element(account_ele).click(account_ele).perform()
    username_ele=driver.find_element_by_xpath('//input[@type="text"]')
    password_ele=driver.find_element_by_xpath('//input[@type="password"]')
    submit_ele=driver.find_element_by_xpath('//button[@class="btn ivu-btn ivu-btn-error ivu-btn-long ivu-btn-large"]')
    username_ele.send_keys(username)
    password_ele.send_keys(password)
    submit_ele.click()
    try:
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, '//strong[@data-v-3c70514d]')))
    except Exception as e:
        print(e)
    cookie=driver.get_cookies()[0]['value']
    time_ele=driver.find_element_by_xpath('//strong[@data-v-3c70514d]')
    for i in range(60): #该循环最多执行1min（约）
        if(time_ele.text=='0:00:00'):   #设置定时提交的时间
            return True
        time.sleep(1)
    return False

def submit(submit_url,username,password,code_file_name,prob_url):
    try:
        json={
            "code":getCode(code_file_name),
            "contestId":str(prob_url.split('/')[4]),  #contest的编号
            "judgeTemplateId":"6",  #默认使用c++提交，6是SDUOJ平台对于c++的编号
            "problemCode":"1"  #一次contest中的题目的编号，一般来说A题对应1，B题对应2，以此类推
            }
        if(judge(username,password,prob_url)==True):
            headers={
                #默认使用的是google浏览器的User-Agent
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "cookie":"SESSION="+cookie    #cookie值会经常改变，及时更新
                }
            r=requests.post(submit_url,headers=headers,json=json)
            r.raise_for_status()
            r.encoding='utf-8'
            return r.text
        else: return "Doesn't submit."
    except Exception as e:
        return e

submit_url="https://oj.qd.sdu.edu.cn/api/contest/createSubmission"
code_file_name='code.txt'   #存放待提交的code的文件名，应确保处于同一目录下
print("请输入题目的url：", end='')
prob_url=input()    #这里的url应类似于：https://oj.qd.sdu.edu.cn/contest/91/overview ，即是一个contest的overview页面
print("请输入当前用户的username：", end='')
username=input()
print("请输入当前用户的password：", end='')
password=input()
print(submit(submit_url,username,password,code_file_name,prob_url))