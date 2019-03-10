#何謂List Comprehension

#這個功能是以一個特別的方式應用for迴圈，並創造出帶有元素的List。
#應用List Comprehension，除了程式碼比較好看，執行效率其實也比較高喔!


#好的，在體驗List Comprehension的威力之前，先來用比較基本的方式來產生List。
#請創造一個含有整數0~9的List。
#請用for迴圈，不要寫10行...

#如果你有好好練習前幾天的語法，你的程式應該會像這樣：

arr1 = []

for i in range(10):
    arr1.append(i)

print(arr1)


#使用List Comprehension

# in-place construction
arr1 = [i for i in range(10)]

print(arr1)

""" 你看看，一行就解決，是不是讓人很心動呢!
這邊來解釋一下，這行程式碼要怎麼讀 & 理解。
這行是說我們要創造一個Listarr1。
裡面要放什麼? 要放變數i。
變數i哪裡來? 從後面的for迴圈來
那for迴圈會從range拿出什麼呢? 是0~9。
於是我們就得到一個含有0~9的List啦! """


#變化型List Comprehension
#除了單純的從for迴圈取得元素之外，List Comprehension還有很多變化型可用

# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)

""" 好的，又到了程式碼解釋時間，事情是這樣的：
第二個List Comprehension，我們加上了if條件。
arr2要放什麼? 放x。
x怎麼來，從後面的for來。
for從啥提取元素? 從arr1。
有什麼過濾條件嗎? 取出的元素至少要通過除以2的餘數為0 (即為2的倍數)
於是我們從arr1取出0~9，把為2的倍數的元素存入arr2，故答案為0, 2, 4, 6, 8。
其實這樣的寫法就等於告訴Python，要在for迴圈內包一層if的意思。

第三個List Comprehension，我們用上了多個條件。
但其實基本概念與第二個很像，除了條件變多以外，沒什麼大改變，故不多做解釋。

第四個List Comprehension，我們用了兩個for迴圈。
那就跟剛剛說的一樣，我們可以想像成第一層for迴圈裡面又包了一個for迴圈。
那就來考考各位，請問arr4裡面總共會有幾個元素啊?
答案是12個，你猜對了嗎? """


#List Comprehension的效率
#如先前所說，List Comprehension除了在語法上比較簡潔優美以外，效率上也是贏過傳統的方式。

import time

arr1 = []
s = time.time()
for i in range(int(1e+6)):
    arr1.append(i)
print('took {} secs'.format(round(time.time() - s, 3)))

s = time.time()
arr2 = [i for i in range(int(1e+6))]
print('took {} secs'.format(round(time.time() - s, 3)))

""" 這個範例做的事情很簡單，首先我們引入了time模組。
並在兩次創造List的前後計時，以算出執行所需時間。
由於每個人電腦的效能不同，算出來的時間會不一樣。
但基本上，使用List Comprehension的方式應該會比傳統方法來的快很多。
 """

#引入模組
#既然上面都用到了，那我們就順便說說如何在Python引入模組吧!
#引入模組的方法大概如下：

# standard import
import time

# import and give alias
import random as rd

# precise imoprt
from pathlib import Path

# useless statement
from datetime import *

#使用import關鍵字引入模組
#可引入模組後，用as幫他取暱稱，這樣就可以不用打又臭又長的套件名稱XD
#可使用import ... from ...的語法，從某套件中拿出特定的功能
#最後一個方法感覺很糟，會汙染全域，建議不要使用XD


#List Comprehension背後的原理
#讓我們來稍微了解一下，List Comprehension這個神奇的東西好了。

# what if we don't assign comprehension to list?
comp = (i for i in range(10))
print(comp)
print(type(comp))

arr1 = list(comp)
arr2 = list(comp)
arr3 = [comp]
print(arr1)
print(arr2)
print(arr3)

""" 先看前三行，我們用了List Comprehension，但沒有把它放進List裡面，而是把它塞在變數裡，之後把他的值與型別印出來看看。
你會發現，其實他是一個叫做generator的東西，並且印出的時候，無法看到裡面的值。
這個東西我們現在不談，之後再細細說明。

接著我們下面的程式開始執行，猜猜看，arr1 & arr2的值會不會一樣?
執行後會發現，arr2是空List，原因是generator這個東西被arr1消耗掉了，所以arr2並沒有拿到元素!


學了那麼多天語法，好像都沒有練習ㄟ?
不然我們來個小練習好了，題目是這樣的： """

""" 請創造兩個陣列
第一個陣列包含0~20中的偶數
另一個包含0~20中的奇數
然後請用一個for迴圈印出以下結果： """

""" 1 <---> 2
3 <---> 4
5 <---> 6
7 <---> 8
9 <---> 10
11 <---> 12
13 <---> 14
15 <---> 16
17 <---> 18
19 <---> 20 """

