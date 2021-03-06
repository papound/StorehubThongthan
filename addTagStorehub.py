# -*- coding: utf-8 -*-
import os
import csv
import codecs
from os import listdir
from os.path import isfile, join

class AddTagStorehubThongthan():

    def __init__(self):
        print("Hello World")

    def isCSVFile(self, fileName) -> bool:
        return not fileName.startswith("~$") and not fileName.startswith(".") and fileName.startswith("รายงานสินค้าคงเหลือ") and not fileName.startswith("current_thongthan_stock_price") and fileName.endswith(".csv")

    current_stock_price_file_name = "./input/current_thongthan_stock_price.csv"

    def doAddTagStorehubThongthan():
        csvFiles = [f for f in listdir("./input/") if (isfile(join("./input/", f)) and self.isCSVFile(self, f))]
        print(csvFiles)
        storehubDatas = None
        csvData = '''SKU,Parent Product SKU,Product Name,Category,Price Type,Unit,Price,Discounted Price,Cost,Supplier Price,Product Tags,Inventory Type,Track Stock Levels,Barcode,Thongthan_Quantity,Thongthan_Warning Stock Level,Thongthan_Ideal Stock Level,Highbury-Platinum_Quantity,Highbury-Platinum_Warning Stock Level,Highbury-Platinum_Ideal Stock Level,Sale_Quantity,Sale_Warning Stock Level,Sale_Ideal Stock Level,Presale_Quantity,Presale_Warning Stock Level,Presale_Ideal Stock Level,OnlineSale_Quantity,OnlineSale_Warning Stock Level,OnlineSale_Ideal Stock Level,Supplier,Tax Name,Store Credits,Kitchen Printer,Product Id\nSKU,Parent Product SKU,Product Name,Category,Price Type,Unit,Price,Discounted Price,Cost,Supplier Price,Product Tags,Inventory Type,Track Stock Levels,Barcode,Thongthan_Quantity,Thongthan_Warning Stock Level,Thongthan_Ideal Stock Level,Highbury-Platinum_Quantity,Highbury-Platinum_Warning Stock Level,Highbury-Platinum_Ideal Stock Level,Sale_Quantity,Sale_Warning Stock Level,Sale_Ideal Stock Level,Presale_Quantity,Presale_Warning Stock Level,Presale_Ideal Stock Level,OnlineSale_Quantity,OnlineSale_Warning Stock Level,OnlineSale_Ideal Stock Level,Supplier,Tax Name,Store Credits,Kitchen Printer,Product Id\n'''
        try:
            with codecs.open(self.current_stock_price_file_name, encoding='utf-8-sig') as csvfile:
                storehubDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                storehubDatas.pop(0)
        except Exception as e:
            print("Exception: %s" % (e))
        for fileName in sorted(csvFiles):
            fileNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
            csvFileName = "./input/"+fileNameNoExt+".csv"
            csvFileNameGen = "./result/thongthan-add-tag-gen-all.csv"
            newPriceDatas = None
            catagories = "Shirts"
            tt_quantity = 'Thongthan_Quantity'
            hb_quantity = 'Highbury-Platinum_Quantity'
            s_quantity = 'Sale_Quantity'
            ps_quantity = 'Presale_Quantity'
            os_quantity = 'OnlineSale_Quantity'
            count = 0
            try:
                with codecs.open(csvFileName, encoding='utf-8-sig') as csvfile:
                    newPriceDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                    newPriceDatas.pop(0)
                for sData in storehubDatas:
                    tags = []
                    #gender_tags
                    gender_tags = "ชาย;" if sData['Product Name'].find("ชาย") != -1 else "หญิง;" if sData['Product Name'].find("หญิง") != -1 else ""
                    #shirt_tags
                    shirt_tags = "เชิ้ต;" if sData['Product Name'].find("เชิ้ต") != -1 or sData['Product Name'].find("เชิ๊ต") != -1 else "โปโล;" if sData['Product Name'].find("โปโล") != -1 else "เข็มขัด;" if sData['Product Name'].find("เข็มขัด") != -1 else "กางเกง;" if sData['Product Name'].find("กางเกง") != -1 else ""
                    #stripes_tags
                    stripes_tags = "ลายสก๊อต;" if sData['Product Name'].find("สก๊อต") != -1 else "ผ้าพื้น;" if sData['Product Name'].find("พื้น") != -1 else "ลายริ้ว;" if sData['Product Name'].find("ริ้ว") != -1 else ""
                    #length_tags
                    shirt_length_tags = "แขนสั้น;" if sData['Product Name'].find("แขนสั้น") != -1 else "แขนยาว;" if sData['Product Name'].find("แขนยาว") != -1 else "แขนสามส่วน;" if sData['Product Name'].find("สามส่วน") != -1 else ""
                    kangkeng_length_tags = "ขาสั้น;" if sData['Product Name'].find("สั้น") != -1 else "ขายาว;" if sData['Product Name'].find("ยาว") != -1 else "ขาสามส่วน;" if sData['Product Name'].find("สามส่วน") != -1 else ""
                    tags.append(gender_tags)
                    tags.append(shirt_tags)
                    tags.append(stripes_tags)
                    if shirt_tags.find('') != -1: 
                        tags.append(shirt_length_tags)
                    else:
                        tags.append(kangkeng_length_tags)
                    fullTag = ""
                    for tag in tags:
                        if tag != "":
                            fullTag += tag
                    csvLine = sData['SKU']+",,"+sData['Product Name']+","+catagories+",Fixed,,"+sData['Price']+",,"+sData['Price']+",,"+fullTag+",,1,"+sData['SKU']+","+sData[tt_quantity]+",,,"+sData[hb_quantity]+",,,"+sData[s_quantity]+",,,"+sData[ps_quantity]+",,,"+sData[os_quantity]+",,,,,,,"+sData['Product Id']+"\n"
                    csvData += csvLine
                    count+=1
                print("----------------------------------")
                print('Total Fixed = %d products' % (count))
                if os.path.exists(csvFileNameGen):
                    print("----------------------------------")
                    print('Remove Existing %s' % (csvFileNameGen))
                    os.remove(csvFileNameGen)
                    print("----------------------------------")
                print('Writing full report to %s' % (csvFileNameGen))
                d = codecs.open(csvFileNameGen, "w","utf-8")
                d.write(csvData)
                d.close()
                print("----------------------------------")
            except Exception as e:
                print("Exception2: %s" % (e))
self = AddTagStorehubThongthan
self.doAddTagStorehubThongthan()