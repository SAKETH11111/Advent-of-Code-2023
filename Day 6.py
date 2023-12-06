D = open("input.txt").read().strip()
L = D.split('\n')
ans = 0 

#print(L)

t,d = L
times = [int(x) for x in t.split(':')[1].split()]
dist = [int(x) for x in d.split(':')[1].split()]

#print(t)
#print(d)
#print(times)
#print(dist)
T = ''
for t in times:
  T += str(t)
T = int(T)
#print(T)
D = ''
for d in dist:
  D += str(d)
D = int(D)
#print(D)
def f(t, d):
  ans = 0
  for x in range(t+1):
    dx = x*(t-x)
    #print(dx)
    if dx>=d:
      ans += 1
  return ans

ans = 1
for i in range(len(times)):
  ans *= f(times[i], dist[i])
print("---Part 1---")
print(ans)
print("---Part 2---")
print(f(T,D))
