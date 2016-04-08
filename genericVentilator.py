import zmq
import sys

def main(reciever_ip, sink_ip, bash_script):
    context = zmq.Context()

    # Get reciever
    sender = context.socket(zmq.PUSH)
    sender.bind(reciever_id)

    sinker = context.socket(zmq.PUSH)
    sinker.connect(sink_ip)

    sender.send_unicode(u'%s' % bash_script)



if __name__ == '__main__' :
    reciever_id = sys.argv[1]
    sink_ip = sys.argv[2]
    bash_script = sys.argv[3]
    main(reciever_ip=reciever_id,sink_ip= sink_ip ,bash_script= bash_script)





