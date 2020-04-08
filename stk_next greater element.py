def CreateStack():
    stack=[]
    return stack
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def push(stack,data):
    stack.append(data)
def pop(stack):
    if(isEmpty(stack)):
        print("stack underflow")
    else:
        return stack.pop()                
def Next_Greater_Element(arr):
    element=0
    stack=CreateStack()
    next=0
    push(stack,arr[0])
    for i in range(1,len(arr),1):
        next=arr[i]
        if not isEmpty(stack):
            element=pop(stack)
            while(element<next):
                print(str(element)+"-->"+str(next))
                if isEmpty(stack):
                    break
                element=pop(stack)
            if (element>next):
                push(stack,element)
        push(stack,next)
    while(isEmpty(stack)==False):
        element=pop(stack)
        print(str(element)+"-->"+str(-1))
   
if __name__=="__main__":
    array=[10,9,11,13,2]
    Next_Greater_Element(array)

        



