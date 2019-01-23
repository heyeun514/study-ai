# -*- coding: utf-8 -*-
# from urllib.request import urlopen
from urllib2 import urlopen
# 명령행 파싱 모듈 argparse 모듈 사용
import argparse
# request => 요청하는거를 웹에 요청한 결과값을 얻어올수 있는 모듈
import requests as req
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup
from selenium import webdriver
# key 조직
from selenium.webdriver.common.keys import Keys 
import os
import time
from multiprocessing import Pool
from lxml.html import fromstring
from fake_useragent import UserAgent
no = 1


parser = argparse.ArgumentParser()
#argparse 모듈 에 ArgumentParse() 함수 사용하여 parser 생성

parser.add_argument("-name", required=True)
# parser.add_argument("keyword", help="the keyword to search")
#  명령행 옵션을 지정하기 위해 사용합니다 명령행 옵션 인자는 -name으로 지정

# args = parser.parse_args()
#parse에 add_argument()함수 사용해 args 인스턴스생성

# people = args.people
# 명령행에서 받은 인자값을 people에 값을 넘겨줌

fish_list = (('꼼치','Tanaka snaifish',' Grassfish'),
('빨간양태','Red flathead','Bembras japonicus Cuvier'),
('까지양태','Spotted flathead','Cociella crocodila'),
('비늘양태','Devil flathead','Onigocia spinosa'),
('양태',' Bartail flathead','Platycephalus indicus'),
('홍감펭','Rosefish','Helicolenus hilgendorfi'),
('쏠배감펭','Butterfly fish','Pterois lunulata Temminck et Schlegel'),
('점감펭','Fire fish','Scorpaena neglecta neglecta Temminck et Schlegel'),
('볼락','Rock fish','Sebastes inermis Cuvier'),
('개볼락','Spotbelly rockfish','Sebastes pachycephalus pachycephalus Temminck et Schlegel'),
('조피볼락','Jacopever','Sebastes pachycephalus pachycephalus Temminck et Schlegel'),
('불볼락','Goldeye rockfish','Sebastes thompsoni '),
('우럭볼락','Armorclad rockfish','Sebastes hubbsi'),
('붉감펭','Yellowbarred red rockfish','Sebastiscus albofasciatus'),
('쏨뱅이','Scorpion fish','Sebastiscus marmoratus'),
('쑤기미','Devil stinger','Inimicus japonicus'),
('성대','Bluefin searobin','Chelidonichthys spinosus'),
('쌍뿔달재','Forksnout searobin','Lepidotrigla alata'),
('꼬마달재','Redbanded searobin','Lepidotrigla guentheri Hilgendorf'),
('가시달갱이','Longwing searobin','Lepidotrigla japonica'),
('달강어','Red guruard','Lepidotrigla microptera Gunther'),
('밑달갱이','Abyssal searobin','Lepidotrigla abysalis Jordan et Starks'),
('밑성대','Spottyback searobin','Pterygotrigla hemisticta'),
('꽁지양태','Japanese dragonet','Callionymus japonicus Houttuyn'),
('도화양태','Red dragonet','Callionymus japonicus Houttuyn'),
('풀넙치','Lyre flatfish','Citharoides macrolepidotus Hubbs'),
('넙치','Bastard','Paralichyhus olivaceus'),
('별넙치','Cinnamon flounder','Pseudorhombus cinnamoneus'),
('용가자미','Pointhead flounder','Cleisthenes pinetorum herzensteini'),
('줄가자미','Roughscale sole','Clidoderma asperrimum'),
('눈가자미','Rikuzen sole','Dexistes rikuzenius Jordan et Starks'),
('물가자미','Shotted halibut','Eopsetta grigorjewi'),
('기름가자미','Korean flounder','Glyptocephalus stelleri'),
('돌가자미','Stone flounder','Kareius bicoloratus '),
('참가자미','Flounder','Limanda herzensteini Jordan et Snyder'),
('층거리가자미','sand flounder','Limanda punctatissima'),
('문치가자미','Marbled sole','Limanda yokohamae'),
('찰가자미','Slime flounder','Microstomus achne'),
('도다리','Finespotted flounder','Pleuronichthys cornutus'),
('갈가자미','Willowy flounder','Tanakius kitaharai'),
('범가자미','Spotted halibut','Verasper variegatus'),
('참서대','Red tongue sole','Cynoglossus joyneri Gunther'),
('개서대','Robust tonguefish','Cynoglossus robustus Gunther'),
('흑대기','Black tonguefish','Paraplagusia japonica'),
('노랑각시서대','Many-banded sole','Zebrias fasciatus'),
('객주리','Unicorn filefish','Aluterus monoceros'),
('날개쥐치','Figured leathe rjacket','Aluterus scriptus'),
('말쥐치','Black scraper','Navodon modestus'),
('쥐치','File fish','Stephanolepis cirrhifer'),
('거북복','Black spotted boxfish','Ostracion cubicus Linnaeus'),
('가시복','Porcupine fish','Diodon holocanthus Linnaeus'),
('개복치','Head fish','Mola mola'),
('은밀복','Blowfish','Lagocephalus wheeleri Abe'),
('흑밀복','Brown-backed toadfish','Lagocephalus golveri Abe et Tabeta'),
('복섬','Grass puffer','Takifugu niphobles'),
('졸복','Panther puffer','Takifugu pardalis'),
('흰점복','Finepatterned pufferb','Takifugu poecilonotus'),
('검복','Globe fish','Takifugu porphyreus'),
('검자주복','Eyespot puffer','Takifugu pseudommus'),
('자주복','Tiger puffer','Takifugu rubripes'),
('까치복','Striped puffer','Takifugu xanthopterus'))

def download_image(link):
    global no
    # print(link)
    ua = UserAgent()
    headers = { "User-Agent": ua.random }

    try:
        r = req.get("https://www.google.com" + link.get("href"), headers=headers)
        
    except:
        print("Cannot get link")

    title = fromstring(r.content).findtext(".//title")
    link = title.split(" ")[-1]
    # print("At : " + os.getcwd() + ", Downloading from " + link)


    # try:
        
    if link.split(".")[-1] == ('jpg' or 'png' or 'jpeg'):
        # print("####" + link)
        # print(str(os.getcwd()) + "/" + str(no) + str(link.split(".")[-1]))
        # wget.download(link, str(os.getcwd()) + "/" + str(no) + str(link.split(".")[-1]))
        # print(no)
        # no = no+1
        t = urlopen(link).read()
        filename = str(no)+'.jpg'
        with open(filename,"wb") as f:
            f.write(t)
        # urllib.req.urlretrieve(link, link.split("/")[-1])
        no = no + 1
    # except:
    #     pass


def search(url):
    driver = webdriver.Chrome('/Users/fxd/Downloads/chromedriver')
    
    print(url)
    driver.get(url)
    driver.implicitly_wait(3)

    element = driver.find_element_by_tag_name("body")

    # scroll down
    for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(3)

    # driver.find_element_by_id("smb").click()

    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(3)

    time.sleep(1)

    source = driver.page_source
    driver.close()

    return source

def main():

    # 사용한 구글 url https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch
    # print(args)
    # query = args.name
    # url_info = "https://www.google.co.kr/search?"
    print(os.path.dirname(__file__))

    for fish in fish_list:
        global no
        no = 0
        query = fish[0] + ' ' + fish[2]
        url_info = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + query + \
                  "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:svga,itp:photo,ift:jpg"

        source = search(url_info)
        print("dir name : " + fish[2])

        if not(os.path.isdir(fish[2])):
            os.makedirs(os.path.join(fish[2]))

            os.chdir(os.getcwd() + "/" + fish[2])

            bsObject = BeautifulSoup(source, "html.parser")
            links = bsObject.find_all("a", class_="rg_l")

            for a in links[0:-1]:
                try:
                    download_image(a)
                except:
                    pass
            os.chdir("..")


    # with Pool() as pool:
    #     pool.map(download_image, links)


    
    # #url 요청 파싱값
    # html_object = req.get(url_info,params) #html_object html source 값
    # directory = params

    # if html_object.status_code == 200:
    #     #페이지 status_code 가 200 일때 2XX 는 성공을 이야기함
    #     bs_object = BeautifulSoup(html_object.text,"html.parser")
    #     #인스턴스 생성
    #     img_data = bs_object.find_all("img")
    #     #인스턴스의 find_all 이라는 함수에 img 태그가 있으면 img_data에 넣어줌

        
    #     if not(os.path.isdir(params["q"])):
    #         os.makedirs(os.path.join(params["q"]))
    #     # except OSError as e:
    #     #     if e.errno != errono.EEXIST:
    #     #         print("Failed to make directory")
    #     #         raise
    #     os.chdir(os.getcwd() + "/" + params["q"] )

    #     for i in enumerate(img_data[1:]):
    #         #딕셔너리를 순서대로 넣어줌
    #         t = urlopen(i[1].attrs['src']).read()
    #         filename = "byeongwoo_"+str(i[0]+1)+'.jpg'
    #         with open(filename,"wb") as f:
    #             f.write(t)
    #         print("Img Save Success")

if __name__=="__main__":
    main()