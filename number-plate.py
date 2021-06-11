# 20:36 ณฐมนต์ ตัด 7 1 6 เหลือเศษ 9 
# 20:38 ณฐมนต์ รวมเศษ 5 ทำมาหากินดีและ หรือ 9 เทวดารักษา จะดีที่สุด บวกเลขในออนไลน์แล้วจอง 

import random

class NumberPlate():

    def __init__(self):
        print("Hello World")

    def doFindNumberPlate():
        try:
            tummahagin = []
            godblessed = []
            definitelyNotOK = ['01', '02', '03', '06', '07', '10', '11', '12', '13', '17', '19', '20', '21', '30', '31', '33', '35', '36', '37', '38', '39', '53', '60', '63', '67', '70', '71', '73', '76', '77', '83', '91', '93']
            definitelyOK = ['15', '22', '23', '24', '26', '28', '29', '32', '35', '36', '42', '45', '49', '51', '53', '54', '55', '59', '62', '63', '66', '82', '89', '92', '94', '95', '98', '99']
            while (len(godblessed) < 8 or len(tummahagin) < 8):
                number = str(random.randint(0,999))
                number = number.zfill(3)
                lists = [int(number[0]),int(number[1]),int(number[2])]
                sum4Digit = str(lists[0] + lists[1] + lists[2])
                sum4Digit = sum4Digit.zfill(2)
                sum2Digit = int(sum4Digit[0]) + int(sum4Digit[1])
                notOK = [0,1,3,6,7]
                bool1 = str(lists[0])+str(lists[1]) in definitelyOK
                bool2 = str(lists[1])+str(lists[2]) in definitelyOK
                bool3 = str(lists[0])+str(lists[1]) not in definitelyNotOK
                bool4 = str(lists[1])+str(lists[2]) not in definitelyNotOK
                if len(list(filter(lambda tempData: tempData not in notOK and bool1 and bool2 and bool3 and bool4,lists))) == 3:
                    # ไม่มี เลข 7, 1, 6
                    wantedStr = str(lists[0])+str(lists[1])+str(lists[2])
                    # print("--------this number %s is ok-----sum2digit----%s" % (wantedStr, sum2Digit))
                    if sum2Digit == 5 and wantedStr not in tummahagin:
                        print("ทะเบียน ทำมาหากิน %d%d%d, ผลรวม 3 หลัก = %s, ผลรวม 2 หลัก = %s" % (lists[0],lists[1],lists[2],sum4Digit,sum2Digit))
                        tummahagin.append(wantedStr)
                    elif sum2Digit == 9 and wantedStr not in godblessed:
                        print("ทะเบียน เทวดารักษา %d%d%d, ผลรวม 3 หลัก = %s, ผลรวม 2 หลัก = %s" % (lists[0],lists[1],lists[2],sum4Digit,sum2Digit))
                        godblessed.append(wantedStr)
                        # i+=1
            print("-----------ทำมาหากิน-------------")
            print(sorted(tummahagin))
            print("-----------เทวดารักษา------------")
            print(sorted(godblessed))
        except Exception as e:
            print(e)
self = NumberPlate
self.doFindNumberPlate()
