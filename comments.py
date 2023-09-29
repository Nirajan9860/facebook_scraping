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

# #disable notification
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
url = "https://www.facebook.com/DishHomeFibernetTimes"  # Replace with the URL of the Facebook page you want to visit
driver.get(url)

driver.implicitly_wait(5)



    


#For clicking in see more if present in caption
def see_more(elem):
    see_more = elem.find_elements(By.CSS_SELECTOR,".x126k92a .x1s688f")
    if see_more:
        for see in see_more:
            see.click() 
def extract_comments(element,css_selector):
    all_comments = [] 
    click_comment = element.find_elements(By.CSS_SELECTOR,css_selector)

    if click_comment:
        for commen in click_comment:
            driver.execute_script("arguments[0].click();", commen)  
        time.sleep(3) 
    # else:
    #     continue

        comments = driver.find_elements(By.CSS_SELECTOR,".xjkvuk6 .x1mh8g0r.x1vvkbs div")
        # see_more(comments)
        
        print(len(comments))
        for text in comments:
            all_comments.append(text.text)
        close = driver.find_element(By.CSS_SELECTOR,".x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.x14yjl9h.xudhj91.x18nykt9.xww2gxu.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1")
        close.click() 
        return all_comments

  
#iterate through post for extraction of date, caption, like_count, comment_count, share_count

def process_element(element,post_list):
    post_info = {}
    
    css_selectors = [
    ('.x1heor9g.xo1l8bm span', 'Date'),
    ('.x1w0mnb .xi81zsa','Comments')
]
    for css_selector, label in css_selectors:
        # print(label)
        elems = element.find_elements(By.CSS_SELECTOR, css_selector)
        if elems:
            if label == 'Date':
                # print(elems)
                hover_element = elems[0]
                # print(hover_element)
                actions = ActionChains(driver)
                actions.move_to_element(hover_element).perform()
                time.sleep(2)
                date_elem = driver.find_element(By.CSS_SELECTOR,".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")
                post_info[label] = date_elem.text
                print(f"{label}:{date_elem.text}")
                # date_elem = WebDriverWait(element, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".xu96u03.xm80bdy.x10l6tqk.x13vifvy.x47corl")))
            elif label == "Comments":
                    all_comments = extract_comments(element,css_selector)
                
                    post_info[label] = all_comments
        else:
            post_info[label] = "Nan"
                    
    
    post_list.append(post_info)
    
    print("*-------------------------------------------------------------------------*")

    
try:
      
    # Scroll the page and extract data
    scroll_pause_time = 5  # Adjust this value based on your needs
    screen_height = driver.execute_script("return window.screen.height;")
    # print(screen_height)
    csv_file_path = 'post_info1.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date','Comments']  # Add more fields if needed
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write CSV header
    start=0
    
    while True:
        post_list = []
        # Extract data (replace with appropriate CSS selector)
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
        # time.sleep(5)
        driver.implicitly_wait(3)
        if len(new_div_elements) == len(div_elements):
            break
        # Update the list of div elements
        end =len(new_div_elements)
        print(end)
        div_elements = new_div_elements[start:end]#*
        
        start = end 

        for element in div_elements:
            process_element(element,post_list)
            # extract_comments(element)
        print(post_list)
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for row in post_list:
                writer.writerow(row)
            
           
                
except Exception as e:
    print("Element not found or error occurred:", e)

driver.quit()



