import sympy
D = open("input.txt").read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])

S = []
for line in L:
  pos, vel = line.split('@')
  x,y,z = pos.split(', ')
  vx,vy,vz = vel.split(', ')
  x,y,z = int(x),int(y),int(z)
  vx,vy,vz = int(vx),int(vy),int(vz)
  S.append((x,y,z,vx,vy,vz))

n = len(S)
ans = 0
for i in range(len(S)):
  for j in range(i+1, len(S)):
    x1 = S[i][0]
    x2 = S[i][0]+S[i][3]
    x3 = S[j][0]
    x4 = S[j][0]+S[j][3]
    y1 = S[i][1]
    y2 = S[i][1]+S[i][4]
    y3 = S[j][1]
    y4 = S[j][1]+S[j][4]

    den = ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    if den != 0:
      px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
      py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
      validA = (px>x1)==(x2>x1)
      validB = (px>x3)==(x4>x3)

      if 200000000000000<=px<=400000000000000 and 200000000000000<=py<=400000000000000 and validA and validB:
        ans += 1
print(ans)


hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open("input.txt")]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break
    
answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])
print(i)