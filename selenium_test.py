from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Make sure you have the correct WebDriver installed)
driver = webdriver.Chrome()  # Change this to match your WebDriver (e.g., Firefox, Edge)

# Load the index.html file
driver.get("file:https://github.com/kaviraj2003/AWS-DevOps-Pipeline-Project1/blob/kavi/index.html")

# Wait for the page to load
time.sleep(2)

# Test: Check if the page title is correct
assert "DevOps with AWS" in driver.title, "Title does not match"

# Test: Check if the navbar is present
navbar = driver.find_element(By.ID, "myNavbar")
assert navbar.is_displayed(), "Navbar is not displayed"

# Test: Check if the "Learn more" button is present and clickable
learn_more_button = driver.find_element(By.LINK_TEXT, "Learn more and start today")
assert learn_more_button.is_displayed(), "Learn More button is not displayed"
learn_more_button.click()
time.sleep(2)

# Test: Check if the 'About' section is present
about_section = driver.find_element(By.ID, "about")
assert about_section.is_displayed(), "About section is not displayed"

# Test: Check if the 'Team' section is present
team_section = driver.find_element(By.ID, "team")
assert team_section.is_displayed(), "Team section is not displayed"

# Test: Check if social media icons exist
social_icons = driver.find_elements(By.CLASS_NAME, "fa")
assert len(social_icons) > 0, "Social media icons are missing"

# Close the browser
driver.quit()

print("All tests passed successfully!")
