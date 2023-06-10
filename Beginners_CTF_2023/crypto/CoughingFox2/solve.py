import math

cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293,
          38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

flag = [""] * len(cipher)

for c in cipher:
    for i in range(len(cipher)):
        tmp_i = 0
        while math.sqrt(c - tmp_i) % 1 != 0:
            tmp_i += 1
        flag[tmp_i] = int(math.sqrt(c - tmp_i) - tmp_i)

ans = [""] * (len(cipher) + 1)
for i in range(len(cipher)):
    if i == 0:
      ans[i] = chr(99)
      ans[i+1] = chr(flag[i]-99)
    if i == 1:
       ans[i+1] = chr(flag[i] - ord(ans[i]) + 1)
    else:
      ans[i+1] = chr(flag[i] - ord(ans[i]) + i)

print("".join(ans))
