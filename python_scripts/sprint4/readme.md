
A client/server implementation of more than two 
microservices.

To begin, start the pop_server.py script

Then, start the life_client.py file

To terminate:

    Ctrl + C on the server

  or send the parameter DONE from the client

  Example: 

    py population_client.py DONE
    
  
  Reason for DONE is the SIGINT is not working with either
  ctrl + c     or ctrl + break
  on windows.