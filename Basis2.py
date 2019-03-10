#Range
#Range這個型別可用來創建並儲存特定範圍內的整數，故得名Range。
#必須特別注意的是，一旦Range被創建了，裡面的內容是不可修改的
#在Python中，我們有幾個方法可以創造Range。

#Range(stop)
#stop：停止點
#Range(start, stop)
#start：起始點
#stop：停止點
#Range(start, stop, step)
#start：起始點
#stop：停止點
#step：間隔

r1 = range(10)
r2 = range(5, 50, 5)

print(type(r1))
print(r1)
print(r2)

""" 若沒有給起始值，將預設為0
若沒有給間隔，將預設為1
遇到停止點後，創造的過程就會終止，因此Range中的數字將不會包含停止點 """


#Tuple
#Tuple可用來存放一組資料。
#這組資料的個數不限，型別也不須相同。
#同Range，一旦被創造，將無法修改內容。
#值與值之間，要以,隔開。

t1 = 10, 20
# it can hold different types of data
t2 = 10, 'hello world'

print(type(t1))
print(t1)
print(t2)


#List
#List即為Python中的陣列(Array)。
#如果你不知道什麼陣列也沒關係，讓哥來解釋給你聽。
#陣列是一種容器，可用來儲存眾多資料。與Tuple最大的不同處在於，
#針對一個以創建的陣列，你可以隨時增加或減少其內部資料的個數，也可以修改裡面的內容。


arr1 = [1, 2, 3]
arr2 = [10, 'hello world', 8.7]
arr1[0] = [1, 2, 3]

print(type(arr1))
print(arr1)
print(arr2)

""" 宣告陣列可用[]
陣列內的資料型別不必相同
對於任何序列型別來說，我們可用[index]的語法來存取其中的元素。
那這個index要帶多少才能拿到想要的元素呢? 簡單來說，大部分的程式語言，
容器的index都是從0起算的。因此假設今天有個陣列有三個元素，他們對應的index就為0, 1, 2。
 """

#String (字串)
#其實我們一開始介紹過的基本型別String，也是一種序列型別喔。
#一個比較好理解的方式為，其實String就像是一堆字元排在一起組合而成的 (字元指的為一個字)。
#需要注意的是，字串的內容也是不能修改的。



str1 = 'hello python'
str2 = str1
# str2[0] = 'y'
# a = a + b could be written as a += b
str2 += ' journey'
print(str2 is str1)

print(str1)
result = str2.split(' ')
print(result)
result_back = '***'.join(result)
print(result_back)


""" 如果今天想要用兩個字串，組合成一個新的字串，我們可用+來做到這件事
假設今天我們想判斷兩個變數是否共享記憶體位置 (判斷兩者是否為同一個人)，可用is來做到
兩個很重要String方法一定要知道，split & join
split可將一個字串用指定的方式(字串)拆散為陣列。
以上述的例子來說，我們將'hello python journy'，
以空白' '隔開成陣列，於是他便成了['hello', 'python', 'journey']
join可將一個陣列，用指定的方式(字串)組合成字串。
以上述的例子來說，我們['hello', 'python', 'journey']用'***'組合，
就成了hello***python***journey
 """
#序列型別的操作
#1. 取出部分的內容
#若是想從一個序列容器中取出一部份的內容來使用，
#我們可以用seq[start:stop:step]這樣的語法來達成 (是不是有點眼熟啊!)
#必需要注意的是，上面的start, stop, step要填入的是元素的index。




str1 = 'hello world'
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mind the stop
arr2 = arr1[0:5]
# -1 represent the last element
arr3 = arr1[0:-1:2]
# you can ignore the args...
arr4 = arr1[:]

print(arr2)
print(arr3)
print(arr4)
print(arr4 is arr1)
print(str1[5:])
# print(arr1[:-1])

""" step不給預設為1
遇到stop則停止取出，所以index為stop的元素不會被取出
可用-1代表最後一個元素的index
start不給則預設為0
stop不給則會將start之後的元素都取出
seq[start:stop:step]會製造新的容器，因此他們不共享記憶體位置
猜猜看，最後一行會印出什麼，拿掉註解再執行，你猜對了嗎? """


""" 常見的序列容器操作方法
操作	描述
x in s	檢查X是否存在於S這個容器之中
x not in s	檢查X是否不存在於S這個容器之中
s + t	容器S與容器T的內容相加
s * n	三個容器S => s + s + s
len(s)	取得容器的長度 (裡面有幾個元素的意思)
min(s)	取得容器內的最小值 (前提是裡面的元素要能比大小啊!)
max(s)	取得容器內的最大值
s.index(x[,i[,j]])	X元素在S容器的索引值，如果有給i, j就只會在index為i~j的範圍找
s.count(x)	X這個元素在S這個容器內出現幾次
2. 修改序列容器的內容
操作	描述
s[i] = x	index為i的元素的內容置換為X
s[i:j] = t	index從i到j的元素內容置換為X
s[i:j:k] = t	index從i到j的元素，以step為k的方式，將內容置換為X
del s[i:j]	把index從i到j的元素刪除
del s[i:j:k]	index從i到j的元素，以step為k的方式刪除元素
s.append(x)	將X塞到S容器的最後面
s.clear()	將S容器的內容全部刪除(same as del s[:])
s.copy()	複製S容器(same as s[:])
s.extend(t)	同 s = s + t
s.insert(i,x)	在S容器index為i的位置將X插入，原有的元素(們)將會往後移
s.pop([i])	將index為i的元素取出，並將其移出容器
s.remove(x)	刪除第一個找到的X
s.reverse()	讓容器的內容順序顛倒



今天我們介紹了序列容器，這個東西不論在什麼語言都是非常重要的。
因為大部分的情況下，我們都要同時處理很多筆資料，
因此序列容器的操作都必須非常熟悉才行。
以機器學習來說，通常會取得很多數據給程式來學習，
這時候要怎麼操作儲存這些資料的容器，就是一大重點呢! """