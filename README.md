## Objective
To create an API endpoint that makes use on a machine learning model that can be used in any application.

## Introduction
For this demo, we will use the Iris dataset.

This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) based on certain characteristics. The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

## Running the API
Have a .env file with you ngrok token: NGROK_TOKEN=XXX. 

Execute the `build_container.sh` script to build and run the container:
```
./build_container.sh
```

## Accessing the API
This will open a tunnel to your localhost on port 12000. Go to `https://bat-absolute-apparently.ngrok-free.app` to access the API.