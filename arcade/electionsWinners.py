# passed all tests
def electionsWinners(votes,k):
    # using variables to avoid repeating functions
    s=sorted(votes)
    m=s[-1]

    # no one more to vote and 2 or more draw
    if k==0 and s[-1]==s[-2]:
        return 0
    # no more votes one bigger
    elif k==0 and s[-1]!=s[-2]:
        return 1

    else:
        # looping all the list was causing time limit
        # so stop looping when reach first v+k <= m
        c=0
        for v in reversed(s):
            # incressing if is bigger
            if v+k>m:
                c+=1
            # return c when reach the lessers
            else:
                return c
        # every one can win
        return c

# works but time limit
# def electionsWinners1(votes, k):
#     if k !=0:
#         return len([v+k for v in votes if v + k> max(votes)])
#     else:
#         return 1 if votes.count(max(votes))==1 else 0

#works but time limit
# def electionsWinners2(votes, k):
    # a = k == 0
    # b = votes if a else [v+k for v in votes if v+k>max(votes)]
    # c = b.count(max(b))
    # d = c if (c==1 and a) else len(b)
    # return 0 if (c>1 and a) else d

# works but time limit
# def electionsWinners3(votes, k):
    # if k !=0:
    #     return len([ i+k for i in votes if i + k> max(votes)])
    # else:
    #     m= max(votes)
    #     votes.remove(m)
    #     return 1 if m > max(votes) else 0

# works but time limit
# def electionsWinners(votes,k):
    # if k == 0:
    #     return 0 if votes.count(max(votes))>1 else 1
    # else:
    #     possible_candidates = 0
    #     for i in range (len(votes)):
    #         count = 0
    #         for j in range (len(votes)):
    #             if votes[i]+k>votes[j]:
    #                 count+=1
    #         print "c",count
    #         if count == len(votes):
    #             possible_candidates+=1
    #         print "p",possible_candidates
    #     return possible_candidates
    #
# works but time limit
# def electionsWinners(votes,k):
    # m=max(votes)
    # if k==0:
    #     return 0 if votes.count(m)>1 else 1
    # else:
    #     return len(votes) if k>=m else sum([v+k>m for v in votes])

# works but time limit
# def electionsWinners(votes,k):
#     s=sorted(votes)
#     m=s[-1]
#     if k==0 and s[-1]==s[-2]:
#         return 0
#     elif k==0 and s[-1]!=s[-2]:
#         return 1
#     else:
#         return len(votes) if k>=m else sum([v+k>m for v in votes])


print electionsWinners([5, 1, 3, 4, 1],0)
print electionsWinners([1, 1, 1, 1],1)
print electionsWinners([2, 3, 5, 2],3)
print electionsWinners([5, 4, 1, 2, 3],0)
print electionsWinners([1, 3, 3, 1, 1],0)
print electionsWinners([1, 1, 1, 1],0)
print electionsWinners([3, 1, 1, 3, 1],2)
