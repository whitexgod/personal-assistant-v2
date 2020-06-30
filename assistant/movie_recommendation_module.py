from speak_module import speak
from input_module import take_command,take_input
from output_module import output

def movie_recommendation():

    import pickle
    import pandas as pd
    import numpy as np
    from sklearn.neighbors import NearestNeighbors
    from fuzzywuzzy import process

    movie_features_df=pickle.load(open('movie_features_df_remake.pkl','rb'))
    movie_names=pickle.load(open('movie_names_remake.pkl','rb'))


    def get_matches(query, choices, limit=5):
        results = process.extract(query, choices, limit=limit)
        return results


    output("Please enter the movie name:\n")
    text=take_input()
    movie_list=get_matches(text, movie_names)
    new_list=[]
    for i in range (5):
        if movie_list[i][1]>=90:
            new_list.append(movie_list[i])
    movie_nam=[]
    for i in range (len(new_list)):
        movie_nam.append(str(new_list[i][0]))
    d={'movie':movie_nam}
    data=pd.DataFrame(d)
    data.drop_duplicates(inplace=True)
    output('Please wait Sir while i am thinking for recommendations.')
    from scipy.sparse import csr_matrix
    movie_features_df_matrix = csr_matrix(movie_features_df.values)

    from sklearn.neighbors import NearestNeighbors
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(movie_features_df_matrix)

    rec_mov=[]
    try:
        query_index = np.where(movie_features_df.index==data['movie'].iloc[0])[0][0]
        distances, indices = model_knn.kneighbors(movie_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 10)
        for i in range(10):
            rec_mov.append(movie_features_df.index[indices.flatten()[i]])
        d={'recommended_movies':rec_mov}
        df=pd.DataFrame(d)
        df=df.head(6)
        output("The recommendations for you are -")
        print(df['recommended_movies'].tolist())
        speak(df['recommended_movies'].tolist())

    except:
        print("Sorry please try something else")
        output("Sorry please try something else")

