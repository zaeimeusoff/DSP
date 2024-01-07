from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

from program import dataset

# Extract product descriptions and remove null values
product_descriptions = dataset['about_product'].dropna()

# Use TfidfVectorizer to transform the product descriptions into numerical feature vectors
vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(product_descriptions)
X = X1

# Use KMeans clustering algorithm to cluster to 10 clusters
kmeans = KMeans(n_clusters=10, init='k-means++')
y_kmeans = kmeans.fit_predict(X)

# Function to print top terms within each cluster
def print_cluster(i):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()
true_k = 10

# Initialize KMeans model
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
# Fit the model with the TF-IDF transformed data
model.fit(X1)

# Display top terms for each cluster
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()
for i in range(true_k):
    print_cluster(i)

# Function to give 20 products recommendation
def show_recommendations(product, num_recommendations=20):
    Y = vectorizer.transform([product])
    # Predict cluster for the input product
    prediction = model.predict(Y)
    # Get the predicted cluster for the input product
    cluster = prediction[0]

    print(f"Products in Cluster {cluster}:")
    # Find indices of products belonging to the predicted cluster
    cluster_indices = [idx for idx, lbl in enumerate(model.labels_) if lbl == cluster]
    # Retrieve recommended products from the dataset based on cluster
    recommended_products = dataset.iloc[cluster_indices][:num_recommendations]
    
    # Create new df with recommended product details (20)
    recommendations_df = recommended_products[['product_id', 'product_name', 'about_product']].copy()
    recommendations_df.columns = ['Product ID', 'Product Name', 'Product Description']
    recommendations_df.index = range(1, len(recommended_products) + 1)
    return recommendations_df
