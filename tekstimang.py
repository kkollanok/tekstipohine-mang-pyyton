#--------------- < KOODIS KASUTATAVAD MUUTUJAD JA IMPORDID > ----------------

from time import sleep
from sys import exit

helistamine = "ei"   # - tingimuse kontroll, kasutusel funktsioonis KRUUSATEE_TELEFON
mobiililevi = 0      # - levi loendur, kasutusel funktsioonis KRUUSATEE_TELEFON
# kasutajanimi = ""    - mängija valitud nimi, kasutusel funktsioonis LÕPP_2

#--------------- <        FUNKTSIOONID MÄNGU JAOKS         > ----------------

def start():
    print("-> Sa ärkad üles liivarannal. Sul pole õrna aimugi, kuidas sa siia sattusid.")
    sleep(4.5)
    print("-> Karge meretuul puhub üle su juuste ning õhukeste riideesemete vahelt läbi. Parem võiks liikuma hakata, vahest saab veidikegi sooja.")
    sleep(6)
    print("-> Ümberringi vaadates märkad sa männimetsa, mis rannaga ühineb. Ühest kohast paistab metsa sisenevat väike teerada.")
    sleep(6)
    print("-> Rannajoont järgides on näha veidike maad edasi kõrgeid rannakaljusid - vahest saaks sealt rohkem infot su asukoha kohta.")
    sleep(6)
    print("-> Kas soovid minna männimetsa või mööda randa edasi? (männimets / rannakaljud)")
    
def männimets():
    sleep(0.5)
    print("\n-> Enesekindlalt suundud sa merelainetest kaugemale.")
    sleep(2)
    print("-> Metsa äärel jõuad sa väikese teeraja juurde. Sa otsustad seda järgida.")
    sleep(8)
    print("-> Vaevu pärast minut kõndimist hakkab rada harvenema ning eemalt paistab sulle midagi silma.")
    sleep(6)
    print("-> Lähemale kõndides näed, et see on üks vana kahekorruseline puitmaja, mis ei ole just kõige paremas seisus. Ilmselgelt pole siin keegi kaua elanud...")
    sleep(9)
    print("-> Maja õuest hargub välja teine rada.")
    sleep(3)
    print("-> See paistab enda suuna poolest minevat rannakaljude poole, kuigi päris kindel olla ei saa.")
    sleep(6)
    print("-> Kas sa soovid siseneda majja või liikuda mööda rada edasi? (maja / teerada)")
    
def rannakaljud():
    sleep(0.5)
    print("-> Soe liiv sinu jalge all krudisemas, alustad sa vaikselt kõnnakut mööda rannajoont edasi.")
    sleep(4)
    print("-> Mida lähemale jõuad, seda kõrgemad need kaljud tegelikusses paistavad.")
    sleep(5)
    print("-> Jalamile jõudes vaatled sa enda ees seiskuvat järsku tõusu ja väsimus võtab sinu üle võimust.")
    sleep(6)
    print("-> Ometi tõded sa endale, et midagi mõistlikumat teha ei ole ning sul on oluline teada saada, mis põhjusel sa siin ranna peal lebasid.")
    sleep(6)
    print("-> Tasapisi hakkad sa üles rühkima.")
    sleep(4)
    print("-> ...")
    sleep(3)
    print("-> ...")
    sleep(2)
    print("-> ...")
    sleep(1)
    print("-> ...")
    sleep(0.5)
    print("-> Nüüdseks tipus, viskad sa ennast maha ja võtad kena minuti enne kui ennast uuesti püsti ajad.")
    sleep(5)
    print("-> Sinu ees avaneb suurepärane vaade ümbruskonnale: ühelt poolt vaikne meri, teiselt poolt näivalt lõppematu männimets.")
    sleep(4)
    print("-> Neid kahti ühendab rand, mis ulatub ühest horisondist teise.")
    sleep(4)
    print("-> Metsa sees on näha erinevad lagendikke, kuid need ei sobi kokku tiheda metsamustriga, mis paneb sind kahtlustama, et siin on hiljuti tehtud raiet.")
    sleep(7)
    print("-> Suurimatest lagendikest veidike vasakule on näha midagi, mis meenutab mingi hoone katust, ning edasisel uurimisel selgub metsa äärel üks autotee, mis just maja juurde viib.")
    sleep(6)
    print("-> Tahe maja juurde rutata on suur, kuid sama suur on ka sinu kahtlustunne - sul ei ole õrna aimugi kus sa oled, ning mis siin toimub.")
    sleep(5)
    print("-> Kas sa soovid veel ringi vaadata või maja juurde minna? (maja / vaatan veel ringi)")

def rannakaljud_ringivaatamine():
    sleep(0.5)
    print("-> Vahest on tõesti parem veel veidike ringi vaadata.")
    sleep(3)
    print("-> Sa alustad mere kammimisega - vahest sattusid sa siia mingist laevast?")
    sleep(5)
    print("-> Kuid merest ei ole näha miskit. Enne kui sa aga enda pilgu pöörad, märkad sa midagi enda silmanurgast.")
    sleep(4)
    print("-> Kalju all, ranna peal lebab kinnitatult väike paat ning selle kõrval üks kuur.")
    sleep(5)
    print("-> Need on nutikalt ehitatud ühe kivinuki taha, nii et neid ei ole ranna pealt võimalik märgata, aga ülevalt avaneb sulle kogu vaatepilt.")
    sleep(5)
    print("-> See on kindlasti midagi huvitava...")
    sleep(1.5)
    print("-> Äkitselt tunned, kuidas keegi sind täiest jõust tagant lükkab.")
    sleep(3)
    print("-> Sa kaotad tasakaalu üle kontrolli ning koperdad pea ees üle kaljuääre.")
    sleep(4)
    print("-> Langemine ei võta kaua ning sa olid nii ehmunud, nii et ei suutnud olukordast kinni haarata, enne kui...")
    sleep(4)
    print("-> ...sa rind ees vastu maad lendasid.")
    sleep(2)

def tee_rannakaljudest_majja():
    return(0)

def tee_majast_rannakaljudesse():
    return(0)
    
def maja():
    sleep(0.5)
    print("\n-> Sa krabad ukselingist kinni, kuid vähimagi jõuga tõmmates on tunda, et uks ei ole raami korras korralikult kinni. Jõuad vaevalt eemale põigata, kui see eest kukub.")
    sleep(5)
    print("-> Seestpoolt ei näe maja sugugi nii hüljatud välja. Kõik mööbel on terve, kuid väga tolmune ja päikesevalgusest pleekinud.")
    sleep(5)
    print("-> Esimesel korrusel ringi käies märkad, et majas ei leidu mitte ühtegi muud eset - kõik on vaid mööbel, lihtsalt mööbel.")
    sleep(3)
    print("-> Tundub, nagu keegi ei olekski siin kunagi elanud. Nagu kõik on ainult dekoratsiooniks, mingiks eksponaadiks.")
    sleep(8)
    print("-> Tiirutades mööda esimest korrust jõuad sa lõpuks tagasi esikusse. Sinu ette jääb trepikoda, ning sul on võimalik liikuda ülesse, teisele korrusele, või alla, keldrisse.")
    sleep(7)
    print("-> Kas sa soovid liikuda üles või alla? (üles / alla)")
    
def kelder():
    sleep(0.5)
    print("\n-> Trepp alla on ebamugavalt kitsas, sundides sind liikuma aeglaselt.")
    sleep(5)
    print("-> Trepi lõpus asub veel üks uks, kuid see tundub kuidagi 'värksem' kui kõik muu siin majas, nagu see oleks hiljuti paigaldatud.")
    sleep(7)
    print("-> Sa avad ukse ning esimese asjana tungib sulle ninna tugev lõhn - terve ruum tundus olevat sidrunilõhnalist õhuvärskendajat täis.")
    sleep(6)
    print("-> Vaevalt jõuad sa lõhna päritolu uurida, kui su pilk jääb seisma ruumi nurgas asuvale objektile.")
    sleep(5)
    print("-> Alguses tundus see uskumatu, kuid lähemale liikudes said su silmad aina rohkem tõestust - nurgas seisis täies ilus päris leegiheitja.")
    sleep(8)
    print("-> Ülima uudishimu vastu leegiheitjat käsitleda ja katsetada, otsustad sa veel ringi vaadata.")
    sleep(5)
    print("-> Teisel pool ruumi seisab üks laud, mille peal lebavad paar kaustikut erinevate dokumentidega, tunduvalt saksa keeles, ning lisaks üks telefon.")
    sleep(7)
    print("-> Sa hakkad just dokumentidesse süvenema...")
    sleep(1)
    print("...kui korraga kuuled sa ülalkorruselt samme.")
    sleep(4)
    print("-> Proovides kiiresti telefoni krabada, tõukad sa seda kogemata ning see kukub see väikse kolksuga laua alla.")
    sleep(5)
    print("-> Piiksugi tegemata seisad sa laua juures paigal, kui korraga seiskuvad ka sammud.")
    sleep(4)
    print("-> Otsides väljapääsu võimalusi, jääb sulle silma vastasseinas asuv õhutusaken, mis on sinu jaoks piisava suurusega.")
    sleep(5)
    print("-> Sama kiiresti kui need seiskusid, taastuvad sammude hääled ning need suunduvad kindlalt keldri poole.")
    sleep(5)
    print("-> Sulle jääb vaid lühike hetk otsustada, kas kiiresti haarata leegiheitja või kummardada laua alla telefoni järgi.")
    sleep(6)
    print("-> Kumma sa valid? (mobiiltelefon / leegiheitja)")
    
def teine_korrus():
    return(0)
    
def mobiiltelefon():
    sleep(0.5)
    print("\n-> Mitte nii graatsiliselt laskud sa enda põlvedele ning hakkad telefoni otsima.")
    sleep(4)
    print("-> Kui see sul kätte on saanud, liipad sa laua juurest ukse ette ning lajatad selle kinni.")
    sleep(5)
    print("-> Sinu põksuvate südamelöökide vahelt on vahele kuulda, kuidas see tundmatu isik nüüd trepist alla suundub.")
    sleep(5)
    print("-> Otsustavalt sörgid sa akna juurde, tõmbad selle pärani lahti ning roomad kergelt läbi.")
    sleep(6)
    print("-> Nüüd seisad sa maja tagumisel poolel. Lahtisest aknast läbi pilgates märkad sa enda jälitajat, tumedas riietuses meesterahvast, kes otsustab akna sinnamaale jätta ning jookseb tagasi trepist ülesse, esikusse.")
    sleep(10)
    print("-> Telefonil on peal koodlukk, kuid nalja pärast 1234 proovides õnnestub sul siseneda. No muidugi - levi puudub.")
    sleep(5)
    orint("-> Telefonis on ka veel paar tavapärast rakendust ning Messenger, kuid ilma internetita see ei tööta.")
    sleep(5)
    print("-> Sa ei soovi siia enam kauemaks jääma, sest see mees võib iga hetk välja ilmuda. Maja taga märkad sa veel üht teed, mis paistab olevat suurem ning mille kohal liiguvad elektrijuhtmed majast metsa.")
    sleep(10)
    print("-> Maja nurgast aga paistab teerada, mis sinu arust viib rannakaljudeni. Äkki on seal levi olemas?")
    sleep(6)
    print("-> Kas soovid liikuda rannakaljude juurde või järgida kruusateed? (rannakaljud / kruusatee)")
    
def leegiheitja():
    return(0)
    
def magamistuba():
    return(0)
    
def kruusatee_telefon():
    global helistamine
    global mobiililevi
    sleep(0.5)
    print("\n-> Sa hakkad mööda teed kiirkõnnil edasi liikuma.")
    sleep(3)
    print("-> Esimese käänu juures majale järgi vaadates ei näe sa tundmatut meest kusagil. Sama palju kui see on ka kergendav, tekitab see ka muret, kuhu ta minna võis.")
    sleep(8)
    print("-> Mõne aja pärast väriseb su telefon, märgistamiseks, et oled tagasi levivõrgus.")
    sleep(1)
    while helistamine == "ei" and mobiililevi != 4:
        mobiililevi += 1
        print("-> *brrr*")
        sleep(3)
        print("-> Sinu telefon näitab " + str(mobiililevi) + " levipulka neljast.")
        sleep(2)
        if mobiililevi == 1:
            print("-> Sul on võimalus proovida kellegagi ühendust saada.")
            sleep(3)
        print("-> Kas soovid helistada? (jah / ei)")
        helistamine = input("> ")
        if helistamine == "ei" and mobiililevi != 4:
            print("-> Otsustasid veel veidike paremat levi oodata.")
            sleep(5)
        if helistamine == "ei" and mobiililevi == 4:
            print("-> Otsustasid üldse telefoni ära panna. Pigem hoiduda kahtlaste inimese asjade käsitlemisest!")
            sleep(4)
            lõpp_3()
    print("-> Esimese refleksina sisestad numbrivalikusse 112, kuid tekstiparandussüsteem automaatselt korrigeerib selle mingiks teiseks numbriks, mida sa ei tunne.")
    sleep(6)
    print("-> Sisestades 911 süsteem aga midagi ei paranda, nii et sellele on võimalik helistada.")
    sleep(5)
    print("-> Telefon kutsub...")
    sleep(12 / mobiililevi)
    if mobiililevi > 2:
        print("-> Mobiililevi oli hea, sellepärast ühendus kõne kiiresti.")
    else:
        print("-> Mobiililevi oli halb, sellepärast läks kõne ühendumisega kauem.")
    sleep(3)
    
def kruusatee_leegiheitja():
    return(0)
    
def magamistoast_kruusateele():
    return(0)
    
def magamistoast_rannakaljudele():
    return(0)
            
def lõpp_1():
    print("->")

def lõpp_2():
    print("-> Kõne on ühendatud, kuid mitte midagi ei ole kuulda. 'Hallo?' ütled sa torusse.")
    sleep(3)
    print("-> Hetkeline vaikus hõljub õhus, kuni seda lõikab vali hüüe telefonist: " + karakteri_nimi + ", aeg üles tulla!")
    sleep(4)
    print("\n\n\n-> Sa avad enda silmad. Kohev padi sinu pea all ning pehme tekk tekitavad sinus sooja ja kindla tunde. Siin küll mingit ohtu ei ole.")
    sleep(6)
    print("-> Kuigi oled veel väga unine, ajad end siiski püsti. Kui ema nõuab, siis on juba teada, et oled kooli hiljaks jäämas.")
    sleep(5)
    print("-> Proovid kangesti meenutada, mida öö jooksul unes nägid, kuid midagi ei torka pähe. Sa mäletad küll, et need on alati veidraid unenäod, kuid iga hommik on nad meelest läinud.")
    sleep(9)
    print("-> Viimasel ajal on need unenäod sulle meelde tuletanud ühte mänguasja, mida väiksena alati endaga voodisse võtsid.")
    sleep(5)
    print("-> See mänguasi, Käsna-Kalle kaisukas, seisab siiamaani sinu riiulil.")
    sleep(6)
    print("-> Vahest võiks järgmine õhtu kindluse mõttes selle enda kõrvale panna.")
    sleep(5)
    
def lõpp_3():
    return(0)

def lõpp():
    print("\nLÕPP!")
    print("Kas soovid uuesti mängida?")


#--------------- <         FUNKTSIOONID MÄNGU JAOKS        > ----------------
    


#--------------- <                MÄNGU KOOD               > ----------------

#--------------- <                MÄNGU KOOD               > ----------------