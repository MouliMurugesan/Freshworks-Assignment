import json
#Function to create or insert the key and value into file 
def create(key,value):
    dic=dict()
    dic[key]=value
    data={}
    with open('file.json', 'r') as f:
        data= json.load(f)
    if key in data:
        print("Error: The key is already exists")
    else:
        with open('temp.json', 'w') as f:
            json.dump(dic, f)
        temp1=dict(data)
        with open('temp.json', 'r') as f:
            temp2=json.load(f)
            temp1.update(temp2)
        with open('file.json', 'w') as f:
            json.dump(temp1,f)
    return 1;
#Function to read the value of the given key
def read(key):
    data={}
    with open('file.json', 'r') as f:
        data= json.load(f)
    if key in data.keys():
        print(f"The Value of key {key} is {data[key]}")
    else:
        print("Error:The key is not exist")
    return 1
#Funtion to delete the key and value
def delete(key):
    data={}
    with open('file.json', 'r') as f:
        data= json.load(f)
    if key in data.keys():
        del data[key]
        with open('file.json', 'w') as f:
            json.dump(data,f)
    else:
        print("Error:The key is not exist")
    return 1
while(True):
    op=input("For create enter 1 For Read enter 2 For Delete enter 3 For exit 0 ")
    if op=="1":
        fcheck=input("Is this first  operation ? yes/no ")
        key=input("Enter the key ")
        value=input("Enter the value")
        dic=dict()
        dic[key]=value
        if fcheck.lower()=="yes":
            with open('file.json', 'w') as f:
                json.dump(dic, f)
        else:
            create(key,value)
    elif op=="2":
        key=input("Enter the key that you want to read")
        read(key)
    elif op=="3":
        key=input("Enter the key that you want to delete")
        delete(key)
    elif op=="0":
        exit()
    else:
        print("invalid Option")
    data={}
    with open('file.json', 'r') as f:
        data= json.load(f)
    print("The data that currently present in the file")
    print(data)
    
