#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[3]:


2+2


# In[2]:


import os


# In[4]:


# What we can do with OS
print(dir(os))


# In[4]:


# Print Current working directory
os.getcwd()


# In[5]:


# Change Current working directory
os.chdir("C:\\Users\\Sunil")


# In[6]:


# Print Current working directory
os.getcwd()


# In[14]:


# Read File of content from privious directory
f = open('img_2.png')


# In[7]:


# Read File of content directory
f = open('Adversarial Search.pdf')


# In[8]:


# List dawn all file of current working directory.
os.listdir() 


# In[11]:


# See What is inside content
os.listdir('C:\\Users\\Vandana')


# In[12]:


# See What is inside content
os.listdir('D:\SLRTCE\BIL File Submission')


# In[9]:


# Create Folder in current directory
os.mkdir("SUN1")


# In[10]:


os.mkdir("D:\\Os")


# In[17]:


# Create directory within directory
os.makedirs("D:\\SUN1\Sun2")


# In[19]:


# Change Current working directory
os.chdir("D:\\")


# In[21]:


# Rename directory
os.rename("SUN1","Sun1")


# In[36]:


# Check whether Path exist or not
os.path.exists("D:\\SUN1\Sun2")


# In[35]:


# Check whether Path exist or not
os.path.exists("D:\\Sun1\Sun2")


# In[25]:


# Check whether specified thing is file
os.path.isfile("/bin/Sun1")


# In[33]:


os.path.isfile("C:\\Users\Vandana\pie.png")


# In[34]:


# Check whether specified thing is folder
os.path.isdir("D:\\SUN1\Sun2")


# In[30]:


os.path.isdir("C:\\Users\Vandana\pie.png")


# In[3]:


# Set environment variables
os.environ['API_USER'] = 'sunil'
os.environ['API_PASSWORD'] = 'osmod'


# In[10]:


# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')


# In[11]:


USER


# In[12]:


PASSWORD


# In[8]:


os.getenv('API_USER')


# # Environment Variable

# ### What Are Environment Variables?
# Two fundamental components of any computer programming language are variables and constants. Like independent variables in a mathematical equation, these take on values that change the results of the program. Variables and constants both represent unique memory locations containing data the program uses in its calculations. The difference between the two is that variables values may change during execution, while constant values cannot be reassigned.
# An environment variable is a variable whose value is set outside the program, typically through functionality built into the operating system or microservice. An environment variable is made up of a name/value pair, and any number may be created and available for reference at a point in time.

# In[17]:


from os import environ


# In[35]:


# To see all environment variables on your system just call it                
print(os.environ)


# In[22]:


# Access the environment variabnle path
environ.get('path')


# In[23]:


# Access the environment variabnle PROCESOR_LEVEL
environ.get('PROCESSOR_LEVEL')


# In[25]:


# Access the environment variabnle PROCESOR_LEVEL
environ.get('PSModulePath')


# In[6]:


# How to Set Environment Variables in Python
os.environ['USER'] = 'Sun'


# In[7]:


# If you need to clear a single environment variable in the session you can use
os.environ.pop('USER')


# In[8]:


# Check whether USER key enviribment variable are cleared or nor 
os.environ.get('USER')


# In[9]:


# Agaion Set Environment Variables in Python
os.environ['USER'] = 'Sun'
os.environ['USER'] = 'Sun'


# In[10]:


# Acces the environment variable 
os.environ.get('USER')


# In[13]:


# Set another environment variable
os.environ['PASS'] = 'abc'


# In[14]:


# access environment variable PASS
os.environ.get('PASS')


# In[16]:


# if you need to clear all environment variables you can use os.environ.clear()
os.environ.clear()


# In[17]:


# Check whether PASS key enviribment variable are cleared or nor 
os.environ.get('PASS')


# In[18]:


# Check whether PASS key enviribment variable are cleared or nor 
os.environ.get('USER')

Note: It’s important to remember that the settings you apply in a Python script don’t work outside that specific process; os.environ doesn’t overwrite the environment variables system-wide. If you need to permanently delete or set environment variables you will need to do so with a shell environment, such as Bash.
# # Python - Object Serialization
Object serialization is the process of converting state of an object into byte stream. This byte stream can further be stored in any file-like object such as a disk file or memory stream. It can also be transmitted via sockets etc. Deserialization is the process of reconstructing the object from the byte stream.

Python refers to serialization and deserialization by terms pickling and unpickling respectively. The 'pickle' module bundled with Python’s standard library defines functions for serialization (dump() and dumps()) and deserialization (load() and loads()).

The data format of pickle module is very Python specific. Hence, programs not written in Python may not be able to deserialize the encoded (pickled) data properly. In fact it is not considered to be secure to unpickle data from unauthenticated source.
# ## pickle protocols
# Protocols are the conventions used in constructing and deconstructing Python objects to/from binary data. Currently pickle module defines 5 different protocols as listed below:
# 
# * Protocol version 0: Original “human-readable” protocol backwards compatible with earlier versions.
# * Protocol version 1: Old binary format also compatible with earlier versions of Python.
# * Protocol version 2: Introduced in Python 2.3 provides efficient pickling of new-style classes.
# * Protocol version 3: Added in Python 3.0. recommended when compatibility with other Python 3 versions is required.
# * Protocol version 4: was added in Python 3.4. It adds support for very large objects
# * Protocol version 5 was added in Python 3.8. It adds support for out-of-band data and speedup for in-band data. 

# In[11]:


import pickle


# In[12]:


# To know highest and default protocol version of your Python installation use following constants defined in pickle module.
pickle.HIGHEST_PROTOCOL


# In[13]:


pickle.DEFAULT_PROTOCOL

The dump() and load() functions of pickle module respectively perform pickling and unpickling of Python data. The dump() function writes pickled object to a file (or file like object) and load() function unpickles data from file back to Python object.
# In[19]:


# Change Current working directory
os.chdir("D:\\Sun1\\Sun2")


# In[22]:


# Serialise the dictionary object
f = open("pickled.txt","wb")
dct = {"name":"Sun", "age":27, "Gender":"Male", "marks":95}
pickle.dump(dct,f)
print('Pickling Completed...')
f.close()

When above code is executed, the dictionary object’s byte representation will be stored in 'pickled.txt' file. The file must have 'write and binary' mode enabled.

On the other hand load() function unpickles or deserializes data from binary file back to Python dictionary. Run following script
# In[23]:


# Deserialise the dictionary byte stream
f=open("pickled.txt","rb")
d=pickle.load(f)
print('Unpickling the data : ')
print (d)
f.close()

Note that the dictionary object doesn't retain order of insertion of keys. Hence the k-v pairs in retrieved dictionary may not be in original order.The pickle module also consists of dumps() function that pickles Python data to a string representation.
# In[25]:


from pickle import dumps


# In[26]:


dct={"name":"Patel", "age":21, "Gender":"Male","marks":80}
dctstring = dumps(dct)
print("Pickled Byte stream: ")
dctstring

Use loads() function to unpickle the string and obtain original dictionary object
# In[28]:


from pickle import loads


# In[29]:


dct=loads(dctstring)
dct

In addition to above convenience functions, the pickle module also defines Pickler and Unpickler classes. Pickler class has dump() method that writes pickle data to a binary file. Unpickler class reads binary data from file and constructs Python object.
To write Python object’s pickled data
# In[30]:


# To write Python object’s pickled data
from pickle import *
f=open("pickled.txt","wb")
dct={'name': 'Rajneesh', 'age': 23, 'Gender': 'Male', 'marks': 75}
Pickler(f).dump(dct)
f.close()


# In[31]:


# To read back data by unpickling binary file from pickle 
f=open("pickled.txt","rb")
dct=Unpickler(f).load()
print (dct)
f.close()


# Python library also contains 'marshal' module that is used b Python interpreter itself for internal serialization of Python objects.

# ## Modules available for Serialization and Deserialization in Python
Python provides three different modules which allow us to serialize and deserialize objects :  

1) Marshal Module
2) Pickle Module
3) JSON Module
# 1. Marshal Module: It is the oldest module among these three. It is mainly used to read and write the compiled byte code of Python modules. Even we can use marshal to serialize Python objects, but it is not recommended to use. It is mainly used by the interpreter and the official documentation warns that the python maintainers may modify the format in backward-incompatible ways.
# 
# Note: It is recommended to never unmarshal data received from an untrusted or unauthenticated source.  

# In[50]:


# importing the module
import marshal 
 
data = {'name': 'sun','age': 27,'address': 'Mumbai'}
 
bytes = marshal.dumps(data)    # dumps() return byte object stored in variable 'bytes'
print('After serialization : ', bytes)
 
new_data = marshal.loads(bytes)   # loads() convert byte object to value
print('After deserialization : ', new_data)


# 2. Pickle Module: It is another way to serialize and deserialize Python objects. It serializes the Python object in a binary format, due to which it is not human-readable. It is faster and it also works with custom-defined objects. The Python pickle module is a better choice for serialization and deserialization of python objects. If you don’t need a human-readable format or if you need to serialize custom objects then it is recommended to use the pickle module. 
#   

# In[51]:


f = open("pickled.txt","wb")
data = {'name': 'sun','age': 27,'address': 'Mumbai'}
pickle.dump(data,f)
print('Pickling Completed...')
f.close()

f=open("pickled.txt","rb")
d=pickle.load(f)
print('Unpickling the data : ')
print (d)
f.close()


# 3. JSON Module: It is a newly created module. It allows us to work with standard JSON files. JSON is a widely used format for data exchange and it is very convenient. It is human-readable and language-independent, and it’s lighter than XML. Using the JSON module we can serialize and deserialize several standard Python types like bool, dict, int, float, list, string, tuple, none etc. The JSON module and XML are a good choice if we want to interoperability among different languages. 

# In[52]:


# Example: Serializing
import json   

data = {
  "id": "484",
  "name": "Sun",
  "department": "IT"
}
    
json_object = json.dumps(data)   # Serializing json
print(json_object)
print('Serialization Completed.')


# In[53]:


# Example: Deserializing
import json  
students = '{"id":"484", "name": "Sun", "department":"IT"}' # JSON string  
student_dict = json.loads(students) # convert string to Python dict
print(student_dict)   
print(student_dict['name'])
print('Deserialization Completed.')

