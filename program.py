import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

datasetbefore = pd.read_csv("amazon.csv")
dataset = pd.read_csv("amazon(cleaned).csv")
history = pd.read_csv("purchasehistory.csv")
