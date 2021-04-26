import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
options = Options()
options.add_argument("--user-data-dir={USER DATA PATH]")
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
    cvv.send_keys("[YOUR CVV]")

    #place order
    placeOrder = browser1.find_element_by_class_name('button__fast-track')
    #placeOrder.click()
    print('ORDER PLACED :)')




#3080s
skus = ['6436191','6429440','6432400','6432399','6436196','6432655','6432658','6436194']

#test 5000 series
#skus = ['6438941','6438942','6432400','6439000','6438943']  #6438943 6439000  ,'6439000','6438943'


def callGPUs():
    time.sleep(2)
    inCart = False
    while not inCart:
        for sku in skus:
            try:
                item = browser1.find_element_by_xpath(f"//button[contains(@data-sku-id, '{sku}')]")
            except:
                item = browser1.find_element_by_xpath(f"//a[contains(@data-sku-id, '{sku}')]")   #button[contains(@data-sku-id, '{sku}')]
            if item is not None:
                print(f"Found sku: {sku} on page.")
            else:
                print(f"Can't find item {sku}")
            color = Color.from_string(item.value_of_css_property('background-color')).hex
            print(f"Color: {color}")
            if color != '#c5cbd5':
                print()
                item.click()
                inCart = True
                break
            if inCart: break        # we want it to insta-break out of the loop
        if not inCart: 
            print("Nothing found in stock")
            time.sleep(3)
            browser1.refresh()


            

browser1.get("https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080")

#browser1.get('https://www.bestbuy.com/site/promo/amd-ryzen-5000')

callGPUs()

atcBttn = False

while not atcBttn:
    try:
        browser1.find_element_by_class_name('btn-primary').click()
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
    except:
        print("Button not ready")
        browser1.refresh()


#### LINKS ####


#3080s
# EVGA - GeForce RTX 3080 XC3 ULTRA GAMING 10GB - $839
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400')

#EVGA - GeForce RTX 3080 XC3 BLACK GAMING 10GB - $799
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432399.p?skuId=6432399')

#EVGA - GeForce RTX 3080 FTW3 GAMING - $859
# browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191')

#EVGA - GeForce RTX 3080 XC3 GAMING 10GB - $819
#browser1.get('https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436194.p?skuId=6436194')

#PNY GeForce RTX 3080 10GB XLR8 Gaming EPIC-X RGB - $799
#browser1.get('https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432658.p?skuId=6432658')


#1660 super
#browser1.get('https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6409171.p?skuId=6409171')

#tester
#browser1.get('https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353')
#browser1.get('https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000')
