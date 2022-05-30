#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests 


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import requests 


# In[5]:


url="https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail="


# In[6]:


allow=requests.get(url)


# In[7]:


print(allow)


# In[8]:


soup=BeautifulSoup(allow.text)


# In[9]:


product_name = soup.select(".product-title")


# In[10]:


print(product_name)


# In[11]:


product_titles = []
product_links = []


# In[12]:


for item in product_name:
    product_titles.append(item.text)
    link= "https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy" 
    product_links.append(link)


# In[13]:


product_links


# In[14]:


product_titles


# In[15]:


shoes_name=[]


# In[16]:


import pandas as pd


# In[17]:


shoe = pd.DataFrame(product_titles,columns=["Movies"])


# In[18]:


shoe 


# In[19]:


shoe.to_csv("shoe.csv")


# In[ ]:




