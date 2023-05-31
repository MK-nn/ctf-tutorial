cipher = b"cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
ans = ''

for c in cipher:
    if (c >= ord('a') and c <= ord('a') + 12) or (c >= ord('A') and c <= ord('A') + 12):
        ans += chr(c + 13)
    elif (c >= ord('a') + 13 and c <= ord('z')) or (c >= ord('A') + 13 and c <= ord('Z')):
        ans += chr(c - 13)
    else:
        ans += chr(c)

print(ans)
