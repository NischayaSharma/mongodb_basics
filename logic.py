import collections
following=[1,2,3,4]
subFollowing=[[2,3,9,10,15,28],[9,23,16,47,39],[4,9,37,58,28,69],[1,2,3,5,45,9,78,19]]
subsFinal = []
for sub in subFollowing:
    subsFinal.append(list(set(sub) - set(following)))
freqDic = dict(collections.Counter([x for sublist in subsFinal for x in sublist]))
print(freqDic)