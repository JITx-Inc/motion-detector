from z3 import *

def filter_case():
    """ Non-inverting bandpass filter design.
    """
    Rf = Real('Rf')
    Rg = Real('Rg')
    R1 = Real('R1')
    R2 = Real('R2')
    Cf = Real('Cf')
    Cin = Real('Cin')

    VCC = 3.0
    Vref = VCC

    margin = 0.2
    VinPP = 0.038
    VinOffset = 0.0

    fmin = 100.0
    fmax = 20e3
    
    Vi1 = -VinPP + VinOffset
    Vi2 = VinPP + VinOffset

    Vo1 = VCC - margin
    Vo2 = 0.0 + margin

    s = Solver()
    
    s.add(Vo1 == (-Rf / Rg) * Vi1 + ((R1/(R1+R2)) * Vref))
    s.add(Vo2 == (-Rf / Rg) * Vi2 + ((R1/(R1+R2)) * Vref))    

    s.add(fmax == 1 / (2 * 3.14 * Rf * Cf))
    s.add(fmin == 1 / (2 * 3.14 * Rg * Cin))
    s.add(Cf > 0.0)
    s.add(Cin > 0.0)
    s.add(Cf < 1e-6)
    s.add(Cin < 100e-6)
          
    s.add(Rf == 51.0e3)
    s.add(Rg > 0.0)
    s.add(R2 == 51.0e3)
    s.add(R1 > 0.0)
                                     
    return s


s = filter_case()

print(s.check())
print(s.model())
