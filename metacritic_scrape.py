from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests

all_data = []
for page in range(1): 
    url = f'https://www.metacritic.com/browse/movies/release-date/theaters/date?view=detailed&page={page}'
    session = requests.Session()
    session.max_redirects = 1000
    # session.get('http://www.amazon.com')
    webpage = session.get(url)
    sp = BeautifulSoup(webpage.content, 'html.parser')

    title = sp.find_all('a', 'title')
    # price = sp.find_all('span', 'lfloat product-price')
    # rating = sp.find_all('p', 'product-rating-count')
    # color = sp.find_all('span', ' sub-attr-val ')
    # discount = sp.find_all('div', 'product-discount')
    # originalprice = sp.find_all('span', 'lfloat product-desc-price strike ')
    # size = sp.find_all('span', ' sub-attr-value ')

    titleloop = [titles.text for titles in title]
    # priceloop = [prize.text for prize in price]
    # ratingloop = [rate.text for rate in rating]
    # colorloop = [colour.text for colour in color]
    # discloop = [disc.text for disc in discount]
    # origloop = [orig.text for orig in originalprice]
    # sizeloop = [siz.text for siz in size]

    data = {
        'Name of the Movie': titleloop,
    }

print (len(titleloop))
    # print (len(priceloop))
    # print (len(ratingloop))
    # print (len(origloop)) 
    # print (len(discloop)) 
    # print (len(sizeloop)) 

print(data)

    # df = pd.DataFrame(data, columns=[
    #     'Name of the product',
    #     'Price',
    # ])

    # disc=pd.DataFrame(data, columns=['Discount'])['Discount']
    # sizes = pd.DataFrame(data, columns=['Size'])['Size']
    # Rate = pd.DataFrame(data, columns=['Rating'])['Rating']
    # df = df.join(Rate).join(disc).join(sizes)
    # all_data.append(df)

# df_all = pd.concat(all_data, ignore_index=True)

# df_all.to_csv('snapdeal.csv', index=False)
# data = pd.read_csv("snapdeal.csv")


# fig, (ax1, ax2) = plt.subplots(2,2)
# ax1.scatter(data['Price'],data['Name of the product'])
# ax2.bar(data['Price'],data['Name of the product'])
# fig.tight_layout()
# plt.show()

