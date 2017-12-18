file = open('sample.py', 'w')
text = 'print ("python")'
file.write(text)
file.flush()
file.close()

html = 'html'
with open('sample.html', mode='w', encoding='utf-8') as f:
  f.write(html)