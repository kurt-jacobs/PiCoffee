#!/usr/bin/env python

import coffeeUtils
import time
import gpioPins


class CoffeeButton(object):
   def __init__(self):
     self.coffeeIO=coffeeUtils.CoffeeIO()
     self.persistence=coffeeUtils.Persistence()
     self.buttonState=True;

   def processUserInput(self):
     while True:
       try: 
          self.inputValue=self.coffeeIO.readPin(gpioPins.inputPin)
          if self.inputValue==False:
             self.buttonState=self.persistence.getMakerState()
             if self.buttonState==True:
                self.coffeeIO.shutOff()
             else:
                self.coffeeIO.startBrew()

             while self.inputValue==False:
               self.inputValue=self.coffeeIO.readPin(gpioPins.inputPin)
             time.sleep(0.5)
       except (KeyboardInterrupt,SystemExit):
             self.coffeeIO.gpioCleanup()
             raise



coffeeButton=CoffeeButton()
coffeeButton.processUserInput()




