import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect('tcp://localhost:5556')

while True:
    msg = socket.recv_string()
    print('[RCVD] {}'.format(msg))
