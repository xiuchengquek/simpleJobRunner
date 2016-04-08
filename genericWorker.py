import zmq
import subprocess
import sys

def main(reciever_ip, sinker_ip):
    context = zmq.Context()

    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.connect(reciever_ip)

    sinker = context.socket(zmq.PUSH)
    sinker.connect(sinker_ip)

    while True:
        bash_script = receiver.recv_unicode()
        cmd = ['sh', bash_script]
        p = subprocess.check_call(cmd)
        if (p == 1):
            sinker.send_unicode(u'%s fails\n' % bash_script)
        elif ( p == 0):
            sinker.send_unicode(u"%s completed\n"  % bash_script)

if __name__ == '__main__' :
    reciever_ip = sys.argv[1]
    sinker_ip =  sys.argv[2]
    main(reciever_ip, sinker_ip)

