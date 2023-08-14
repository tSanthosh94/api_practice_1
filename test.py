# "url->>,view> related  class/function--Business logic-->> query set>>response to renser>"

# # url="app1/user_info/, get_user_info.asview()"

# ## From django app urls

# # app1-urls.py

# # class get_user_info(View):
# #     def get(self, requset,file_id):
# #         requset.GET()
# #         orm_query= vales()

# #         return render(status, "show_csv_.html", locals())
    
    
# #     def postt(self, requset):
# #         pass
# #         return Response(status, data)
    

# # show_csv_.html:

# #     <table>
# #         header
# #         row
# #     <\table>



# # n=1234
# # y=0
# # while n>0:
# #     y=(n%10)+y*10
# #     n=n//10
# # print(f'final reversed num {y}')


# # a=[1,2,1,3,4,9,6,7,4]
# # new_list=[]
# # for idx,i in enumerate(a):
# #     if  i not in new_list:
# #             new_list.append(i)

# # print(new_list)

# a=[1,10,2,9,6,4,5,11]
# x=15
# list_pairs=[]

# for i in a:
#     for j in a:
#         if i+j == x and all([True if i not in ele and j not in ele else False for ele in list_pairs ]):
#             list_pairs.append((i,j))

# print(list_pairs)



# a = [1, 10, 2, 9, 6, 4, 5, 11]
# x = 15
# list_pairs = set()

# for i in a:
#     j = x - i
#     if j in a and (j, i) not in list_pairs:
#         list_pairs.add((i, j))

# print(list_pairs)


# # database=
# # file_path=" santhosh\file1.csv"

# # <button 1 id= "file_1">

# # onclick(
# #     {
# #         href=" url = app1/show_info/<int.1>"

# #     }
# # )




# class Sample:
#     def __init__(self,li) -> None:
#         self.li=li
#     def __str__(self) -> str:
#         print("Checkinggg")
#         return '6666'
#     def method1(self,a):
#         self.li.append(a)
#         print(self.li)
#     def method2(self):
#         print('Hello2')

# x= Sample([])
# x.method1(5)
# print(x.li)


# from enum import Enum

# class Color:
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color.RED)  # Output: Color.RED
# # print(Color.RED.value)  # Output: 1


a=[10,1,6,2,21,3,9,5]
n=len(a)
x=0
for i in range(n-1):
    temp=i
    for j in range(i+1,n):
        x+=1
        if a[j]<a[temp]:
            temp=j
    a[i],a[j]=a[j],a[i]

print(a,x)
        





