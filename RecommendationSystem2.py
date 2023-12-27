import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def get_purchase_history(dataset, history, user_id):
    # Get the purchase history for the user from the 'history' dataset
    user_history = history[history['user_id'] == user_id]

    # Extract product IDs from user's purchase history
    product_ids = user_history['product_id'].tolist()

    # Use the 'dataset' dataset to retrieve product information based on product IDs
    user_purchase_history = dataset[dataset['product_id'].isin(product_ids)]

    return user_purchase_history


def recommend_products(dataset, history, user_id):
    # Use TfidfVectorizer to transform the product descriptions into numerical feature vectors
    tfidf = TfidfVectorizer(stop_words='english')
    dataset['about_product'] = dataset['about_product'].fillna('')  # fill NaN values with empty string
    tfidf_matrix = tfidf.fit_transform(dataset['about_product'])

    # Get the purchase history for the user
    user_history = history[history['user_id'] == user_id]

    # Get the indices of purchased products
    indices = user_history.index.tolist()

    if indices:
        # Create a new similarity matrix with only the rows and columns for the purchased products
        cosine_sim_user = cosine_similarity(tfidf_matrix[indices], tfidf_matrix)

        # Create a pandas Series with product indices as the index and product names as the values
        products = dataset.iloc[indices]['product_name']
        indices = pd.Series(products.index, index=products)

        # Get the indices and similarity scores of products similar to the ones the user has already purchased
        similarity_scores = list(enumerate(cosine_sim_user[-1]))
        similarity_scores = [(i, score) for (i, score) in similarity_scores if i not in indices]

        # Sort the similarity scores in descending order
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top 20 most similar products
        top_100_products = [i[0] for i in similarity_scores[:100]]

        # Remove duplicates from the top 100 products
        unique_products = []
        unique_scores = []
        for i in top_100_products:
            if i not in unique_products:
                unique_products.append(i)
                unique_scores.append(similarity_scores[i][1])

        # Sort the unique similarity scores in descending order and get the top 20
        top_20_indices = sorted(range(len(unique_scores)), key=lambda i: unique_scores[i], reverse=True)[:20]

        # Get the indices of the top 20 unique products
        top_20_unique_products = [unique_products[i] for i in top_20_indices]

        # Get the names of the top 20 unique products
        recommended_products = dataset.iloc[top_20_unique_products]['product_name'].tolist()
        recommended_products_id = dataset.iloc[top_20_unique_products]['product_id'].tolist()

        # Get the reasons for the recommendation
        score = [unique_scores[i] for i in top_20_indices]

        # Create a DataFrame with the results
        results_df = pd.DataFrame({'Product ID': recommended_products_id,
                                   'Product Name': recommended_products,
                                   'Recommendation Score': score
                                   })

        results_df.index = range(1, len(recommended_products) + 1)
        print(results_df)

        return results_df

    else:
        print("No purchase history found.")
        return None
