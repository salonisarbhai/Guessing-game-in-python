class TreeNode:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key


class BinaryTree:
    def __init__(self,key):
        self.root = None
        
    def begin(self,t,b):
        ch = ""
        ch1 = ""
        ch2 = ""

        if t != None:
            print("\t\t\t")
            print(t.data)
            '''
            input syntax is not ----> input(var1,var2)
            it is
            var_name1 = input()
            var_name2 = input()
            check kar leh i think there is input syntax error somewhere
            make the change according to your functionality of the code.
            '''
            ch = input()
            if ch == "N" or ch == "n":
                if t.right != None:
                    if t.right.left == None and t.right.right == None:
                        print("\t\t\t")
                        print("Is it" + t.right.data+"?") 
                        ch1=input()
                        if ch1 == "Y" or ch1 == "y":
                            self.win()
                        else:
                            self.lose(t,t.right,b)
                    else:
                        self.begin(t.right,b)
                else:
                    self.lose(t.right,t,b)
            else:
                if t.left != None:
                    if t.left.left != None:
                        self.begin(t.left,b)    #### CHECK THIS ERROR> YOU ARE CALLING A FUNCTION WITH
                    else:                     #### WITH 2 PARAMETER ARGUMENTS BUT SENDING ONLY ONE
                        print("\t\t\t")
                        print("Is it" + t.left.data + "?")
                        if ch2 == "Y" or ch2 == "y":
                            self.win()
                        else:
                            self.lose(t,t.left,b)
                else:
                    self.lose(t.left, t,b)
        else:
            self.lose(t,t,b)

    def win(self):
        ch = ""
        print("\t\t\t")
        print("I win")
        print("\t\t\t")
        print("Play Again [Y/N]")
        ch = input()
        if ch == 'y' or ch == 'Y':
                print("\n")
                self.begin(self.t,self.b)
        else:
                print("\n\t\t\t\t\t\t\t\t")
                print("*********Thank you for playing************")

    def lose(self,t,t2,b):
        question = ""
        answer = ""
        ch = ''
        ch2 = ''
        onenode=TreeNode("KeyVal1")
        twonode=TreeNode("KeyVal2")
        
        if b.root == None:
            print("\n\t\t")
            print("*********I KNOW NOTHING YET*********")
            print("\n\t\t")
            print("Think and give me a person, place or thing")
            answer=input()
        else:
            print("\t\t\t\t")
            print("I give up")
            print("\t\t\t")
            answer= input()
            print("What is it? Please tell me\n")
            answer= input()
            
        if t != None:
            print("\n\t\t")
            print("I need a question to distinguish")
            print(answer)
            print("from a/an")
            print(t2.data)
            print(".")
        elif b.root != None:
                print("\n\t\t")
                if t2.left != None:
                    if t2.left.left == None:
                        print("I need a question to distinguish")
                        print(answer)
                        print("from a\an")
                        print(t2.data)
        else:
            print("\n\t\t")
            print("I need a question for me to know what that is")
        print("\n\t\t")
        print("Enter the question")
        question = input()
        print("\n\t\t")
        print("If answer is were "+ answer + " the answer would be ?")
        ch = input()
        
        if t != None:
            onenode.data = question
            if ch == 'Y' or ch == 'y' :
                onenode.right = t2
                onenode.left = twonode
            else:
                onenode.left = t2
                onenode.right = twonode
            t2 = onenode
            twonode.data = answer
            twonode.right = twonode.left = None
        else:
            t = onenode
            onenode.data = question
            if ch=='Y'or ch == 'y':
                onenode.right = None
                onenode.left = twonode
            else:
                onenode.left = None
                onenode.right = twonode
            twonode.data = answer
            twonode.left = twonode.right = None
        if self.root == None:
            root = t
        print("\t\t\t")
        print("Play Again? y/n")
        ch2 = input()
        if ch2 == 'Y' or ch2 == 'y':
            self.begin(root,self.b)   ## NEED TO SEND TWO ARGUMENTS>>>>>>
        else:
            print("\n\t\t")
            print("********Thank you for playing*************")


    def instructions(self):
        print("***********Hello and welcome to the guessing game****************")
        print("INSTRUCTIONS\n")
        print("1. THINK OF A WORD")
        self.b=BinaryTree("Key1")
        self.t=TreeNode("Key2")
        self.begin(self.t,self.b)





            
        
                     
                     
                     
         
         
     
     
    
         
        


