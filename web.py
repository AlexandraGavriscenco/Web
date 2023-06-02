from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")

driver.maximize_window()

e = "text@yahoo.com"
p = "parola123"

email = driver.find_element_by_xpath("//*[@id='email']")
email.send_keys(e)


parola = driver.find_element_by_xpath("//*[@id='pass']")
parola.send_keys(p)

