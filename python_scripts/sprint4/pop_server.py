import socket
from population_generator import PopulationGenerator

if __name__ == '__main__':
    PORT = 6000
    host = 'localhost'
    population = PopulationGenerator()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, PORT))
    s.listen(5)
    while True:
        (client_socket, addr) = s.accept()
        with client_socket:
            print('addr:', addr)
            content = str(client_socket.recv(4096), 'utf-8')
            print('content:', content)
            a_list = content.split(',')
            print("alist", a_list)
            #if len(a_list) >= 2:
            value = population.getValue(a_list[0], a_list[1])
            print(value)
            client_socket.send(','.join([a_list[0], a_list[1], str(value)]).encode('utf-8'))
        client_socket.close()

    s.close()
# if __name__ == '__main__':
#     a_list = json.loads('["one","two"]')
#     for item in a_list:
#         print(item)