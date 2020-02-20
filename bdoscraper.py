import requests
import json
import numpy as np

## MainCategory, Number of SubCategories. Can look in game to figure out what subcategory is what. It's in same order as CM.
Mainhand = [1,13]
SubWeapon = [5,12]
AwakeningWeapon = [10,17]
Armor = [15,6]
Accessories = [20,4]
Material = [25,8]
Enhancement = [30,2]
Consumables = [35,8]
## Food = 4, Elixers: Offense = 1, Defense = 2, Functional = 3
## Item Parts = 7
Lifetools = [40,10]
AlchemyStone = [45,4]
MagicCrystal = [50,7]
PearlItem = [55,8]
Dye = [60,8]
Mount = [65,13]
Ship = [70,9]
Wagon = [75,6]
Furniture = [80,9]

masterMainList = [1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
masterSubList = [13,12,17,6,4,8,2,8,10,4,7,8,8,13,9,6,9]



def getbuysellinfops4(itemid):
    url = "https://na-trade.ps.playblackdesert.com/Home/GetWorldMarketSubList"
    payload = '__RequestVerificationToken=Chdh-yD-44SMIBy0Y3F0umDRNiNDPfIk8rfqvabvqinbL8jQSi-g0vfXiu-8JCG7NF2kX1uB8oKheFrxEBSBBojh3-Kpy63OLsvXOsZ7GY01&mainKey=' + str(itemid) + '&usingCleint=0'

    ## Replace Cookie if this isn't working
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': '_ga=GA1.2.96153141.1580156083; _fbp=fb.1.1580308940744.908712404; _gid=GA1.2.616548541.1580844602; PA_CONSOLE_Session=xo032pu3khcwco1hzqikiyfn; __RequestVerificationToken=CBx2ewr4BsMXHITi-HscWDZjPOQH07TSuy714sBMNlRcpDhsqnukEmQ5d0fYlIByUQRxFaHiCupxG-Kau3nllP-Ep6dTcn-wkPtEl3pAim41',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}

    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)
    return json_data

#print(getbuysellinfo(9220))
## main category, sub category, name of file to write too, and if you want to loop through all sub categories (1) or just the one you've selected (0)
def centralMarketInfops4(mainCategory, subCategory, fileName):
    ## Replace this with new verification token each time you're loggin into central market to run this
    payloadrequestverification = 'ORz9lsTJid18oaiiqk1M_0xYZuKyOozkzCGQRDp7CvvlES9cwRLwe8ILaRxMB8TlCYLuhP0OY_V4MpFj8JUHT9MGUYXtteekWVtGKopjt0E1'

    url = "https://na-trade.ps.playblackdesert.com/Home/GetWorldMarketList"
    f = open(fileName, "w")
    info = []
    c = 0
    for mainCategoryNum in mainCategory:
        sub = subCategory[c]
        for subCategoryNum in range(0, sub):
            payload = '__RequestVerificationToken=' + str(payloadrequestverification) +'&mainCategory=' + str(mainCategoryNum) + '&subCategory=' + str(subCategoryNum)

            ## Replace Cookie if this isn't working
            headers= {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': '_ga=GA1.2.96153141.1580156083; _fbp=fb.1.1580308940744.908712404; _gid=GA1.2.616548541.1580844602; _gat=1; _gat_gtag_UA_115394003_1=1; PA_CONSOLE_Session=xo032pu3khcwco1hzqikiyfn; __RequestVerificationToken=CBx2ewr4BsMXHITi-HscWDZjPOQH07TSuy714sBMNlRcpDhsqnukEmQ5d0fYlIByUQRxFaHiCupxG-Kau3nllP-Ep6dTcn-wkPtEl3pAim41', 'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}

            response = requests.request("POST", url, headers=headers, data = payload)

            json_data = json.loads(response.text)

            for x in json_data['marketList']:
                info += getbuysellinfops4(x['mainKey'])['detailList']
        c += 1
    json.dump(info, f)
    f.close()

#centralMarketInfops4(masterMainList,masterSubList, 'marketinfo.json')


def deepinfotho():

    payload = '__RequestVerificationToken=LodrEPyaDZkceWwWfebrH0E6elwIIIn7Nf6jhvlj8jLp6BWEFXU2jsicGKkRYCC1el90-vWh25bHLjMSJicDzWoTr026ytMTXUaDWP6j7ZQ1&pricePerOne=16500&totalTradeCount=5648&keyType=0&mainKey=9220&subKey=0&count=0&name=Couscous&grade=2&mainCategory=35&subCategory=4&chooseKey=0&iconPath=url(%22https%3A%2F%2Fs1.playblackdesert.com%2Fps%2FStatic%2FNA%2FTradeMarket%2FCommon%2Fimg%2FBDO%2Fitem%2F9220.png%22)&sumCountText=0&countText=0&isUp=true&selectPrice=17700'
    url = "https://na-trade.ps.playblackdesert.com/Home/GetItemSellBuyInfo"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': '_ga=GA1.2.96153141.1580156083; _fbp=fb.1.1580308940744.908712404; _gid=GA1.2.616548541.1580844602; PA_CONSOLE_Session=xo032pu3khcwco1hzqikiyfn; __RequestVerificationToken=CBx2ewr4BsMXHITi-HscWDZjPOQH07TSuy714sBMNlRcpDhsqnukEmQ5d0fYlIByUQRxFaHiCupxG-Kau3nllP-Ep6dTcn-wkPtEl3pAim41', 'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'}

    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)

    return json_data

#print(deepinfotho())

def getbuysellinfo(itemid):
    url = "https://marketweb-na.blackdesertonline.com/Home/GetWorldMarketSubList"
    payload = '__RequestVerificationToken=gcTbcT21fM9ABmRM1MBdzC6YD6cqnkHJRkaXCv9o3ncAPsronblQJvkxYtBDMopN8LqkVeuKuqylxKeMUq2TYfTXZJbUNC-kaWRfj_jFLpk1&mainKey=' + str(itemid) + '&usingCleint=0'

    ## Replace Cookie if this isn't working
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': '_ga=GA1.2.1958542481.1581975632; _gid=GA1.2.1152027087.1581975632; ASP.NET_SessionId=nejqqzbdddpxwhmt0wyal55x; __RequestVerificationToken=8SAOQx-UWjXEEukXoH7ZReKqMb6DYIIfCPr-pW9s1IzJ1AWlNFNaiRG7vf8K61MxXIc9faKT2bdETSXApWxYahbK4n48Ltq6yWX4PVzxKbk1',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}

    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)

    return json_data


#print(getbuysellinfo(9220))
## main category, sub category, name of file to write too, and if you want to loop through all sub categories (1) or just the one you've selected (0)
def centralMarketInfo(mainCategory, subCategory, fileName):
    ## Replace this with new verification token each time you're loggin into central market to run this
    payloadrequestverification = 'Wjc2rQjslu4YO7tqyq3hkh-mIQQATP1G0qHFgkBNSeoR-aXlQqlul-XMbzfcTyrUQK0TJW-6T9K_GAvSegp5-GdraZLrYbCkoQH__9q7RXo1'

    url = "https://marketweb-na.blackdesertonline.com/Home/GetWorldMarketList"
    f = open(fileName, "w")
    info = []
    c = 0
    for mainCategoryNum in mainCategory:
        sub = subCategory[c]
        for subCategoryNum in range(0, sub):
            payload = '__RequestVerificationToken=' + str(payloadrequestverification) +'&mainCategory=' + str(mainCategoryNum) + '&subCategory=' + str(subCategoryNum)

            ## Replace Cookie if this isn't working
            headers= {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': '_ga=GA1.2.1958542481.1581975632; _gid=GA1.2.1152027087.1581975632; ASP.NET_SessionId=nejqqzbdddpxwhmt0wyal55x; __RequestVerificationToken=8SAOQx-UWjXEEukXoH7ZReKqMb6DYIIfCPr-pW9s1IzJ1AWlNFNaiRG7vf8K61MxXIc9faKT2bdETSXApWxYahbK4n48Ltq6yWX4PVzxKbk1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}

            response = requests.request("POST", url, headers=headers, data = payload)

            json_data = json.loads(response.text)

            for x in json_data['marketList']:
                info += getbuysellinfo(x['mainKey'])['detailList']
        c += 1
    json.dump(info, f)
    f.close()

centralMarketInfo(masterMainList,masterSubList, 'marketinfo.json')