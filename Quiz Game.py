#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(" Welcome to my Computer quiz!")


# In[ ]:


playing = input("Do you want to play? ")


# In[ ]:


if playing != "yes":
    quit()


# In[ ]:


print " Okay lets play :) "
score = 0


# In[ ]:


answer = input(" What does CPU Stand for? ")

if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


# In[ ]:


answer = input(" What does GPU Stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


# In[ ]:


answer = input(" What does RAM Stand for? ")

if answer.lower() == "rondom access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    


# In[ ]:


answer = input(" What does PSU Stand for? ")

if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


# In[ ]:


print("You got " + str(score) + "questions correct!")


# In[ ]:


print("You got " + str((score /4) * 100) + "%.")

