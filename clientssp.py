# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:58:13 2020

@author: SHIVANI MALIWAL
"""


import socket


def client_program():
    target_ip = "192.168.43.127" 
    target_port= 2623

    client_socket = socket.socket()
    client_socket.connect((target_ip, target_port))  

    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data) 

        message = input(" -> ")  

    client_socket.close()


if __name__ == '__main__':
    client_program()
