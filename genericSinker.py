import zmq
import sys

def main(receiver_ip):
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind(receiver_ip)
    while True:
        msg = receiver.recv_unicode()
        print(msg)

if __name__ == '__main__':
    receiver_ip = sys.argv[1]
    main(receiver_ip)
