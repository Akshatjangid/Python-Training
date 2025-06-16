import socket
try:
    #creatting a socket
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #dgram--> datagram ---> it is used for UDP protocol
    #AF_INET --> is use to specify the address family, which is IPv4 in this case.
    
    print("Socket created ")
    ip_add = "192.168.129.117"  # IP address of the receiver
    port = 33344 # Port number for the receiver
    target_add=(ip_add,port)                                             #0-65535
    message = input("Enter the message to send: 🤣")
    encoded_msg = message.encode('ascii')  # Encoding the message to bytes
    s.sendto(encoded_msg, target_add)  # Sending the message to the target address
    s.close()  # Closing the socket

except Exception as e:
    print("An error occurred: ", e)