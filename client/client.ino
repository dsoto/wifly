#include <SPI.h>
#include <WiFly.h>

#include "Credentials.h"

WiFlyClient client(DATASERVER, 8000);
char packet[64];

void setup() {
  Serial.begin(9600);
  
  WiFly.begin();
  
  //SpiSerial.begin();
  
  //Wifly.setUart(&Spi
  
  WiFly.join("wifly", "", 0);
}

int value=0;

void loop() {
  delay(60 * 1000 * 5);

  value = analogRead(0);
  
  // create data payload
  sprintf(packet, "time_stamp=2000-01-01T12:00&tag=ardfly&value=%d",value);

  // print post text to serial
  Serial.print("POST / HTTP/1.1\r\n");
  Serial.print("Host: 108.166.92.185:8000\r\n");
  Serial.print("Content-Length: ");
  Serial.print(strlen(packet));
  Serial.print("\r\n\r\n");
  Serial.print(packet);
  
  Serial.println();
  Serial.println();
  
  // post to server
  if (client.connect()) {
    client.print("POST / HTTP/1.1\r\n");
    client.print("Host: 108.166.92.185:8000\r\n");
    client.print("Content-Length: ");
    client.print(strlen(packet));
    client.print("\r\n\r\n");
    client.print(packet);
  
    client.println();
    client.println();
  }
  
}


