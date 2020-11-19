#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Load CSv file into memory

# In[5]:


data= pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[43]:


#data.head() #means first 5#


# In[9]:


#data.tail() #means last 5#


# # Convert datetime and add some useful columns

# In[15]:


dt = ('4/30/2014 23:22:00')
dt = pandas.to_datetime(dt) #converting the string into this datetime format for better use#


# In[6]:


data ['Date/Time'] = data["Date/Time"].map(pandas.to_datetime)


# In[22]:





# In[8]:


def get_dom(DT):
    return DT.day
data['dom']=data['Date/Time'].map(get_dom) 

def get_weekday(DT):
    return DT.weekday()
data['Weekday']=data['Date/Time'].map(get_weekday)

def get_hour(DT):
    return DT.hour
data['hour']=data['Date/Time'].map(get_hour)

#data.drop(['Date of Month'], axis=1, inplace=True) #delete a column by its name#


# In[70]:


#DT = data['Date/Time'][454410]
#DT.day


# In[72]:


#get_dom(DT) this will return (because of the code above) the date of month that the record 454410 for example is in.


# In[9]:


data.tail()


# 
# # Analysis
# # Analyse the Date of Month

# In[10]:


hist(data.dom, bins=30, rwidth=0.8, range=(0.5,30.5))
xlabel("Date of Month")
ylabel('Frequency')
title('Frequency by dom - uber- apr 14')


# In[29]:


for k, rows in data.groupby('dom'):
       print((k,len(rows)))#len counts how many records there are for example for day 1#


# In[30]:


def count_rows(rows):
    return len(rows)
by_date=data.groupby('dom').apply(count_rows)


# In[31]:


by_date #panda way of doing the same as before.


# In[34]:


bar(range(1,31),by_date)


# In[35]:


by_date_sorted=by_date.sort_values()
by_date_sorted


# In[38]:


bar(range(1,31),by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('date of month')
ylabel("frequency")
title('Frequency by dom - uber - Apr 2014')
("")


# # # Analyse the hour

# In[42]:


hist(data.hour, bins=24, range=(0,24))
("")


# # analyse the weekday

# In[46]:


hist(data.Weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='red')
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
("")


# # cross analysis (hour,dow)

# In[53]:


by_cross=data.groupby('Weekday hour'.split()).apply(count_rows).unstack()


# In[54]:


seaborn.heatmap(by_cross)


# # by latitude and longitude

# In[14]:


hist(data['Lat'], bins=100, range=(40.5,41))
("")


# In[17]:


hist(data['Lon'], bins=100, range=(-74.1,-73.9))
("")


# In[24]:


hist(data['Lat'], bins=100, range=(40.5,41),color='red',alpha=.5, label='Latitute')
legend(loc='upper left')
twiny()
hist(data['Lon'], bins=100, range=(-74.1,-73.9),color='green',alpha=.5, label='Longitude')
legend(loc='best')
("")


# In[37]:


figure(figsize=(20,20))
plot(data['Lon'],data['Lat'],'.', ms=1, alpha=.5)
xlim(-74.2,-73.7)
ylim(40.7,41) #we will see Manhattan


# In[ ]:




