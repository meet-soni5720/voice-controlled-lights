# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:37:52 2019

@author: Meet
"""
     #code for converting speech into text
import serial
import speech_recognition as sr
import time

r=sr.Recognizer()
mic=sr.Microphone()

with mic as source:
    print("speak anything")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        transmit=text.lower()
        print('{}'.format(transmit))
        
    except:
        print('sorry we could not recognize your voice')
        
     # code for assigning character to the given speech input

     
if transmit == 'all led off' or transmit == 'all led of' or transmit == 'turn off all the led' or transmit == 'turn of all the led' or transmit == 'turn off all the leds' or transmit == 'turn of all the leds' or transmit == 'turn off all the lights' or transmit == 'turn of all the lights'  :
    transmit='a'
    print(transmit)
    
if transmit =='turn on all the led' or  transmit == 'all the led on' or  transmit =='turn on all the leds' or transmit == 'all the leds on'or transmit == 'all led on' or transmit == 'all leds on' :
     transmit='b'
     print(transmit)
     
if transmit =='led 1 off' or  transmit == 'led 1 of' or  transmit =='turn off led 1' or transmit == 'turn of led 1' or transmit =='led one off' or  transmit == 'led one of' or  transmit =='turn off led one' or transmit == 'turn of led one' :
     transmit='o'
     print(transmit)
         
if transmit =='led 1 with intensity 25%' or  transmit == 'turn on led 1 with intensity 25%' or transmit == 'led 1 on with 25% intensity' or transmit == 'led one with intensity 25%' or transmit =='turn on led one with intensity 25%' or  transmit == 'led one with intensity 25%' or transmit == 'led one on with 25% intensity':
     transmit='i'
     print(transmit)

if transmit =='turn on led 1 with intensity 75%' or  transmit == 'led 1 with intensity 75%' or transmit == 'led 1 on with 75% intensity' or transmit =='turn on led one with intensity 75%' or  transmit == 'led one with intensity 75%' or transmit == 'led one on with 75% intensity':
     transmit='j'
     print(transmit)
 
if transmit =='turn on led 1' or  transmit == 'led 1 on' or  transmit =='turn on led 1 with its peak value' or transmit == 'turn only led 1 on' or transmit == 'turn on only led 1' or transmit == 'turn on led one' or transmit == 'led one on' :
     transmit='c'
     print(transmit)
     
if transmit =='turn on led 2 with intensity 25%' or  transmit == 'led 2 with intensity 25%' or transmit == 'led to with intensity 25%' or transmit == 'turn on led to with intensity 25%':
     transmit='k'
     print(transmit)
     
if transmit =='turn on led 2 with intensity 75%' or  transmit == 'led 2 with intensity 75%' or transmit == 'led to with intensity 75%' or transmit == 'turn on led to with intensity 75%'  :
     transmit='l'
     print(transmit)
     
if transmit =='turn on led 3 with intensity 75%' or  transmit == 'led 3 with intensity 75%' or transmit == 'led three with intensity 75%' or transmit == 'turn on led three with intensity 75%'  :
     transmit='n'
     print(transmit)
               
if transmit =='turn on led 3 with intensity 25%' or  transmit == 'led 3 withintensity 25%' or transmit == 'led three with intensity 25%' or transmit == 'turn on led three with intensity 25%':
     transmit='m'
     print(transmit)
         
if transmit =='turn on led 2' or  transmit == 'led 2 on' or  transmit =='turn on led 2 with its peak value' or transmit == 'turn only led 2 on' or transmit == 'turn on led 2 only' or transmit == 'turn on only led 2' or transmit =='turn on led to' or  transmit == 'led to on' or  transmit =='turn on led to with its peak value' or transmit == 'turn only led to on' or transmit == 'turn on led to only' or transmit == 'turn on only led to'  :
     transmit='d'
     print(transmit)
     
if transmit =='turn on led 3' or  transmit == 'led 3 on' or  transmit =='turn on led 3 with its peak value' or transmit == 'turn only led 3 on' or transmit == 'turn on led 3 only' or transmit == 'turn on only led 3' or transmit =='turn on led three' or  transmit == 'led three on' or  transmit =='turn on led three with its peak value' or transmit == 'turn only led three on' or transmit == 'turn on led three only' or transmit == 'turn on only led three'  :
     transmit='e'
     print(transmit)
          
if transmit == 'led 1 and led 2 on' or transmit == 'led 1 and led to on' or transmit == 'both led 1 and led 2 on' or transmit =='both led 1 and led to on' or transmit == 'led 1 on and led 2 on' or transmit == 'led 1 on and led to on' or transmit == 'led 2 and led 1 on' or transmit == 'led to and led 1 on' or transmit == 'both led 2 and led 1 on' or transmit =='both led to and led 1 on' or transmit == 'led 2 on and led 1 on' or transmit == 'led to on and led 1 on':
     transmit='f'
     print(transmit)
     
if transmit == 'led 1 and led 3 on' or transmit == 'led 1 and led three on' or transmit == 'both led 1 and led 3 on' or transmit =='both led 1 and led three on' or transmit == 'led 1 on and led 3 on' or transmit == 'led 3 and led 1 on' or transmit == 'led three and led 1 on' or transmit == 'both led 3 and led 1 on' or transmit =='both led three and led 1 on' or transmit == 'led 3 on and led 1 on' or transmit=='turn on led 1 and led 3' :
     transmit='g'
     print(transmit)
     
if transmit == 'led 2 and led 3 on' or transmit == 'led to and led 3 on' or transmit == 'both led 2 and led 3 on' or transmit =='both led to and led 3 on' or transmit == 'led 2 on and led 3 on' or transmit == 'led 3 and led 2 on' or transmit == 'led 3 and led to on' or transmit == 'both led 3 and led 2 on' or transmit =='both led 3 and led to on' or transmit == 'led 3 on and led 2 on'  :
     transmit='h'
     print(transmit)
     
if transmit =='led 2 off' or  transmit == 'led 2 of' or  transmit =='turn off led 2' or transmit == 'turn of led 2' or transmit =='led to off' or  transmit == 'led to of' or  transmit =='turn off led to' or transmit == 'turn of led to' :
     transmit='r'
     print(transmit)
     
if transmit =='led 3 off' or  transmit == 'led 3 of' or  transmit =='turn off led 3' or transmit == 'turn of led 3' or transmit =='led three off' or  transmit == 'led three of' or  transmit =='turn off led three' or transmit == 'turn of led three' :
     transmit='q'
     print(transmit)
               
if transmit =='turn on dj lights' or  transmit =='turn on dancing leds' or transmit =='turn on dancing led' or transmit == 'turn on dancing lights' or transmit == 'turn on dancing light' :
     transmit='ss'
     print(transmit)
     
if transmit == 'turn on disco lights' or transmit == 'turn on disco light' : 
     transmit='tt'
     print(transmit)
     
if transmit== 'turn on pattern 1' or transmit == 'turn on patent one' or transmit == 'turn on patent 1' or transmit == 'turn on pattern one' :
    transmit='u'
    print(transmit)
    
if transmit == 'turn lights dim to high':
    transmit='p'
    print(transmit)
    
if transmit == 'terminate the current activity' or transmit=='terminate current activities':
    transmit='x'
    print(transmit)
            
     # code for transmitting character to microcontroller via HC05 using pyserial      
#port="COM3"     #this is mine bluetooth port give bluetooth according to your's.find it in device manager
ser=serial.Serial(port='COM3',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False      #disable hardware (DSR/DTR) flow control
#ser.writeTimeout = 2     #timeout for write
print(ser.name)
print('okk')
'''if ser.isOpen():
  ser.close()
print('ok1)
ser.open()
print('r')
ser.isOpen()
print('s')'''
ser.write(transmit.encode()) 
print('ok')
#ser.close()

