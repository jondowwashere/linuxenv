
#!/usr/bin/env python
import os
command1 = 'apt-get update'
command2 = 'apt-get install -y bind9'
commands = command1+'\n'+command2
os.system(commands)
