## 01 Class exercise slicing dataframe
def slicing_dataframe1():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    print("1. Create a DataFrame (wrap the data above in a pandas DataFrame in a way that printing the dataframe and its index and column attributes gives this result)")
    
    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
    
    pd.DataFrame(data)
    data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    print(data)
    print('\n')
    print(data.index)
    print(data.columns)
    
#________________________________________________________________________________________________    
    
def slicing_dataframe2a():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("1. second column using column name")
    
    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
    
    pd.DataFrame(data)
    data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    
    print(data["Col2"])
    
#________________________________________________________________________________________________ 
    
def slicing_dataframe2b():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("2. third column using column index (.iloc[])")
    
    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
    
    pd.DataFrame(data)
    data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    
    print(data.iloc[:,2])
    
#________________________________________________________________________________________________ 
    
def slicing_dataframe2c():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("3. slice element at third row of second column (use .iloc())")
    
    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
    
    pd.DataFrame(data)
    data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    
    print(data.iloc[2,1])
    
#________________________________________________________________________________
## 02 Exercise Pandas Data Series
def panda_data_series1a():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("1. Create a Pandas Series with emission data from 2014 for each country or region")
    
    
#___________________________________________________________________________________
## 03 Exercise pandas dataframe
def panda_dataframe1a():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    dates = pd.date_range('20200602', periods=6) # create 6 dates from september 2nd, 2020.
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # use np.random.randn to generate a dataframe of 6 by 4 random numbers

    print(df.describe())
    print('\n')
    print("1. Mean, Min, Max values for all 4 columns")
    print("mean for A: ", df["A"].mean())
    print("min for A: ", df["A"].min())
    print("max for A: ", df["A"].max())
    print('\n')
    print("mean for B: ", df["B"].mean())
    print("min for B: ", df["B"].min())
    print("max for B: ", df["B"].max())
    print('\n')
    print("mean for C: ", df["C"].mean())
    print("min for C: ", df["C"].min())
    print("max for C: ", df["C"].max())
    print('\n')
    print("mean for D: ", df["D"].mean())
    print("min for D: ", df["D"].min())
    print("max for D: ", df["D"].max())
    
#________________________________________________________________________________________________ 

def panda_dataframe1b():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    dates = pd.date_range('20200602', periods=6) # create 6 dates from september 2nd, 2020.
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # use np.random.randn to generate a dataframe of 6 by 4 random numbers
    
    print("2. The 2 dates with the largest and smallest sum (by column)")
    
    print(dates)
    
#________________________________________________________________________________________________ 
    
def panda_dataframe1c():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    dates = pd.date_range('20200602', periods=6) # create 6 dates from september 2nd, 2020.
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # use np.random.randn to generate a dataframe of 6 by 4 random numbers    
    
    print("3. All dates where both A's and B's are positive")