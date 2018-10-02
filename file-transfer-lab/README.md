# File Transfer Protocol lab

This lab contains `fileClient.py` and `fileServer.py` which can transfers a file ("put") from a client to the server. This lab does the following:
* works with and without the proxy
* support multiple clients simultaneously using `fork()`
* gracefully deal with scenarios such as: 
    * zero length files ---
    * user attempts to transmit a file which does not exist ---
    * file already exists on the server ---
    * the client or server unexpectedly disconnect

The following files are shown the order in which they should be runned:
*  `framedClient.py` and `framedServer.py` are a demonstration TCP client and server which exchange frames consisting of byte arrays in the form payload_length:payload where payload_length is in decimal.

        python3 fileServer.py

*   `stammerProxy.py` forwards tcp streams. It may delay the transmission of data but ensures all data will be forwarded, eventually.
   By default,
   it listens on port 50000 and forwards to localhost:50001.  Use the -?
   option for help. Run the following command to start proxy:

        pyhton3 stammerProxy.py

*   `framedClient.py` should be make a connection to the proxy using the following commnad:

        python3 fileClient.py -s localhost:5000

To run multiple clients,  open another terminal and run `python3 framedClient.py` ( make sure input file, `input.txt`, is not empty ).

# Refrences

* https://stackoverflow.com/questions/46775320/simple-python-server-client-file-transfer

* https://stackoverflow.com/questions/28840624/forking-server-in-python

* https://stackoverflow.com/questions/6204003/kill-a-process-by-looking-up-the-port-being-used-by-it-from-a-bat
