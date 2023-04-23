from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests

all_data = []
for page in range(1,5): 
    url = f'https://www.rottentomatoes.com/browse/movies_in_theaters/?page={page}'
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')

    title = soup.findAll('span', class_= 'p--small')
    date = soup.find_all('span', 'smaller')
    rating = soup.findAll('span', class_='percentage')
    # color = sp.find_all('span', ' sub-attr-val ')
    # discount = sp.find_all('div', 'product-discount')
    # originalprice = sp.find_all('span', 'lfloat product-desc-price strike ')
    # size = sp.find_all('span', ' sub-attr-value ')

    titleloop = [titles.text for titles in title]
    dateloop = [date.text for date in date]
    ratingloop = [rate.text for rate in rating]
    # colorloop = [colour.text for colour in color]
    # discloop = [disc.text for disc in discount]
    # origloop = [orig.text for orig in originalprice]
    # sizeloop = [siz.text for siz in size]

    data = {
        'Name of the Movie': titleloop,
        'Rating':ratingloop,
        'Date':dateloop
    }

print (len(titleloop))
print(len(dateloop))
print (len(ratingloop))
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

