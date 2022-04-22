#!/usr/bin/env python
# coding: utf-8

# Q.1.In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# *
# 
# 'hello'
# 
# -87.8
# 
# -
# 
# /
# 
# +
# 
# 6

# In[11]:


# Answer  (1.)
#      * ------------- expression
#       'hello' ------------ value(string)
#       -87.8 -------------value(float)
#        -    ---------------expression
#        /    ---------------expression
#        +      ---------------expression
#         6   ----------------- value(integer)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q.2 What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[26]:


'''
Answer (2.)
  A variable is something that holds a value or infromation that may change. In simple words variables are symbols 
  that we can use to store data in a program .
  Where as a string is a type of information that can be stored in a variable. A string is usually words,
  enclose with " string "

'''


# In[ ]:





# In[ ]:


Q.3  Describe different data types.


# In[31]:


'''
Answer(3.).
    The different types of data types are as follows :
        a) Integer type  (e.g :  4,  8,  -34 etc)
        b) Floating point type (e.g :  -78.35 , 0.0 , 4.356 etc)
        c) String type (e.g : "Hello Python")
        d) Boolean type (e.g. : true , false)
'''


# In[ ]:





# In[ ]:


Q.4. What is an expression made up of? What do all expressions do


# In[30]:


'''
Answer(4).
  An expression is a combination of operators and operands that is interpreted to produce
   some other value.
 
   Types of expressions are as follows :
 
    a) Constant Expression - Having only constant values only.
 
    b) Arithematic Expression - An arithmetic expression is a combination of numeric values,
      operators, and sometimes parenthesis. The result of this type of expression is also a numeric value.
      some operators used in this expression are 
      +      x + y       Addition
      –      x – y      Subtraction
      *       x * y       Multiplication
      /       x / y        Division
      //      x // y      Quotient
      %      x % y       Remainder
      **      x ** y      Exponentiation
      
      c) Integral Expressions: These are the kind of expressions that produce only integer results after all computations and type conversions.
    
      d) Floating Expressions: These are the kind of expressions which produce floating point numbers as result after all computations and type conversions.
      
      e) Relational Expressions: In these types of expressions, arithmetic expressions are written on both sides of relational operator (> , < , >= , <=). 
          Those arithmetic expressions are evaluated first, and then compared as per relational operator and produce a boolean output in the end.
          
      f) Logical Expressions: These are kinds of expressions that result in either True or False. Some logical operators are OR, AND,NOT etc
'''


# In[ ]:





# Q.5 . This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# In[34]:


'''
Answer(5.) 
    Anything that evaluates to something is an expression, while on the other hand , anything that does something is a statement.
    Expressions always returns a value but statements never returns a value. Expressions can print the result value unlike statement. 
    Examples of expressions are "sudh" + "tan" , 4+7 etc
    
    Examples of statements are assignment statements, conditional branching , loops ,
    classes , import, def , try , except , pass , del etc.
    
    
    In the given question spam = 10 is an assignment statement.
    '''


# In[ ]:





# Q.6. After running the following code, what does the variable bacon contain? 
# 
#     bacon = 22
# 
#     bacon + 1

# In[35]:


#Answer (6.)
bacon = 22
bacon +1


# In[ ]:





# Q.7. What should the values of the following two terms be? 
# 
#     'spam' + 'spamspam'
#     
#     'spam' * 3

# In[36]:


'spam' + 'spam'


# In[37]:


'spam' * 3


# In[ ]:





# 8. Why is eggs a valid variable name while 100 is invalid?

# In[40]:


'''
Answer(8.)
    A variable name can consist of alphabets (upper case, lower case), numbers (0-9), and _ (underscore) character.
    But the name of any variable must not start with a number. Any number is a constant value so it can not be used as a variable.
'''


# In[ ]:





# Q.9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[42]:


'''
Answer(9.)
    For integer -  int     
    For floating point number -  float        
    For string    -  str         
'''


# In[ ]:





# Q.10. Why does this expression cause an error? How can you fix it?
# 
# 'I have eaten ' + 99 + ' burritos.'

# In[43]:


'I have eaten ' + 99 + ' burritos.'


# In[44]:


'''
Answer(10.)
    We are getting the error because concatenation operation can be done only with the same types of data.
    We can not conctenate string with integer or vice- versa. This issue can be fixed by type casting.
'''


# In[45]:


'I have eaten ' + str(99 )+ ' burritos.'


# In[ ]:




