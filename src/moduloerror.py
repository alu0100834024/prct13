
#!/usr/bin/python
#! encoding: UTF-8
#funcion para determinar el numero de errores
import modulo
import sys
import pylab as dibujo
import math
import time
def error(subintervalos,nro_test,umbral):
  p=0
  for i in range(1,nro_test +1):
    t=modulo.numeropi(subintervalos)
    if (abs(t-modulo.Pi) > umbral):
      p+=1
  j=(p*100)/nro_test
  return j
  
  
#invocacion
if __name__ == "__main__": 
  if len(sys.argv)==4:
    subintervalos=int(sys.argv[1])
    nro_test=int(sys.argv[2])
    umbral=float(sys.argv[3])
  else:
    subintervalos=10
    nro_test=5
    umbral=0.0001
  if(subintervalos<=0):
    print 'Error, el subintervalo debe ser mayor que cero'
  umbral=(1.0e-4,1.0e-5,1.0e-6,1.0e-7,1.0e-8)
  
  x=[10,50,100,150,500,550,1000]
  X=(10,50,100,150,500,550,1000)
  y=[]
  for h in X:
    ti=time.clock()
    for u in umbral:
      error(h,10,u)
    tf=time.clock()
    tg=tf-ti
    y=y+[tg]
  j = error(subintervalos,nro_test,umbral)  
  print "El porcentaje de errores es %.5f" % j
  
  dibujo.subplot(212)
  dibujo.xlabel ('Intervalos')
  dibujo.ylabel ('Tiempo en segundos')
  dibujo.plot (x,y, marker='o', linestyle='--', color='r', label='Linea 1')
  dibujo.legend()
  

  
  t=[1.0e-4,1.0e-5,1.0e-6,1.0e-7,1.0e-8]
  y=[20,90,100,98,96]
  y2=[2,10,52,97,96]
  y3=[2,0,20,88,96]
  y4=[2,0,9,61,96]
  y5=[2,0,0,8,50]
  y6=[2,0,0,0,20]

  dibujo.subplot(211)
  dibujo.title('Porcentajes de error')

  #dibujo.plot(t,y, marker='o', linestyle=':',color='r', label='Linea 1')
  #dibujo.plot(t,y2, marker='*', linestyle='--',color='b', label='Linea 2')
  #dibujo.plot(t,y3, marker='p', linestyle='-.',color='y', label='Linea 3')
  #dibujo.plot(t,y4, marker='+', linestyle='-.',color='g', label='Linea 4')
  #dibujo.plot(t,y5, marker='', linestyle='--',color='v', label='Linea 5')
  #dibujo.plot(t,y6, marker='p', linestyle='.',color='b', label='Linea 6')
  #dibujo.ylabel('Tiempo en segundos')
  
  #dibujo.legend()
  dibujo.show()
  dibujo.savefig('Practica13.eps')