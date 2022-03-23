'''
    开启appium
'''


import os

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'appium -a %s -p %s'%(host, port)
    os.system(cmd)

if __name__ == "__main__":
    #启动appium
    host = '127.0.0.1'
    port = 4723
    appium_start(host, port)
