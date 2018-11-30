import sys
import time
import select
import paramiko
def functionName(event, context):
        host = '***' 
        i = 1
        if i == 1:    
	    try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host,username="xxxx",password="xx",port=22)
                print "Connected to %s" % host
            except paramiko.AuthenticationException:
                print "Authentication failed when connecting to %s" % host
                sys.exit(1)
        # Send the command (non-blocking)
        stdin, stdout, stderr = ssh.exec_command("mkdir ~/s3-test")
        #
        # Disconnect from the host
        #
        print "Command done, closing SSH connection"
        ssh.close()
functionName("asdfsafd","Asdfasdf")
