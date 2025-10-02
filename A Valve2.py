""" Colin Innes (100834391) this is my own work, any work taken from outside sources have been linked below

"""
class Valve(object):
    """Model a fixed valve."""
    def __init__(self, rate):
        """Constructor sets the standard valve flow in litres."""
        self.flow_rate = rate

    def Max_flow(self, bore):
        """Given a bore, return the flow."""        
        #return bore / self.flow_rate
        return self.flow_rate

    def __str__(self):
        """Return a string representation of the flow_rate."""
        return "Ltrs=" + str(self.flow_rate)

    def Status(self, state):
        """ Set the current valve state on/off [True/False]"""
        if state == True:
            self.state = True
        else:
            self.state = False
            self.flow_rate = 0
        return self.state


class ModValve(Valve):
    """A simpler modulating valve with % control."""

    def __init__(self, rate):
        super().__init__(rate)     # start with rated flow
        self.opening = 100         # default 100% open
        self.state = True          # start open

    def set_rate(self, percent):
        """Set opening percentage (0–100)."""
        if percent < 0:
            percent = 0
        elif percent > 100:
            percent = 100
        self.opening = percent

    @property
    def actual_rate(self):
        
        if not self.state:         # closed → no flow
            return 0
        return self.flow_rate * (self.opening / 100)

def __str__(self):
    return f"Ltrs={self.actual_rate:.1f} at {self.opening}% open"


if __name__ == "__main__":
    '''
    while True: 
        Valve_state = input("Enter state of the state ? ")
        if Valve_state == "True":
            Valve_state = True
        else:
            Valve_state = False
        print("A standard On/Off valve :-")
        v1 = Valve(30.0)
        v1.Status(Valve_state)
        print("V1: volume = ", v1)
        print("V1: Open =", v1.state, " - Has a Bore size of 10.0mm, Flow rate = ", v1.Max_flow(100.0))
        print ()
    '''

    print("A modulating valve :-")
    v2 = ModValve(200.0)
    print("V2: volume =", v2)
    print("V2 100% open: bore=10.0", " Actual Rate = ", v2.actual_rate)
    v2.set_rate(50.0)
    print("V2 50% open: bore=10.0", " Actual Rate = ", v2.actual_rate)
    v2.set_rate(30.0)
    print("V2 30% open: bore=10.0", " Actual Rate = ", v2.actual_rate)
    