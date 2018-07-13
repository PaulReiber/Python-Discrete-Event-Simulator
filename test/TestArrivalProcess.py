from simkit.rand import Exponential
from examples.arrivalprocess import ArrivalProcess
from examples.arrivalprocess import EntityCreator
from simkit.simkit import EventList
from simkit.simutil import SimpleStateChangeDumper

if __name__=="__main__":
    generator = Exponential(1.7)
    arrivalProcess = ArrivalProcess(generator)
    print(arrivalProcess)

    print(type(arrivalProcess))

    dumper = SimpleStateChangeDumper()
    arrivalProcess.addStateChangeListener(dumper)

    EventList.stopAtTime(100.0)

    EventList.verbose = True

    EventList.reset()
    EventList.startSimulation()

    EventList.coldReset()
    EventList.stop_on_event(10, 'entityArrival')

    entityCreator = EntityCreator(generator)

    print("With EntityCreator")
    EventList.reset()
    EventList.startSimulation()

    # This should throw a ValueError
    # arrivalProcess.waitDelay('Foo', -.001)