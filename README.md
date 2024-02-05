# ML Model Pipeline implementation End-to-end Using Rest API

## Objective
Implement a ML model and integrate it with website for real time prediction using Rest Api's

## Dataset
Dataset is about estimating obesity level based on different parameters which is explained in the paper, 
Estimation of obesity levels based on eating habits and physical condition . (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5H31Z.
The Data set is also available, [UCI ML Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)

## Preprocessing
After basic preprocessing centralisation of values and making sure each features are in same range, standard scaler and Min-Max scaler used. Based on results, the Min-Max scaler is chosen.

## Model
Initially Kmeans and GMM model were implemented, but these are unsupervised models and they classify based on relative distance between different data points. For this problem, the logic needs more complexity, so we could able to achieve 96 percent accuracy after using Gradient Boosting Classifer. The Gradient Boosting Classifier is a powerful machine learning technique that builds on the idea of boosting. Boosting is an ensemble technique that combines the predictions from multiple machine learning algorithms to make more accurate predictions than any individual model

## Rest Api
After preprocessing and training the model, both preprocessing step and model have been saved so that real time data is preprocessed and predicted to share the results. The Server whenever receives data from client machine via REST API 'POST' method, preprocess it and then predict the obesity level based on saved Gradient boost classifier and send it back.
![alt_text](https://github.com/rakesh09111996/ML-Pipeline-RESTAPI/blob/59b4044e21ac5738e7efb1651a2427b1976e4266/Restapi.png)

The advantages of REST APIs lie in their simplicity, flexibility, and wide support across different platforms and languages. These characteristics make REST a popular choice for designing and implementing web services that need to be scalable, efficient, and easy to integrate.

## Results
Accuracy of Gradient Classifier: 0.96

Classification Report:
                      
           class  precision  recall    f1-score    support
           0       1.00      0.97      0.98        58
           1       0.90      0.95      0.92        56
           2       0.95      0.91      0.93        57
           3       0.98      0.96      0.97        57
           4       0.97      0.94      0.96        72
           5       0.93      1.00      0.96        55
           6       1.00      1.00      1.00        67
           
    macro avg      0.96      0.96      0.96       422
    weighted avg   0.96      0.96      0.96       422
    accuracy                           0.96       422
    
[ML model implemented with RestAPI](https://rakesh09111996.github.io/ML-pipeline-implemented-with-RestAPI/)


