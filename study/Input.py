
# inputはユーザに入力してもらい戻り値を文字列型で取得する

a = input ('値を入力してください')
print ('入力された値', a)

num = input('数字を入力してください')
print ('3倍にします', int(num) * 3)

while (True):
  print ('繰り返し')
  break

dic = {'Apple': 'iPhone', 'Microsoft': 'windows', 'Amazon': 'EC'}
for company in dic:
  print (company + 'といえば' + dic[company])