##*args and **kwargs

Please write a program using Class.
class addition:
    def my_sum(self,*integers):
        res=int(0)
        for x in integers:
            res=res+int(x)
        return res
obj=addition()
result=obj.my_sum(1,2,3,4,5,6)
print(result)


##***************************
class sentence:
    def concatenate(self,**kwargs):
        result = ""
        # Iterating over the Python kwargs dictionary
        for arg in kwargs.values():
            result += arg
        return result
obj=sentence()
res=obj.concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!")
print(res)
