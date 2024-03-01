import math
from asyncio.windows_events import NULL
class AssignmentWeek2:
    def threesquares(m):
        if m<=0 or math.modf(m)[0]>0 or math.modf(m)[1]<=0:
            return False
        # Legendre's theorem - If m can be written in the form 4^a(8b+7) then it can not be expressed as a sum of three squares
        while m%4==0:
            m=m/4
        if m%8==7:
            return False
        return True

    def repfree(s):
        if s is not NULL and len(s)>0:
            print(set(s))
            print(len(set(s)))
            if(len(s)>len(set(s))):
                return False
        else:
            return False
        return True
    
    def hillvalley (l):
        trend= []
        if len(l) in {0,1,2}:
            return False
        for a in range(1, len(l)):
            if l[a] >= l[a-1] and (len(trend)==0 or trend[-1]!='up'):
                trend.append('up')
            if l[a] <= l[a-1] and (len(trend)==0 or trend[-1]!='down'):
                trend.append('down')
        if len(trend) >2 or len(trend) ==1:
            return False
        if len(trend) ==2 and (trend[-1]=='up' or trend[-1]=='down'):
            return True
        return False 
