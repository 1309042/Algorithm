def solution(arr1, arr2):
    return_val = []
    
    for i in range(len(arr1)):
        temp = []
        
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        return_val.append(temp)
            
    return return_val