# Running the TCP server and client
If you don't have mininet, you can open 2 terminals and begin by running the server
    ```python server.py```
Then run the client with 
   ```python client.py 127.0.0.1 6789 hello.html```
If you are running with mininet you will need to use ```ifconfig``` to find the host ip then run the client with that instead.
Also keep in mind the port number may be changed within the server code. Or the server code may be implemented to take the port number from the command line on runtime
