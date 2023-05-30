cipher = 'fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}'
ans = ''

for i in cipher:
    if i != "{" and i != "_" and i != "}":
        ans += chr(ord(i)-3)
    else:
        ans += i

print(ans)
