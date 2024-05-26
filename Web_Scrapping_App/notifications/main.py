import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import traceback
import psycopg2






# /**********************************/


def result(rname):

    global product_common_name,param1,param2

    product_common_name=rname

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
            # print("findstr=")
            # print(findstr)
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

                # print("Hello==")
                # print(p_name[0].getText())
                #
                # print("Brand Name:")
                # print(soup.select('.a-size-medium.a-color-base')[i].getText())
                tp_name = soup.select('.a-size-medium.a-color-base')[i].getText()
                #
                # if (tp_name is p_name):
                #     print("Ben Stokes")
                # else:
                #     print("Joe Root")

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
                # print("common")
                # print(common)
                # print("common 1")
                # print("https://www.amazon.in" + common1.get('href'))
                image_amazon = common.select('.s-image')
                # print("image")
                # print(image_amazon[0].get('src'))
                price = common.select('.a-price-whole')
                # print("IIIIIIIIII====",price)
                # print("price:")
                if price:
                    print(price[0].getText())
                    amazon_price = price[0].getText()
                else:
                    amazon_price = ""
                p_name = common.select('.a-color-base.a-text-normal')
                # print("Product Name=")
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
                # print("common")
                # print(common)
                # print("common 1")
                # print("https://www.amazon.in" + common1.get('href'))
                image_amazon = common.select('.s-image')
                # print("image")
                # print(image_amazon[0].get('src'))
                price = common.select('.a-price-whole')
                # print("price:")
                if price:
                    print(price[0].getText())
                    amazon_price = price[0].getText()
                else:
                    amazon_price = ""
                p_name = common.select('.a-color-base.a-text-normal')
                # print("Product Name=")
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
            # print("findstr=")
            print(findstr)

            # print(soup.title)
            # print(soup)

            if (soup.find("div", class_="slAVV4")):
                common = soup.find("div", class_="slAVV4");
                # print(common)
                flip_name = common.find("a", class_="wjcEIp")
                # print(flip_name)
                # print("Title=" + flip_name['title'])
                # print("Product Name=" + flip_name.getText())
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
                # print("Product Price=" + flip_price.getText())
                flip_price = flip_price.getText()

                flip_img_link = common.find("img", class_="DByuf4")
                # print("Product Img Link=" + flip_img_link['src'])
                flip_img_link = flip_img_link['src']

                flip_prod_link = common.find("a", class_="wjcEIp")
                # print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
                flip_prod_link = "https://www.flipkart.com" + flip_prod_link['href']



            else:
                common = soup.find("div", class_="tUxRFH")
                # print(common)

                flip_name = common.find("div", class_="KzDlHZ")
                # print(flip_name.getText())
                flip_name = flip_name.getText()

                # removing comma and brackets

                flip_name = flip_name.replace(",", "")

                flip_name = flip_name.replace("(", " ")

                flip_name = flip_name.replace(")", " ")

                flip_name = flip_name.replace("|", " ")

                flip_price = common.find("div", class_="Nx9bqj")
                # print(flip_price)
                # print(flip_price.getText())
                flip_price = flip_price.getText()

                flip_img_link = common.find("img", class_="DByuf4")
                # print("Product Img Link=" + flip_img_link['src'])
                flip_img_link = flip_img_link['src']

                flip_prod_link = common.find("a", class_="CGtC98")
                # print(flip_prod_link)
                # print("Product Link=https://www.flipkart.com" + flip_prod_link['href'])
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
            print('Exception:' ,e)
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
            # print("Product Img Link=" + product_img_link1.get('data-src'))
            product_img_link = product_img_link1.get('data-src')

            product_link = product_name.find('a')
            # print("Product Link=" + "https://www.croma.com" + product_link.get('href'))

            product_link = "https://www.croma.com" + product_link.get('href')

            chroma_price = product_price
            chroma_product_image = product_img_link
            chroma_product_link = product_link

            return chroma_price
        except Exception as e:
            # print("error")
            # print(e)

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

            # print("Url")
            # print(url)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.text, 'html.parser')

            common = soup.find('div', {'class': 'pl__container'})
            common1 = common.findAll('li',
                                     {'class': 'grid pl__container__sp blk__lg__3 blk__md__4 blk__sm__6 blk__xs__6'})

            for i in common1:
                # print("Product Name:")
                product_name = i.select('.sp__name')
                product_name = product_name[0].getText()
                # print(product_name)

                if (bool == False):
                    # print("Reliance Bool")
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

                    # print("Product Name:")
                    # print(reliance_name)
                    # print(reliance_price)
                    # print(reliance_product_image)
                    # print(reliance_product_link)

                    # flag = True
                    break

            # if (flag == False):
            #     reliance_price = "NA"
            #     reliance_name = "NA"
            #     reliance_product_link = 'NA'
            #     reliance_product_image = 'NA'

            low_str = str(reliance_name)
            res = [sub for sub in findstr if sub in low_str.lower()]
            # print("RES=")
            # print(res)
            # print("LENGTH+")
            # print(len(res))
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
    chroma_price=chroma(product_common_name)
    reliance_price=reliance(product_common_name)

    if amazon_price=="NA":
        amazon_price=''
    if flipkart_price=="NA":
        flipkart_price=''
    if chroma_price=="NA":
        chroma_price=''
    if reliance_price=="NA":
        reliance_price=''


    rlist=[]
    rlist.append(amazon_price)
    rlist.append(flipkart_price)
    rlist.append(chroma_price)
    rlist.append(reliance_price)
    print("Rlist=",rlist)
    return rlist




























def fetch_table_data(table_name):

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="Himanshu",
            host="127.0.0.1",
            port="5432",
            database="DB1")

        # Create a cursor object
        cursor = connection.cursor()

        # Fetch all data from the specified table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Fetch column names
        colnames = [desc[0] for desc in cursor.description]

        # Print column names and rows
        print(f"Column names: {colnames}")
        for row in rows:
            print(row)
            templist=list(result(row[3]))

            al_price=int(row[4])
            mail=row[2]
            prod_name=row[3]
            name=row[2]
            # if templist[0]=='':
            #     prod0_price="0"
            # if templist[1]=='':
            #     prod1_price="0"
            # if templist[2]=='':
            #     prod2_price="0"
            # if templist[3]=='':
            #     prod3_price="0"

            if templist[0] != '':
                prod0_price=int(""+templist[0].replace(',',''))
            else:
                prod0_price = int("0")
            if templist[1] != '':
                prod1_price =int(""+templist[1][1:].replace(',',''))
            else:
                prod1_price = int("0")
            if templist[2] != '':
                prod2_price = int("" + templist[2].replace(',', '').replace("₹", ""))
            else:
                prod2_price =int("0")
            # nstr = ""
            # # for i in range(1, len(prod2_price)):
            #     print(prod2_price[i])
            #     nstr += prod2_price[i]
            #
            # print(prod2_price)
            if templist[3] != '':
                if templist[3][1]=='₹':
                    prod3_price =int(""+templist[3][1:].replace(',','').replace(".", ""))
                else:
                    prod3_price = int("" + templist[3].replace(',', '').replace(".00", ""))
            else:
                prod3_price = int("0")
            print("POEoo",prod0_price,prod1_price,prod2_price,prod3_price)

            if al_price<=prod0_price or al_price<=prod1_price or al_price<=prod2_price or al_price<=prod3_price:
                sendmail(str(prod0_price),str(prod1_price),str(prod2_price),str(prod3_price),name,prod_name,mail)
                delete_query = f"DELETE FROM {table_name} WHERE id = {row[0]}"
                cursor.execute(delete_query, (row[0],))

                # Commit the transaction
                connection.commit()





    except Exception as e:

        print('Exception:', str(e))
        traceback.print_exc()
        #print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# ::::::::::::::::::::::::::::::::::::::::::::::::
import smtplib as s
def sendmail(prod1,prod2,prod3,prod4,name,prod_name,mail):
    ob = s.SMTP("smtp.gmail.com", 587)

    ob.starttls()

    ob.login("himanshukpatil2002@gmail.com", "svqd xzhv pgda dqyj")

    str1=""

    if prod1 !="NA":
        str1+="Amazon:"+prod1
    if prod2 !="NA":
        str1+="Flipkart:"+prod2
    if prod3 !="NA":
        nstr = ""
        for i in range(1, len(prod3)):
            print(prod3[i])
            nstr += prod3[i]
        str1+="Croma:"+nstr.replace(',', '')
    if prod4 !="NA":
        str1+="Reliance:"+prod4

    print(str1)

    subject = "Alert Price Mail"
    body = f"Hey {name}...\nYou Got Alert of {prod_name}\n Price is under your budget \n {str1}"
    message = "Subject:{}\n\n{}".format(subject, body)

    listOfAddresses = [""+mail]
    ob.sendmail("himanshukpatil2002@gmail.com", listOfAddresses, message)

    print("Send Sucessfully")
    ob.quit()


# :::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == "__main__":
    table_name = "app1_wishlist"  # Replace with your table name
    fetch_table_data(table_name)
    # print(result("samsung galaxy f13 mobile"))





