if __name__ == '__main__':
    Data = []
    second_lowest_names = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Data.append([name, score])
        scores.add(score)
        
    second_lowest = sorted(scores)[1]
        
    for name, score in Data:
        if score == second_lowest:
            second_lowest_names.append(name)

    for name in sorted(second_lowest_names):
        print(name, end='\n')
        