# A = [ 3,33,333,4,45,6,667,31  ]
# opt = [ [3,33,333,31], [4,45], [6,667] ]

# final_dict={}
# for ele in A:
#     for j in A:

#         if str(j).startswith(str(ele)[0]) :
#             if not final_dict.get(str(ele)[0]):
#                 final_dict[str(ele)[0]]=[j]
#             elif final_dict.get(str(ele)[0]) and j not in final_dict[str(ele)[0]] :

#                 final_dict[str(ele)[0]].append(j)


# print(list(final_dict.values()))



# A = "{[[[((}]]])"  # gates closed
# closed_gates=['}',']',')']
# open_gates=['{','[','(']

# new_list=[]

# gates_dict={
#     '}':'{',
#     ']':'[',
#     ')':'('   }

# for idx,char in enumerate(A):
#     if char in open_gates:
#         new_list.append(char)
#     elif char in closed_gates and new_list.pop()!=gates_dict[char]:
#         print(char,idx)
        

# A = [5,5,5,5,7,7,6,6,6,6,8,1,1]
# B = [6,1,8,5]
# opt = [6,6,6,6,1,1,8,5,5,5,5 ]

# final_list=[]

# x=sorted(A,key =lambda y:B.index(y),reverse=False)
# # def sort_func(x):
# #     pass

# # for i in B:
# #     for j in A:
# #         if i == j :
# #             final_list.append(j)

# print(x)




# class Sample1():
#     static_variable=20
#     @staticmethod
#     def func1(a,b):
#         x= a+b+Sample1.static_variable
#         return x
    

# # x=Sample1()
# y=Sample1.func1(2,5)
# print(y)


# # Method overloading
# class MathOperations:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# math_ops = MathOperations()
# print(math_ops.add(2, 3))       # Output: Error, the second add() method overloads the first
# print(math_ops.add(2, 3, 4))    # Output: 9, uses the second add() method


print(dd := 43)











