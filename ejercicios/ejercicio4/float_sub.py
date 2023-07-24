#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('float_sub', anonymous=True)	

float_value=0

#se crea la funcion para recibir el mensaje del topico
def callback1(data):	
    global int_value
    int_value=data.data
    #print("valor1: ",int_value)
def callback2(data):	
    global int_value1
    int_value1=data.data
    #print("valor2: ",int_value1)
def callback3(data):	
    global int_value2
    int_value2=data.data
    #print("valor3: ",int_value2)
    print("valor1: ",int_value,"valor2: ",int_value1,"valor3: ",int_value2)


# se suscribe al topico
sub = rospy.Subscriber("random_float1", Float64, callback1)
sub = rospy.Subscriber("random_float2", Float64, callback2)
sub = rospy.Subscriber("random_float2", Float64, callback3)
# el codigo float_pub.py publica al topico 'random_float'

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo