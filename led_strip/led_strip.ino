#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PINLEFT            9
#define NUMPIXELS          27

Adafruit_NeoPixel left = Adafruit_NeoPixel(NUMPIXELS, PINLEFT, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);

  left.begin(); // This initializes the NeoPixel library.

}

void loop()
{
      for (int i = 0; i < NUMPIXELS; i++) {
        left.setPixelColor(i, left.Color(50, 205, 50));
        left.show();
      }
  }
