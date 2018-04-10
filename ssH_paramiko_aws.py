import paramiko
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect('172.31.26.176',port =22, username = '', password='')
stdin, stdout, stderr = p.exec_command('uname -a')
opt = stdout.readlines()
opt ="".join(opt)
print(opt)
