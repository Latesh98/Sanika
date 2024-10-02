#  Write a program to accept IPaddress and port and display in list of list.
def ip():
    ip_port_list = []
    while True:
        ip_address = input("Enter IP address (or type 'exit' to finish): ")
        if ip_address.lower() == 'exit':
            break
        port = input("Enter port number: ")
        ip_port_list.append([ip_address, port])
        print("\nList of IP addresses and ports:") # Display the list of lists
    for entry in ip_port_list:
        print(entry)
ip()

