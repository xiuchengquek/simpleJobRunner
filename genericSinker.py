import zmq

def main(receiver_ip):
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind(receiver_ip)
    while True:
        msg = receiver.recv_unicode()
        print(msg)

if __name__ == '__main__':
    receiver_ip = "tcp://*:5558"
    main(receiver_ip)
