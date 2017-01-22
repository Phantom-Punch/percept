#!/usr/bin/env python3
def iterations(iter):
    data1 = [7, 2, 4, 6, 3, 9, 2, 5]
    data2 = [8, 1, 12, 6, 1, 4, 2, 9]
    sol = [0, 1, 1, 1, 1, 1, 0, 0]
    weight = [0, 0, 0, 0, 0, 0] 
    eta = 0.1
    ans = [0, 0, 0, 0, 0, 0, 0, 0]
    for n in range(iter+1):
        for i in range(len(sol)):
            ans[i] =  weight[0] + weight[1]*data1[i] + weight[2]*data2[i] + weight[3]*(data1[i]**2) + weight[4]*(data2[i]**2) + weight[5]*data1[i]*data2[i]
            if ans[i] < 0:
                ans[i] = 0
            else:
                ans[i] = 1
            weight[0] = weight[0] + eta*(sol[i]-ans[i])
            weight[1] = weight[1] + eta*(sol[i]-ans[i])*data1[i]
            weight[2] = weight[2] + eta*(sol[i]-ans[i])*data2[i]
            weight[3] = weight[3] + eta*(sol[i]-ans[i])*(data1[i]**2)
            weight[4] = weight[4] + eta*(sol[i]-ans[i])*(data2[i]**2)
            weight[5] = weight[5] + eta*(sol[i]-ans[i])*(data1[i]*data2[i])
        print(weight)
iterations(500)
