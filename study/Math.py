num = 3
print (num * num)
print(type(num), type('hello'))

# コメント
coment = 'コメント' # コメント
type(coment)
#「#」は１行コメントを表します。
 
#以下「#」の後ろに型返還後の結果を書いていきます。
 
# float(浮動小数点型)の3.14を整数に変換
e1 = int(3.14) #3
print(e1)
 
#ブール値型のTrue（必ず１文字目は大文字なのに注意！）を整数に変換
e2 = int(True) #1
print(e2)
 
# ブール値型のFlase（必ず１文字目は大文字なのに注意！）を整数に変換
e3 = int(False) #0
print(e3)
 
# 文字列の32を整数の32に変換
e4 = int('32') #32
print(e4)
 
# 文字列の55を整数の55に変換
e5 = int("55") #55
print(e5)
 
# 文字列型の'-99'を整数に変換
e6 = int('-99') # -99
print(e6)
 
#int()を使わず文脈で型変換する例、Trueは整数だと1である点に注意
e7 = True + 2 # 3
print(e7)

mozi = '''
sss

sss
'''
print (mozi)