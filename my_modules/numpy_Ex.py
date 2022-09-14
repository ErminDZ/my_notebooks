def table_ex():
    import numpy as np
    a = np.arange(10, 30).reshape(4, 5)

    red = a[0, 1:4]
    yellow = a[0,0]
    lightBlue = a[:,1::2]
    green = a[0:3,2]
    darkBlue = a[0:-1:2, 4]

    print('red: ',red, '\nyellow: ',yellow, '\nlightBlue: ',lightBlue, '\ngreen: ',green, '\ndarkBlue: ',darkBlue)

def cube_ex():  
    import numpy as np
    a = np.arange(0, 27).reshape((3, 3, 3))# = (z, y, x)

    first = a[1,1,:]
    second = a[:,1,0]
    third = a[0,:,2]

    print('first: ',first, '\nsecond: ',second, '\nthird: ',third)
    
    
def masking_ex():    
    import numpy as np
    data = np.arange(1,101).reshape(10,10)

    evenNumbers = data[data%2==0]

    print('evenNumbers: ',evenNumbers)
        
def german_children():
    import numpy as np
    filename = './my_data/befkbhalderstatkode.csv'

    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df

    mask = (dd[:,0] == 2015) & (dd[:,2] == 0) & (dd[:,3] == 5180)
    data = np.sum(dd[mask][:,4])

    print('German children at age 0 in Denmark:', data)
    
    
def takes_4_param():
    import numpy as np
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df 
    