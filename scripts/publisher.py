#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String 

# cipher shift value 
SHIFT = 10

# encrypted words 
encrypted_words = list()

def read_file(filename="lorem_ipsum.txt"):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, filename)
    
    # list of words in the file 
    word_list = list()
    
    try:
        file = open(filepath, "r")
        word_list = file.read().split()
    except IOError:
        print("File not found")
        exit()
        
    return word_list


def Encrypt():
    words = read_file()
    
    for word in words:
        caesar_cipher(word)

# simple caesar cipher
def caesar_cipher(word):
    chars = list(word)
    cipher_word = ""
    
    for char in chars:
        if char in '\'?#$,"./;:%^*&(){}[]':
            cipher_value = char 
        else:
            if char.isupper():
                cipher_value = chr((ord(char) + SHIFT - 65) % 26 + 65)
            else: #lowercase
                cipher_value = chr((ord(char) + SHIFT - 97) % 26 + 97)
        cipher_word += cipher_value
        
    encrypted_words.append(cipher_word)
    
def talker():
    pub = rospy.Publisher('cipher', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10)
    
    word_count = len(encrypted_words)
    index = 0

    while not rospy.is_shutdown():
        info = "Simple Casear Cipher encryption -- log time: %s" % rospy.get_time()
        rospy.loginfo(info)
        pub.publish(encrypted_words[index % word_count])
        rate.sleep()
        index += 1
        
if __name__ == '__main__':
    Encrypt()
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
