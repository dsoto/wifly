
import serial
import time

delay = 5

def send_command(command):
    print 'sent command:', command
    s.write(command)

def get_reply(s):
    reply = s.readlines()
    print 'received reply:', reply
    return ''.join(reply)

s = serial.Serial('/dev/tty.usbserial-A700fpBT',
                  timeout=1,
                  baudrate=9600)
verbose = True
while 1:
    print 'top of loop'

    # enter command mode
    send_command('$$$')
    time.sleep(delay)

    reply = get_reply(s)
    if 'CMD' in reply:
        print 'entered command mode'
    else:
        print 'did not enter command mode'

    # exit command mode
    send_command('exit\r\n')
    time.sleep(delay)
    reply = get_reply(s)

    if 'EXIT' in reply:
        print 'successful exit'
    else:
        print 'unsuccessful exit'

    '''
    s.write('open 50.56.226.226 80\r\n')
    if '*OPEN*' in s.readlines():
        print 'connected to server'

    print s.readlines()
    s.write('GET / HTTP/1.0\r\n\r\n')
    print s.readlines()
    '''
