jobs=[(2,100),(1,19),(2,27),(3,15)]
jobs.sort(key = lambda x:x[1], reverse=True)
max_deadline=max(job[0] for job in jobs)
result=[-1]*max_deadline
for job in jobs:
    deadline,profit=job
    for i in range(deadline-1,-1,-1):
        if result[i]==-1:
            result[i]=profit
            break

total_profit=sum(result)
print("job seq:",result)
print("total profit:",total_profit)
