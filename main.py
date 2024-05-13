import requests
from bs4 import BeautifulSoup

url="https://www1.kaiho.mlit.go.jp/KANKYO/KAIYO/qboc/index.html"

r = requests.get(url)
page1_soup=BeautifulSoup(r.content,'html.parser')

page1_a_tag=page1_soup.find_all("a")

for i in range(len(page1_a_tag)):
    page1_a_tag_str=str(page1_a_tag[i])
    if  'alt="海流"'  in page1_a_tag_str :
        scraping_key=page1_a_tag[i]
scraping_key_str=str(scraping_key).replace(" ","")
print(scraping_key_str)
# y=scraping_key_str.split('"')

#初期書き込み
# f = open('kairyu.txt', 'w', encoding='UTF-8')
#f.write(x)
# f.close()

#2回目以降
f=open('kairyu.txt','r',encoding='UTF-8')
read_txt=f.read()
f.close()

print(read_txt)
read_txt_arr=read_txt.split('"')
read_txt_arr2=read_txt_arr[1].split(".")

scraping_key_arr=scraping_key_str.split('"')
read_txt_arr3=read_txt_arr2[0].split("/")
read_txt_str=read_txt_arr3[2][4:11]
#print(read_txt_str)
print(read_txt)
print(scraping_key_str)

if read_txt!=scraping_key_str:
    url2="https://www1.kaiho.mlit.go.jp/KANKYO/KAIYO/qboc/"+b[1]
    r = requests.get(url2)
    soup=BeautifulSoup(r.content,'html.parser')
    test=soup.find_all("img")
    aa=str(test[0])
    ab=aa.split('"')
    ac=ab[1][6:]
    url3="https://www1.kaiho.mlit.go.jp/KANKYO/KAIYO/qboc/"+ac
    print(url3)
    img = requests.get(url3, stream=True)
    img_name=read_txt_str+".png"
    with open(img_name,"wb") as f:
        f.write(img.content)
        print("テストダウンロード")
    f = open('kairyu.txt', 'w', encoding='UTF-8')
    f.write(x)
    f.close()

print("完了")




    # url2="https://www1.kaiho.mlit.go.jp/KANKYO/KAIYO/qboc/"+c[0]+".png"
    # print(url2)
    # img = requests.get(url2, stream=True)
    # # d=c[0].split("/")
    # # print(d[2])
    # img_name=d[2][4:11]+".png"
    # print(img_name)
    # with open(img_name,"wb") as f:
    #     f.write(img.content)
    #     print("テストダウンロード")
 
# f = open('kairyu.txt', 'r', encoding='UTF-8')
# z=f.read()
# xx=z.split(",")
# f.close()
# print(xx)

# if xx[0] != y[0][1]:
#     print()
#     f = open('myfile.txt', 'a', encoding='UTF-8')

# # f.write(y[0][1]+","+y[1][1])

# # f.close()


# #海保のページのうち該当部分が更新されているかを確認ののち更新されていればダウンロードしてtextを更新これを複数回行う。ダウンロードされたデータについて速報(QBOC) … 海洋速報(Quick Bulletin of Ocean Conditions)