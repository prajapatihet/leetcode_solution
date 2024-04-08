class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c0 = 0
        c1 = 0
        for i in range(len(students)):
            if students[i]==0:
                c0+=1
            else:
                c1+=1
                
        for i in range(len(sandwiches)):
            if sandwiches[i]==0:
                if c0>0:
                    c0-=1
                else:
                    return c1
            else:
                if c1>0:
                    c1-=1
                else:
                    return c0
        return 0
        