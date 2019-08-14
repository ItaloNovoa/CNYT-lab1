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
    b=round(math.degrees(math.atan(c1[1]/c1[0])*100))/100
    if (c1[0]<0 and c1[1]<0):
        b=180+b
    elif (c1[0]>0 and c1[1]<0):
        b=360-b
    elif (c1[0]<0 and c1[1]>0):
        b=180+b
    else:
        b=b    
    return ("el radio es igual a "+str(round(((c1[0]**2+c1[1]**2)**0.5)*1000)/1000)+" y el angulo es igual a "+str(b))

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
    def test_caso_modulo_1(self):
        self.assertEqual((34**0.5),modulo((3,5)))
    #conjugado
    def test_caso_conjugado_1(self):
        self.assertEqual((1,-2),conjugado((1,2)))
    #polarAcartesiano
    def test_caso_polarAcartesiano_1(self):
        self.assertEqual((-1,round((3**0.5)*1000)/1000),polarAcartesiano(2,120))
    #cartesianoApolar
    def test_caso_cartesianoApolar_1(self):
        self.assertEqual('el radio es igual a 2.0 y el angulo es igual a 120.0',cartesianoApolar((-1,3**0.5)))
    #fase
    def test_caso_fase_1(self):
        self.assertEqual(59.04,fase((3,5)))       

if __name__ =='__main__':
    unittest.main()
