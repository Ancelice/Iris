## What is Federated Learning ?


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


Federate Learning / Google  
https://ai.googleblog.com/2017/04/federated-learning-collaborative.html  


What is Federated Learning? Techniques, Use Cases, & Benefits  
https://research.aimultiple.com/federated-learning/#what-is-federated-learning  


## How to apply Federated Learning to Iris dataset  

For prediction, I used Federated Learning and Deep Neural Network.

What’s a Deep Neural Network?
https://www.bmc.com/blogs/deep-neural-network/


～Workflow for prediction (Federated Learning)～  

1. The data that could be collected at current time is used as training data  
2. (ie: 2022/10/25 11:00), and divided by each region (Africa, Asia, Europe, NA, Oceania, and SA)  
3. The server sends the current machine learning model in the server (Global model) to the clients  
4. The clients train machine learning model by their own training data and create Local model  
5. Predict Data for the next time period (2022/10/25 12:00)  
6. Calculate MSE (Mean Square Error) and MAE (Mean Absolute Error) for local model  
7. The clients send Local model to the server  
8. The server updates Global model based on the information sent by the clients  
9. Calculate MSE and MAE for Global model  
10. Return step 1 and continue...


～Intended Environment～

・Iris dataset is collected for 1 week (The collection interval is 100,000 data / hour).
Dataset : 2022/10/25 11:00 ~ 2022/11/1 10:00 (JST)

・Dataset each time period is divided by 6 region group : six continents (Africa, Asia, Europe, NA, Oceania, and SA)

・There are 1 administrator (World), and 6 clients (Africa, Asia, Europe, NA, Oceania, and SA)

・When calculating MSE and MAE, all 7 worker (World, Africa, Asia, Europe, NA, Oceania, and SA) calculate using the same test data in order to make it fair
