from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
																					#								----copied above part-----------			



import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode ----> remove this line if assertion error is thrown
browser = Firefox(options=opts)
browser.get('https://quora.com')

#email = browser.find_element_by_id('__w2_w6qKKs8E21_email')
#email = browser.find_element_by_css_selector('*[id$="email"]')
email = browser.find_element_by_css_selector('input[class*="header_login_text_box"][placeholder="Email"]')
email.clear()
email.send_keys('suraj.decen@gmail.com')
#password = browser.find_element_by_id('__w2_w6qKKs8E21_password')
#password = browser.find_element_by_css_selector('*[id$="password"]')
password = browser.find_element_by_css_selector('input[class*="header_login_text_box"][placeholder="Password"]')
password.clear()
password.send_keys('Enter password here')


time.sleep(1)

login = browser.find_element_by_css_selector('input[class^="submit_button"][type="submit"][value="Login"]')
login.click()


'''
form = browser.find_element_by_class_name('inline_login_form')
form.submit()

delay = 5 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
except TimeoutException:
    print ("Loading took too much time!")
------------'''


time.sleep(5)
question = browser.find_element_by_css_selector('a[class="AskQuestionButton"][href="#"]')
time.sleep(1)
question.click()
qa = browser.find_element_by_css_selector('textarea[class^="selector_input"][title^="Start your question with"]')
qa.clear()
qa.send_keys('afsjhafbabfasbfoaenfpaefcanlsvcnvnaernnngnkle fnroinsgoniwosgnlsdgklvnsognnla')
add = browser.find_element_by_css_selector('a[class="submit_button modal_action"][href="#"]')
time.sleep(1)
add.click()


'''
<textarea class="selector_input text" type="text" rows="1" title="Start your question with &quot;What&quot;, &quot;How&quot;, &quot;Why&quot;, etc." data-group="js-editable" placeholder="Start your question with &quot;What&quot;, &quot;How&quot;, &quot;Why&quot;, etc." w2cid="w7z2LQPz12" id="__w2_w7z2LQPz12_input" style="overflow: hidden; overflow-wrap: break-word; height: 31px;"></textarea>



<a class="submit_button modal_action" href="#" id="__w2_w7z2LQPz2_submit">Add Question</a>'''
