def electionsWinners(votes, k):
    if k !=0:
        return len([v+k for v in votes if v + k> max(votes)])
    else:
        return 1 if votes.count(max(votes))==1 else 0

# def electionsWinners(votes, k):
#     if k !=0:
#         return len([ i+k for i in votes if i + k> max(votes)])
#     else:
#         m= max(votes)
#         votes.remove(m)
#         return 1 if m > max(votes) else 0
print electionsWinners([5, 1, 3, 4, 1],0)
print electionsWinners([1, 1, 1, 1],1)
print electionsWinners([2, 3, 5, 2],3)
print electionsWinners([5, 4, 1, 2, 3],0)
print electionsWinners([1, 3, 3, 1, 1],0)
print electionsWinners([1, 1, 1, 1],0)
print electionsWinners([3, 1, 1, 3, 1],2)
