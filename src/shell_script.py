import subprocess

cmd = ['ls', '-l', '.']

output = subprocess.run(cmd, stdout=subprocess.PIPE)
text = output.stdout.decode()

file = open('sample.py', 'w')
file.write(text)
file.flush()
file.close()
