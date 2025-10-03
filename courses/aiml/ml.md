# [Machine Learning](../../courses.md)

- [Machine Learning](#machine-learning)
  - [Google: Machine Learning Crash Course](#google-machine-learning-crash-course)
    - [Introduction](#introduction)
  - [LLM: Machine Learning](#llm-machine-learning)
    - [Linear Algebra](#linear-algebra)
  - [Educative: Machine Learning System Design](#educative-machine-learning-system-design)
    - [Introduction](#introduction-1)
    - [Video Recommendation](#video-recommendation)
    - [Feed Ranking](#feed-ranking)
    - [Ad Click Prediction](#ad-click-prediction)
    - [Rental Search Ranking](#rental-search-ranking)
    - [Estimate Food Delivery Time](#estimate-food-delivery-time)
    - [Questions](#questions)
    - [Other](#other)
  - [CodeAcademy: Machine Learning Engineer](#codeacademy-machine-learning-engineer)
    - [Introduction](#introduction-2)
    - [Introduction to Feature Engineering](#introduction-to-feature-engineering)


## Google: Machine Learning Crash Course

### Introduction

- ML -- train a piece of software called model (mathematical relationship derived from data) to make useful predictions or generate content
- Supervised - how data maps to correct answers
  - Regression -- predict numeric value
  - Classification -- predict a class/category
    - Binary 
    - Multi-class
  - concepts
    - Datasets are made up of individual examples that contain features and a label
      - size - number of examples 
      - diversity - range the examples cover
      - features 
    - Model
- Unsupervised -- identify patterns in data
  - Clustering
- Reinforcement -- predictions by getting rewards/penalties based on actions within an environment
  - generates a policy that defines strategy for getting most rewards
- Generative AI - class of models creating content
  - learn patterns in data with the goal to produce new but similar data
  - model learns to mimic the data it's trained on
  - trained as unsupervised, then optionally as supervised or reinforcement


## LLM: Machine Learning 

### Linear Algebra

Scalars: 
- single numeric value, magnitude, quantity, point in 1D scale. 
- how much or how many --- int, float, double, feature values, hyperparameters, weights, biases
- No direction or spatial relationships

Vectors:
- both magnitude and direction
- ordered list of numbers (row or col) (components or elements corresponding to the vector's projection onto axes of a coordinate system)
- N-dimensional space (represented by $\mathbb{R}^N$)
- magnitude/length/norm is calculated by generalized Pythogorean theorem (L2 norm) denoted by $\| \mathbf{v} \|_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_N^2}$
- `magnitude_2d = np.linalg.norm(vector_2d)`



<br/><br/>


Matrices:
- ordered rectangular grid of numbers
- rows -- items/observations; cols -- attributes/features
- represent linear transformations -- take vector as input and transform it into another vector preserving vector addition and scalar multiplication -- Additivity and Homogeneity
  - types: Rotation (rotate around origin), Scaling (stretch/compress), Shearing (shift a vector along one axis depending on its position along other), Projection

## Educative: Machine Learning System Design

### Introduction

- Solid Engineering Foundation + Hands-on experience
- Problem solving, System design, Knowledge
- Dev Cycle => Data Collection, Problem formulation, Model creation, Model implementation, Model enhancement
- Approach
  1. Problem Statement: intention of design and optimzation; ask questions, seek information; make right assumptions
  2. Identify Metrics: logloss, AUC for binary classification; RMSE, MAPE for forecast
  3. Identify Requirements: 
     1. Training requirements: data collection, feature engineering, feature selection, loss function
     2. Inference requirements: low latency, and scalable
  4. Train and Evaluate Model: feature engineering, feature selection, models
  5. Design high level system: system components and how data flows through them
  6. Scale the design: system bottlenecks and addressing them


<br/><br/>

- Feature selection and feature engineering
- One-hot encoding
  - categorical variables into one hot numeric array
  - cons
    - expensive computation and high memory consumption -- dimensions as many as unique
    - not suitable for NLP tasks
  - practices
    - some levels can be grouped together
  - companies: Instakart, Doordash
- Feature hashing
  - aka hashing trick --> text/categorical data with high cardinalities (unique values) into feature vector of arbitrary dimensionality
  - cons
    - way to manage high cardinality or dimensions by mapping multiple values as same value
  - ex: the quick brown fox => h(the) mod 5 (desired dimensions) = 0 (say) => there is 1 word at dimension 0. So vector is now [0, ...] where each represents number of words at that dimension
  - common
    - MurmurHash3
    - JenkinsHash
    - CityHash
    - MD5
  - companies: Booking, Facebook, Yahoo, Yandex, Avazu and Criteo.
  - Collisions if dimensions are small
- Crossed feature
  - aka conjugation between two categorical variables of cardinality c1 and c2 is another categorical variable of cardinality c1 x c2; Hashing is important
  - say lat x long 
  - Haversine distance
  - Manhattan distance
  - Linkedin: User Location x User Job Title; Airbnb
- Embedding
  - transform features from one space to another capturing semantics (closer words mean closer meaning)
  - companies
    - Twitter - UserIds
    - Doordash - Store embedding
    - Instagram - Account embedding
  - usually pre-computed and stored in key-value storage
- Numeric Features
  - Normalization -- can cause issues as min and max are usually outliers; So use clipping -- chose your own min and max
    - mean = 0; values range -1 and 1
    - v = v - min / max - min
  - Standardization
    - if feature resembles normal distribution v = v - mean / std
    - if feature resembles power laws => log( 1 + v / 1 + median)


<br/><br/>

- Training pipeline
  - store data in column oriented format (Parquet, ORC) -- high throughput; tfrecord
- Data partioning
- Handle imbalance class distribution
  - class weights in loss functions: penalize more in the class with most records
  - naive resampling: validation and test data are intact (no resampling)
  - synthetic resampling: SMOTE Synthetic Minority Oversampling Technique -- not widely used for practical reasons -- picks a random minority class point, calculates k nearest neighbors, adds a point between them
- Chose the right loss function
  - binary classification - cross entropy; Facebook uses Normalized Cross Entropy (logloss) for Click Through Rate Prediction
  - forecast
    - MAPE Mean Absolute Percentage Error -- pay attention to target value being skewed
    - SMAPE Symmetric Absolute Percentage Error -- not symmetric; treats under and over forecast differently
    - Quantile Loss -- used by doordash
    - Uber uses RNNs, Gradient boosting trees, Support Vector Regressors
- Retraining requirements -- data distribution is non-stationary, capture changing user behavior
- Logloss formula and Accuracy isn't differentiable, so can't use back-propagation


<br/><br/>

- Inference - use trained ML model to make prediction
- Imbalance workload
  - split workload onto multiple inference servers (worker pool) via Aggregator Service (load balancer)
  - pick workers based on
    - work load
    - round robin
    - request parameter
  - serving logics and multiple models
- Non-Stationary problem  
  - data distribution shift is common
  - Bayesian Logistic Regression
  - based on how quickly the models performance degrades, decide on update/retrain
- Exploration vs Exploitation: Thompson sampling
  - at time t, need to decide on what action to take based on the reward


<br/><br/>

- Metrics Evaluation
- Offline Metrics
  - logloss, MAE (Mean Absolute Error), R2 (Coefficient of Determination), 
- Online Metrics
  - Staging/Sandbox with real traffic
  - AB testing


### Video Recommendation

1. Problem Statement: Youtube recommendations system -- maximize user engagement, recommend new content
2. Metrics design and reqirements
   1. Offline: precision (relevant among retrieved), recall (total relevant actually retreived), ranking loss, log loss 
   2. Online: AB Testing
   3. Training requirements -- train many times during day to capture temporal changes (viral videos)
   4. Inference requirements -- 100 videos recommended, 200ms, ideally 100ms; balance between older videos and new (exploration vs exploitation)
3. Multi-stage models -- for scalability
   - Candidate Generation and Ranking Model (natural fit for logistic regression) -- two stages
   - Architecture
     - User/Video DB --Millions--> Candidate Generation Service -- Hundereds --> Ranking Service -- Dozen --> User
     - User Watch History --> Candidate Generation Service
     - User Watch History --> Ranking Service
     - Video Features --> Ranking Service
   - Candidate generation model
     - matrix facotrization
     - collaborative algorithms -- capture similarity in user-video space
     - practical
       - Inverted Index -- Lucene Elastic Search
       - FAISS
       - Google ScaNN
   - Ranking Model
   - feature engineering
     - video id
     - historical search query
     - location
     - age, gender
     - previous impression
     - time related features
   - Model
     - fully connected neural networks -- capture non-linear relationships
     - sigmoid activation in the last layer -- returns value in range 0 and 1 -- natural fit for estimating probability
     - for deep learning ReLU Rectified Linear Unit is effictive for hidden layer activations
     - Cross Entropy Loss
4. Calculation and Estimation
   1. assumptions
      1. 150 billion views per month
      2. 10% from recommendations -- 15 billion
      3. 100 videos on homepage
      4. watches 2 out of 100 on avg
      5. missed recommendation if not watched within say 10 mins
      6. 1.3 billion users
   2. data size
      1. assume each row is 500 bytes, then multiply it with 800 billion rows a month --> 0.4 Petabytes
      2. Data Lake and Cold Storage
   3. Bandwidth
      1. 10 million user recommendations each second
   4. Scale 1.3 billion users
5. System Design
   1. User watch history --> Train Candidate Model --> Model Repos --> Train ranking model
   2. User historical recommendations --> resampling data (downsampling negative samples) --> features pipeline (Spark -- in memory computation engine, Elastic MapReduce, Google Dataproc -- cloud native spark and Hadoop) --> train ranking model
   3. Search query Db --> features pipeline --> user/video db --> train candidate model
   4. challenges
      1. huge data size
      2. imbalance data
      3. high availability
         1. use model as a service using docker containers
         2. use kubernetes to autoscale the pods
   5. ex:
      1. Application Server <--> Candidate Generation Service <-- User/Video DB
      2. Application Server <--> Ranking Service <-- User Watch History | Search query DB
6. Scale the design
   1. Scale out -- horizontal; Kubernetes pod, and leverage autoscaler
   2. We can also use Kube-Proxy so candidate generation service can call ranking service directly
7. Follow up questions


### Feed Ranking

1. Problem Statement: Linkedin feed to maximize user engagement (click through rate CTR)
   1. feed
      1. connections
      2. informational
      3. profile
      4. opinion
      5. site-specific
2. Metrics Design and Requirements
   1. Offline
      1. CTR = number of clicks / number of times shown
      2. Supervised binary classification model; Normalize cross entropy NCE and AUC Area Under Curve
   2. Online
      1. Convertion rate (clicks / feeds)
   3. Training requirements
      1. online data shift vs offline data distribution
      2. models are trained in distributed settings
      3. support for personalization
      4. data freshness -- avoid repetitive feed. 
   4. Inference requirements
      1. scalability -- 300 million users
      2. latency -- 200ms for feed activities and 50ms for ranking service
      3. data freshness -- faster data pipeliness to become fully aware of user watching a feed
3. Model
   1. Feature Engineering
      1. User profile: job title, industry, demographic... One Hot Encoding (low cardinality); Embedding (higher cadinality)
      2. Connection strength between users -- user similarity -- can use embeddings and measure distance
      3. Age of activity
      4. Activity features -- activity, hashtag, media, ...
      5. Cross features
   2. Training Data
      1. rank by chronicle order -- serving bias (user attention on first few posts) and data sparsity problem (job feed compared to newsfeed -- changes are not proportional)
      2. random serving -- doesn't help solve anything
      3. feed ranking algorithm -- rank top feeds, permute randomly. use clicks for data collection. 
   3. Model
      1. Selection
         1. probabilistic sparse linear classifier -- logistic regression
         2. distributed training -- spark or alternating direction method of multipliers
         3. can also use deep learning in distributed settings -- fully connected layer with sigmoid activation layer at end
      2. Evaluation
4. Calculation and Estimation
   1. Assumptions
      1. 300 million active monthly users
      2. 40 activities per visit. 10 visits a month
      3. 120 billion observations or samples
   2. Data Size
      1. assume CTR is 1% per month. 1 billion +ve labels and 110 billion negative labels
      2. say each row 500 bytes
      3. 60 Terabytes in one month
5. High level design
   1. HLD
      1. Client --> Application Server --Feed Request--> Feed Service <--Get Feature Values--  Item Store (all activities generated by users) | Model Store <-- Model Training : Inference
      2. Feature Store <--Receive the right feature for model to store--> Feed Service : Inference
      3. Feature Pipeline --> Feature Store (MySQL Cluster/Redis/DynamoDB)--> Model Training : Training
6. Scale
   1. scale out feed service module -- retrieval service and ranking service
   2. scale out application server and put load balancer infront of it
   3. architecture
      1. client --> load balancer --> application server pool <--> Feed service pool --> Feature store
      2. Application server pool --> Logging service --> log data --> feature pipeline --> feature store --> model training --> model store
      3. Model Store | item store --> Feed service. 

### Ad Click Prediction

1. Problem Statement: Ad Click prediction
   1. Publisher's direct sale -> Premium ad network -> Vertical ad network -> Remnant ad network
2. Metrics design and requirements
   1. Offline 
      1. Normalized Cross Entropy NCE --> logloss divided  by cross-entropy
   2. Online 
      1. Revenue Lift -- percentage of revenue changes over time
   3. Training requirements
      1. Imbalance data
      2. Retraining frequency to capture data shift
      3. train/validation split by time
   4. Inference requirements
      1. Serving 50-100ms for ad prediction
      2. overspent: repeated serving of ads coule mean over-spending campaign budget
3. Model
   1. Feature engineering
      1. advertiserid -- feature hashing or embedding
      2. user's historical behavior -- feature scaling -- normalization
      3. temporal -- one hot encoding
      4. cross features
   2. Training
   3. Model
      1. Selection
         1. deep learning in distributed settings
      2. Evaluation
         1. training data and validation data 
         2. replay evaluation to avoid biased offline evaluation
4. Calculation and estimation
   1. assumptions
      1. 40k ad requiests per second or 100b ad requests per month
      2. each record -- 100s of features -- 500 bytes per record
   2. data size
      1. 100 * 10^12 * 500 => 50 PB
   3. Scale 100m users
5. High Level Design
   1. Data Lake
   2. Batch data prep -- ETL jobs storing training data store
   3. Batchh training -- retrain models
   4. Model Store
   5. Ad Candidates 
   6. Stream data prep pipeline -- processes online features and stores features in key-value storage for low latency down-stream processing
   7. Model Serving -- standalone service loads diff models
   8. architecture
      1. client --request data--> ads candidate generation service --generate ads candidates--> ads candidates --> stream data pipeline --> feature store --ad candidates with features--> ads ranking service --return ad ranking--> 
      2. Data Lake --> data prep job (spark) --> training data store --> batch training job --> model store --> ads ranking service
      3. data prep job (spark) --> feature store --> batch training job
6. Scale
   1. scale out model serving service and put aggregator service to spread load

### Rental Search Ranking

1. Problem Statement: Airbnb homes sorted with most booked at the top
   1. custom score ranking function based on text similarity given query -- doesn't guarantee booking
   2. likelihood of booking -- binary classification
2. Metrics design and requirements
   1. Offline
      1. discounted cumulative gain DCG -- rel_i relevance of result at position i
      2. Normalized Discounted Cumulative Gain -- nDCG = DCG/IDCG
      3. Ideal Discounted Cumulative Gain -- IDCG
   2. Online
      1. covertion rate, revenue lift
   3. Training requirements
      1. Imbalanced data
      2. train/validation data -- split by time to mimic production traffic
   4. Inference requirements
      1. Serving -- 50-100ms search ranking
      2. under-predicting for brand new listings (not enough data)
3. Model
   1. Feature engineering
      1. geolocation -- lat long -- log of distance from the center of map for lat long separately
      2. favorite place -- 2d grid -- embedding
      3. listing id -- embedding
      4. list features
      5. location -- normalize 
      6. historical search query -- text embedding
      7. user associated features, previous bookings, length of stays -- normalization/standardization
      8. time related features
   2. Training
      1. search/view history, bookings
   3. Architecuture
      1. deep learning -- fully connected layer
      2. variational autoencoder 
      3. denoising autoencoder
4. Calculations and Estimation
   1. Assumption
      1. 100m active monthly users
      2. 5 bookings per year -- 30 rental listings for each booking
      3. 5 * 30 * 10^8 or 15b observations per year or 1.25b samples per month
   2. Data Size 500 * 1.25 * 10^9 = 625GB
   3. Scale 150m users
5. High Level Design
   1. Architecture
      1. Client <--> Application Server <--Search rental--> Search Service <--Rereank rental result--> Ranking service <-- Model Store <-- Model Training --> Feature Store
      2. Feature pipelines --> Feature Store <--Receive the right features--> Ranking Service
6. Scale
   1. Architecture
      1. Client <--> Load Balancer --> Booking Service --> Booking DB --> Trainiing Pipeline --> Model Training --> Model Store --> Ranking Services 
      2. Client <--> Load Balancer --> Application Servers <--> Search Services --> Logs --> Training Pipeline
      3. Search Services <-- Ranking Services <-- Feature Store <-- Feature Pipeline

### Estimate Food Delivery Time

1. Problem Statement: predict total delivery time given order details, market conditions, and traffic status
2. Metrics Design and Requirements
   1. Offline
      1. RMSE Root Mean Square Error
   2. Online 
      1. AB Testing, monitor RMSE, customer engagement, customer retention, ...
   3. Training requirements
      1. data in Parquet files
      2. schedulers to retrain the model throughout the day to leann external factors
   4. Inference
      1. real-time estimations; 30 predeictions per delivery
      2. near real-time updates -- changes on status
      3. changes in delivery --> new estimate
      4. capture real-time aggregated statistics
      5. 100-200ms
3. Model
   1. Feature engineering
      1. Order features; Item features; Order type
      2. Store id -- embedding
      3. realtime features -- orders, dashers, traffic, travel estimates
      4. time feature
      5. historical aggregates
      6. similarity
      7. lat long
   2. training data
   3. Model 
      1. Gradient Boosted Decision Tree
         1. Data --> Residuals --> Residuals ... --> Improved Model 
         2. Process
            1. avg delivery time -- baseline
            2. residual(error) between actual and prediction
            3. decision trees for predicting residuals
            4. predeict using all the trees.  estimated delivery time = avg delivery time + learning rate * residuals
            5. given new estimated delivery time --> model computes new residuals
            6. repeat 3 - 5 
         3. problem
            1. optimizing RMSE penalizes similarly for under-estimates and over-estimates
4. Calculation and Estimation
   1. Assumptions
      1. 2m active monthly users, 20m users in total, 300k restaurants, 200k drivers
      2. 20m deliveries per year
   2. Data Size -- 1GB
   3. scale 20m users
5. System Design 
   1. Restaurant | Deliver --> Application Server
   2. User <-- Application Server
   3. Application Server --> Status Service --> Deliver/Order DBs <--> Feature Pipeline --> Feature Store --> Estimate Delivery Time Service
   4. Deliver/Order DBs --> Data Prep --> Training Data --> Training Pipeline --> Model Training --> Model Store --> Estimate Delivery Time Service
   5. Notification Service --> Application Server
   6. Application Server <--> Estimate Delivery Time Service <-- Feature Store
6. scale
   1. Scale out services, use load balancer
   2. leverage streaming process systems like kafka to handle notifications as well as model rpedictions 

### Questions

1. How do we train models to handle an imbalance class?
2. How do we monitor and make sure models don’t go stale?
3. How do we design inference components to provide high availability and low latency?
4. Which components are likely to be overloaded?
5. How can we scale the overloaded components?
6. Is the system good enough to serve millions of users?
7. How we would handle some components becoming unavailable, etc.
8. How do we adapt to user behavior changing over time?
9. How do we handle the ranking model being under-explored?
10. What are the cons of using ListingID embedding as features?
11. Assuming there is a strong correlation between how long users spend on listings and the likelihood of booking, how would you redesign the network architecture?


### Other

1. logloss is only applicable for binary classification and can be sensitive to background CTR


## CodeAcademy: Machine Learning Engineer

### Introduction

- ML -- mathematics (parameters) + cs (implementation) + statistics (evaluation)
- ![Machine Learning Timeline](https://content.codecademy.com/courses/updated_images/timeline2_Updated_1-01.svg)
- ML -- Supervised (Classification, Regression), Unsupervised (Clustering)

```py
# Supervised Learning Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

housing_data = pd.read_csv('housing_data.csv')
X = housing_data[['Sq ft', 'Burglaries']]
y = housing_data['Rent']

reg = LinearRegression()

reg.fit(X, y)

square_footage = 5390
number_of_burglaries = 39

y_pred = reg.predict(np.array([square_footage, number_of_burglaries]).reshape(1, 2))

print(y_pred)
```

```py
# Supervised Learning Classification

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

photo_id_times = pd.read_csv('photo_id_times.csv')

X = np.array(photo_id_times['Time to id photo']).reshape(-1, 1)
y = photo_id_times['Class']

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

time_to_identify_picture = 5

y_pred = neigh.predict(np.array(time_to_identify_picture).reshape(1, -1))

if y_pred == 1:
    print("We think you're a robot.")
else:
    print("Welcome, human!")
```

```py
# plot.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_clusters(media_usage, labels):
"""
This function plots the clusters for this exercise. This function is in a different file so that script.py is easier to read.
"""
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(111, projection='3d')

  xs = media_usage['Hours reading text']
  ys = media_usage['Hours watching video']
  zs = media_usage['Hours in VR']

  ax.scatter(xs, ys, zs, c=labels)
  ax.set_xlabel('Hours reading text')
  ax.set_ylabel('Hours watching video')
  ax.set_zlabel('Hours in VR')

  # Set the perspective so the clusters are easier to see
  ax.azim = 40
  ax.elev = 30

  plt.show()
return
```

```py
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import codecademylib3
from plot import plot_clusters

media_usage = pd.read_csv('media_usage.csv')

kmeans = KMeans(n_clusters=3)

kmeans.fit(media_usage)

labels = kmeans.predict(media_usage)

plot_clusters(media_usage, labels)
```

### Introduction to Feature Engineering

- feature -- measurable property
- ...
  - performance -- accuracy in predicting
  - runtime -- computation
  - interpretability -- goal is to understand factors driving outcomes
  - generalizability -- 
- categories
  - feature transformation methods -- scaling, binning, log transformations, hashing, one-hot encoding
  - dimensionality reduction methods aka feature extraction methods -- PCA Principal Component Analysis, LDA Linear Discreminant Analysis
    - lack of interpretability due to these being mathematical objects and not real world objects
  - feature selection methods -- 
    - filter methods -- statistical techniques -- correlation coefficients (pearson, spearman, ), chi^2, ANOVA, Mutual Information calculations
    - wrapper methods -- greedy search strategy -- forward feature selection, backward feature elimination, sequential floating
    - embedded methods -- lasso, ridge, tree-based feature importance
- ![Feature Engineering](https://static-assets.codecademy.com/skillpaths/feature-engineering/feature-engineering-intro/intro%20to%20Feature%20Engg%20Table%20NEW.png)
- 