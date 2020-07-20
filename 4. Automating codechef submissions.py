#first pip install selenium
#then install webdriver for your web browser. extract zip. copy path to .exe file


from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\SeleniumDrivers\chromedriver.exe")

#starting of browser session
browser=webdriver.Chrome()

#opening codechef link in the browser
browser.get("https://codechef.com")

#Username entry
username_element=browser.find_element_by_id("edit-name")
username_element.send_keys("USER NAME")

#Password entry
password_element=browser.find_element_by_id("edit-pass")
password_element.send_keys("PASSWORD")              #or import if ou dont want to show it (getpass as in video)

#submitting username and password
browser.find_element_by_id("edit-submit").click()

#Opening the submission page for the problem
browser.get("https://www.codechef.com/submit/PROBLEM-NAME")

#for slow internet connection
time.sleep(10)

#for opening toggle editor
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#solution is the file the user wants to submit as solution to the problem

with open("solution.cpp.txt",'r') as f:
    code=f.read()
code_element=browser.find_element_by_id('edit-program')
code_element.send_keys(code)

#replace i with language option the solution is to be submitted in
browser.find_element_by_xpath('//*[@id="edit-language"]/option[i]')

#to click on submit button
browser.find_element_by_id("edit-submit").click()