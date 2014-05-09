#!/usr/bin/python
#! encoding: UTF-8
#funcion para aproximar el numero pi
import sys
Pi=3.1415926535897931159979634685441852
def numeropi(n):
  subintervalos = int(n) 
  suma=0.0
  for i in range(1,subintervalos+1):
    x=float(i-0.5)/(subintervalos)
    y=4/(1+x**2)
    suma=suma+y
  pi=(1.0/float(subintervalos))*suma
  return pi
  

#invocacion
if __name__ == "__main__":
  if len(sys.argv)==3:
    subintervalos=int(sys.argv[1])
    multiplos=int(sys.argv[2])
  else:
    subintervalos=9
    multiplos=3
  if(subintervalos<=0):
    print 'Error, el subintervalo debe ser mayor que cero'
  t=[]
  for repetir in range(1,multiplos+1):
    api = numeropi(subintervalos)
    print 'El valor de pi es pi=%1.35f' % api
    t=t+[api]
  print t

  #Para saber más....
  print'i                PI35DT                      lista i                            PI35DT-lista i'
  for repetir in range(1,multiplos+1):
    diferencia=numeropi(subintervalos)-Pi
    print'%d %1.35f | %1.35f | %1.35f' %(repetir,Pi,numeropi(subintervalos), diferencia)
    subintervalos=subintervalos*2
