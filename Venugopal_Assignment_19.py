def histogram():
    hist = {}
    for ch in s:
        if ch in hist:
            hist[ch]+=1
        else:
            hist[ch]=1

    for key in sorted(hist.keys()):
        print(f"Letter {key}  appears  {hist[key]}  time/s")
    print()


T=int(input())
for i in range(T):
    s=input().strip()
    histogram()

