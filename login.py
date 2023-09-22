from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv


# Set your Facebook username and password
username = 'romanojhaojha1@gmail.com'
passwd = 'RRoommee88$$'

#disable notification
option = Options()
option.add_argument('--disable-notifications')

# Initialize the Chrome WebDriver

chromedriver_path = './chromedriver-win64/chromedriver'
chrome_service = Service(chromedriver_path)
driver= webdriver.Chrome(service=chrome_service,options=option)
driver.get('https://www.facebook.com')
driver.implicitly_wait(5)



# Find the username and password input fields and enter your credentials
txtUsername = driver.find_element(By.ID, 'email')
txtUsername.send_keys(username)

txtPasswd = driver.find_element(By.ID, 'pass')
txtPasswd.send_keys(passwd)

# Find and click the login button
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Wait for a few seconds for the login to complete
time.sleep(5)

# Navigate to the desired Facebook page
url = "https://www.facebook.com/wlinknp"  # Replace with the URL of the Facebook page you want to visit
driver.get(url)

driver.implicitly_wait(5)



#For clicking in see more if present in caption
def see_more(elem):
    see_more = elem.find_elements(By.CSS_SELECTOR,".x126k92a .x1s688f")
    if see_more:
        for see in see_more:
            see.click()     
#iterate through post for extraction of date, caption, like_count, comment_count, share_count

def process_element(element,post_list):
    post_info = {}
    
    css_selectors = [
    ('.x1heor9g.xo1l8bm span', 'Date'),
    ('.xckqwgs.x26u7qi.x7g060r.x1gslohp.x11i5rnm.xieb3on.x1pi30zi.x1swvt13.x1d52u69','Blackquote'),
    ('.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13', 'Caption'),
    ('.xt0b8zv.x1e558r4', 'Like Count'),
    ('.x1yrsyyn:nth-child(2) .xo1l8bm', 'Comment Count'),
    ('.x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm', 'Share Count')
]
    for css_selector, label in css_selectors:
        # print(label)
        elems = element.find_elements(By.CSS_SELECTOR, css_selector)
        if elems:
            if label == 'Date':
                hover_element = elems[0]
                actions = ActionChains(driver)
                actions.move_to_element(hover_element).perform()
                time.sleep(5)
                date_elem = driver.find_element(By.CSS_SELECTOR,".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")
                post_info[label] = date_elem.text
                # print(f"{label}:{date_elem.text}")
                # date_elem = WebDriverWait(element, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")))
                # print(f"{label}: {date_elem.text}")
            else:
                for elem in elems:
                    if label == "Caption" or label == "Blackquote":
                        see_more(elem)
                    # elif label in ["Like Count","Comment Count","Share Count"]:
                    #     if elem.text is None:
                    #         print(f"{label}:0")
                    #         continue
                        # check_null(elem,label)
                    
                    post_info[label] = elem.text
                    # print(f"{label}: {elem.text}")
        else:
            post_info[label] = "0"
            # print(f"{label}:0")
    post_list.append(post_info)
    
    print("*-------------------------------------------------------------------------*")
    
try:
      
    # Scroll the page and extract data
    scroll_pause_time = 10  # Adjust this value based on your needs
    screen_height = driver.execute_script("return window.screen.height;")
    # print(screen_height)
    start=0
    
    while True:
        post_list = []
        # Extract data (replace with appropriate CSS selector)
        time.sleep(3)
        div_elements = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
        driver.implicitly_wait(3)
        # print(len(div_elements))
        


    # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

    # Check if we've reached the end of the page
        new_screen_height = driver.execute_script("return document.body.scrollHeight")
        # print(new_screen_height)
        if new_screen_height == screen_height:
            break
        screen_height = new_screen_height

    
    
        
        new_div_elements = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
        time.sleep(5)
        driver.implicitly_wait(3)
        if len(new_div_elements) == len(div_elements):
            break
        # Update the list of div elements
        end =len(new_div_elements)
        div_elements = new_div_elements[start:end]#*
        
        start = end 

        for element in div_elements:
            process_element(element,post_list)
        # print(len(post_list))
        
        csv_file_path = 'post_info.csv'

# Write data to a CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Date','Blackquote','Caption','Like Count','Comment Count','Share Count']  # Add more fields if needed
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()  # Write CSV header
            for row in post_list:
                writer.writerow(row)  # Write data rows
        
        

        

        

        


            
        
   
    
                
except Exception as e:
    print("Element not found or error occurred:", e)

driver.quit()



