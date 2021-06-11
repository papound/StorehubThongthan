import os
import csv
import codecs
from os import listdir
from os.path import isfile, join

class FixedPriceStorehubThongthan():

    def __init__(self):
        print("Hello World")

    def isCSVFile(self, fileName) -> bool:
        return not fileName.startswith("~$") and not fileName.startswith(".") and fileName.startswith("รายงานสินค้าคงเหลือ") and not fileName.startswith("current_thongthan_stock_price") and fileName.endswith(".csv")

    current_stock_price_file_name = "./input/current_thongthan_stock_price.csv"

    def doFixedPriceStorehubThongthan():
        csvFiles = [f for f in listdir("./input/") if (isfile(join("./input/", f)) and self.isCSVFile(self, f))]
        print(csvFiles)
        storehubDatas = None
        csvData = "SKU,Parent Product SKU,Product Name,Category,Price Type,Unit,Price,Cost,Supplier Price,Product Tags,Inventory Type,Track Stock Levels,Barcode,Variant Name 1,Variant Value 1,Variant Name 2,Variant Value 2,Variant Name 3,Variant Value 3,Thongthan_Quantity,Warning Stock Level,Ideal Stock Level,Supplier,Tax Name,Store Credits,Kitchen Printer,Product Id\n#Required (Must be unique),,Required,Optional,Required (Fixed/Variable/Unit),Required if the price type is Unit. Leave this field empty if the price Type is either Fixed or Variable.,Optional; 0 by default,Optional,Optional(this field can only be modified if 'Fix Supplier Price' is selected for at least one store in Account Settings),Optional; use semicolon ( ; ) to separate multiple tags,Optional(Simple/Composite/Serialized; Simple by default if tracking inventory),Required (0/1),Optional; Must be unique if specified; use semicolon ( ; ) to separate multiple barcodes,,,,,,,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; use semicolon ( ; ) to separate multiple suppliers,Optional,Optional,Optional,Please DO NOT TOUCH this column; as it contains each product's unique reference ID. Doing so will result in unsuccessful import for all products listed in this sheet.\n"
        try:
            with codecs.open(self.current_stock_price_file_name, encoding='utf-8-sig') as csvfile:
                storehubDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                storehubDatas.pop(0)
        except Exception as e:
            print("Exception: %s" % (e))
        for fileName in sorted(csvFiles):
            fileNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
            csvFileName = "./input/"+fileNameNoExt+".csv"
            csvFileNameGen = "./result/thongthan-fixed-price-gen-all.csv"
            newPriceDatas = None
            catagories = "Shirts"
            quantity = 'Thongthan_Quantity'
            count = 0
            try:
                with codecs.open(csvFileName, encoding='utf-8-sig') as csvfile:
                    newPriceDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                    newPriceDatas.pop(0)
                for sData in storehubDatas:
                    filteredData = list(filter(lambda newPrice: newPrice['SKU']==sData['SKU'],newPriceDatas))
                    if len(filteredData) > 0:
                        if float(filteredData[0]['Price']) != float(sData['Price']):
                            csvLine = sData['SKU']+",,"+sData['Product Name']+","+catagories+",Fixed,,"+filteredData[0]['Price']+","+filteredData[0]['Price']+",,,,1,"+sData['SKU']+",,,,,,,"+sData[quantity]+",,,,,,,"+sData['Product Id']+"\n"
                            csvData += csvLine
                            count+=1
                            print("%s : ราคา Storehub = %s, ราคา Aristosoft = %s" % (sData['SKU'],sData['Price'],filteredData[0]['Price']))
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
self = FixedPriceStorehubThongthan
self.doFixedPriceStorehubThongthan()