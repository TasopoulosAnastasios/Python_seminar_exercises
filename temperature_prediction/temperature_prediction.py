import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import requests
from sklearn import linear_model

#request to weather api
d1=requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/athens/2022-10-10/2022-10-20?unitGroup=metric&include=days%2Calerts%2Ccurrent%2Cevents%2Chours&key=YourKeyHere&contentType=json')

#create dictionary with the json recieved
response=d1.json()
#print(type(response))
#print(response.keys())
#create dictrionary to add the information we want
alldays = {'datetime': [],
           'Pressure': [],
           'Humidity': [],
           'Temperature': []}

#create list with the data we want(days)
days=response['days']
#print(type(days))
#print(len(days))

for i in range(len(days)):
    #print(days[i])
    #print(type(days[i]))
    day=days[i]
    #print(day.keys())
    hours=day['hours']
    for j in range(len(hours)):
        aday=hours[j]
        #print("aday= ",type(aday))
        #print(aday.keys())
        #we find the date from the unix timestamp wich is in datetimeEpoch data
        alldays['datetime'].append(datetime.datetime.fromtimestamp(aday['datetimeEpoch']).strftime('%Y-%m-%d %H: %M: %S'))
        alldays['Pressure'].append(aday['pressure'])
        alldays['Humidity'].append(aday['humidity'])
        alldays['Temperature'].append(aday['temp'])

#create dataframe
df=pd.DataFrame.from_dict(alldays)
#print(df)
#finding the hour from full datetime
df['Hour'] = pd.to_datetime(df['datetime'],format="%Y-%m-%d %H: %M: %S").dt.hour
#print(df)
##date=pd.to_datetime(df['datetime'])
##print("date type:",type(date))
##print(date)
#save to csv file
df.to_csv("wheather-data-athens.csv",index=False)
#read from csv to a dataframe df
df=pd.read_csv("wheather-data-athens.csv")

print(df)

#Creation of diagrams
#Time series variance diagram
fig, (ax1, ax2, ax3)=plt.subplots(3, 1, figsize=(10, 10))

#pressure diagram

ax1.plot(df["datetime"], df["Pressure"], color='red')
ax1.set_xlabel("Date")
ax1.set_ylabel("Pressure [inHg]")
ax1.set_xticks(df['datetime'][::20])
ax1.set_xticklabels(df['datetime'][::20], rotation=25)
#Temperature diagram
ax2.plot(df['datetime'], df['Temperature'], color='green')
ax2.set_xlabel('Date')
ax2.set_ylabel('Temperature (°C)')
ax2.set_xticks(df['datetime'][::20])
ax2.set_xticklabels(df['datetime'][::20], rotation=25)
#humidity diagram
ax3.plot(df['datetime'], df['Humidity'], color='blue')
ax3.set_xlabel('Date')
ax3.set_ylabel('Temperature (°C)')
ax3.set_xticks(df['datetime'][::20])
ax3.set_xticklabels(df['datetime'][::20], rotation=25)
plt.show()
#independent variables as list
feat_cols=['Hour','Humidity','Pressure']
#diagram of independent variables with temperature
fig, (ax1,ax2,ax3)=plt.subplots(3,1,figsize=(10,10))
ax1.scatter(df[feat_cols[0]],df['Temperature'],color='red', alpha=0.2)
ax2.scatter(df[feat_cols[1]],df['Temperature'],color='yellow', alpha=0.2)
ax3.scatter(df[feat_cols[2]],df['Temperature'],color='blue', alpha=0.2)
ax1.set_xlabel(feat_cols[0])
ax2.set_xlabel(feat_cols[1])
ax3.set_xlabel(feat_cols[2])
plt.tight_layout()
plt.show()

#transform the data of independent variables to 2D-array
h_array=df[feat_cols].values
w_array=df['Temperature'].values
#creation of linear regression model
model_reg=linear_model.LinearRegression()
model_reg.fit(h_array, w_array)

#print coefficient
print("Printing coefficients:")
print("coefficients bn: ",list(zip(model_reg.coef_,feat_cols)))
print("Coefficient b0: ", (model_reg.intercept_))
print("Coefficient of determination: ", (model_reg.score(h_array,w_array)))
#save model
with open("model.pickle","wb") as f:
    pickle.dump(model_reg,f)


###########Functions#############
def start_menu():
    print("Find the next hours temperature")
    while True:
        print("Select an option: ")
        print("A - Next hours temperature forecast")
        print("B - Exit")
        option=input("Give your choise: ")
        if(option=="A"):
            hour, humidity, pressure=user_input()
            #model's input data
            input_data=[hour,humidity,pressure]
            #transform data to 2D array
            final_input=np.array([input_data]).reshape((1,-1))
            print("Prediction..\n")
            model_load=get_model()
            prediction_1=model_load.predict(final_input)
            print("Next hour the temperature will be:",prediction_1[0])
        elif option=="B":
            print("Exit program")
            break
        else:
            print("Your choise is not correct")
        
def user_input():
    #Finding current time
    hour=pd.Timestamp.now().hour
    while True:
        try:
            hum=float(input("Give the humidity: "))
            press=float(input("Give the pressure: "))
            if hum>0 and press>0:
                break
            else:
                print("please give possitive numbers")
        except ValueError:
            print("Wrong input data please enter numbers")
    return hour,hum,press
#Functiol loading model
def get_model():
    print("Model recovery...")
    with open("model.pickle","rb") as f:
        model_load=pickle.load(f)
    return model_load
start_menu()
