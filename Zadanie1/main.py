def hanoi(n , source, destination, auxiliary):
    if n==1:
        print(f"{source} -> {destination}")
        return
    hanoi(n-1, source, auxiliary, destination)
    print(f"{source} -> {destination}")
    hanoi(n-1, auxiliary, destination, source)
          
hanoi(10,'A','B','C') 