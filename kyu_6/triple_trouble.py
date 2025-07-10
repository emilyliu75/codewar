def triple_double(num1, num2):
    num_1 = [n for n in str(num1)]
    num_2 = [n for n in str(num2)]
    num_2_duplicates = [num_2[idx] for idx in range(0, len(num_2)-1) if num_2[idx] == num_2[idx + 1]]
    num_1_tri = [num_1[idx] for idx in range(0, len(num_1) - 2) if num_1[idx] == num_1[idx+1] and num_1[idx] == num_1[idx+2]]
    if any(num in num_1_tri for num in num_2_duplicates):
        return 1
    else:
        return 0