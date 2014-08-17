#
# Dispatches the request the user has made to the code that will process the request.  In this case CoffeeIO will process
# all the requests we need.  Reflection is used to reflect into CoffeeIO and call the appropriate fuction.
# The operations are taken directory from remote.html. 
#
# Example:
#   <button class="btn btn-lg btn-danger custom" id="shutOff" onclick="remoteOperation(this.id)">Power Off</button> 
# remote.html defines a button with the id "shutOff".  shutOff is a function in CoffeeIO and so the button's id determines
# what will be called.         
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
# License along
# with this program. If not, see <http://creativecommons.org/licenses/by-sa/3.0/>.


import coffeeUtils


coffeeIO=coffeeUtils.CoffeeIO()


def processRequest(operation):
  result=""
  try:
    result = getattr(coffeeIO, operation)()
    print(result)
  except AttributeError:
    print(operation, "is not an operation")
  
  return result



