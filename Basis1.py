# ctrl+/ 單行註解 
""" shift+alt+A 區塊註解 """

print ("hello world")
#習慣其他語言的人，可能會使用{}來定義一個程式區塊，但是Python中，程式區塊是用:以及縮排來定義的。這點千萬要切記啊!
#在Python中，寫在#後面的文字，都會變成註解。
#我們可用type這個函式以及print來得知變數的型別
#Python的空值 (沒有存放任何東西)是以None來表示
#如果想要確認某變數是否為特定型別的時候，可用isinstance這個函式
iv = 10
fv = 12.3
cv = 3 + 5j
sv = 'hello python'
bv = True
nv = None

print(iv, fv, cv, sv, bv)
print(type(iv))
print(type(fv))
print(type(cv))
print(type(sv))
print(type(bv))
print(nv)
print(isinstance(sv, str))


#你可以用input這個函式，他會回傳外部送來的訊息。
#在終端機輸入你的名字
name = input('Hello, what is your name?  ')
print('Hi, ', name)

#一個if...else區塊，只要其中一個條件成立，程式就會離開這個區塊。
#條件不需要放()之中
#每個條件後面記得要有:
#條件成立要做的事情，要以縮排的方式放在條件句底下
#else if在Python寫作elif

grade = 90
# there's no ()
if grade >= 90:
    print('Excellent!')
elif grade >= 60:
    print('Good enough!')
else:
    print('Loser!')


h = 180
w = 85
grade = 80

# 身高超過175或是體重超過80，看起來就很大隻
if h > 175 or w > 80:
    print('big dude')

# 成績高於70但是不高於90，就是個普通學生
if grade > 70 and grade < 90:
    print('noraml')