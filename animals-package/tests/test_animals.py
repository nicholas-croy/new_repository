
import sys

sys.path.insert(1,"C:/Users/niccr151/Documents/Python_Scripts/python-course/aspp2022-nac/animals-package/src/animals")

from mammals import Mammals
from birds import Birds
from fish import Fish

myMammal = Mammals()
myMammal.printMembers()

myBird = Birds()
myBird.printMembers()

myFish = Fish()
myFish.printMembers()
