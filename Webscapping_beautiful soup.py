import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

#we can define a function to get the stock reading in real time:
def real_time_stock_price(stock_code):
    #modify the cold to add different stock codes
    url = ('https://finance.yahoo.com/quote/%5E') + stock_code + ('?p=^') + stock_code #+ ('AAPL?p=AAPL&.tsrc=fin-srch')
    r = requests.get(url)
    #print(r.text)
    web_content = BeautifulSoup(r.text, 'lxml')
    #find function to locate the 'div'
    #web_content = web_content.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)')

    #another way using a dictnary to find multiple content.
    web_content = web_content.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})

    #another find function to locate the span
    web_content = web_content.find('span')
    #to add only the value we add ".text" at the end
    web_content = web_content.text

    if web_content == []:
        web_content = '99999' #incase not able to capture the value in real time

    return web_content

#web_content = real_time_stock_price('IXIC')
#print(web_content)

SP = ['BSESN', 'NSEI', 'DJI', 'IXIC', 'HSI', 'N225', 'NYE']

for step in range(1,100):
    price = []
    col = []
    time_stamp = datetime.datetime.now() #add time to know when data was taken
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S") #add time in a format
    for stock_price in SP:
        price.append(real_time_stock_price(stock_price)) #append price
    col = [time_stamp] #add timestamp in columns
    col.extend(price) #add price to columns
    df = pd.DataFrame(col) #create the dataframe
    df=df.T #since column, make it row easier to read
    df.to_csv('real_time_stock_data_extract.csv', mode='a', header=False) #append mode and without the header
    print(col)


