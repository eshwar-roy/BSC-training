data = {
 "ModelID": [
 "M001","M002","M003","M004","M005","M006","M007","M008","M009","M010",
 "M011","M012","M013","M014","M015","M016","M017","M018","M019","M020",
 "M021","M022","M023","M024","M025","M026","M027","M028","M029","M030",
 "M031","M032","M033","M034","M035","M036","M037","M038","M039","M040",
 "M041","M042","M043","M044","M045","M046","M047","M048","M049","M050"
 ],
 "Algorithm": [
 "RandomForest","XGBoost","CNN","LSTM","SVM",
 "DecisionTree","Transformer","RandomForest","CNN","XGBoost",
 "LSTM","Transformer","SVM","RandomForest","CNN",
 "XGBoost","DecisionTree","LSTM","Transformer","CNN",
 "RandomForest","XGBoost","CNN","Transformer","SVM",
 "DecisionTree","RandomForest","CNN","LSTM","Transformer",
 "RandomForest","CNN","XGBoost","LSTM","SVM",
 "Transformer","DecisionTree","RandomForest","CNN","XGBoost",
 "LSTM","Transformer","CNN","RandomForest","SVM",
 "DecisionTree","XGBoost","Transformer","CNN","RandomForest"
 ],

"TrainingSamples": [
 120000,95000,150000,210000,85000,
 60000,300000,140000,175000,98000,
 225000,315000,90000,132000,182000,
 110000,72000,250000,330000,165000,
 128000,103000,194000,280000,88000,
 64000,145000,180000,240000,350000,
 150000,190000,100000,260000,92000,
 340000,70000,155000,205000,115000,
 270000,360000,170000,149000,87000,
 62000,108000,320000,185000,142000
],
"Accuracy": [
 96.2,91.5,98.1,94.6,88.2,
 84.5,99.1,95.8,97.3,90.8,
 95.2,99.4,89.3,94.8,96.7,
 92.4,83.9,95.9,99.5,97.0,
 95.1,91.2,97.8,99.0,87.6,
 84.2,95.7,97.5,96.0,99.2,
 95.5,97.2,91.0,95.8,88.5,
 99.1,83.7,95.6,97.4,92.1,
 95.9,99.6,96.8,94.9,88.8,
 84.0,91.8,99.3,97.1,95.3
 ],
"InferenceLatency": [
 45,80,120,95,40,
 30,210,55,130,85,
 110,260,42,60,125,
 78,28,108,240,135,
 58,82,118,225,38,
 25,52,132,105,250,
 63,128,76,115,41,
 235,26,50,138,74,
 112,255,127,57,39,
 27,79,220,129,56
 ],
"DataDrift": [
 2,8,3,6,18,
 25,1,4,5,10,
 7,0,20,6,3,
 9,27,5,1,4,
 6,8,2,1,19,
 26,5,4,6,0,
 3,2,9,5,18,
 1,28,4,5,10,
 6,0,4,5,21,
 25,9,1,3,4
 ],
"CPUUsage": [
 42,60,75,68,38,
 30,91,50,72,61,
 69,95,41,52,76,
 59,28,67,94,74,
 53,62,73,90,39,
 26,49,71,66,96,
 54,70,63,68,40,
 92,25,48,74,60,
 69,97,77,51,37,
 29,58,93,72,47
 ],
"dictionConfidence": [
 0.98,0.91,0.99,0.95,0.84,
 0.80,0.99,0.97,0.98,0.90,
 0.96,0.99,0.85,0.95,0.98,
 0.92,0.79,0.96,0.99,0.98,
 0.95,0.91,0.98,0.99,0.83,
 0.81,0.96,0.97,0.95,0.99,
 0.96,0.98,0.90,0.96,0.84,
 0.99,0.78,0.95,0.98,0.91,
 0.96,0.99,0.97,0.95,0.85,
 0.80,0.92,0.99,0.98,0.96
],
 "FailureRisk": [
 0,0,0,0,1,
 1,0,0,0,0,
 0,0,1,0,0,
 0,1,0,0,0,
 0,0,0,0,1,
 1,0,0,0,0,
 0,0,0,0,1,
 0,1,0,0,0,
 0,0,0,0,1,
 1,0,0,0,0
 ]
}


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(data) 


numeric_columns=df.select_dtypes(include=[np.number]).columns
# print(numeric_columns)
for col in numeric_columns:
    arr=df[col].to_numpy() #this converts numeric coloumns into numpy array
    print(f"{col}")
    print("array:",arr)
    print("shape:",arr.shape ,"\n", "dim:", arr.ndim, "\n",arr.size, "\n",arr.dtype)#the same line prints shape,size,dimensions,datatype

print(df["Accuracy"].mean(),df["Accuracy"].std(),df["Accuracy"].var(),df["Accuracy"].median())
print("inference latency (max and min values aree)",df["InferenceLatency"].max(),df["InferenceLatency"].min())

#all models with CPUUsage greater than 90%.
high_cpumodels=df[df['CPUUsage']>90]
print(high_cpumodels)

datadrift_model=df[df["DataDrift"]>20]
print(datadrift_model)

training_min= df['TrainingSamples'].min()
training_max=df['TrainingSamples'].max()
training_normalized=(df['TrainingSamples']-training_min)/(training_max-training_min)
print("min_max_normalization of training samples:",training_normalized)


# Health Score = Accuracy + PredictionConfidence × 100 − DataDrift
df['health_score']=df["Accuracy"]+df['dictionConfidence']*100-df['DataDrift']
print("health score:",df['health_score'])



''' pandas from now on---------------------- dataframe is already created on top'''
print("top 10 :",df.head(10),"\n","tail 10 records:",df.tail(10) )

print(df.info(),"\n", df.describe())
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
print(df.groupby('Algorithm').size())
print(df.groupby("Algorithm")["Accuracy"].mean())
print(df.nlargest(10,'dictionConfidence'))
#sorting 
print(df.sort_values(by='InferenceLatency',ascending=False))

df['HealthStatus']=df['health_score'].apply(lambda x:'healthy' if x>180 else ('moderate' if x>170 else 'critical'))

print(df["HealthStatus"])

# df.to_csv("assis_model.csv",index=False)

'''sklearn'''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
le=LabelEncoder()
df["Algorithm"]=le.fit_transform(df['Algorithm'])
X=df.drop(["ModelID", "FailureRisk"],axis=1)
y=df["FailureRisk"]
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=45)

model=RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('accuracy:',accuracy_score(y_test,y_pred))
print('confusion matrix',confusion_matrix(y_test,y_pred))
print("classification report : ",classification_report(y_test,y_pred))

"""matplotlib------"""
import matplotlib.pyplot as plt


plt.figure(figsize=(6,4))
plt.hist(df["Accuracy"], bins=10, edgecolor="black")
plt.title("Histogram of Accuracy")
plt.xlabel("Accuracy")
plt.ylabel("Frequency")
plt.show()



plt.figure(figsize=(6,4))
plt.hist(df["InferenceLatency"], bins=10, edgecolor="black")
plt.title("Histogram of Inference Latency")
plt.xlabel("Inference Latency")
plt.ylabel("Frequency")
plt.show()



plt.figure(figsize=(6,4))
plt.scatter(df["DataDrift"], df["Accuracy"])
plt.title("Accuracy vs Data Drift")
plt.xlabel("Data Drift")
plt.ylabel("Accuracy")
plt.show()



plt.figure(figsize=(6,4))
plt.scatter(df["CPUUsage"], df["InferenceLatency"])
plt.title("CPU Usage vs Inference Latency")
plt.xlabel("CPU Usage")
plt.ylabel("Inference Latency")
plt.show()



algorithm_counts = df["Algorithm"].value_counts()

plt.figure(figsize=(8,4))
plt.bar(algorithm_counts.index, algorithm_counts.values)
plt.title("Number of Models by Algorithm")
plt.xlabel("Algorithm")
plt.ylabel("Number of Models")
plt.xticks(rotation=45)
plt.show()



failure_counts = df["FailureRisk"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    failure_counts.values,
    labels=failure_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribution of Failure Risk")
plt.show()


'''eda'''


print(df.corr(numeric_only=True))



correlation = df.corr(numeric_only=True)["FailureRisk"].drop("FailureRisk")
print(correlation)



print("\nAverage Inference Latency")
print(df.groupby("FailureRisk")["InferenceLatency"].mean())


print("\n Average CPU Usage for Each Algorithm")
print(df.groupby("Algorithm")["CPUUsage"].mean())


print("\nAverage Prediction Confidence")
print(df.groupby("FailureRisk")["dictionConfidence"].mean())



print(df[(df["Accuracy"] > 95) & (df["FailureRisk"] == 1)])


print(df.groupby("Algorithm")["DataDrift"].mean())


# # 28. Identify the top 5 healthiest AI models
# # (Highest Accuracy, Highest Prediction Confidence, Lowest Data Drift)
# healthy_models = df.sort_values(
#     by=["Accuracy", "dictionConfidence", "DataDrift"],
#     ascending=[False, False, True]
# )

# print("\n28. Top 5 Healthiest AI Models")
# print(healthy_models.head(5))


# # 29. Identify the top 5 highest-risk AI models
# # (Highest FailureRisk, Highest DataDrift, Lowest Accuracy)
# risk_models = df.sort_values(
#     by=["FailureRisk", "DataDrift", "Accuracy"],
#     ascending=[False, False, True]
# )

# print("\n29. Top 5 Highest-Risk AI Models")
# print(risk_models.head(5))






'''ml algorithms'''
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('accuracy_score',accuracy_score(y_test,y_pred))
print('accuracy:',accuracy_score(y_test,y_pred))
print('confusion matrix',confusion_matrix(y_test,y_pred))
print("classification report : ",classification_report(y_test,y_pred))


from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import load_diabetes, load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
data=load_diabetes()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=45)
sc=StandardScaler()
x_trains=sc.fit_transform(x_train)
x_tests=sc.transform(x_test)
lr=LinearRegression(fit_intercept=True,n_jobs=1)
lr.fit(x_trains,y_train)
y_pred=lr.predict(x_tests)
print("r1score",r2_score(y_test,y_pred))
print('mse',mean_squared_error(y_test,y_pred))
print('mae',mean_absolute_error(y_test,y_pred))




model=LogisticRegression()
model.fit(x_trains,y_train)
y_pred=model.predict(x_tests)
print('accuracy:',accuracy_score(y_test,y_pred))
print("confusion matrix",confusion_matrix(y_test,y_pred))
print('classification report:',classification_report(y_test,y_pred))

from sklearn.svm import SVC
model=SVC(kernel='linear',c=1.0,random_state=42)
model.fit



