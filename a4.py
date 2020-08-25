#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"


# In[2]:


kb = []
C = []
while True:
    print("kb>",end ='')
    command = input() or "empty"
    command_list = command.split()
    ## valid command: load, tell, infer_all, and stop
    if(command_list[0]=="load"):
        if(len(command_list)==1 or len(command_list)>2):
            print("Error: load needs only one someKB.txt")
        else:
            valid_kb = True
            try:
                text = open(command_list[1])
            except FileNotFoundError:
                print("Error:", command_list[1] ,"is not a valid knowledge base")
                valid_kb = False
            if valid_kb == True:
                lines = text.read().splitlines()
                c = len(lines)
                d = 0
                for i in range(c):
                    if '<--' not in lines[i] :
                        print("Error:", command_list[1] ,"is not a valid knowledge base")
                        valid_kb = False
                        break
                    #remove item that exists in kb already
                    if(lines[i] in kb):
                        kb.remove(lines[i])
                        d +=1
                        
                if valid_kb == True:
                    for i in range(c):
                        kb.append(lines[i])
                        print(lines[i])
                    print()
                    print(c-d, "new rule(s) added") 
            else:
                continue
            text.close()
    elif(command_list[0]=="tell"):
        if len(command_list)==1:
            print("Error: tell needs at least one atom")
        else:
            valid_atom = True
            command_list.remove("tell")
            for item in command_list:
                if(is_atom(item)==False):
                    valid_atom = False
                    print("Error: \""+item+"\" is not a valid atom")
                    break
            if valid_atom == True:
                for item in command_list:
                    if item in C:
                        print("atom \""+item+"\" already known to be true")
                    else:
                        C.append(item)
                        print("\"" +item+"\" added to KB")
    elif(command_list[0]=="infer_all"):
        if len(C)==0:
            print("Newly inferred atoms:")
            print("\t<none>")
            print("Atoms already known to be true:")
            print("\t<none>")
        else:
            k = len(kb)
            c = len(C)
            if(k==0):
                print("Newly inferred atoms:")
                print("\t<none>")
                print("Atoms already known to be true:")
                print("\t",', '.join(map(str, C)))
            else:
                limit = range(k*k)
                new_atom = []
                temp_kb = kb
                C_temp = C
                update = False
                for i in limit:
                    kk = len(temp_kb)
                    if(kk==0):
                        break
                    elif(i > k and update==False):
                        break
                    elif(i > len(new_atom)*k*2 and update == True):
                        break
                    else:
                        if kk==1:
                            rule =temp_kb[0]
                        else:
                            rule = temp_kb[i%kk-1]
                        rule = rule.split()
                        r = rule[0]
                        if r in C_temp and kk==1:
                            del temp_kb[0]
                        elif r in C_temp:
                            del temp_kb[i%kk-1]
                        else:
                            rule.remove(r)
                            rule.remove('<--')
                            while True:
                                if "&" in rule:
                                    rule.remove("&")
                                else:
                                    break
                            counter = 0
                            for item in rule:
                                if item not in C_temp:
                                    break
                                else:
                                    counter +=1
                            if counter==len(rule):
                                new_atom.append(r)
                                C_temp = new_atom + C_temp
                                update = True
                                if kk==1:
                                    del temp_kb[0]
                                else:
                                    del temp_kb[i%kk-1]

                if(len(new_atom)==0):
                    print("Newly inferred atoms:")
                    print("\t<none>")
                else:
                    print("Newly inferred atoms:")
                    print("\t",' '.join(map(str, new_atom)))
                print("Atoms already known to be true:")
                print("\t",', '.join(map(str, C)))
                C = C_temp
    elif(command_list[0]=="stop"):
        break
    else:
        print("Error: unknown command \""+command+"\"")
    print()
        
        

