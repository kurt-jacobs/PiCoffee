#!/usr/bin/env python
#
# This utility manages the I/O and persistence of the coffee maker.  
#
#
# Kurt Jacobs
#
#--
#
# This work is free: you can redistribute it and/or modify it under the terms of Creative Commons Attribution ShareAlike license 
# v3.0
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the License for more details. You should have received a copy of the 
# License along with this program. If not, see <http://creativecommons.org/licenses/by-sa/3.0/>.


import RPi.GPIO as gpio
import time
import sqlite3
import sys
import gpioPins


class CoffeeIO(object):

   def __init__(self):
      self.persistence=Persistence()
      gpio.setwarnings(False)
      gpio.cleanup()
      gpio.setmode(gpio.BCM)
      gpio.setup(gpioPins.inputPin,gpio.IN)
      gpio.setup(gpioPins.powerPin, gpio.OUT)

   def gpioCleanup():
      gpio.cleanup()

   def readPin(self,pinToRead):
      return gpio.input(pinToRead)

   def shutOff(self):
      self.buttonState=self.persistence.getMakerState()
      if self.buttonState==True:
         self.buttonState=False
         gpio.output(gpioPins.powerPin,self.buttonState)
         self.persistence.updateState(self.buttonState)
         return "Coffee maker is now off"
      else:
         return "Coffee maker is already off"

    # start brew if and only if current state is idle
   def startBrew(self):
      self.buttonState=self.persistence.getMakerState()
      if self.buttonState==False:
         self.buttonState=True
         gpio.output(gpioPins.powerPin,self.buttonState)
         self.persistence.updateState(self.buttonState)
         return "Brew started"
      else:
         return "Brew already started"           

   def getCurrentState(self):      
      self.state= self.persistence.getMakerState()
      if self.state==False:
        return "Coffee maker is not brewing"
      else:
        return "Coffee maker is brewing"



class Persistence(object):

   def getMakerState(self):
      conn = sqlite3.connect('CoffeeMaker.db')
      cur = conn.cursor()
      row=cur.execute("SELECT * FROM makerInfo")
      row=cur.fetchone()
      state=row[2]
      conn.close()
      return state

   def updateState(self,currentState):
      conn = sqlite3.connect('CoffeeMaker.db',isolation_level=None)
      cur = conn.cursor()
      cur.execute("UPDATE makerInfo SET state=? WHERE ID=?", (currentState,1))
      conn.commit 
      conn.close()


