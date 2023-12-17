from bs4 import BeautifulSoup
import pandas as pd
import request

url= "https://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs"

bright_star_table = soup.find("table",atts={"class","wikitable"})

table_body = bright_star_table.find('tbody')

table_rows = table_body.find_all('tr')

page = requests.get(url)

temp_list=[]

table_rows= star_table[1].find_all("tr")

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

table = soup.find_all('table',{"class","wikitable"})
for row in table_rows:
    table_clos = row.find_all('td')
    print(table_cols)
    
    temp_list=[]

    for col_data in table_cols:
        data = col_data.text.strip()
        
        temp_list.append(data)

    scraped_data.append(temp_list)

    stars_data = []
    for i in range(0,len(scraped_data)):

        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        mass = scraped_data[i][5]
        radius = scraped_data[i][6]
        lum = scraped_data[i][7]

        required_data = [Star_names,Distance,mass,radius,lum]
        stars_data.append(required_data)

headers = ['Star_name','Distance','mass','radius','luminosity']

star_df_1 = pd.DataFrame(stars_data, cloumns=headers)
star_df_1.to_csv('scrapped_data.csv',index=True,index_laber=id)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=headers)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")