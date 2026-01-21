import time
from Pages.Login_page import LOGIN
from Utilities.Login_data import read_login_data
path= r'C:\Users\HP\PycharmProjects\HYBRID\Test_data\DDT_Login_hrm.xlsx'
def test_login(setup):
    driver=setup
    driver.get(r'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    l=LOGIN(driver)
    data=read_login_data(path)
    for un,pwd in data:
        l.login_orange_hrm(un,pwd)
        time.sleep(2)
        if "dashboard" not in driver.current_url:
            driver.save_screenshot(r'C:\Users\HP\PycharmProjects\HYBRID\Screenshots\Login_failed.png')
            print("Login Failed")
        else:
            print('Login passed')
            time.sleep(2)
            # driver.back()
            driver.find_element('xpath','//span[@class="oxd-userdropdown-tab"]').click()
            driver.find_element('xpath',"//a[text()='Logout']").click()