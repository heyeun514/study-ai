from icrawler.builtin import GoogleImageCrawler
import os

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

for fish in fish_list:
    dirName = os.getcwd() + "/" + fish[2]
    print(dirName)

    if os.path.isdir(dirName) == False:
        os.makedirs(dirName, exist_ok=True)

    google_crawler = GoogleImageCrawler(feeder_threads=1,\
                                         parser_threads=2,\
                                         downloader_threads=4,\
                                         storage={'root_dir' : dirName})

    google_crawler.crawl(keyword=fish[0], max_num=5000)
    google_crawler.crawl(keyword=fish[2], max_num=5000)
