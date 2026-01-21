class LOGIN:
    un='//input[@name="username"]'
    pwd='//input[@name="password"]'
    sub="//button[text()=' Login ']"
    def __init__(self,driver):
        self.driver=driver
    def username_text(self,username):
        self.driver.find_element('xpath',self.un).send_keys(username)
    def password_text(self,password):
        self.driver.find_element('xpath',self.pwd).send_keys(password)
    def submit(self):
        self.driver.find_element('xpath',self.sub).click()
    def clear_data(self,path):
        self.driver.find_element('xpath',path).clear()
    def login_orange_hrm(self,username,password):
        self.driver.find_element('xpath', self.un).clear()
        self.driver.find_element('xpath', self.un).send_keys(username)
        self.driver.find_element('xpath', self.pwd).clear()
        self.driver.find_element('xpath', self.pwd).send_keys(password)
        self.driver.find_element('xpath',self.sub).click()