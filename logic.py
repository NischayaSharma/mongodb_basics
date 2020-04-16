import collections

# Sample list of users which i am following
following=[1,2,3,4]

# Sample List of users whom the users i follow are following
subFollowing=[[2,3,9,10,15,28],[9,23,16,47,39],[4,9,37,58,28,69],[1,2,3,5,45,9,78,19]]
subsFinal = []

# Making a list of users which my followings are following but not me
for sub in subFollowing:
    subsFinal.append(list(set(sub) - set(following)))

# Making a frequency dictionary like how many times is a user repeated in the subsFinal list
freqDic = dict(collections.Counter([x for sublist in subsFinal for x in sublist]))
print(freqDic)