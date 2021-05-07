import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import Select
#from scalper import bot
options = Options()
options.add_argument(
    "--user-data-dir=[USER DATA PATH HERE]")
options.page_load_strategy = 'normal'
browser1 = webdriver.Chrome(options=options)

#https://www.officedepot.com/a/browse/graphic-cards/N=5+1461934&cbxRefine=1421023&cbxRefine=1486397/


def bot():
    time.sleep(1)
    print("Added to cart")
    print("Going to cart")
    browser1.get('https://www.bestbuy.com/cart')

    # checks if we need to click 'ship to'
    time.sleep(1)
    # ship to home ID: id="fulfillment-shipping-4pmjcw2zz24ff-4odjuv524m635"
    try:
        shipHome = browser1.find_element_by_xpath(
            "//*[contains(@id, 'fulfillment-shipping')]")
        if shipHome is not None:
            shipHome.click()
    except:
        print('oof1')
    

    time.sleep(1)
    # try to order 2
    try:
        quantity = Select(browser1.find_element_by_class_name('c-dropdown'))
        if quantity is not None:
            quantity.select_by_value("2")
    except:
        print('oof2')

    # click checkout button
    time.sleep(1)
    checkout = browser1.find_element_by_class_name('btn-primary')
    checkout.click()

    # wait for cvv box to appear
    time.sleep(2)
    cvv = browser1.find_element_by_id("credit-card-cvv")
    cvv.send_keys("332")

    # place order
    time.sleep(0.5)
    placeOrder = browser1.find_element_by_class_name('button__fast-track')
    placeOrder.click()
    print('ORDER PLACED :)')


skus = ['6407309','6389333','6409171','6405063']
def callGPUs():
    time.sleep(2)
    inCart = False
    while not inCart:
        error = False
        for sku in skus:  
            color = '#c5cbd5'        
            try:
                item = browser1.find_element_by_xpath(f"//button[contains(@data-sku-id, '{sku}')]")
            except:
                item = browser1.find_element_by_xpath(f"//a[contains(@data-sku-id, '{sku}')]")   #button[contains(@data-sku-id, '{sku}')]
            if item is not None:
                print(f"Found sku: {sku} on page.")
            else:
                print(f"Can't find item {sku}")
            #time.sleep(0.06)
            try:
                color = Color.from_string(item.value_of_css_property('background-color')).hex
            except:
                error = True
                print(f"Error with finding color for item {sku}...continuing...")
            if color != '#c5cbd5':
                print()
                item.click()
                inCart = True
                break
            if inCart: break        # we want it to insta-break out of the loop
        if not inCart and not error: 
            print("Nothing found in stock")
            time.sleep(2)
            browser1.refresh()




browser1.get("https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20GTX%201660%20SUPER")
callGPUs()

# testers
# browser1.get("https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=soldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items")
# browser1.get("https://www.bestbuy.com/site/promo/amd-ryzen-5000")





# invokes purchase bot only if we get one added to our cart

atcBttn = False

while not atcBttn:

    addToCart = browser1.find_element_by_class_name('btn-primary').click()
    time.sleep(1)
    try:
        # see if we're in queue....
        browser1.find_element_by_xpath(
            "//*[@aria-describedby = 'add-to-cart-wait-overlay']")
        yourTurn = False
        while not yourTurn:
            # check color of add to cart button, breaks out of exception when color changes
            color = browser1.find_element_by_class_name(
                'btn-primary').value_of_css_property('background-color')
            colorCheck = Color.from_string(color).hex
            print(colorCheck)
            print("Still waiting")
            time.sleep(1)
            if colorCheck != '#c5cbd5':
                print("Adding!")
                browser1.find_element_by_class_name('btn-primary').click()
                yourTurn = True
                atcBttn = True
                bot()
    except NoSuchElementException:
        atcBttn = True
        bot()
