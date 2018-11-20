#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# cipher shift value 
SHIFT = 10

def callback(data):
    rospy.loginfo('word - [ %s ]. decrypted - [ %s ]', data.data, Decrypt(data.data))
    
def Decrypt(word):
    chars = list(word)
    decrypted_val = ""
    
    for char in chars:
        if char in '\'?#$,"./;:%^*&(){}[]':
            decrypted_value = char 
        else:
            if char.isupper():
                decipher_value = chr((ord(char) + (26 - SHIFT) - 65) % 26 + 65)
            else: # lowecase
                decipher_value = chr((ord(char) + (26 - SHIFT) - 97) % 26 + 97)
        
        decrypted_val += decipher_value
        
    return decrypted_val

def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('cipher', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
