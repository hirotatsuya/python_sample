# Stringの練習
str = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
# スライス → 文字列変数 [スタート : エンド : ステップ]
print (str)
print (str[:]) # すべての文字列を取得
print (str[2]) # 0番目から2番目までをスライスして表示
print (str[:2]) # 0番目から2番目までをスライスして表示
print (str[::2]) # ステップは抜かすということ
print (str[-1::-1]) # 逆順になる
# len(文字列)
print (len(str)) # 文字列の長さの取得
print (len(num))
print (num[-1::-1])
supreme = 'a,aa,aaa,aaaa,aaaaa'
# str.split('セパレータ')
print (supreme.split(',')) # splitはセパレータと呼ばれる区切りで分割してリストを作成する
# str.replace(before, after)
print (supreme.replace('a', 'b'))

