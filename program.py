import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

datasetbefore = pd.read_csv("C:/Users/zaeim/Desktop/1/SEM 5/WIH3001 DATA SCIENCE PROJECT/Project/dataset/amazon.csv")
dataset = pd.read_csv("C:/Users/zaeim/Desktop/1/SEM 5/WIH3001 DATA SCIENCE PROJECT/Project/dataset/amazon(cleaned).csv")
history = pd.read_csv("C:/Users/zaeim/Desktop/1/SEM 5/WIH3001 DATA SCIENCE PROJECT/Project/dataset/purchasehistory.csv")
