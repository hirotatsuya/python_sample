# listの生成
py = list('python3')
print (py, py[6])
os = ['windows', 'ios', 'android']
print (os)
list = ['ケーキ', 'チョコ', 'キャラメル', 'アメ', 'シュークリーム']
print (list[0:2])
print (list[::-1]) # 逆順にする
list.append('クッキー') # リストの最後に要素を追加する
print (list)
like = ['ミルクレープ', 'ラムネ', 'メロンパン']
list.extend(like) # リストを合体する
print (list)
del list[0] # 指定した要素を削除する
print (list)
tpl = (1,2,3,4,5) # タプルの生成
print (tpl)
a,b,c,d,e = tpl
print (a,b,c,d,e)
number = {'one': 1, 'two': 2, 'three': 3} # 辞書
print (number['two'])
kakaku_list = [['a', 1], ['c', 3], ['b', 2]]
kakaku_dict = dict(kakaku_list) # dict()関数によりリストを辞書に変換する
print (kakaku_dict)
print (kakaku_dict['b'], kakaku_list[2][1])