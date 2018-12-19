import sys
import numpy as np


def levenshtein_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    distance_array = np.zeros((m+1, n+1))
	
    for i in range(m+1):
        distance_array[i, 0] = i
		
    for j in range(n+1):
        distance_array[0, j] = j

    for j in range(n):
        for i in range(0, m):
            if word1[i] == word2[j]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            distance_array[i+1, j+1] = min(
                distance_array[i, j+1] + 1,
                distance_array[i+1, j] + 1,            
                distance_array[i, j] + substitution_cost
	    )
     
    return distance_array[-1, -1]


def spell_correction(data, k):
    train_set = ['sitting', 'meeting', 'kitchen', 
				 'friend', 'meat']
    distances = np.array([])
    suggested_word = []
 
    for train_data in train_set:
        distances = np.hstack((distances, 
            np.array([
            levenshtein_distance(train_data, data)
           ])
        ))
        
    indexes = distances.argsort()
    nearest = indexes[:k]
	
    if min(distances) == 0:
        return suggested_word
		
    for i in nearest:
        suggested_word.append(train_set[i])
		
    return suggested_word
	

if __name__ == '__main__':
    out = spell_correction(sys.argv[1], 3)
    print(out)


