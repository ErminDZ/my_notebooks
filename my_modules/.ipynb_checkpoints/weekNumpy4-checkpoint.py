def lived_in_each_areas():
    import numpy as np
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df 
    
    neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

    print('3. Find out how many people lived in each of the 11 areas in 2015?')
    
    indreby_mask = (dd[:,0] == 2015) & (dd[:,1] == 1)
    print('\nIndre By: ',np.sum(dd[indreby_mask][:,4]))
    
    østerbro_mask = (dd[:,0] == 2015) & (dd[:,1] == 2)
    print('Østerbro: ',np.sum(dd[østerbro_mask][:,4]))
    
    nørrebro_mask = (dd[:,0] == 2015) & (dd[:,1] == 3)
    print('Nørrebro: ',np.sum(dd[nørrebro_mask][:,4]))
    
    vesterbro_kgs_enghave_mask = (dd[:,0] == 2015) & (dd[:,1] == 4)
    print('Vesterbro/kgs_enghave: ',np.sum(dd[vesterbro_kgs_enghave_mask][:,4]))
    
    valby_mask = (dd[:,0] == 2015) & (dd[:,1] == 5)
    print('valby: ',np.sum(dd[valby_mask][:,4]))
    
    vanløse_mask = (dd[:,0] == 2015) & (dd[:,1] == 6)
    print('vanløse: ',np.sum(dd[vanløse_mask][:,4]))
    
    brønshøj_husum_mask = (dd[:,0] == 2015) & (dd[:,1] == 7)
    print('brønshøj-husum: ',np.sum(dd[brønshøj_husum_mask][:,4]))
    
    bispebjerg_mask = (dd[:,0] == 2015) & (dd[:,1] == 8)
    print('bispebjerg: ',np.sum(dd[bispebjerg_mask][:,4]))
    
    amager_øst_mask = (dd[:,0] == 2015) & (dd[:,1] == 9)
    print('amager_øst: ',np.sum(dd[amager_øst_mask][:,4]))
    
    amager_vest_mask = (dd[:,0] == 2015) & (dd[:,1] == 10)
    print('amager_vest: ',np.sum(dd[amager_vest_mask][:,4]))
    
    udenfor_mask = (dd[:,0] == 2015) & (dd[:,1] == 99)
    print('udenfor: ',np.sum(dd[udenfor_mask][:,4])) 
    
#______________________________________________________________________________________________________________
    
def bar_plot_city():
    import matplotlib.pyplot as plt
    import numpy as np
    
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df 
    
    neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}
    
    print('4. Make a bar plot to show the size of each city area from the smallest to the largest in 2015?\n')
    
    #udenfor_mask = (dd[:,0] == 2015) & (dd[:,1])
    #print('udenfor: ',np.sum(dd[udenfor_mask][:,4])) 
    #udenfor_mask_sorted = udenfor_mask.sort()
    
    a = np.array([51937,75113,78802,61623,51727,39537,43908,53604,55204,64967,3872])
    a.sort()
    
    plt.bar(list(set(dd[:,1])), (list(a)))
    plt.axis([1,10,3000,80000])

 #_____________________________________________________________________________________________________________
    
def boolean_mask_above65():
    import matplotlib.pyplot as plt
    import numpy as np
    
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df
    
    print('5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015?\n')
    
    over_65_mask = (dd[:,0] == 2015) &  (dd[:,3] == 5100) & (dd[:,2] > 65)
    data = np.sum(dd[over_65_mask][:,4])
    
    under_65_mask = (dd[:,0] == 2015) &  (dd[:,3] == 5100) & (dd[:,2] < 65)
    data1 = np.sum(dd[under_65_mask][:,4])
    
    print('how many people above 65 years lived in Copenhagen: ', data)
    print('how many people under 65 years lived in Copenhagen: ',data1)
  
 #_____________________________________________________________________________________________________________
    
def other_nordic_countries():
    import numpy as np

    filename = './my_data/befkbhalderstatkode.csv'
    country_codes = {5110: 'Norge', 5120: 'Sverige',5104: 'Finland',5106: 'Island',5101: 'Grønland'}
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df
    
    print('6. How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"?\n ')
    
    data = dd
    nordic_countries = ["Norge","Sverige","Finland","Island","Grønland"] 
    old_nords = 0 
    for x,y in country_codes.items(): 
        if y in nordic_countries: 
            #print(x) 
            print(y) 
            mask = (data[:,0] == 2015) & (data[:,2] > 65) & (data[:,3] == x) 
            country_sum = (dd[mask][0:,4].sum()) 
            print(country_sum)
            old_nords += country_sum
    print("Nordiske beboere over 65 år: ",old_nords) 

    # control the sum by slicing a different way
    control = dd[np.isin(dd[:,3],[5101,5104,5106,5110,5120])]
    control = control[(control[:,0] == 2015) & (control[:,2]>65)]
    control[:,4].sum()
    
 #_____________________________________________________________________________________________________________
    
def line_plot():
    import matplotlib.pyplot as plt
    import numpy as np
    
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df
    
    print("7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015?\n")
    
    østerbro_mask = (dd[:,0] == 2015) & (dd[:,1] == 2)
    print('Østerbro: ',np.sum(dd[østerbro_mask][:,4]))
    
    vesterbro_kgs_enghave_mask = (dd[:,0] == 2015) & (dd[:,1] == 4)
    print('Vesterbro/kgs_enghave: ',np.sum(dd[vesterbro_kgs_enghave_mask][:,4]))
    
    test_mask = (dd[:,1] == 2) & (dd[:,3] == 5100) 

    x = (dd[:,0])
    y = (dd[:,0]) & np.sum((dd[test_mask])[:,4]) 

    plt.title("Mennesker i Østerbro pr. år")
    plt.xlabel("Årstal")
    plt.ylabel("Antal Mennesker")
    plt.plot(x,y,color = "red")
    plt.show