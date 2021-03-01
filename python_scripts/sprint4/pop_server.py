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
            content = str(client_socket.recv(4096), 'utf-8')
            a_list = content.split(',')
            value = population.getValue(a_list[0], a_list[1])
            client_socket.send(','.join([a_list[0], a_list[1], str(value)]).encode('utf-8'))
        client_socket.close()

    s.close()