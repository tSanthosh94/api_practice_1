# arr=[10,9,1,13,6,8,4]
# n=len(arr)

# for i in range(n):
#     min=i
#     for j in range(0,n-i-1):
#         if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
   

# # for i in range(n):
# #     min_idx = i
# #     for j in range(i + 1, n):
# #         if arr[j] < arr[min_idx]:
# #             min_idx = j
# #     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# print(arr)

# import multiprocessing
# import time

# def square_numbers(numbers, result):
#     for num in numbers:
#         result.append(num * num)
#         time.sleep(1)

# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#     result = []

#     # Create a process pool with 2 processes
#     processes = []
#     for _ in range(2):
#         process = multiprocessing.Process(target=square_numbers, args=(numbers, result))
#         processes.append(process)
#         process.start()

#     # Wait for all processes to finish
#     for process in processes:
#         process.join()

#     print("Multiprocessing example is done!")
#     print("Result:", result)




# import daten

###To check the invalid recotds from the table
# q1=list(type_01_query_set=cust_cust_table.objects.filter( cust_type=1,).values('cus_id',flat=True))
# # type_01_query_set=cust_cust_table.objects.filter( cust_type=1,).values('cus_id','cust_type','from','to','rec_id').order_by('cust_id','cust_type') ## Silver
# type_02_query_set=cust_cust_table.objects.filter( cust_type=2,cust_id__in=(type_01_query_set=cust_cust_table.objects.filter( cust_type=1,).values('cus_id','cust_type','from','to','rec_id').order_by('cust_id','cust_type') ).exclude(## Silver
# ).values('cus_id','cust_type','from','to','rec_id').order_by('cust_id','cust_type') ## Gold

# invalid_records=[]
# for type_1,type_2 in zip(type_01_query_set,type_02_query_set):
#     if type_1  and type_2  and type_1.to < type_2.from and : ### (mar,feb) 

#         invalid_records.append(type_1,type_2)
#     else:



class Sample:
    def __init__(self,name,age):
        name= self.name
        age=self.age

    def check(self):
        print('Hello world')



x=Sample("Santhosh",26)
print(x.check())

# y=Sample("Santhosh",26)
# print(y.check())



# Expectation:  Hello world
                # hello india


def outer_func(func):
    def inner_func():
        print("Hello india")
        return func()
    return inner_func

@outer_func
def check():
    print('Hello world')
# print(check())
# print(outer_func(check()))

def sample2():
    print('Hello world')



print("++++++++++++++")
print(check())
print(sample2())


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

class LanguageStudent():
    def __init__(self,language_list):
        self.language_list=language_list
    def add_language(self,lanuage):
        # print('test')
        self.language_list=self.language_list.append(lanuage)

class LanguageTeacher(LanguageStudent):
    def __init__(self):
        super().__init__([])
    def teach(self,student,lanuage):
        if lanuage in language_list:
            print('added stufdent lanugages')
            return True
        else:
            return False

teacher=LanguageTeacher()
teacher.add_language('english')

student=LanguageStudent()
teacher.teach(student,'english')

print(student.language_list)
 




        


    


















