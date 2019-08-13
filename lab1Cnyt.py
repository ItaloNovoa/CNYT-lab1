import math
import unittest

#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def suma(c1,c2):
    preal=c1[0]+c2[0]
    pimaginaria=c1[1]+c2[1]
    return (preal,pimaginaria)

#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def producto(c1,c2):
    pr=(c1[0]*c2[0])-(c1[1]*c2[1])
    pi=(c1[0]*c2[1])+(c2[0]*c1[1])
    return (pr,pi)

#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def resta(c1,c2):
    preal=c1[0]-c2[0]
    pimaginaria=c1[1]-c2[1]
    return (preal,pimaginaria)

#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def division(c1,c2):
    c=(c2[0],(c2[1]*-1))
    a=producto(c1,c)
    b=producto(c2,c)
    return ((a[0]/b[0]),(a[1]/b[0]))

#recibe una tupla con una parte real y otra imaginaria
#EJEMPLO --> (3,-4) 
def modulo(c1):
    preal=((c1[0]**2)+(c1[1]**2))**(1/2)
    return preal

#recibe una tupla con una parte real y otra imaginaria
#EJEMPLO --> (3,-4)
def conjugado(c1):
    return (c1[0],(c1[1]*-1))

#recibe el numero del radio y el angulo
def polarAcartesiano(r,a):
    return ((round(r*math.cos(math.radians(a))*1000))/1000,round(1000*r*math.sin(math.radians(a)))/1000)

#recibe una tupla con una parte real y otra imaginaria
#EJEMPLO --> (3,-4)
def cartesianoApolar(c1):
    return ("el radio es igual a "+str(round(((c1[0]**2+c1[1]**2)**0.5)*1000)/1000)+" y el angulo es igual a "+str(round(math.degrees(math.atan(c1[1]/c1[0])*100))/100))

#recibe una tupla con una parte real y otra imaginaria
#EJEMPLO --> (3,-4)
def fase(c1):
    return (round(math.degrees(math.atan(c1[1]/c1[0])*100))/100)

class TestUM(unittest.TestCase):
    #suma
    def test_caso_suma_1(self):
        self.assertEqual((1,3),suma((1,2),(0,1)))
    #multiplicacion    
    def test_caso_producto_1(self):
        self.assertEqual((-52,-20),producto((-4,0),(13,5)))
    def test_caso_producto_2(self):
        self.assertEqual((1,21),producto((1,4),(5,1)))
    #resta    
    def test_caso_resta_1(self):
        self.assertEqual((3,4),resta((5,4),(2,0)))
    #division
    def test_caso_division_1(self):
        self.assertEqual((-1/5,8/5),division((3,2),(1,-2)))
    def test_caso_division_2(self):
        self.assertNotEqual((-3,-2),division((2,-3),(3,2)))
    #modulo
        

if __name__ =='__main__':
    unittest.main()
