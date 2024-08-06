第 02 天：for、while迴圈、常用集合
==========================================
參照JAVA或C#語言的語法，Python相對比較簡潔，也支持多種函數處理，這邊筆記一下常用功能。

## dict
Python內建字典dict支援，使用方法如下
```python
dc = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dc['Bob'])
```

## set
set和list相似，但是set不儲存重複的值。
```python
s = {1, 1, 2, 2, 3, 3}
print(s) # {1, 2, 3}

# set因為沒有順序，也不支援index取值，只能用for來一個一個訪問
for x in s:
    print('Set裡面每個元素：' + str(x))
```

## 函數返回多個值(與Java、C#不同)
```python
def add(x, y, z):
    xz = x + z
    yz = y + z
    return xz, yz

a, b = add(1, 2, 3)
```
