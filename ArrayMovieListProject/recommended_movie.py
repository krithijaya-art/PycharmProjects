import array
import numpy as np

'''
The built-in array module is designed for homogeneous numeric data and efficient memory storage. 
It does not support storing multiple strings as elements. 
For string collections, Python lists are preferred, or NumPy arrays if vectorized operations are needed.
'''

action_movies = np.array(["john Wick", "Mad Max", "Gladiator"])
# action_movies = array.array('i', [10, 20, 30])
comedy_movies = ["Superbad", "Step Brothers", "The Hangover"]
trending_movies = ["Oppenheimer", "Barbie", "Dune"]

print("Top Trending Movie:", trending_movies[0])
print("Second Trending Movie:", trending_movies[1])


horror_movies = ["The Conjuring", "It", "A Quiet Place"]
user_recommendations = horror_movies

print("Recommended Horror Movie:", user_recommendations[2])

print(type(action_movies))
