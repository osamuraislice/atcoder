# https://atcoder.jp/contests/abc198/submissions/21631021
from itertools import permutations
 
S=[input() for i in range(3)]
for i in range(3):S[i]=list(reversed(S[i]))
for i in range(3):S[i]=list(map(ord,S[i]))
 
chars=set(S[0]+S[1]+S[2])
if len(chars)>10:
	print("UNSOLVABLE")
	exit()
 
inv=[0]*256
for i,c in enumerate(chars):
	inv[c]=i
 
for i in range(3):
	for j in range(len(S[i])):
		S[i][j]=inv[S[i][j]]
 
for perm in permutations(list(range(10)),len(chars)):
	if perm[S[0][-1]]==0 or perm[S[1][-1]]==0 or perm[S[2][-1]]==0:
		continue
	temp=[0,0,0]
	for i in range(3):
		for j,c in enumerate(S[i]):
			temp[i]+=perm[S[i][j]]*10**j
	if temp[0]+temp[1]==temp[2]:
		print(*temp)
		exit()
 
print("UNSOLVABLE")