## What is Federated Learning ?


Federate Learning / Google  
https://ai.googleblog.com/2017/04/federated-learning-collaborative.html  


What is Federated Learning? Techniques, Use Cases, & Benefits  
https://research.aimultiple.com/federated-learning/#what-is-federated-learning  


In recent years, machine learning has been used in many cases to discover common and hidden patterns and rules from a large amount of data.  
Although current machine learning commonly aggregates data centrally on a server, the drastic increase in the data makes it difficult to calculate on a single server.  


Therefore, “distributed machine” learning such as Federated learning has been attracting attention to avoid the concentrated load on the server.  
The purpose of distributed machine learning is to distribute the processing load on the server and to improve the performance, by sharing the processing of the server with the client.  
By utilizing the computing power of multiple clients, learning can be performed more efficiently than with a server alone.   
Also, since the client does not need to send its own data to the server, Federated Learning is also effective in terms of privacy protection.  


The workflow of Federated Learning is described as follows:  
1. The server sends the current machine learning model in the server (Global model) to the clients  
2. The clients train machine learning model by their own local data and create Local model  
3. The clients send Local model to the server  
4. The server updates Global model based on the information sent by the clients  

![FL](https://user-images.githubusercontent.com/103622417/201034330-23224148-c3c3-407a-9ec4-52d120d1700b.PNG)
