import math

cipher = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649,
          15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

ans_list = []
for i in range(len(cipher)):
    ans_list.append(0)

for j in range(len(cipher)):
    tmp_j = 0
    while math.sqrt(cipher[j] - tmp_j) % 1 != 0:
        tmp_j += 1
    ans_list[tmp_j] = math.sqrt(cipher[j] - tmp_j) - tmp_j

ans = ""
for k in range(len(ans_list)):
    ans += chr(int(ans_list[k]))

print(ans)
