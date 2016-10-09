# DiabetesPredictionSystemPrototype
Neural Network, Big Data. The design of the diabetes prediction system based on Neural Network.
We used the PyBrain as the Neural Network data training and prediction framework.
It's a prototype based on “python with django” as the programing language and framework.

Purpose: We are going to develop an online system that is used to predict females’ health conditions, especially for diabetes. After initial specification, we decide to use the neural network as an approach to train the prediction model. Otherwise some web pages using will be the user interfaces. Because we are lack of clarity in conceptual design, we are going to build an experimental prototype that could help us to complement the specification. This prototype will have high fidelity and become a part of the system in the future. In this prototype, we are mainly focus on the following points.

1. Choosing the best neural network that could generate efficient and accurate algorithm, and using the trained model to do the prediction service.
2. Building a stable and excellent interactive interface.

Test Scenarios:

1. Enter the main page by 127.0.0.1:8000/main/;
2. Then click the start button to enter the data processing page; in this page, it shows the
related algorithm to do the data processing, and there are two options, one is the “Show the Raw Data” button to show the list of the raw training data, the other one is “Data Processing” to do the processing;
3. Enter the data processing page, we could see the data which we remove from the raw data based on the outlier algorithm of the box plot; moreover, the processed data can be shown by clicking the “Show Processed Data” button, and the following step can be processed by clicking the “Training and Test” button;
4. After clicking the “Training and Test” button, the client will send the request for training and test the processed data to the server by jQuery/Ajax (cause the training and test stage will spend longer time comparatively), and the server will begin training and test the related data, then the result will show on the next page;
5. Then just clicking the “Predict” button, two options (multiple-record predict and single- record predict) can be chosen for the prediction stage;
6. For the multiple-record prediction, just uploading the CSV file with the related format, and for the single-record prediction, just filling with the blanks (still using jQuery/JavaScript to control the input), then the prediction output will be shown on the page; then, there still are two options that one is prediction by the current trained neural network model, and the other is return to the main page.
