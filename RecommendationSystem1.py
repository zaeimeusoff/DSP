import numpy as np
import pandas as pd

from program import dataset

# Group by 'main_category', then sort within each group and extract top 3 items
top_3_per_category = dataset.groupby('main_category').apply(lambda x: x.nlargest(3, 'rating_weight')).reset_index(drop=True)

# Get the maximum 'rating_weight' from items not in the top_3_per_category
max_rating = dataset[~dataset.index.isin(top_3_per_category.index)].max()

# Find a product that matches this maximum 'rating_weight' and is not in top_3_per_category
additional_item = dataset[
    (dataset['rating_weight'] == max_rating['rating_weight']) &
    (~dataset.index.isin(top_3_per_category.index))
].head(1)

# Concatenate the additional item with the top items per category
final_top_items = pd.concat([top_3_per_category, additional_item])
final_top_items.index = np.arange(1, len(final_top_items) + 1)
