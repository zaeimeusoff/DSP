from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

from program import dataset

product_descriptions = dataset['about_product'].dropna()

vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(product_descriptions)
X = X1

kmeans = KMeans(n_clusters=10, init='k-means++')
y_kmeans = kmeans.fit_predict(X)

def print_cluster(i):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()

true_k = 10

model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X1)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print_cluster(i)


def show_recommendations(product, num_recommendations=20):
    Y = vectorizer.transform([product])
    prediction = model.predict(Y)
    cluster = prediction[0]

    print(f"Products in Cluster {cluster}:")
    cluster_indices = [idx for idx, lbl in enumerate(model.labels_) if lbl == cluster]
    recommended_products = dataset.iloc[cluster_indices][:num_recommendations]

    recommendations_df = recommended_products[['product_id', 'product_name', 'about_product']].copy()
    recommendations_df.columns = ['Product ID', 'Product Name', 'Product Description']
    recommendations_df.index = range(1, len(recommended_products) + 1)
    return recommendations_df