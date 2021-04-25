import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
options = Options()
options.add_argument("--user-data-dir=C:\\Users\\just_\\OneDrive\\Desktop\\UserData")
options.page_load_strategy = 'normal'
browser1 = webdriver.Chrome(options=options)

        
def bot():
    time.sleep(1)                   
    print("Added to cart")
    print("Going to cart")
    browser1.get('https://www.bestbuy.com/cart')

    #checks if we need to click 'ship to'
    time.sleep(1)
    shipHome = browser1.find_element_by_xpath("//*[contains(@id, 'fulfillment-shipping')]") # ship to home ID: id="fulfillment-shipping-4pmjcw2zz24ff-4odjuv524m635"
    if shipHome is not None: 
        shipHome.click()

    #click checkout button
    time.sleep(1)
    checkout = browser1.find_element_by_class_name('btn-primary')
    checkout.click()

    #wait for cvv box to appear
    time.sleep(2)
    cvv = browser1.find_element_by_id("credit-card-cvv")
    cvv.send_keys("332")

    #place order
    placeOrder = browser1.find_element_by_class_name('button__fast-track')
    placeOrder.click()
    print('ORDER PLACED :)')


#3080s
# EVGA - GeForce RTX 3080 XC3 ULTRA GAMING 10GB - $839
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400')

#EVGA - GeForce RTX 3080 XC3 BLACK GAMING 10GB - $799
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432399.p?skuId=6432399')

#EVGA - GeForce RTX 3080 FTW3 GAMING - $859
browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191')

#EVGA - GeForce RTX 3080 XC3 GAMING 10GB - $819
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436194.p?skuId=6436194')

#PNY GeForce RTX 3080 10GB XLR8 Gaming EPIC-X RGB - $799
#browser1.get('https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432658.p?skuId=6432658')


#1660 super
#browser1.get('https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6409171.p?skuId=6409171')

#tester
#browser1.get('https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353')
#browser1.get('https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000')

atcBttn = False

while not atcBttn:

    try:

        addToCart = browser1.find_element_by_class_name("btn-disabled")
        print("Button not ready")
        time.sleep(1)
        browser1.refresh()

    except:

        print("Button ready!")
        addToCart = browser1.find_element_by_class_name('btn-primary').click()
        time.sleep(1)
        try:
            # see if we're in queue....
            browser1.find_element_by_xpath("//*[@aria-describedby = 'add-to-cart-wait-overlay']")
            yourTurn = False
            while not yourTurn:     
                # check color of add to cart button, breaks out of exception when color changes
                color = browser1.find_element_by_class_name('btn-primary').value_of_css_property('background-color')
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



