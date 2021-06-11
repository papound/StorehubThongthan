import os
import csv
import codecs
from os import listdir
from os.path import isfile, join
import shutil

class PrepareCountStockThongthanCSV():

    def __init__(self):
        print("Hello World")

    def isCSVFile(self, fileName) -> bool:
        return not fileName.startswith("~$") and not fileName.startswith(".") and fileName.startswith("PI") and not fileName.startswith("current_thongthan_stock_price") and fileName.endswith(".csv")

    dataDriven = {}
    current_stock_price_file_name = "./input/current_thongthan_stock_price.csv"

    def doPrepareStockThongthanCSV():
        csvFiles = [f for f in listdir("./input/") if (isfile(join("./input/", f)) and self.isCSVFile(self, f))]
        print(csvFiles)
        i = 0
        totalCount = 0
        totalLen = 0
        notFound = 0
        notFoundCsvData="Not Found SKU\n"
        stockPrices = None
        duplicatedProducts = []
        notFoundProduct = []
        csvData = "SKU,Parent Product SKU,Product Name,Category,Price Type,Unit,Price,Cost,Supplier Price,Product Tags,Inventory Type,Track Stock Levels,Barcode,Variant Name 1,Variant Value 1,Variant Name 2,Variant Value 2,Variant Name 3,Variant Value 3,Thongthan_Quantity,Warning Stock Level,Ideal Stock Level,Supplier,Tax Name,Store Credits,Kitchen Printer,Product Id\n#Required (Must be unique),,Required,Optional,Required (Fixed/Variable/Unit),Required if the price type is Unit. Leave this field empty if the price Type is either Fixed or Variable.,Optional; 0 by default,Optional,Optional(this field can only be modified if 'Fix Supplier Price' is selected for at least one store in Account Settings),Optional; use semicolon ( ; ) to separate multiple tags,Optional(Simple/Composite/Serialized; Simple by default if tracking inventory),Required (0/1),Optional; Must be unique if specified; use semicolon ( ; ) to separate multiple barcodes,,,,,,,Optional; 0 by default if tracking inventory,Optional,Optional,Optional; use semicolon ( ; ) to separate multiple suppliers,Optional,Optional,Optional,Please DO NOT TOUCH this column; as it contains each product's unique reference ID. Doing so will result in unsuccessful import for all products listed in this sheet.\n"
        try:
            with codecs.open(self.current_stock_price_file_name, encoding='utf-8-sig') as csvfile:
                stockPrices = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                stockPrices.pop(0)
        except Exception as e:
            print("Exception: %s" % (e))
        for fileName in sorted(csvFiles):
            fileNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
            csvFileName = "./input/"+fileNameNoExt+".csv"
            csvFileNameGen = "./result/thongthan-count-gen-all.csv"
            csvFileNameTemp = "./result/thongthan-count-temp.csv"
            csvFileNameNotFound = "./result/notFound.csv"
            stockDatas = None
            tempDatas = None
            catagories = "Shirts"
            count = 0
            try:
                if i < len(csvFiles):
                    print("i = %d" % (i))
                    # Get csv data
                    with codecs.open(csvFileName, encoding='utf-8-sig') as csvfile:
                        stockDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                        stockDatas.pop(0)
                    # Get temp data
                    if i == 0:
                        # first load temp data
                        if os.path.exists(csvFileNameTemp):
                            print('Remove existing %s' % (csvFileNameTemp))
                            os.remove(csvFileNameTemp)
                            print('Copying %s' % (csvFileNameTemp))
                            shutil.copyfile(csvFileName, csvFileNameTemp)
                        else:
                            print('Copying %s' % (csvFileNameTemp))
                            shutil.copyfile(csvFileName, csvFileNameTemp)
                        with codecs.open(csvFileNameTemp, encoding='utf-8-sig') as csvfile:
                            tempDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                            tempDatas.pop(0)
                    else:
                        # reload temp data
                        print('Loading existing temp data %s' % (csvFileNameTemp))
                        with codecs.open(csvFileNameTemp, encoding='utf-8-sig') as csvfile:
                            tempDatas = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
                            tempDatas.pop(0)
                    print("----------------------------------")
                    totalLen += len(stockDatas)
                    for stockData in stockDatas:
                        existingData = None
                        filteredData = list(filter(lambda price: price['SKU']==stockData['Barcode'],stockPrices))
                        if tempDatas is not None:
                            existingData = list(filter(lambda tempData: tempData['Barcode']==stockData['Barcode'],tempDatas))
                        if len(filteredData) > 0:
                            fData = filteredData[0]
                            price = fData['Price']
                            desc = fData['Product Name']
                            productId = fData['Product Id']
                            #Find duplicate data
                            if i>0 and existingData is not None and len(existingData) > 0:
                                print("Found duplicate %s" % (existingData[0]['Barcode']))
                                print("Exisitng Quantity %s" % (existingData[0]['Quantity']))
                                print("Current Quantity %s" % (stockData['Quantity']))
                                newQuantity = str(float(int(float(existingData[0]['Quantity'])) + int(float(stockData['Quantity']))))
                                print("New Quantity %s" % (newQuantity))
                                print('Removing duplicate products')
                                reading_file = open(csvFileNameTemp, "r")
                                restFile = reading_file.readlines()
                                reading_file.close()
                                for line in restFile:
                                    if line.startswith(existingData[0]['Barcode']):
                                        line= stockData['Barcode']+",,"+desc+","+catagories+",Fixed,,"+price+","+price+",,,,1,"+stockData['Barcode']+",,,,,,,"+newQuantity+",,,,,,,"+productId+"\n"
                                updating_file = open(csvFileNameTemp, "w+")
                                updating_file.writelines(restFile)
                                updating_file.close()
                                print("Found duplicate %s, update quantity to %s" % (existingData[0]['Barcode'], newQuantity))
                                duplicatedProducts.append({
                                    'SKU': existingData[0]['Barcode'],
                                    "Desc": desc,
                                    'NewQuantity': newQuantity,
                                    "Price": price,
                                    "ProductId": productId
                                })
                                print("----------------------------------")
                            else:
                                csvData += stockData['Barcode']+",,"+desc+","+catagories+",Fixed,,"+price+","+price+",,,,1,"+stockData['Barcode']+",,,,,,,"+stockData['Quantity']+",,,,,,,"+productId+"\n"
                            count += 1
                        else:
                            notFoundCsvData += stockData['Barcode']+"\n"
                            notFoundProduct.append(stockData['Barcode'])
                            notFound+=1
                    
                    print('Analyzed data from %s total of %d rows' % (csvFileName, count))
                    
                    totalCount+= count
                # append temp data
                if i>0:
                    f=open(csvFileNameTemp, "a+")
                    # Append 'hello' at the end of file
                    print('appending temp file')
                    reading_file = open(csvFileName, "r")
                    reading_file.readline()
                    restFile = reading_file.readlines()
                    # restLines = ""
                    # for line in restFile:
                    #     restLines += line
                    f.writelines(restFile)
                    f.close()
                i+=1
                if i > len(csvFiles) -1:
                    if notFound > 0:
                        if os.path.exists(csvFileNameNotFound):
                            # print('Remove existing %s' % (csvFileNameNotFound))
                            os.remove(csvFileNameNotFound)
                        print("-----------notFoundProduct-------------")
                        print(notFoundProduct)
                        print("----------------------------------")
                        f = codecs.open(csvFileNameNotFound, "w","utf-8")
                        f.write(notFoundCsvData)
                        f.close()
                    if os.path.exists(csvFileNameGen):
                        print('Remove existing %s' % (csvFileNameGen))
                        os.remove(csvFileNameGen)
                    print('Writing full report to %s' % (csvFileNameGen))
                    d = codecs.open(csvFileNameGen, "w","utf-8")
                    d.write(csvData)
                    d.close()
                    print("Total Data = %d row(s)\nTotal Insert = %d row(s)\nDuplicated %d row(s)\nNot Found %d product(s)" % (totalLen, totalCount, len(duplicatedProducts), len(notFoundProduct)))
                    print("----------------------------------")
                    if len(duplicatedProducts) > 0:
                        print("-----------duplicatedProducts-------------")
                        print(duplicatedProducts)
                        print("----------------------------------")
                        for dup in duplicatedProducts:
                            print("Replace duplicate %s, update quantity to %s" % (dup['SKU'], dup['NewQuantity']))
                            reading_file = open(csvFileNameGen, "r")
                            restFile = reading_file.readlines()
                            reading_file.close()
                            dupCode = 0
                            restFileDistinct = []
                            for line in restFile:
                                if dupCode==0 and line.startswith(dup['SKU']):
                                    line= dup['SKU']+",,"+dup['Desc']+","+catagories+",Fixed,,"+dup['Price']+","+dup['Price']+",,,,1,"+dup['SKU']+",,,,,,,"+dup['NewQuantity']+",,,,,,,"+dup['ProductId']+"\n"
                                    restFileDistinct.append(line)
                                    dupCode+=1
                                elif not line.startswith(dup['SKU']):
                                    restFileDistinct.append(line)
                            updating_file = open(csvFileNameGen, "w+")
                            updating_file.writelines(restFileDistinct)
                            updating_file.close()
                    print("----------------------------------")
                    if os.path.exists(csvFileNameTemp):
                        print('Remove %s' % (csvFileNameTemp))
                        os.remove(csvFileNameTemp)
                        print("----------------------------------")
                    break
            except Exception as e:
                print("Exception2: %s" % (e))
self = PrepareCountStockThongthanCSV
self.doPrepareStockThongthanCSV()