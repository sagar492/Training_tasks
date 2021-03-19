a=['''ImageAsset: Uri=/system_ex/apps/appdb/default/icon0.png?ts=315532800+336_336_KeepFitSize_Bc7U, Width=336, Height=336 Format=Bc7U''']
b=['''ImageAsset: Uri=/system_ex/apps/appdb/default/icon1.png?ts=315532800+336_336_KeepFitSize_Bc7U, Width=340, Height=356 Format=Bc7U''']
## type 1

l=['image','Width','Height']
d=dict.fromkeys(l)
a1=a[0]
s=a1.split('?')
s2=s[0].split('/')
a2=s[1].split(' ')
for i in s2:
    if i.endswith('.png'):
        d['image']=i
for i in a2:
    if i.startswith("Width"):
        d['Width']=i.split('=')[1]
    elif i.startswith('Height'):
        d['Height']=i.split('=')[1]
        
print(d)
        


#type 2


input__1 = '''ImageAsset: Uri=/system_ex/apps/appdb/default/icon0.png?ts=315532800+336_336_KeepFitSize_Bc7U, Width=336, Height=336 Format=Bc7U'''
input__2 = '''ImageAsset: Uri=/system_ex/apps/appdb/default/icon1.png?ts=315532800+336_336_KeepFitSize_Bc7U, Width=340, Height=356 Format=Bc7U'''
list_needed = ['Image', 'Width', 'Height']
class Exploring:
    
    def __init__(self,input_,required_list,string_1):
        self.input_ = input_
        self.required_list = required_list
        self.string_1 = (input_.split('/'))[-1]
    
    def operation(self,dict_1):
        for i in self.required_list:
            if i =='Image':
                dict_1[i] = (self.string_1.split('?'))[0]
            elif i == 'Width':
                dict_1[i] = ((self.string_1.split(','))[1].split('='))[1]
            elif i == 'Height':
                dict_1[i] = ((self.string_1.split(','))[2].split('='))[1][:3]
        return dict_1

Exploring_object = Exploring(input__2,list_needed,'')
 
print(Exploring_object.operation({}))
