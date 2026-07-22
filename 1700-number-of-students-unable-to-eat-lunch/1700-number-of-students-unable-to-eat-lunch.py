class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
            one=sum(students)
            zero=len(students)-one
            for s in sandwiches:
                if s==0 and zero>0:
                    zero-=1
                elif s==1 and one>0:
                    one-=1
                else:
                    break
            return one+zero