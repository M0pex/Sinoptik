import requests
from bs4 import BeautifulSoup as BS





def get_html(city):
    url = ("https://sinoptik.ua/погода-" + city)
    response = requests.get(url)
    return response.text

def get_html_ua(city):
    url = ("https://ua.sinoptik.ua/погода-" + city)
    response = requests.get(url)
    return response.text


def get_data(html):
    data = []
    soup = BS(html,'lxml')
    city = soup.find('div', {'class': 'cityName'}).get_text()
    temp_row = soup.find('tr', {'class': 'temperature'})
    temp_now = temp_row.find('td', {'class': 'cur'}).get_text()
    sens_row = soup.find('tr', {'class': 'temperatureSens'})
    temp_sens = sens_row.find('td', {'class': 'cur'}).get_text()
    img_row = soup.find('tr', {'class': 'img'})
    img_sec_row = img_row.find('td', {'class': 'cur'})
    img_show = img_sec_row.find('div', {'class': 'weatherIco'}).get('title')
    gray_row = soup.select_one('tr.gray:not(.time)')
    gray = gray_row.find('td', {'class': 'cur'}).get_text()
    tr_without_class = soup.find_all('tr', class_=False)[1]  # Get the second <tr> without a class
    h20 = tr_without_class.find('td', {'class': 'cur'}).get_text()
    wind_row = soup.find_all('tr', {'class': 'gray'})[2]
    wind_sec_row = wind_row.find('td', {'class': 'cur'})
    wind_show = wind_sec_row.find('div', {'class': 'Tooltip'}).get('data-tooltip')
    sec_tr_without_class = soup.find_all('tr', class_=False)[2]
    rain = sec_tr_without_class.find('td', {'class': 'cur'}).get_text()


    days = soup.find('tr', {'class': 'gray time'})
    dayt0 = days.find('td', {'class': 'p1'}).get_text()
    dayt3 = days.find('td', {'class': 'p2'}).get_text()
    dayt6 = days.find('td', {'class': 'p3'}).get_text()
    dayt9 = days.find('td', {'class': 'p4'}).get_text()
    dayt12 = days.find('td', {'class': 'p5'}).get_text()
    dayt15 = days.find('td', {'class': 'p6'}).get_text()
    dayt18 = days.find('td', {'class': 'p7'}).get_text()
    dayt21 = days.find('td', {'class': 'p8'}).get_text()

    temps = soup.find('tr', {'class': 'temperature'})
    temp0 = temps.find('td', {'class': 'p1'}).get_text()
    temp3 = temps.find('td', {'class': 'p2'}).get_text()
    temp6 = temps.find('td', {'class': 'p3'}).get_text()
    temp9 = temps.find('td', {'class': 'p4'}).get_text()
    temp12 = temps.find('td', {'class': 'p5'}).get_text()
    temp15 = temps.find('td', {'class': 'p6'}).get_text()
    temp18 = temps.find('td', {'class': 'p7'}).get_text()
    temp21 = temps.find('td', {'class': 'p8'}).get_text()

    data.append(city)
    data.append(temp_now)
    data.append(temp_sens)
    data.append(img_show)
    data.append(gray)
    data.append(h20)
    data.append(wind_show)
    data.append(rain)

    data.append(dayt0)
    data.append(dayt3)
    data.append(dayt6)
    data.append(dayt9)
    data.append(dayt12)
    data.append(dayt15)
    data.append(dayt18)
    data.append(dayt21)

    data.append(temp0)
    data.append(temp3)
    data.append(temp6)
    data.append(temp9)
    data.append(temp12)
    data.append(temp15)
    data.append(temp18)
    data.append(temp21)



    return data