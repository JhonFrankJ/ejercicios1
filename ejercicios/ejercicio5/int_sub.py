#!/usr/bin/env python3
# --------------suscriptor de Int32----------------
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('int_sub', anonymous=True)	
#rospy.init_node('nombre-nodo', anonymous=True)
# nombre-nodo puede ser cualquiera, 
# preferible que sea igual al nombre del codigo

#se crea la funcion para recibir el mensaje del topico
def callback(data):	
    global int_value
    int_value=data.data
    #print("valor1: ",int_value)
def callback1(data):	
    global int_value1
    int_value1=data.data
    print("valor1: ",int_value," valor2: ",int_value1)
    print("suma: ",int_value + int_value1)

# se suscribe al topico
sub = rospy.Subscriber("random_int1", Int32, callback)
sub = rospy.Subscriber("random_int2", Int32, callback1)

# sub = rospy.Subscriber("nombre-topico", tipo-mensaje, funcion-callback)
# el codigo int_pub.py publica al topico 'random_int'

# Lo siguiente solo es para que el codigo no se cierre

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s

# en este caso el while es para que el codigo no se cierre
# pues no hace nada :v
while not rospy.is_shutdown():
    #suma = int_value + int_value1
    #print(suma)
    rate.sleep() # delay de 1 segundo