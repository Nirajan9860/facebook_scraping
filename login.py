from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Set your Facebook username and password
username = 'romanojhaojha1@gmail.com'
passwd = 'RRoommee88$$'

#disable notification
option = Options()
option.add_argument('--disable-notifications')

# Initialize the Chrome WebDriver

chromedriver_path = './chromedriver-win64/chromedriver'
chrome_service = Service(chromedriver_path)
driver = webdriver.Chrome(service=chrome_service,options=option)
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


def scroll_page(driver, pixels):
    driver.execute_script(f"window.scrollBy(0, {pixels});")

# def print_element_text(element, css_selector, message):
    # elements = element.find_elements(By.CSS_SELECTOR, css_selector)
    # if elements:
    #         print(f"{message}:{elements[0].text}")
    # else:
    #     print(f"{message}:Null")

# def get_element_text(element, selector):
    # elements = element.find_elements(By.CSS_SELECTOR, selector)
    # if elements:
    #     return elements[0].text
    # return None

# def process_element(element, driver):

    hover_element = element.find_element(By.CSS_SELECTOR, '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm')
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    
    date_elem_text = get_element_text(element, ".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")
    if date_elem_text:
        print(date_elem_text)
    
    caption_elem_text = get_element_text(element, ".x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13")
    if caption_elem_text:
        print(caption_elem_text)
    
    like_elem_text = get_element_text(element, ".xt0b8zv.x1e558r4")
    if like_elem_text:
        print(f"like_count:{like_elem_text}")

    comment_elem_text = get_element_text(element, ".x1yrsyyn:nth-child(2) .xo1l8bm")
    if comment_elem_text:
        print(f"comment_count:{comment_elem_text}")

    share_elem_text = get_element_text(element, ".x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm")
    if share_elem_text:
        print(f"share_count:{share_elem_text}")

    print("*-------------------------------------------------------------------------*")

css_selectors = [
    ('.x1heor9g.xo1l8bm span', 'Date'),
    ('.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13', 'Caption'),
    ('.xt0b8zv.x1e558r4', 'Like Count'),
    ('.x1yrsyyn:nth-child(2) .xo1l8bm', 'Comment Count'),
    ('.x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm', 'Share Count')
]


def process_element(element):
    for css_selector, label in css_selectors:
        elems = element.find_elements(By.CSS_SELECTOR, css_selector)
        if elems:
            if label == 'Date':
                hover_element = elems[0]
                actions = ActionChains(driver)
                actions.move_to_element(hover_element).perform()
                time.sleep(3)
                date_elem = WebDriverWait(element, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")))
                print(f"{label}: {date_elem.text}")
            else:
                for elem in elems:
                    print(f"{label}: {elem.text}")

        print("*-------------------------------------------------------------------------*")






try:
      
    # Scroll the page and extract data
    scroll_pause_time = 10  # Adjust this value based on your needs
    screen_height = driver.execute_script("return window.screen.height;")
    # print(screen_height)
    start=0
    while True:
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
        
        
        # # Assuming div_elements is a list of WebElement objects
        # for element in div_elements:
        #     process_element(element, driver)
        # see_more = caption_elem.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "x126k92a", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1s688f", " " ))]')
        #         if see_more:
        #             for see in see_more:
        #                 see.click()

        div_elements = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')

        for element in div_elements:
            process_element(element)
        
        

        # Process extracted data from the div list
        # for element in div_elements:
            

        #     if not element.find_elements(By.CSS_SELECTOR,'.x1heor9g.xo1l8bm span'):
        #         continue
        #     else:
        #         hover_element =  element.find_element(By.CSS_SELECTOR,'.x1heor9g.xo1l8bm span')
        #         actions = ActionChains(driver)
        #         actions.move_to_element(hover_element).perform()
        #         time.sleep(3)
        #         date_elem = driver.find_element(By.CSS_SELECTOR,".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")
        #         print(date_elem.text)

        #     if not element.find_elements(By.CSS_SELECTOR,".x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13"):                
        #         continue
                
        #     else:
        #         caption_elem = element.find_element(By.CSS_SELECTOR,".x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13")
        #         see_more = caption_elem.find_elements(By.CSS_SELECTOR,".x126k92a .x1s688f")
        #         # print(len(see_more))
        #         if see_more:
        #             for see in see_more:
        #                 see.click()
            
        #         print(caption_elem.text)

        #     if not element.find_elements(By.CSS_SELECTOR,".xt0b8zv.x1e558r4"):
        #         continue
        #     else:
        #         like_elem = element.find_element(By.CSS_SELECTOR,".xt0b8zv.x1e558r4")
        #         print(f"like_count:{like_elem.text}")


              
                

           


        #     if not element.find_elements(By.CSS_SELECTOR,".x1yrsyyn:nth-child(2) .xo1l8bm"):
        #         continue
        #     else:
        #         comment_elem = element.find_element(By.CSS_SELECTOR,".x1yrsyyn:nth-child(2) .xo1l8bm")
        #         print(f"comment_count:{comment_elem.text}")

        #     if not element.find_elements(By.CSS_SELECTOR,".x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm"):
        #         continue
        #     else:
        #         share_elem = element.find_element(By.CSS_SELECTOR,".x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm")
        #         print(f"share_count:{share_elem.text}")

            

            

        #     print("*-------------------------------------------------------------------------*")
            

        

        # css_selectors = [(".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm","hover"),
        #                  (".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl","date"),
        #                  (".x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13", "Caption"),
        #          (".xt0b8zv.x1e558r4", "like_count"),
        #          (".x1yrsyyn:nth-child(2) .xo1l8bm", "comment_count"),
        #          (".x1yrsyyn~ .x1yrsyyn+ .x1yrsyyn .xo1l8bm", "share_count")]

        # for element in div_elements:
        #     for css_selector, message in css_selectors:
        #         print_element_text(element, css_selector, message)
        #     print("*-------------------------------------------------------------------------*")

        

        


            
        
   
    
                
except Exception as e:
    print("Element not found or error occurred:", e)

driver.quit()



