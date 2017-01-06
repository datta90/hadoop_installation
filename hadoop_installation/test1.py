# import numpy as np
from __future__ import print_function
import imaplib
import base64
import time
from passwd import encoded_pass
import sys
from t import countdown
def open_connection(verbose=False):
    # Read the config file
    
    ##

    # Connect to the server
#     hostname = config.get('server', 'hostname')
    hostname = 'infrasofttech-com-imap.mail.na.collabserv.com'
    if verbose: print ('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname,port=993)

    # Login to our account
    username = 'duttatreya.sadhu@infrasofttech.com'
    password = base64.b64decode(s=encoded_pass)
    if verbose: print ('Logging in as', username)
    connection.login(username, password)
    return connection

import email
# from pprint import pprint
if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
#         c.select('INBOX', readonly=True)
        typ, data = c.select('INBOX')
        print (c.status('INBOX', '(RECENT UNSEEN)'))
        
        num_msgs = int(data[0])
        print ('There are %d messages in INBOX' % num_msgs)
        rv12, data12 = c.search(None, "ALL")
        
        list1 = data12[0].split()
        list1.reverse()
        count = 0
               
        for num in list1:        
            
            typ, msg_data = c.fetch(num, '(RFC822)')
#             print msg_data
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    
                    msg = email.message_from_string(response_part[1])
                    
    #                 print msg.keys()
    #                 print msg.values()
                    for header in [ 'subject', 'to', 'from','date']:
                        print ('%-8s: %s' % (header.upper(), msg[header]))
                    
                    count+=1
                    print ("##########################\n")
            print ("count",count)            
            if count == 30:
                break
       
        # for i in range(40, 0, -1):
        #     print("."*i, end='\r')
           
        #     time.sleep(1)        
        print ('exiting in \n')
        countdown(120)

    finally:
        try:
            c.close()
        except:
            pass
        c.logout()

#     try:
#         typ, data = c.list()
#     finally:
#         c.logout()
#     print 'Response code:', typ
# 
#     for line in data:
#         print 'Server response:', line
        

    
#     try:
#         typ, data = c.select('INBOX')
#         print typ, data
#         num_msgs = int(data[0])
#         print 'There are %d messages in INBOX' % num_msgs
#     finally:
#         c.close()
#         c.logout()
