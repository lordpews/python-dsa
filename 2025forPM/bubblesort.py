elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]


# for k in range(len(elements)-1):    
#     for i in range(len(elements)-1):
#         print(elements)
#         if elements[i] > elements[i+1]:
#             print("swapping",elements[i],elements[i+1])
#             elements[i],elements[i+1] = elements[i+1],elements[i]
# print(elements)

def bubble_sort(elements,key):
    for i in range(len(elements)-1):
        for j in range(len(elements)-1):
            if elements[j][key] >  elements[j+1][key]:
                elements[j][key],elements[j+1][key] = elements[j+1][key],elements[j][key]
    print(elements)

bubble_sort(elements,key = 'transaction_amount')