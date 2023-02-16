def find_similar_movie(description):
    # Read in the movies.txt file and split into individual descriptions
    with open("movies.txt", "r") as file:
        movies = file.read().splitlines()

    # Calculate similarity scores between input description and each movie description
    scores = []
    for movie in movies:
        score = 0
        for word in description.split():
            if word in movie:
                score += 1
        scores.append(score)

    # Return title of the most similar movie
    index = scores.index(max(scores))
    return movies[index].split(" :")[0]

# Example usage:
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("You should watch:", similar_movie)
