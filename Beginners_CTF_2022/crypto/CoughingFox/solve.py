import math

cipher = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649,
          15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

ans = []
for i in range(len(cipher)):
    ans.append(0)

for i in range(len(cipher)):
    tmp_i = 0
    while math.sqrt(cipher[i] - tmp_i) % 1 != 0:
        tmp_i += 1
    ans[tmp_i] = math.sqrt(cipher[i] - tmp_i) - tmp_i

solve = ""

for i in range(len(ans)):
    solve += chr(int(ans[i]))

print(solve)