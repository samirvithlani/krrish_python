words = ["banana","apple","grape"]

ans = map(lambda word: "".join(map(lambda c: '*'if c   in 'aeiou' else c,word)),words)
print(list(ans))


numbers = [1,4,5]
