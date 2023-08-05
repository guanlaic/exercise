'''
print() 列印輸出的內容

語法:print(value,......, sep = 分隔字元 end = 結束字元, file = sys.stdout.flush = Flase)



value
想要輸出的資料 . 可一次輸入多筆. 資料間以逗號分隔

sep  
分隔字元 , 想輸入多筆資料時可使用 預設值是一個空白字元

end 
資料結束時插入的字元 預設值為換行字元('\n') 下一次執行print涮就會印在下一行輸出,如不想換行可加入空字串

file  
資料輸出位置 . 預設位置為sys.stdout,也就是螢幕.也可使用此設定,將輸出導入其他檔案,設備等

flush
是否刪除資料流緩衝區,預設為Flase





參數格式化 %

語法 print("---輸出格式區"  % (變數系列區)

%d 格式化整數輸出
%f 格式化浮點數輸出
%x 格式化16進位整數輸出
%X 格式化大寫16進位整數輸出
%o 格式化8進位整數輸出
%s 格式化字串輸出
%e 格式化科學記號e輸出
%E 格式化科學記號E大寫輸出

精準控制格式化輸出

%(+|-)nd 格式化整數輸出
%(+|-)m.nf 格式化浮點數輸出
%(+|-)ns 格式化字串輸出
%(-)m.s m是輸出字串寬度,s是顯示字串長度,n小於字串長度會有裁減效果
%(+|-)e 格式化科學記號e輸出
%(+|-)E 格式化科學記號E輸出



 
參數格式化 {} 和format (函數)

語法 print("...輸出格式區...".format(變數系列區,...))

基本上跟 %格式化概念相似 format是使用":"


>: 靠右對齊
<: 靠左對齊
^: 置中對齊



參數格式化 f-string(方便好用)

語法 f'{變數或運算式}

name = "glass"
hoo = "草"
print(f'{name}是{hoo}')


資料型別轉換

int() 強制轉整數
float() 強制轉浮點數
str() 強制轉換字串


#npm = 23+'88' # 整數與字串相加會產生出錯
#print(npm)

npm1 = 23 + int('88') # 須將字串強制轉換成整數才可相加
print(npm1)

scco = 99
#print("分數"+ scco) # 以print()列印字串時,將字串跟數值組合會產生錯誤

print("分數"+str(scco)) # 將數值轉換成字串就可以跑成功了!


'''
