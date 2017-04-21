def almostIncreasingSequence(sequence):
    j = first_wrong(sequence)
    if j == -1:
        return True
    if first_wrong(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if first_wrong(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False

def first_wrong(sequence):
    for i in range(len(sequence)-1):
        if not sequence[i] < sequence[i+1]:
            return i
    return -1
