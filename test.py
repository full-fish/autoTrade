import win32com.client
 
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
 
# 종목코드 리스트 구하기
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = objCpCodeMgr.GetStockListByMarket(1) #거래소
# codeList2 = objCpCodeMgr.GetStockListByMarket(2) #코스닥
 
count=0
arr = []

print("거래소 종목코드", len(codeList))
for i, code in enumerate(codeList):
    if objCpCodeMgr.GetStockSectionKind(code) == 1 :
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        
        if count < 50 and stdPrice < 20000:
            arr.append(code)
            count+=1	
            print(i, code, secondCode, stdPrice, name)
        
        # print(i, code, secondCode, stdPrice, name)
    
 
# print("코스닥 종목코드", len(codeList2))
# for i, code in enumerate(codeList2):
#     secondCode = objCpCodeMgr.GetStockSectionKind(code)
#     name = objCpCodeMgr.CodeToName(code)
#     stdPrice = objCpCodeMgr.GetStockStdPrice(code)
#     print(i, code, secondCode, stdPrice, name)
 
# print("거래소 + 코스닥 종목코드 ",len(codeList) + len(codeList2))
# print("거래소 갯수",len(arr))
# print(arr.index('A000040'))
# print("거래소 갯수",arr[1])
print("거래소 갯수",len(arr))