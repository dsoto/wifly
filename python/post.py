import serial

s = serial.Serial('/dev/tty.usbserial-A700fpBT', timeout=1)

s.write('$$$')
print s.readlines()
s.write('open 108.166.92.185 8000\r\n')
print s.readlines()
s.write('GET / HTTP/1.0\r\n\r\n')
print s.readlines()

content = ''
content += 'tag=wifly'
content += '&time_stamp=2012-06-12'
content += '&value=%s' % data_value
content += '&point=%s' % stream_name
content_length = len(content)

post_string = ''
post_string += 'POST /service/currentvalue HTTP/1.1\r\n'
post_string += 'Host: app.nimbits.com\r\n'
post_string += 'Content-Length: %s\r\n' % content_length
post_string += 'Content-Type: application/x-www-form-urlencoded\r\n'
post_string += 'Accept-Encoding: identity\r\n'
post_string += 'Accept: */*\r\n'
post_string += 'User-Agent: pysoto\r\n\r\n'
post_string += content
