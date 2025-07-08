# recommender.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = {
    'title': ['Batman', 'Superman', 'Spiderman', 'Ironman', 'Hulk'],
    'genre': ['Action Adventure', 'Action Sci-Fi', 'Adventure', 'Action', 'Sci-Fi']
}
df = pd.DataFrame(data)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])

similarity = cosine_similarity(count_matrix)

def recommend(movie_title):
    index = df[df['title'] == movie_title].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_distances = sorted(distances, reverse=True, key=lambda x: x[1])[1:]
    for i in sorted_distances[:3]:
        print(df.iloc[i[0]]['title'])

recommend('Hulk')
