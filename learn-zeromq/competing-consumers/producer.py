import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5556")

count = 0
while True:
    msg = 'message: {}'.format(count)
    count += 1
    socket.send_string(msg)
    print('[SENT] {}'.format(msg))
    time.sleep(1)
