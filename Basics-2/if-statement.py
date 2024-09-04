# Example2
# Sets = avoid duplication of element within itself
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Please enter a movie you watched recently: ")

if user_movie in movies_watched:
    print(f'user_movie entered:\n"{user_movie}"\n\nThis movie is inside movies_watched:\n{movies_watched}')
else:
    print(f'User entered "{user_movie}" which has NOT been watched yet')