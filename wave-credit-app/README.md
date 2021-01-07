# Credit Risk Scoring with DriverlessAI - Wave App
This application uses H2O DriverlessAI to predict if a customer will default or not. Based on this information, it generates a credit score for each customer. 


## Running this App Locally

### System Requirements 
1. Python 3.6+
2. pip3

### 1. Run the Wave Server
New to H2O Wave? We recommend starting in the documentation to [download and run](https://h2oai.github.io/wave/docs/installation) the Wave Server on your local machine. Once the server is up and running you can easily use any Wave app. 

### 2. Setup Your Python Environment

```bash
$ git clone https://github.com/shivam5992/h2o-wave-apps
$ cd wave-credit-app
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### 3. Run the App

```bash
wave run src.app
```

Note! If you did not activate your virtual environment this will be:
```bash
./venv/bin/wave run src.app
```

### 4. View the App
Point your favorite web browser to [localhost:10101](http://localhost:10101)
