#!/usr/bin/env python
# coding: utf-8

# In[1]:


val = input("How many times do you want to be complimented?  Max is 5.  ")
complimentbank = ["You're amazing!","You're so smart.","I admire you.", "You work so hard.", "You make my day.","Never tell yourself you're not special!"]


# In[2]:


def compImput(val):
    val = input("\nHow many times do you want to be complimented?  Max is 5.  ")
    compliment(val)


# In[3]:


def compliment(val):
    
    #Data types used: Boolean, int, string

    #Check if entered value is an integer
    try: 
        float(val)
        
        isnumeric= True
        
        floatval = float(val)
        
        if floatval.is_integer():
            checkint = True
            valint = int(val)
            
        if not floatval.is_integer():
            checkint = False
            floatint = True
        
    except ValueError: 
        checkint = False
        isnumeric = floatval.isnumeric()
        
    except TypeError:
        checkint = False
    
    #If it is an integer!!! 
    if checkint:
                
        if valint > 5: 
            print("\nI don't think I have enough energy for", valint, "compliments...")
            compImput(val)
        else:
            valintextra = valint + 1
            print("\nAwesome!  Your chosen amount of compliments is", valint, ".  And I'll give you", valintextra,"just because. :)\n")
            
            for x in range(valintextra):
                print(complimentbank[x])
    
    #User gets sassy and tries non-numeric values
    elif not isnumeric:
        print("\nThat isn't even a number.")
        compImput(val)
    
    #User enters a float
    else: 
        print("\nThat was not an integer. I can't give you fractional compliments.")
        compImput(val)


# In[4]:


compliment(val)

