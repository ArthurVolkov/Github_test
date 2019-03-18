# Import the necessary tools and open the website:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
import time
text_url = open("C:/Python test/text_url.txt", "w")     # Create text file to save url


# A. Registration screen
def registration_screen():
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
    driver.find_element_by_class_name("seperator-link").click()     # Click on "כניסה\הרשמה"
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
    driver.find_element_by_class_name("text-btn").click()   # Click on "הרשמה"
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
    registration_field = driver.find_elements_by_class_name("ember-text-field")    # Find text field
    registration_field[0].send_keys("Arthur")   # Enter the first name
    registration_field[1].send_keys("Arthur54321@gmail.com")   # Enter E-Mail
    registration_field[2].send_keys("Password5")   # Enter the password
    registration_field[3].send_keys("Password5")   # Confirm the password
    driver.find_element_by_class_name("ember-checkbox").send_keys(Keys.SPACE)   # Agree with terms and conditions
    driver.find_element_by_class_name("ui-btn").click()     # Click on submit button "הרשמה"
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url


# B. Home Screen:
def home_screen():
    time.sleep(3)  # Waiting until elements would be clickable
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
    driver.find_elements_by_class_name("chosen-single")[0].click()  # Click on price range list
    driver.find_elements_by_class_name("active-result")[3].click()  # Chose the price
    driver.find_elements_by_class_name("chosen-single")[1].click()  # Click on area list
    driver.find_elements_by_class_name("active-result")[1].click()  # Chose the area
    driver.find_elements_by_class_name("chosen-single")[2].click()  # Click category list
    driver.find_elements_by_class_name("active-result")[10].click()  # Chose the category
    driver.find_element_by_class_name("ui-btn").click()  # Click on search button
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url


# C. Choose business screen:
def business_screen():
    time.sleep(2)   # Waiting until elements would be clickable
    driver.find_elements_by_class_name("card-item")[2].click()  # Chose the business
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
    driver.find_element_by_class_name("input-cash").send_keys("500")    # Enter the price
    driver.find_element_by_class_name("input-cash").send_keys(Keys.ENTER)    # Confirm the choice
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url


# D. Sender & Receiver information screen:
def sender_receiver_info():
    driver.find_elements_by_class_name("circle")[0].click()     # Click on radio button "למישהו אחר"
    input_field = driver.find_elements_by_class_name("ui-input")    # Find input field
    input_field[0].send_keys("Bill Gates")   # Enter the name of receiver
    input_field[1].send_keys("Arthur")   # Enter the name of sender
    blessing_field = driver.find_elements_by_class_name("ui-textarea")  # Find blessing field
    blessing_field[0].send_keys("Happy Birthday!")   # Enter the blessing
    driver.find_element_by_name("fileUpload").send_keys("C:/Python test/png.png")   # Uploading the picture
    driver.find_elements_by_class_name("chosen-single")[6].click()  # Click on events list
    driver.find_elements_by_class_name("active-result")[2].click()  # Chose the event
    driver.find_element_by_xpath("//textarea[@rows='4']").clear()   # Clear the the area for blessing from template
    blessing_field[0].send_keys("Happy Birthday!")   # Enter the blessing again
    driver.find_element_by_class_name("send-now").click()   # Click on radio button "מיד אחרי התשלום"
    driver.find_elements_by_class_name("btn-send-option-inner")[0].click()  # Click on SMS option
    input_phone = driver.find_elements_by_class_name("input-theme")    # Find input phone field
    input_phone[0].send_keys("0501234567")    # Enter the sender telephone number
    input_phone[1].send_keys("0507654321")    # Enter the receiver telephone number
    driver.find_element_by_class_name("btn-save").click()   # Click on "save" button
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url


# Calling for functions to start test:


driver = webdriver.Chrome(executable_path="C:/ChD/chromedriver.exe")
driver.implicitly_wait(10)    # Set the time to waiting for elements
driver.get("http://buyme.co.il")    # Open the website
driver.maximize_window()    # Full screen
text_url.write(driver.current_url), text_url.write("\n")  # Save current url


if __name__ == '__main__':
    registration_screen()

if __name__ == '__main__':      # Find business options
    home_screen()

if __name__ == '__main__':      # Choose the business
    business_screen()

if __name__ == '__main__':      # Enter sender and receiver info
    sender_receiver_info()
    driver.find_element_by_class_name("submit-wrapper").click()     # Click on "pay" button
    time.sleep(3)   # Waiting until elements would be clickable
    driver.find_element_by_class_name("submit-wrapper").click()     # Is necessary click on "pay" button again
    text_url.write(driver.current_url), text_url.write("\n")  # Save current url
driver.quit()   # Close the page


# Extras:
# Home screen:
# Open website:
driver = webdriver.Chrome(executable_path="C:/ChD/chromedriver.exe")
driver.implicitly_wait(10)      # Set the time to waiting for elements
driver.get("http://buyme.co.il")    # Open the website
driver.maximize_window()    # Full screen
text_url.write(driver.current_url), text_url.write("\n")  # Save current url


driver.find_element_by_class_name("seperator-link").click()     # Click on "כניסה\הרשמה"
text_url.write(driver.current_url), text_url.write("\n")  # Save current url
driver.find_element_by_class_name("ui-btn").click()     # Click on submit button "הרשמה"
text_url.write(driver.current_url), text_url.write("\n")  # Save current url


# Validate error messages:
error_messages = driver.find_elements_by_class_name("parsley-required")     # Find elements to check
try:
    for error in error_messages:
        assert error.text == "כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה"
except AssertionError:
    print("Error message is not validated")
text_url.write(driver.current_url), text_url.write("\n")  # Save current url


time.sleep(1)
driver.back()   # Back to gift screen
text_url.write(driver.current_url), text_url.write("\n")  # Save current url
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scroll to the bottom of the screen
driver.get_screenshot_as_file("C:/Python test/screenshot.png")  # Taking the screenshot


# Sender & Receiver information screen


if __name__ == '__main__':      # Find business options
    home_screen()

if __name__ == '__main__':      # Choose the business
    business_screen()

if __name__ == '__main__':      # Enter sender and receiver info
    sender_receiver_info()


rgb = driver.find_element_by_class_name("step-title").value_of_css_property("color")    # Find the "step" element
print(Color.from_string(rgb).hex)   # Print the elements color in "hex" format


# Validate sender information:
sender_name = driver.find_elements_by_class_name("name")[1]     # Find element to check
try:
    assert sender_name.text == "Arthur"
except AssertionError:
    print("Sender name is not validated")


# Validate receiver information:
receiver_name = driver.find_elements_by_class_name("name")[0]   # Find element to check
try:
    assert receiver_name.text == "Bill Gates"
except AssertionError:
    print("Receiver name is not validated")


# Validate blessing information:
blessing = driver.find_element_by_class_name("card-text")   # Find element to check
try:
    assert blessing.text == "Happy Birthday!"
except AssertionError:
    print("Blessing is not validated")


print("Arthur")
