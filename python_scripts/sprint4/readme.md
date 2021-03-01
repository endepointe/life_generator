A client/server implementation of more than two microservices.

The micro_server.py is a template server that all micro services can begin with to run their service on a server that can receive requests.

To begin, start the life_server.py script (or whatever your service is called)

    py life_server.py

Then, start the population_client.py file with the given command line args:

    py population_client.py Toys Hobbies <some integer>

To begin, start the pop_server.py script

Then, start the life_client.py file

To terminate:

    Ctrl + C on the server

or send the parameter DONE from the client

Example:

    py population_client.py DONE

Reason for DONE is the SIGINT is not working with either ctrl + c or ctrl + break on windows.
