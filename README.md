# Document_Clustering

## Hierarchical Clustering Exercise
### Context 
Document clustering, or text clustering, is a very popular application of clustering algorithms. A web search engine, like Google, often returns thousands of results for a simple query. For example, if you type the search term "jaguar" into Google, around 200 million results are returned. This makes it very difficult to browse or find relevant information, especially if the search term has multiple meanings. If we search for "jaguar", we might be looking for information about the animal, the car, or the Jacksonville Jaguars football team. 

In this problem, we'll be clustering articles published on Daily Kos, an American political blog that publishes news and opinion articles written from a progressive point of view. Daily Kos was founded by Markos Moulitsas in 2002, and as of September 2014, the site had an average weekday traffic of hundreds of thousands of visits. 
The file dailykos (CSV file) contains data on 3,430 news articles or blogs that have been posted on Daily Kos. These articles were posted in 2004, leading up to the United States Presidential Election. The leading candidates were incumbent President George W. Bush (republican) and John Kerry (democratic). Foreign policy was a dominant topic of the election, specifically, the 2003 invasion of Iraq. 
Each of the variables in the dataset is a word that has appeared in at least 50 different articles (1,545 words in total). The set of  words has been trimmed according to some of the techniques covered in the previous week on text analytics (punctuation has been removed, and stop words have been removed). For each document, the variable values are the number of times that word appeared in the document. 

### Questions
-  Build a hierarchical clustering model with euclidean as distance measure and ward as clustering criterion. R users can use ward.D2. Plot a dendrogram to show the model.
-  Split the Data into 7 clusters based on the above model and show the distribution(number of observations) of each cluster
-  Which clusters have the most, least and median number of observations? Assist your answers with data.
-  Identify the most important words in the clusters found for the previous question. Importance is nothing but mean frequency values of each words in a given cluster
-  Identify 6 most important words in each cluster.
-  Which cluster could best be described as the cluster related to the Iraq war? Support the answer with data
-  In 2004, one of the candidates for the Democratic nomination for the President of the United States was Howard Dean, John Kerry was the candidate who won the democratic nomination, and John Edwards with the running mate of John Kerry (the Vice President nominee). Given this information, which cluster best corresponds to the democratic party. Support the answer with data

## K-Prototype Exercise

### Context
This study has the donor database of the Blood Transfusion Service Center in Hsin-Chu City in Taiwan. The center passes their blood transfusion service bus to one university in Hsin-Chu City to gather blood donated about every three months. There are 748 donor observations, each one included R (Recency - months since last donation), F (Frequency - total number of donation), M (Monetary - total blood donated in c.c.), T (Time - months since first donation), and a binary variable representing whether he/she donated blood in March 2007 (Yes stand for donating blood; No stands for not donating blood). Data is available here Blood Transfusion

### Questions
Use K-Prototype to profile the donors based on the data given. Try to identify the optimal K and support the profiling with data. Submit the answers as a Notebook with proper explanation.



## DBSCAN Exercise
### Data
1 Run a K means algorithm on the dataset circles.csv  and decide the number of clusters.
2: Now run DB Scan on the dataset ‘circles.csv’. Interpret the results. How is this different from K Means? What are the shortcomings and advantages in the two algorithms? Also ,how did you determine the number of clusters in DBSCAN?


## LOF Exercise
### Data
1:The dataset LOF contains two columns. Ignoring the 1st row as header, run a K means algorithm to find out the clusters present in this.

2:Now try running LOF and figuring out the data points that can be labelled as outliers present in this.



## Factor Analysis Exercise
### Data
25 personality self report items taken from the International Personality Item Pool (ipip.ori.org) were included as part of the Synthetic Aperture Personality Assessment (SAPA) web based personality assessment project. The data from 2800 subjects are included here as a demonstration set for scale construction, factor analysis, and Item Response Theory analysis. Three additional demographic variables (sex, education, and age) are also included.
 
### Format
A data frame with 2800 observations on the following 28 variables. (The q numbers are the SAPA item numbers).
A1: Am indifferent to the feelings of others.
A2: Inquire about others' well-being.
A3: Know how to comfort others.
A4: Love children.
A5: Make people feel at ease.
C1: Am exacting in my work. (q_124)
C2: Continue until everything is perfect. (q_530)
C3: Do things according to a plan. (q_619)
C4: Do things in a half-way manner. (q_626)
C5: Waste my time. (q_1949)
E1: Don't talk a lot. (q_712)
E2: Find it difficult to approach others. (q_901)
E3: Know how to captivate people. (q_1205)
E4: Make friends easily. (q_1410)
E5: Take charge. (q_1768)
N1: Get angry easily. (q_952)
N2: Get irritated easily. (q_974)
N3: Have frequent mood swings. (q_1099
N4: Often feel blue. (q_1479)
N5: Panic easily. (q_1505)
O1: Am full of ideas. (q_128)
O2: Avoid difficult reading material.(q_316)
O3: Carry the conversation to a higher level. (q_492)
O4: Spend time reflecting on things. (q_1738)
O5: Will not probe deeply into a subject. (q_1964)
Gender: Males = 1, Females =2
Education:1 = HS, 2 = finished HS, 3 = some college, 4 = college graduate 5 = graduate degree
Age: age in years

### Question1:
Pre-Process the data and check for all assumptions of the factor analysis.
Also mention those assumptions.     	

### Question2:
 Check the “factorability” of the data. Factorability means "can we find the factors in the dataset?" (check for some statistics test online)

### Question3:
Perform the factor analysis, on the data and select the appropriate number of factors. Justify why you used those factors.

### Question4:
 Determine which variables are important for which factors?


