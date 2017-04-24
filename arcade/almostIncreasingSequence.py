# is possible to make a sequence strictly increasing removing only one value?

def almostIncreasingSequence(sequence):
    j = first_wrong(sequence)
    if j == -1:
        return True # all increasing
    if first_wrong(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True # all increasing if remove index j
    if first_wrong(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True # all increasing if remove index j+1
    return False # more than one change was needed, so False

# find the index of first ocurrence of sequence[i]>=sequence[i+1]
def first_wrong(sequence):
    for i in range(len(sequence)-1):
        if not sequence[i] < sequence[i+1]:
            return i
    return -1
