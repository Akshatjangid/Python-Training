import socket
try:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created ")
    ## sender ke andar ip add receiver ka he aayega
    # hamesha and recevier ka ip add sender ka he aayega
    ip_add = "192.168.59.50" # IP address of the receiver
    port = 5065 # Port number for the receiver
    comlete_add = (ip_add, port)  # 0-65534
    s.bind(comlete_add)  # Binding the socket to the address

    while True:
        message, sender_address= s.recvfrom(1024)

        print("raw message: ", message)
        print("sender address: ", sender_address)

        decoded_msg = message.decode('ascii')  # Decoding the message from bytes
        print("Decoded message: ", decoded_msg)

except Exception as e:
    print("An error occurred: ", e)