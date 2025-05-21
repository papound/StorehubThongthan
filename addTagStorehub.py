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
        return not fileName.startswith("~$") and not fileName.startswith(".") and fileName.startswith("current_thongthan_stock_price") and fileName.endswith(".csv") and not fileName.endswith("bak.csv")

    current_stock_price_file_name = "./input/current_thongthan_stock_price.csv"

    def get_color_info(code):
        try:
            color_code_map = {
                                0: {"thai": "ขาว", "english": "white", "hex": "#FFFFFF"},
                                1: {"thai": "ครีม", "english": "cream", "hex": "#FFFDD0"},
                                2: {"thai": "ฟ้า", "english": "sky blue", "hex": "#87CEEB"},
                                3: {"thai": "ชมพู", "english": "pink", "hex": "#FFC0CB"},
                                4: {"thai": "กรม", "english": "navy", "hex": "#000080"},
                                5: {"thai": "ดำ", "english": "black", "hex": "#000000"},
                                6: {"thai": "เทา", "english": "gray", "hex": "#808080"},
                                7: {"thai": "น้ำตาล", "english": "brown", "hex": "#8B4513"},
                                8: {"thai": "ฟ้าเข้ม", "english": "dark sky blue", "hex": "#4682B4"},
                                9: {"thai": "ม่วง", "english": "purple", "hex": "#800080"},
                                10: {"thai": "แดง", "english": "red", "hex": "#FF0000"},
                                11: {"thai": "เขียว", "english": "green", "hex": "#008000"},
                                12: {"thai": "ส้ม", "english": "orange", "hex": "#FFA500"},
                                13: {"thai": "ฟ้าทะเล", "english": "sea blue", "hex": "#5F9EA0"},
                                14: {"thai": "โอรส", "english": "peach", "hex": "#FFDAB9"},
                                15: {"thai": "กรมเข้ม", "english": "dark navy", "hex": "#000066"},
                                16: {"thai": "บานเย็น", "english": "magenta", "hex": "#FF00FF"},
                                17: {"thai": "เลือดหมู", "english": "maroon", "hex": "#800000"},
                                18: {"thai": "น้ำตาลอมเทา", "english": "grayish brown", "hex": "#A0522D"},
                                19: {"thai": "ม่วงเข้ม", "english": "dark purple", "hex": "#4B0082"},
                                20: {"thai": "กากี", "english": "khaki", "hex": "#F0E68C"},
                                21: {"thai": "เทาอ่อน", "english": "light gray", "hex": "#D3D3D3"},
                                22: {"thai": "ฟ้าอมน้ำตาล", "english": "sky brownish", "hex": "#B0C4DE"},
                                23: {"thai": "เหลืองเข้ม", "english": "dark yellow", "hex": "#FFD700"},
                                24: {"thai": "น้ำตาลทอง", "english": "golden brown", "hex": "#996515"},
                                25: {"thai": "เทาดำเข้ม", "english": "dark charcoal", "hex": "#2F4F4F"},
                                26: {"thai": "ฟ้าเทา", "english": "bluish gray", "hex": "#6699CC"},
                                27: {"thai": "น้ำตาลเข้ม", "english": "dark brown", "hex": "#5C4033"},
                                28: {"thai": "ขี้ม้า", "english": "earth brown", "hex": "#70543E"},
                                29: {"thai": "น้ำตาลทอง", "english": "gold brown", "hex": "#996515"},
                                32: {"thai": "ฟ้าอ่อน", "english": "light blue", "hex": "#ADD8E6"},
                                33: {"thai": "เขียวอ่อน", "english": "light green", "hex": "#90EE90"},
                                34: {"thai": "เทาม่วง", "english": "purple gray", "hex": "#8B8BAE"},
                                35: {"thai": "เขียวคล้ำ", "english": "dark green", "hex": "#006400"},
                                36: {"thai": "เขียวหัวเป็ด", "english": "teal green", "hex": "#006A4E"},
                                37: {"thai": "เหลืองมันปู", "english": "mustard yellow", "hex": "#E1B500"},
                                38: {"thai": "กรมเทา", "english": "gray navy", "hex": "#343B4C"},
                                39: {"thai": "ชมพูเข้ม", "english": "deep pink", "hex": "#FF1493"},
                                40: {"thai": "ครีมอ่อน", "english": "light cream", "hex": "#FFF8DC"}
                            }
            code = int(code)
            return color_code_map.get(code, {"thai": "", "english": "", "hex": ""})
        except ValueError:
            return {"thai": "", "english": "", "hex": ""}

    def doAddTagStorehubThongthan():
        csvFiles = [f for f in listdir("./input/") if (isfile(join("./input/", f)) and self.isCSVFile(self, f))]
        print(csvFiles)
        storehubDatas = None
        csvData = '''SKU,Parent Product SKU,Product Name,Category,Price Type,Unit,Tax-Exclusive Price,Min Price,Max Price,Cost,Supplier Price,Product Tags,Inventory Type,Track Stock Levels,Barcode,Thongthan_Quantity,Thongthan_Warning Stock Level,Thongthan_Ideal Stock Level,Highbury-Platinum_Quantity,Highbury-Platinum_Warning Stock Level,Highbury-Platinum_Ideal Stock Level,Sale_Quantity,Sale_Warning Stock Level,Sale_Ideal Stock Level,Presale_Quantity,Presale_Warning Stock Level,Presale_Ideal Stock Level,OnlineSale_Quantity,OnlineSale_Warning Stock Level,OnlineSale_Ideal Stock Level,Shopee_Quantity,Shopee_Warning Stock Level,Shopee_Ideal Stock Level,Lazada_Quantity,Lazada_Warning Stock Level,Lazada_Ideal Stock Level,Showroom_Quantity,Showroom_Warning Stock Level,Showroom_Ideal Stock Level,FactorySale_Quantity,FactorySale_Warning Stock Level,FactorySale_Ideal Stock Level,Supplier,Tax Name,Store Credits,Kitchen Station,Product Id,Online Price,Online Discounted Price,Product Description\n#Required(Must be unique),,Required,Optional,Required(Fixed/Variable/Unit),Required if the price type is Unit. Leave this field empty if the price Type is either Fixed or Variable.,Optional; 0 by default,Optional (This field can only be modified when pricing type is variable); The value should be Tax-Exclusive as per your Display Price setting in the BackOffice.,Optional (This field can only be modified when pricing type is variable); The value should be Tax-Exclusive as per your Display Price setting in the BackOffice.,Optional,Optional(this field can only be modified if 'Fix Supplier Price' is selected for at least one store in Account Settings),Optional(Use ; to separate multiple tags),Optional(Simple/Composite/Serialized; Simple by default if tracking inventory),Required; Enter 0 to disable; 1 to enable,Optional(Must be unique if specified),Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; 0 by default if tracking inventory,Optional,Optional,Optional(Use ; to separate multiple suppliers),Optional,Optional,Optional; Leave it blank for Default Kitchen Station; Enter 'Do Not Print Kitchen Docket' to not print kitchen docket,Please DO NOT TOUCH this column; as it contains each product's unique reference ID. Doing so will result in unsuccessful import for all products listed in this sheet.,Optional; The value should be Tax-Exclusive as per your Display Price setting in the BackOffice.,Optional; The value should be Tax-Exclusive as per your Display Price setting in the BackOffice.,Optional\n'''
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
                    #colour_tags
                    sku_tags = sData['SKU'].split("_")
                    colour_tags = ""
                    colour_thai_tags = ""
                    tags.append(gender_tags)
                    tags.append(shirt_tags)
                    tags.append(stripes_tags)
                    if shirt_tags.find('') != -1: 
                        tags.append(shirt_length_tags)
                        if len(sku_tags) == 3 and (sData['Product Name'].find("เชิ้ต") != -1 or sData['Product Name'].find("เข็มขัด") != -1):
                            colour_tags = "สี"+sku_tags[1]+";"
                            colour_thai = self.get_color_info(sku_tags[1])["thai"]
                            colour_eng = self.get_color_info(sku_tags[1])["english"]
                            tags.append(colour_tags)
                            if (len(colour_thai) > 0):
                                colour_thai_tags = "สี"+colour_thai+";"
                                colour_eng_tags = "สี"+colour_eng+";"
                                tags.append(colour_thai_tags)
                                tags.append(colour_eng_tags)
                    else:
                        tags.append(kangkeng_length_tags)
                    fullTag = ""
                    for tag in tags:
                        if tag != "":
                            fullTag += tag
                    csvLine = sData['SKU']+",,"+sData['Product Name']+","+catagories+",Fixed,,"+sData['Tax-Exclusive Price']+",,,"+sData['Tax-Exclusive Price']+",,"+fullTag+",Simple,1,"+sData['SKU']+","+sData[tt_quantity]+",,,"+sData[hb_quantity]+",,,"+sData[s_quantity]+",,,"+sData[ps_quantity]+",,,"+sData[os_quantity]+",,,,,,,,,,,,,,,,,,,"+sData['Product Id']+",,,\n"
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