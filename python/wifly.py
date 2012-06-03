
import serial
import time

delay = 5

def configure():
    print 'configuration'
    # set authorization mode
    # set authorization key
    # set comm remote 0
    # join network

def send_command(command):
    print 'sent command:', command
    for c in command:
        s.write(c)
        time.sleep(0.1)

def get_reply(s):
    reply = s.readlines()
    print 'received reply:', reply
    return ''.join(reply)

s = serial.Serial('/dev/tty.usbserial-A700fpBT',
                  timeout=1,
                  baudrate=9600)
verbose = True
while 1:
    print
    print 'top of loop'
    print '--------------------------------'

    # enter command mode
    print
    print 'enter command mode'
    send_command('$$$')
    time.sleep(delay)

    reply = get_reply(s)
    if 'CMD' in reply:
        print 'entered command mode'
    else:
        print 'did not enter command mode'


    # connect to server
    print
    print 'connect to server'
    print 'flushing buffer'
    time.sleep(delay)
    reply = get_reply(s)
    send_command('open 50.56.226.226 80\r\n')
    time.sleep(delay)
    reply = get_reply(s)
    if '*OPEN*' in reply:
        print 'connected to server'
        time.sleep(delay)
        print
        print 'sending GET request'
        send_command('GET / HTTP/1.0\r\n\r\n')
        time.sleep(delay)
        reply = get_reply(s)
    else:
        print 'no connection to server'

    # check for successful close


    # exit command mode
    send_command('exit\r\n')
    time.sleep(delay)
    reply = get_reply(s)

    if 'EXIT' in reply:
        print 'successful exit'
    else:
        print 'unsuccessful exit'

    '''
    if '*OPEN*' in s.readlines():
        print 'connected to server'


    print s.readlines()
    s.write('GET / HTTP/1.0\r\n\r\n')
    print s.readlines()
    '''
