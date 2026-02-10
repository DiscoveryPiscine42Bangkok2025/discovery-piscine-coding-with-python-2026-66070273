def play_with_arrays():
    original = [2, 8, 9, 48, 8, 22, -12, 2]

    transformed = [x + 2 for x in original]
    
    unique_transformed = set(transformed)
    
    print(original)
    print(unique_transformed)

if __name__ == "__main__":
    play_with_arrays()