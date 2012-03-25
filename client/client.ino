#include <SPI.h>
#include <WiFly.h>

#include "Credentials.h"

WiFlyClient client(DATASERVER, 8000);
char packet[64];

void setup() {
  Serial.begin(9600);
}

int value=0;

void loop() {
  delay(1000);

  value++;
  
  // create data payload
  sprintf(packet, "time_stamp=2000-01-01T12:00&tag=ardfly&value=%d",value);

  // post to server
  Serial.print("POST / HTTP/1.1\r\n");
  Serial.print("Host: 108.166.92.185:8000\r\n");
  Serial.print("Content-Length: ");
  Serial.print(strlen(packet));
  Serial.print("\r\n\r\n");
  Serial.print(packet);
  
  Serial.println();
  Serial.println();
}


