import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import Select
# from scalper import bot
options = Options()
options.add_argument(
    "--user-data-dir=[YOUR DATA PATH]")
options.page_load_strategy = 'normal'
browser1 = webdriver.Chrome(options=options)



def bot():
    time.sleep(1)
    print("Added to cart")
    print("Going to cart")
    browser1.get('https://www.officedepot.com/cart/shoppingCart.do')

    time.sleep(1)
    checkout = browser1.find_element_by_xpath("//a[contains(@href, '/cart/checkout.do')]")
    checkout.click()
    
    try:
        cvv = browser1.find_element_by_xpath("//input[contains(@name, 'cvvForPreauth')]")
        cvv.clear()
        cvv.click()
        cvv.send_keys("[CVV GOES HERE]")
    except:
        print("Can't find CVV box.")

    time.sleep(1)
    try:
        submit = browser1.find_element_by_xpath("//div[contains(@id, 'paymentsOrderSummary')]")
        print("Found continue button")
        time.sleep(1)
        submit.click()
    except:
        print("Can't find continue button")
    

    time.sleep(1)
    try:
        placeOrder = browser1.find_element_by_css_selector("button[class='btn full_width checkout noValidDoubleClick']")
        print("Found place order button")
        time.sleep(1)
        #placeOrder.click()
        #print("ORDER PLACED :O")
    except:
        print("Can't find place order button")

# GPU Main Page - activate bot on this link
# browser1.get("https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934&cbxRefine=1421023&cbxRefine=1486397/")


# testers
# browser1.get("https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934/")

inCart = False
while not inCart:

    itemNo = 'skuListFormID_INDEX_'
    for i in range(0, 2, 1):
        currentItem = itemNo + str(i)
        #print(currentItem)
        #print(f"//input[contains(@id, '{currentItem}')]")
        winner = browser1.find_element_by_xpath(
            f"//input[contains(@id, '{currentItem}')]")
        try:
            winner.click()
            inCart = True
            break
        except:
            print("ouch")

    if inCart: break
    time.sleep(2)
    browser1.refresh()

bot()
# invokes purchase bot only if we get one added to our cart


