import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import Select
# from scalper import bot
options = Options()
options.add_argument(
    "--user-data-dir=[USE YOUR OWN DATA PATH]")
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
        cvv.send_keys("[CVV HERE]")
    except:
        print("Gay")

    time.sleep(1)
    try:
        submit = browser1.find_element_by_xpath("//div[contains(@id, 'paymentsOrderSummary')]")
        print("Found continue button")
        submit.click()
    except:
        print("Can't find continue button")
    

    try:
        placeOrder = browser1.find_element_by_css_selector("button[class='btn full_width checkout noValidDoubleClick']")
        print("Found place order button")
        time.sleep(1)
        #placeOrder.click()
        #print("ORDER PLACED :O")
    except:
        print("Can't find place order button")

# actual page
browser1.get("https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934&cbxRefine=1421023&cbxRefine=1486397/")

# one with an add to cart
# browser1.get("https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934&cbxRefine=386429&cbxRefine=1421023/")


# testers
# browser1.get("https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934/")

inCart = False
while not inCart:

    i = 0
    itemNo = 'skuListFormID_INDEX_'
    for i in range(0, 17):
        currentItem = itemNo + str(i)
        try:
            clickOne = browser1.find_element_by_id(currentItem)
            if not clickOne.get_attribute('disabled'):
                clickOne.click()
                inCart = True
                break
            else:
                print(f"out of stock for item {currentItem}")
        except:
            print(f"cannot find element {currentItem}")

    if inCart: break
    browser1.refresh()

bot()
# invokes purchase bot only if we get one added to our cart


