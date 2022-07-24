try:
    f = open('myfile.txt','w')
    f.write("hello boy")
    
except IOError:
    print("error: could not find file or read data!")
finally:
    print("success")
    f.close()