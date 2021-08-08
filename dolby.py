# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6

    text = {}
    unique = set()

    frequency = {}

    for i in range(65, 91):
        frequency[chr(i)] = 0

    for i in range(97, 123):
        frequency[chr(i)] = 0

    for i in range(len(S)):
        if S[i].isupper():
            if S[i].lower() in S:
                text[S[i]] = S[i].lower()

            else:
                unique.add(S[i])
        else:
            if S[i].upper() in S:
                text[S[i].upper()] = S[i]
            else:
                unique.add(S[i].upper())
    
    if len(text) == 0:
        return -1

    start = 0
    end = 0
    m = -1
    finalEnd = None
    finalStart = None

    while start < len(S):
        if S[start] in unique:

            while end < start:
                frequency[S[end]] = frequency[S[end]] -1
                end += 1
            start += 1
            end = start

        else:
            frequency[S[start]] = frequency[S[start]] -1

            while True:
                if frequency[S[end]] > 1:
                   frequency[S[end]] = frequency[S[end]] -1
                   end += 1
                else:
                    break

            flag = True

            for key, value in text.items():

                if frequency[key] != 0 and frequency[value] == 0:
                    flag = False
                elif frequency[key] == 0 and frequency[value] != 0:
                    flag = False
    
            if flag:
                if m > (start - end + 1):
                    m = start - end + 1
                    finalStart = end
                    finalEnd = start

            start += 1

    if finalEnd is None and finalStart is None:
         return -1

    else:
        return S[finalStart: finalEnd+1] 
