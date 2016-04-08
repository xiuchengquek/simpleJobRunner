import zmq

def main(receiver_ip, logfile):
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind(receiver_ip)
    while True:
        msg = receiver.recv_unicode()

if __name__ == '__main__':
    receiver_ip = "tcp://*:5558"
    main(receiver_ip)
