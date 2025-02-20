from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Open Web3 Instagram-like app
driver.get("https://your-web3-instagram-clone.com")
time.sleep(5)

# Click on MetaMask login button (Modify XPath if needed)
try:
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login with MetaMask')]")
    login_button.click()
    time.sleep(5)
except Exception as e:
    print("Error clicking login button:", e)

# Upload an image post
try:
    upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    upload_input.send_keys("C:/path/to/your/image.jpg")  # Replace with your image path
    time.sleep(2)
    
    post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Post')]")
    post_button.click()
    time.sleep(5)
except Exception as e:
    print("Error uploading post:", e)

# Like the first post
try:
    like_button = driver.find_element(By.XPATH, "//button[contains(text(),'Like')]")
    like_button.click()
    time.sleep(3)
except Exception as e:
    print("Error clicking like button:", e)

# Close the browser
driver.quit()

