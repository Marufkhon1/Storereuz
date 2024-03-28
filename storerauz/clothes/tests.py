from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from django.test import LiveServerTestCase

class StudentsFormTest(LiveServerTestCase):
    def test_form_submission(self):
        # Initialize the Chrome WebDriver
        selenium = webdriver.Chrome()

        # Choose your URL to visit
        selenium.get('http://127.0.0.1:8000/clothes/add_product/')

        # Find the elements you need to submit the form
        name_input = selenium.find_element(By.ID, "id_name")
        description_input = selenium.find_element(By.ID, 'id_description')
        category_input = selenium.find_element(By.ID, 'id_category')
        brand_input = selenium.find_element(By.ID, 'id_brand')
        price_input = selenium.find_element(By.ID, 'id_price')
        size_input = selenium.find_element(By.ID, 'id_size')
        color_input = selenium.find_element(By.ID, 'id_color')
        image_input = selenium.find_element(By.ID, 'id_image')
        submit_button = selenium.find_element(By.ID, 'id_submit')

        # Populate the form with data
        name_input.send_keys('Jeans')
        description_input.send_keys('This is a test product.')
        category_input.send_keys('Sleepwear')  # Replace with a valid category ID
        brand_input.send_keys('Gucci')  # Replace with a valid brand ID
        price_input.send_keys('29.99')
        size_input.send_keys('M Men')  # Replace with a valid size ID
        color_input.send_keys('Red')  # Replace with a valid color ID
        image_input.send_keys('C:\\Users\\mmman\\Downloads\\boy.jpg')  # Replace with a valid image path

        # Submit the form
        submit_button.click()

        # Wait for the success message or other expected behavior
        success_message = WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.success-message'))
        )

        # Check result; page source looks at the entire HTML document
        assert 'Product added successfully' in success_message.text

        # Clean up
        selenium.quit()
