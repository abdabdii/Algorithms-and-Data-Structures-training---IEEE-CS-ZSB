numberOfContests = input().lstrip().rstrip()
contests = input().lstrip().rstrip()
contestsList = list(map(int, contests.split()))
record = {max:None,min:None}
amazing = 0
for idx,contest in enumerate(contestsList):
    if idx == 0:
        record[max] = contest
        record[min] = contest
    else:
        if contest > record[max]:
            record[max] = contest
            amazing +=1
        elif contest < record[min]:
            record[min] = contest
            amazing += 1
        
print(amazing)