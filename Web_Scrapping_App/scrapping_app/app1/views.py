from django.shortcuts import render, redirect

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app1.models import WishList
from django.urls import reverse
from django.contrib import auth
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

amazon_name = ""
amazon_price=0
amazon_product_link = ""
amazon_product_image=""


flipkart_name = ""
flipkart_price=0
flipkart_product_link = ""
flipkart_product_image=""


chroma_name = ""
chroma_price=0
chroma_product_link = ""
chroma_product_image=""


reliance_name = ""
reliance_price=0
reliance_product_link = ""
reliance_product_image=""


param1=''
param2=''

product_common_name=''
# #
# @login_required(login_url='/app3/login')
# @login_required
def home(request):
    # return render(request,'index.html',{'titles':'Django','link':'http://127.0.0.1:8000/profile'})

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        global product_common_name, param1, param2

        param1 = request.GET.get('param1')
        param2 = request.GET.get('param2')

        print("Param1=", param1)
        print("param2=", param2)

        def amazon(name):
            try:
                global amazon, amazon_name, amazon_price, amazon_product_link, amazon_product_image

                name1 = name.replace(" ", "-")
                name2 = name.replace(" ", "+")
                amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
                res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
                print("\nSearching in amazon...")
                soup = BeautifulSoup(res.text, 'html.parser')
                amazon_page = soup.select('.a-color-base.a-text-normal')

                amazon_page_length = int(len(amazon_page))
                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)
                priority_div = -1
                max_priority = 0
                res1 = []
                bool = False
                # flag = False

                len_all = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')
                print(int(len(len_all)))
                len_all = int(len(len_all))
                for i in range(0, len_all):
                    common = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')[i]
                    p_name = common.select('.a-color-base.a-text-normal')

                    print(str(p_name[0].getText()).strip().lower())
                    print(name)

                    if (bool == False):
                        price = common.select('.a-price-whole')
                        common1 = common.select('.a-link-normal.s-no-outline')[0]
                        amazon_product_link = "https://www.amazon.in" + common1.get('href')
                        image_amazon = common.select('.s-image')
                        amazon_product_image = image_amazon[0].get('src')

                        amazon_price = price[0].getText()

                        tp_name = soup.select('.a-size-medium.a-color-base')[i].getText()
                        amazon_name = common.select('.a-color-base.a-text-normal')[0].getText()

                        if (tp_name != amazon_name):
                            amazon_name = tp_name + amazon_name

                        bool = True

                    low_str = str(p_name[0].getText())
                    res = [sub for sub in findstr if sub in low_str.lower()]

                    if (len(findstr) == len(res)):
                        price = common.select('.a-price-whole')

                        print("Hello==")
                        print(p_name[0].getText())
                        # if(len(price)>0):
                        print("Price:" + price[0].getText())

                        common1 = common.select('.a-link-normal.s-no-outline')[0]
                        amazon_product_link = "https://www.amazon.in" + common1.get('href')
                        image_amazon = common.select('.s-image')
                        amazon_product_image = image_amazon[0].get('src')

                        amazon_price = price[0].getText()

                        tp_name = soup.select('.a-size-medium.a-color-base')[i].getText()
                        amazon_name = common.select('.a-color-base.a-text-normal')[0].getText()

                        if (tp_name != amazon_name):
                            amazon_name = tp_name + amazon_name

                        print("Amazon Product Name=")
                        print(amazon_name)
                        print("AMazon Price=")
                        print(amazon_price)
                        print("Amazon Product Link=")
                        print(amazon_product_link)
                        print("Amazon Product Image=")
                        print(amazon_product_image)

                        break

                        #
                        # for n in p_name:
                        #     print(n.getText())
                        # if (len(price) > 0):
                        #     amazon_price = price[0].getText()
                        # low_str = str(p_name[0].getText())
                        # res = [sub for sub in findstr if sub in low_str.lower()]
                        #
                        # print(res)
                        # if(len(price)>0):
                        #     if (max_priority < len(res)):
                        #         max_priority = int(len(res))
                        #         priority_div = i
                        #         res1 = res
                        #         if (len(res) == len(findstr)):
                        #             break
                        #
                        # print("---------------------------------")

                print("max_priority=")
                print(max_priority)
                print("Priority div=")
                print(priority_div)

                # if (priority_div != -1):
                #     common = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')[
                #         priority_div]
                #
                #     common1 = common.select('.a-link-normal.s-no-outline')[0]
                #     amazon_product_link = "https://www.amazon.in" + common1.get('href')
                #     image_amazon = common.select('.s-image')
                #     amazon_product_image = image_amazon[0].get('src')
                #     price= common.select('.a-price-whole')[0].getText()
                #     print(price)
                #     amazon_price=price
                #     amazon_name = common.select('.a-color-base.a-text-normal')[0].getText()
                #     # print("Product Name=")
                #     # for n in p_name:
                #     #     print(n.getText())
                # else:
                #     print("Products :" + name + " didn't get on amazon")
                # if (flag == False):
                #     amazon_price = "NA"
                #     amazon_name = "NA"
                #     amazon_product_link = 'NA'
                #     amazon_product_image = 'NA'

                low_str = str(amazon_name)
                res = [sub for sub in findstr if sub in low_str.lower()]
                print("RES=")
                print(res)
                print("LENGTH+")
                print(len(res))
                if (len(res) < int(len(findstr)) / 2):
                    amazon_price = "NA"
                    amazon_name = "NA"
                    amazon_product_link = 'NA'
                    amazon_product_image = 'NA'

                return amazon_price
            except:
                print("Exception:")
                amazon_price = "NA"
                amazon_name = "NA"
                amazon_product_link = 'NA'
                amazon_product_image = 'NA'
                # print(e)
                print("Amazon: No product found!@@@@@@@@@@@@@@@")
                print("---------------------------------")
                amazon_price = '0'
            return amazon_price

        def convert(a):
            b = a.replace(" ", '')
            c = b.replace("INR", '')
            d = c.replace(",", '')
            f = d.replace("₹", '')
            g = int(float(f))
            return g

        def flipkart(name):
            try:
                global flipkart, flipkart_name, flipkart_product_image, flipkart_product_link, flipkart_price
                name1 = name.replace(" ", "%20")
                print("Name1===")
                print(
                    'https://www.flipkart.com/search?q=' + name1 + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
                # print('https://www.flipkart.com/search?q='+{name1}+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')

                flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
                res = requests.get(
                    f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
                    headers=headers)

                print("\nSearching in flipkart....")
                soup = BeautifulSoup(res.text, 'html.parser')

                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)

                print(soup.title)
                # print(soup)

                if (soup.find("div", class_="slAVV4")):
                    common = soup.find("div", class_="slAVV4");
                    # print(common)
                    flip_name = common.find("a", class_="wjcEIp")
                    # print(flip_name)
                    print("Title=" + flip_name['title'])
                    print("Product Name=" + flip_name.getText())
                    flip_name = flip_name.getText()

                    # removing comma and brackets

                    flip_name = flip_name.replace(",", "")

                    flip_name = flip_name.replace("(", " ")

                    flip_name = flip_name.replace(")", " ")

                    flip_name = flip_name.replace("|", " ")

                    flip_price = common.find("div", class_="Nx9bqj")
                    print("Product Price=" + flip_price.getText())
                    flip_price = flip_price.getText()

                    flip_img_link = common.find("img", class_="DByuf4")
                    print("Product Img Link=" + flip_img_link['src'])
                    flip_img_link = flip_img_link['src']

                    flip_prod_link = common.find("a", class_="wjcEIp")
                    print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
                    flip_prod_link = "https://www.flipkart.com" + flip_prod_link['href']


                else:
                    common = soup.find("div", class_="tUxRFH")
                    print(common)

                    flip_name = common.find("div", class_="KzDlHZ")
                    print(flip_name.getText())
                    flip_name = flip_name.getText()

                    # removing comma and brackets

                    flip_name = flip_name.replace(",", "")

                    flip_name = flip_name.replace("(", " ")

                    flip_name = flip_name.replace(")", " ")

                    flip_name = flip_name.replace("|", " ")

                    flip_price = common.find("div", class_="Nx9bqj")
                    # print(flip_price)
                    print(flip_price.getText())
                    flip_price = flip_price.getText()

                    flip_img_link = common.find("img", class_="DByuf4")
                    print("Product Img Link=" + flip_img_link['src'])
                    flip_img_link = flip_img_link['src']

                    flip_prod_link = common.find("a", class_="CGtC98")
                    # print(flip_prod_link)
                    print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
                    flip_prod_link = "https://www.flipkart.com" + flip_prod_link['href']

                flipkart_name = flip_name
                flipkart_price = flip_price
                flipkart_product_image = flip_img_link
                flipkart_product_link = flip_prod_link

                return flip_price
            except Exception as e:
                print('Exception:', str(e))
                print("Flipkart: No product found!")
                print("---------------------------------")
                flipkart_price = 'NA'

                flipkart_name = "NA"
                flipkart_product_image = "NA"
                flipkart_product_link = "NA"
                return flipkart_price

        def chroma(name):
            global chroma_name, chroma_price, chroma_product_image, chroma_product_link
            name.replace(" ", "%20")

            print(name)
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'

            url = f'https://www.croma.com/searchB?q={name}%3Arelevance&text={name}'

            print(url)

            print("Searching on croma...............")

            chrome_options = Options()

            chrome_options.add_argument('--headless=new')
            chrome_options.add_experimental_option(
                "prefs", {
                    # block image loading
                    "profile.managed_default_content_settings.images": 2,
                }
            )

            driver = webdriver.Chrome(options=chrome_options)

            driver.get(url)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            try:
                common = soup.find('ul', {'class': 'product-list'})

                # print(common)

                print("Product Name:")
                product_name = common.find('h3', attrs={'class': 'product-title plp-prod-title 999'})
                # print(product_name)
                print(product_name.select("a")[0].getText())
                chroma_name = product_name.select("a")[0].getText()

                product_price = common.find('span', attrs={'class': 'amount plp-srp-new-amount'})
                print(product_price.getText())
                product_price = product_price.getText()

                product_img_link = common.find('div', attrs={'class': 'product-img plp-card-thumbnail plpnewsearch'})
                product_img_link1 = common.find('img')
                print("Product Img Link=" + product_img_link1.get('data-src'))
                product_img_link = product_img_link1.get('data-src')

                product_link = product_name.find('a')
                print("Product Link=" + "https://www.croma.com" + product_link.get('href'))

                product_link = "https://www.croma.com" + product_link.get('href')

                chroma_price = product_price
                chroma_product_image = product_img_link
                chroma_product_link = product_link

                return chroma_price
            except Exception as e:
                print("error")
                print(e)

                chroma_name = "NA"
                chroma_price = "NA"
                chroma_product_image = "NA"
                chroma_product_link = "NA"
                return chroma_price

            driver.quit()

        def reliance(name):
            try:
                global reliance_name, reliance_price, reliance_product_link, reliance_product_image
                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)
                name = name.replace(" ", "%20")
                bool = False

                print("Searching on reliance...............")

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'}

                url = f'https://www.reliancedigital.in/search?q={name}:relevance'

                print("Url")
                print(url)

                html = requests.get(url, headers=headers)

                soup = BeautifulSoup(html.text, 'html.parser')

                common = soup.find('div', {'class': 'pl__container'})
                common1 = common.findAll('li',
                                         {
                                             'class': 'grid pl__container__sp blk__lg__3 blk__md__4 blk__sm__6 blk__xs__6'})

                for i in common1:
                    # print("Product Name:")
                    product_name = i.select('.sp__name')
                    product_name = product_name[0].getText()
                    # print(product_name)

                    if (bool == False):
                        print("Reliance Bool")
                        price1 = i.find('span', {'class': 'TextWeb__Text-sc-1cyx778-0'})
                        price2 = price1.findAll('span')
                        price = ""
                        for p in price2:
                            price += p.getText()
                            print(p.getText(), end="")

                        reliance_price = price.replace('₹', '')

                        p_link = i.find('div', {'class': 'sp grid'})
                        reliance_product_link = "https://www.reliancedigital.in" + p_link.find('a').get('href')

                        p_img = i.select('img')
                        reliance_product_image = "https://www.reliancedigital.in" + p_img[0].get('data-srcset')

                        reliance_name = product_name
                        bool = True

                    low_str = str(product_name)
                    res = [sub for sub in findstr if sub in low_str.lower()]

                    if (len(findstr) == len(res)):
                        price1 = i.find('span', {'class': 'TextWeb__Text-sc-1cyx778-0'})
                        price2 = price1.findAll('span')
                        price = ""
                        for p in price2:
                            price += p.getText()
                            print(p.getText(), end="")

                        reliance_price = price.replace('₹', '')

                        p_link = i.find('div', {'class': 'sp grid'})
                        reliance_product_link = "https://www.reliancedigital.in" + p_link.find('a').get('href')

                        p_img = i.select('img')
                        reliance_product_image = "https://www.reliancedigital.in" + p_img[0].get('data-srcset')

                        print("Product Name:")
                        print(reliance_name)
                        print(reliance_price)
                        print(reliance_product_image)
                        print(reliance_product_link)

                        # flag = True
                        break

                # if (flag == False):
                #     reliance_price = "NA"
                #     reliance_name = "NA"
                #     reliance_product_link = 'NA'
                #     reliance_product_image = 'NA'


            except Exception as e:
                print(e)
                reliance_price = "NA"
                reliance_name = "NA"
                reliance_product_link = 'NA'
                reliance_product_image = 'NA'

            return reliance_price

        product_common_name = "Samsung Galaxy Mobile"
        amazon_price = amazon(product_common_name)
        print("a=" + amazon_name)
        print("aa=" + amazon_product_link)

        flipkart_price = flipkart(product_common_name)
        chroma_price = chroma(product_common_name)
        reliance_price = reliance(product_common_name)
        return render(request, 'index.html', {'amazon_name': '' + amazon_name, 'amazon_price': amazon_price,
                                              'product_link': amazon_product_link,
                                              'Product_image': amazon_product_image, 'flipkart_name': flipkart_name,
                                              'flipkart_price': flipkart_price,
                                              'flipkart_product_link': flipkart_product_link,
                                              'flipkart_Product_image': flipkart_product_image,
                                              'chroma_name': chroma_name, 'chroma_price': chroma_price,
                                              'chroma_product_link': chroma_product_link,
                                              'chroma_Product_image': chroma_product_image,
                                              'reliance_name': reliance_name, 'reliance_price': reliance_price,
                                              'reliance_product_link': reliance_product_link,
                                              'reliance_Product_image': reliance_product_image, 'param1': param1,
                                              'param2': param2, 'param3': product_common_name})
        # {'titles': amazon_price,'flipPrice':flipkart_price, 'link': 'http://127.0.0.1:8000/profile'}


def result(request):

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        global product_common_name, param1, param2
        param1 = request.GET.get('param1')
        param2 = request.GET.get('param2')
        print("Param1:", param1)
        print("Param2:", param2)
        param3 = request.GET.get('param3')
        product_common_name = param3

        # if param3 is None:
        #     product_common_name=str(request.GET['search_box'])
        # else:
        #     product_common_name=str(param3)

        def amazon(name):
            try:
                global amazon, amazon_name, amazon_product_link, amazon_product_image

                name1 = name.replace(" ", "-")
                name2 = name.replace(" ", "+")
                amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
                print(amazon)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'}

                res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
                print("\nSearching in amazon...")
                soup = BeautifulSoup(res.text, 'html.parser')

                # print(soup)

                amazon_page = soup.select('.a-color-base.a-text-normal')

                amazon_price = '0'

                amazon_page_length = int(len(amazon_page))
                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)
                priority_div = -1
                max_priority = 0
                res1 = []

                len_all = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')

                print(int(len(len_all)))
                len_all = int(len(len_all))
                for i in range(0, len_all):
                    common = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')[i]
                    price = common.select('.a-price-whole')
                    p_name = common.select('.a-color-base.a-text-normal')

                    print("Hello==")
                    print(p_name[0].getText())

                    print("Brand Name:")
                    print(soup.select('.a-size-medium.a-color-base')[i].getText())
                    tp_name = soup.select('.a-size-medium.a-color-base')[i].getText()

                    if (tp_name is p_name):
                        print("Ben Stokes")
                    else:
                        print("Joe Root")

                    for n in p_name:
                        print(n.getText())
                    if (len(price) > 0):
                        amazon_price = price[0].getText()

                    temp_name = p_name[0].getText().replace("|", "")
                    temp_name = temp_name.replace(")", "")
                    temp_name = temp_name.replace("(", "")
                    low_str = str(temp_name)
                    res = [sub for sub in findstr if sub in low_str.lower()]

                    print(res)

                    if (priority_div < len(findstr)):
                        max_priority = int(len(res))
                        priority_div = i
                        res1 = res
                        if (len(findstr) == len(res)):
                            print("Length==Length")
                            break

                    # print("---------------------------------")

                print("max_priority=")
                print(max_priority)
                print("Priority div=")
                print(priority_div)

                if (priority_div != -1):
                    common = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')[
                        priority_div]

                    common1 = common.select('.a-link-normal.s-no-outline')[0]
                    print("common")
                    print(common)
                    print("common 1")
                    print("https://www.amazon.in" + common1.get('href'))
                    image_amazon = common.select('.s-image')
                    print("image")
                    print(image_amazon[0].get('src'))
                    price = common.select('.a-price-whole')
                    print("IIIIIIIIII====", price)
                    print("price:")
                    if price:
                        print(price[0].getText())
                        amazon_price = price[0].getText()
                    else:
                        amazon_price = ""
                    p_name = common.select('.a-color-base.a-text-normal')
                    print("Product Name=")
                    # for n in p_name:
                    #     print(n.getText())
                    # print(p_name)
                    # print(p_name[0].getText())

                    amazon_name = p_name[0].getText()
                    amazon_product_link = "https://www.amazon.in" + common1.get('href')
                    amazon_product_image = image_amazon[0].get('src')
                #
                # else:
                #     print("Products :" + name + " didn't get on amazon")

                return amazon_price
            except Exception as e:
                print("Exception:")
                print(e)
                print("Amazon: No product found!@@@@@@@@@@@@@@@")
                print("---------------------------------")

                if (priority_div != -1):
                    common = soup.select('.puis-card-container.s-card-container.s-overflow-hidden.aok-relative ')[
                        priority_div]

                    common1 = common.select('.a-link-normal.s-no-outline')[0]
                    print("common")
                    print(common)
                    print("common 1")
                    print("https://www.amazon.in" + common1.get('href'))
                    image_amazon = common.select('.s-image')
                    print("image")
                    print(image_amazon[0].get('src'))
                    price = common.select('.a-price-whole')
                    print("price:")
                    if price:
                        print(price[0].getText())
                        amazon_price = price[0].getText()
                    else:
                        amazon_price = "NA"
                    p_name = common.select('.a-color-base.a-text-normal')
                    print("Product Name=")
                    # for n in p_name:
                    #     print(n.getText())
                    # print(p_name)
                    # print(p_name[0].getText())

                    amazon_name = p_name[0].getText()
                    amazon_product_link = "https://www.amazon.in" + common1.get('href')
                    amazon_product_image = image_amazon[0].get('src')
                else:
                    amazon_price = "NA"
                    amazon_name = "NA"
                    amazon_product_link = "NA"
                    amazon_product_image = "NA"

                return amazon_price

        def convert(a):
            b = a.replace(" ", '')
            c = b.replace("INR", '')
            d = c.replace(",", '')
            f = d.replace("₹", '')
            g = int(float(f))
            return g

        def flipkart(name):
            try:
                global flipkart, flipkart_name, flipkart_product_image, flipkart_product_link, flipkart_price
                name1 = name.replace(" ", "%20")
                print("Name1===")
                print(
                    'https://www.flipkart.com/search?q=' + name1 + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
                # print('https://www.flipkart.com/search?q='+{name1}+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

                flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
                res = requests.get(
                    f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
                    headers=headers)

                print("\nSearching in flipkart....")
                soup = BeautifulSoup(res.text, 'html.parser')

                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)

                # print(soup.title)
                # print(soup)

                if (soup.find("div", class_="slAVV4")):
                    common = soup.find("div", class_="slAVV4");
                    # print(common)
                    flip_name = common.find("a", class_="wjcEIp")
                    # print(flip_name)
                    print("Title=" + flip_name['title'])
                    print("Product Name=" + flip_name.getText())
                    flip_name = flip_name.getText()

                    # removing comma and brackets
                    #
                    # flip_name = flip_name.replace(",", "")
                    #
                    # flip_name = flip_name.replace("(", " ")
                    #
                    # flip_name = flip_name.replace(")", " ")

                    flip_name = flip_name.replace("|", " ")

                    flip_price = common.find("div", class_="Nx9bqj")
                    print("Product Price=" + flip_price.getText())
                    flip_price = flip_price.getText()

                    flip_img_link = common.find("img", class_="DByuf4")
                    print("Product Img Link=" + flip_img_link['src'])
                    flip_img_link = flip_img_link['src']

                    flip_prod_link = common.find("a", class_="wjcEIp")
                    print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
                    flip_prod_link = "https://www.flipkart.com" + flip_prod_link['href']



                else:
                    common = soup.find("div", class_="tUxRFH")
                    # print(common)

                    flip_name = common.find("div", class_="KzDlHZ")
                    print(flip_name.getText())
                    flip_name = flip_name.getText()

                    # removing comma and brackets

                    flip_name = flip_name.replace(",", "")

                    flip_name = flip_name.replace("(", " ")

                    flip_name = flip_name.replace(")", " ")

                    flip_name = flip_name.replace("|", " ")

                    flip_price = common.find("div", class_="Nx9bqj")
                    # print(flip_price)
                    print(flip_price.getText())
                    flip_price = flip_price.getText()

                    flip_img_link = common.find("img", class_="DByuf4")
                    print("Product Img Link=" + flip_img_link['src'])
                    flip_img_link = flip_img_link['src']

                    flip_prod_link = common.find("a", class_="CGtC98")
                    # print(flip_prod_link)
                    print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
                    flip_prod_link = "https://www.flipkart.com" + flip_prod_link['href']

                low_str = str(flip_name)
                res = [sub for sub in findstr if sub in low_str.lower()]

                print(res)

                if (len(findstr) >= len(res)):
                    flipkart_name = flip_name
                    flipkart_price = flip_price
                    flipkart_product_image = flip_img_link
                    flipkart_product_link = flip_prod_link

                return flipkart_price
            except Exception as e:
                print('Exception:', e)
                print("Flipkart: No product found!")
                print("---------------------------------")
                flipkart_price = "NA"
                flipkart_name = "NA"
                flipkart_product_image = "NA"
                flipkart_product_link = "NA"
                return flipkart_price

        def chroma(name):
            global chroma_name, chroma_price, chroma_product_image, chroma_product_link
            name.replace(" ", "%20")

            print(name)

            name = name.lower()
            findstr = name.split(" ")
            print("findstr=")
            print(findstr)
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'

            url = f'https://www.croma.com/searchB?q={name}%3Arelevance&text={name}'

            print(url)

            print("Searching on croma...............")

            chrome_options = Options()

            chrome_options.add_argument('--headless=new')
            chrome_options.add_experimental_option(
                "prefs", {
                    # block image loading
                    "profile.managed_default_content_settings.images": 2,
                }
            )

            driver = webdriver.Chrome(options=chrome_options)

            driver.get(url)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            try:
                common = soup.find('ul', {'class': 'product-list'})

                # print(common)

                len_all = common.find_all('li', {'class': 'product-item'})
                print(int(len(len_all)))

                print("Product Name:")
                product_name = common.find('h3', attrs={'class': 'product-title plp-prod-title 999'})
                print(product_name)
                print(product_name.select("a")[0].getText())
                chroma_name = product_name.select("a")[0].getText()

                product_price = common.find('span', attrs={'class': 'amount plp-srp-new-amount'})
                print(product_price.getText())
                product_price = product_price.getText()

                # product_img_link = common.find('div', attrs={'class': 'product-img plp-card-thumbnail plpnewsearch'})
                product_img_link1 = common.find('img')
                print("Product Img Link=" + product_img_link1.get('data-src'))
                product_img_link = product_img_link1.get('data-src')

                product_link = product_name.find('a')
                print("Product Link=" + "https://www.croma.com" + product_link.get('href'))

                product_link = "https://www.croma.com" + product_link.get('href')

                chroma_price = product_price
                chroma_product_image = product_img_link
                chroma_product_link = product_link

                return chroma_price
            except Exception as e:
                print("error")
                print(e)

                chroma_name = "NA"
                chroma_price = "NA"
                chroma_product_image = "NA"
                chroma_product_link = "NA"
                return chroma_price

            driver.quit()

        def reliance(name):
            try:
                global reliance_name, reliance_price, reliance_product_link, reliance_product_image
                name = name.lower()
                findstr = name.split(" ")
                print("findstr=")
                print(findstr)
                name = name.replace(" ", "%20")
                bool = False

                print("Searching on reliance...............")

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'}

                url = f'https://www.reliancedigital.in/search?q={name}:relevance'

                print("Url")
                print(url)

                html = requests.get(url, headers=headers)

                soup = BeautifulSoup(html.text, 'html.parser')

                common = soup.find('div', {'class': 'pl__container'})
                common1 = common.findAll('li',
                                         {
                                             'class': 'grid pl__container__sp blk__lg__3 blk__md__4 blk__sm__6 blk__xs__6'})

                for i in common1:
                    # print("Product Name:")
                    product_name = i.select('.sp__name')
                    product_name = product_name[0].getText()
                    # print(product_name)

                    if (bool == False):
                        print("Reliance Bool")
                        price1 = i.find('span', {'class': 'TextWeb__Text-sc-1cyx778-0'})
                        price2 = price1.findAll('span')
                        price = ""
                        for p in price2:
                            price += p.getText()
                            print(p.getText(), end="")

                        reliance_price = price.replace('₹', '')

                        p_link = i.find('div', {'class': 'sp grid'})
                        reliance_product_link = "https://www.reliancedigital.in" + p_link.find('a').get('href')

                        p_img = i.select('img')
                        reliance_product_image = "https://www.reliancedigital.in" + p_img[0].get('data-srcset')

                        reliance_name = product_name
                        bool = True

                    low_str = str(product_name)
                    res = [sub for sub in findstr if sub in low_str.lower()]

                    if (len(findstr) == len(res)):
                        price1 = i.find('span', {'class': 'TextWeb__Text-sc-1cyx778-0'})
                        price2 = price1.findAll('span')
                        price = ""
                        for p in price2:
                            price += p.getText()
                            print(p.getText(), end="")

                        reliance_price = price.replace('₹', '')

                        p_link = i.find('div', {'class': 'sp grid'})
                        reliance_product_link = "https://www.reliancedigital.in" + p_link.find('a').get('href')

                        p_img = i.select('img')
                        reliance_product_image = "https://www.reliancedigital.in" + p_img[0].get('data-srcset')

                        print("Product Name:")
                        print(reliance_name)
                        print(reliance_price)
                        print(reliance_product_image)
                        print(reliance_product_link)

                        # flag = True
                        break

                # if (flag == False):
                #     reliance_price = "NA"
                #     reliance_name = "NA"
                #     reliance_product_link = 'NA'
                #     reliance_product_image = 'NA'

                low_str = str(reliance_name)
                res = [sub for sub in findstr if sub in low_str.lower()]
                print("RES=")
                print(res)
                print("LENGTH+")
                print(len(res))
                if (len(res) < int(len(findstr)) / 2):
                    reliance_price = "NA"
                    reliance_name = "NA"
                    reliance_product_link = 'NA'
                    reliance_product_image = 'NA'

                return reliance_price

            except Exception as e:
                print(e)
                reliance_price = "NA"
                reliance_name = "NA"
                reliance_product_link = 'NA'
                reliance_product_image = 'NA'

                return reliance_price

        amazon_price = amazon(product_common_name)
        flipkart_price = flipkart(product_common_name)
        chroma_price = chroma(product_common_name)
        reliance_price = reliance(product_common_name)

        # return render(request, 'output.html',{'amazon_name':''+amazon_name,'amazon_price':amazon_price,'product_link':amazon_product_link,'Product_image':amazon_product_image,'flipkart_name':flipkart_name,'flipkart_price':flipkart_price,'flipkart_product_link':flipkart_product_link,'flipkart_Product_image':flipkart_product_image,'chroma_name':chroma_name,'chroma_price':chroma_price,'chroma_product_link':chroma_product_link,'chroma_Product_image':chroma_product_image})

        return render(request, 'output.html', {'amazon_name': '' + amazon_name, 'amazon_price': amazon_price,
                                               'product_link': amazon_product_link,
                                               'Product_image': amazon_product_image, 'flipkart_name': flipkart_name,
                                               'flipkart_price': flipkart_price,
                                               'flipkart_product_link': flipkart_product_link,
                                               'flipkart_Product_image': flipkart_product_image,
                                               'chroma_name': chroma_name, 'chroma_price': chroma_price,
                                               'chroma_product_link': chroma_product_link,
                                               'chroma_Product_image': chroma_product_image,
                                               'reliance_name': reliance_name, 'reliance_price': reliance_price,
                                               'reliance_product_link': reliance_product_link,
                                               'reliance_Product_image': reliance_product_image, 'param1': param1,
                                               'param2': param2, 'param3': param3})


def profile(request):
    return render(request,'index.html',{'titles':'Profile Page','link':'http://127.0.0.1:8000'})

def expression(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})


def wishlist(request):
    global param1,param2,product_common_name


    param1=request.GET.get('param1')
    param2=request.GET.get('param2')


    if request.method == 'POST':
        print("WIshlist %%")

        print(param1)
        print(param2)
        url = reverse('alert_price')
        url_with_params = f'{url}?param1={param1}&param2={param2}'
        return redirect(url_with_params)


        #return render(request,'alert_price.html')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete(request,id):
    wish=WishList.objects.filter(id=id)
    wish.delete()
    context={
        'wish':wish,
    }
    return redirect('manage_wishlist')


def alert_price(request):
    global param1, param2

    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    param3 = request.GET.get('param3')

    print(":::::::::::::::::")
    print(request.GET.get('param1'))
    print(request.GET.get('param2'))
    print(request.GET.get('param3'))

    if request.method == 'POST':

        print("Alerttttttttt")
        param1=request.POST['param1']
        param2=request.POST['param2']
        param3=request.POST['param3']
        print(param1)
        print( param2)
        print(param3)
        textfield = request.POST['textfield']
        today = datetime.today()
        if textfield:
            # data = WishList(name=param1, email_id=param2, product_name=product_common_name, alert_price=textfield,date=today)
            data = WishList(name=param1, email_id=param2, product_name=param3, alert_price=textfield,
                            date=today)
            data.save()

            #url = reverse('home page')
            url=reverse('Result search')
            url_with_params = f'{url}?param1={param1}&param2={param2}&param3={product_common_name}'
            return redirect(url_with_params)

    return render(request, 'alert_price.html',{'param1':param1,'param2':param2,'param3':param3})

    # return render(request,'alert.html')



def manage_wishlist(request):
    param1 =request.GET.get('param1')
    param2 = request.GET.get('param2')
    param3 = request.GET.get('param3')
    print("param1=",param1)
    print("param2=", param2)
    print("param3=", param3)
    wish=WishList.objects.filter(name=param1)

    context={
        'wish':wish,
        'param1':param1,
        'param2':param2,
        'param3':param3,
    }

    return render(request,'manage_wishlist.html',context)

def edit(request):

    wish=WishList.objects.all()
    context={
        'wish':wish,
    }


    return render(request,'manage_wishlist.html',context)


def update(request,id):
    if request.method=="POST":


        email=request.POST.get('email')

        date=request.POST.get('date')

        product_name=request.POST.get('product_name')

        alert_price=request.POST.get('alert_price')

        date_obj = datetime.strptime(str(date), "%B %d, %Y")

        # Format the datetime object to 'YYYYMMDD'
        date = date_obj.strftime("%Y-%m-%d")

        print("Date:",date)


        wish=WishList(
            id=id,
            email_id=email,
            date=date,
            product_name=product_name,
            alert_price=alert_price,
        )
        wish.save()
        return redirect('manage_wishlist')

    return render(request,'manage_wishlist.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
