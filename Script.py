#!/usr/bin/env python
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from multiprocessing import Process
from selenium.common.exceptions import NoSuchElementException
import threading


def login(myusername, mypassword):
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files (x86)\chrome-win\chrome.exe"
    chrome_driver_binary = r"C:\Users\ASUS\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    driver.get('https://www.instagram.com/')
    sleep(3)
    name = driver.find_element_by_name('username')
    name.send_keys(myusername)
    pas = driver.find_element_by_name('password')
    pas.send_keys(mypassword)
    login = driver.find_element_by_tag_name('button')
    login.submit()
    sleep(5)
    return driver

messages = [
    'Hey {0}, How you doing?',
    'Hello {0}, How are things?',
    "Hi {0}, How's your day?",
    # Add more messages here
]

def functions(url, driver):
    isDoneEverything = False
    comment=''
    driver.get(url)
    sleep(10)
    try:
        follow = driver.find_element_by_class_name('_aacl')
        if follow.text == 'Follow':
            follow.click()
        else:
            print('Already following')
        
        #liking
    
        driver.find_element_by_class_name('_aagw').click() #clicking on first post
        sleep(2)
        for i in range(2):
            title = driver.find_element_by_xpath("//span[@class='_aamw']/div/div/span")
            if title.get_attribute('innerHTML')[17:21] == 'Like':
                title.click()
            else:
                print('Post', i+1, 'is Already liked')
            try:
                driver.find_element_by_class_name('_aaqg').click()
                sleep(1)
            except Exception as e:
                comment=str(e)
                print('No next post')
                break
                #closing the posts
        close = driver.find_element_by_class_name('x160vmok')
        close.click()
        sleep(2)
        
        try:
            print('checking stories')
            driver.find_element_by_class_name("_aarg").click()
            while True:
                sleep(2)
                storylike = driver.find_elements_by_xpath("//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']")[3]
                title = driver.execute_script("return arguments[0].textContent;", storylike)
                if title == 'Like':
                    storylike.click()
                try:
                    nextele = driver.find_element_by_class_name('_9zm2')
                    nextele.click()
                except Exception as e:
                    comment=str(e)
                    print('No next story')
                    break
        except Exception as e:
            comment=str(e)
            print("User has no story")
        driver.refresh()
        sleep(10)
        driver.find_element_by_class_name('_aagw').click() #clicking on first post
        sleep(2)
        print('like comments')
        try:
            comments=driver.find_elements_by_xpath("//div[@class='xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk x15bjb6t x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd']")
            length = min(len(comments),3)
            for i in range(length):
                comments[i].click()
                sleep(2)
            close = driver.find_element_by_class_name('x160vmok')
            close.click()
            sleep(2)
        except Exception as e:
            comment=str(e)
            print('No comment')

        #firstname
        driver.refresh()
        sleep(5)
        name=driver.find_element_by_xpath("//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']")
        firstname= name.text.split(' ')[0]
        print(firstname)
        #message
        selected_message = random.choice(messages)
        message= selected_message.format(firstname)
        sleep(2)
        messageele = driver.find_element_by_xpath("//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1gjpkn9 x5n08af xsz8vos']")
        messageele.click()
        sleep(5)
        driver.find_element_by_xpath("//p[@class='xat24cr xdj266r']").send_keys(message)
        try:
            popup = driver.find_element_by_class_name('_a9-v')
            print(popup)
            notnow = driver.find_element_by_xpath("//button[@class='_a9-- _a9_1']")
            print(notnow.text)
            if notnow.text=='Not Now':
                notnow.click()
                sleep(2)
            sendmessage = driver.find_element_by_xpath("//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5']")
            if sendmessage.text == 'Send':
                sendmessage.click()
            sleep(5)
            print('DONE')
        except:
            sendmessage = driver.find_element_by_xpath("//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5']")
            if sendmessage.text == 'Send':
                sendmessage.click()
            sleep(5)
            print('DONE')
        isDoneEverything=True     
    except Exception as e:
        sleep(2)
        try:
            driver.find_element_by_class_name('_aacl').text=='Requested'
            print('Request sent but not a public account')
            sleep(5)
            comment = 'Request sent but not a public account'
        except Exception as ee:
            comment = str(ee)
    if isDoneEverything: comment=''
    #driver.close()
    return isDoneEverything, comment

def process_data(df, start_idx, end_idx, driver):
    print('in process')
    results = df.iloc[start_idx:end_idx].apply(lambda row: functions(row[df.columns[0]], driver), axis=1)
    df.loc[start_idx:end_idx, 'isDone'] = [result[0] for result in results]
    df.loc[start_idx:end_idx, 'Comment'] = [result[1] for result in results]
    
    
if __name__ == '__main__':
    print('In main')
    file_path = 'ig.csv'
    df = pd.read_csv(file_path)
    midpoint = len(df) // 2
    df1, df2 = df.iloc[:midpoint], df.iloc[midpoint:]
    driver1 = login('demoaccount1501', 'admin12345')
    driver2 = login('demoaccount1501', 'admin12345')
    thread1 = threading.Thread(target=process_data, args=(df1, 0, len(df1), driver1))
    thread2 = threading.Thread(target=process_data, args=(df2, 0, len(df2), driver2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Concatenate the results back into a single DataFrame if needed
    df = pd.concat([df1, df2])
    df.to_csv('Result.csv')
