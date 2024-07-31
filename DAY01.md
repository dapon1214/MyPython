第 01 天：條件判斷、數據類型、變數
==========================================
由於學習其他同仁AI專案需要有一些Python語言知識，故開啟系列筆記學習過程。

```python
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
```
也可以給if添加一個else語句，意思是，如果if判斷是False，不要執行if的內容，去把else執行了：
```python
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```
當然上面的判斷是很粗略的，完全可以用elif做更細緻的判斷：
```python
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```
python沒有switch為此後來有新增match，下面是使用match範例。
```python
score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')
```
