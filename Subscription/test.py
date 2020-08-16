def exam(v):
    score = v.copy()
    for i,n in enumerate(v):
        score[i] = 1 if n == 1 else -1
    my_score = [0]
    his_score = [0]
    for s in score:
        my_score = my_score + [s+my_score[-1]]
    for s in reversed(score):
        his_score = [s+his_score[0]] + his_score
    # for i in range(len(my))
    print(my_score)
    print(his_score)

exam([1,0,0,1,0])
