#!/usr/bin/env python
# coding: utf-8

# In[1]:


roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',20:'XX', 30:'XXX', 40:'XL' ,50: 'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'}


# In[2]:


num = int(input('Enter the number here :-   '))


# In[3]:


if num < 1000:
    s_num = str(num)
    num_1 = s_num[0] + '00'
    num_2 = s_num[1] + '0'
    num_3 = s_num[2]
    
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_3 = int(num_3)
    
    print(roman[num_1] + roman[num_2] + roman[num_3])
else:
    print(roman[1000])

