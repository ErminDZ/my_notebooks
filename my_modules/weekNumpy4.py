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
    
    a = np.array([51937,75113,78802,61623,51727,39537,43908,53604,55204,64967,3872])
    a.sort()
    
    plt.bar(list(set(dd[:,1])), (list(a)))
    plt.axis([1,10,3000,80000])
    
    
def boolean_mask_above65():
    import matplotlib.pyplot as plt
    import numpy as np
    
    filename = './my_data/befkbhalderstatkode.csv'
    
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    dd = bef_stats_df
    
    print('5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015?\n')
    
    mask_positiv = (dd[:,0] == 2015) &  (dd[:,3] == 5100) & (dd[:,2] >= 65)
    data = np.sum(dd[mask_positiv][:,4])
    
    mask_negativ = (dd[:,0] == 2015) &  (dd[:,3] == 5100) & (dd[:,2] < 65)
    data1 = np.sum(dd[mask_negativ][:,4])
    
    print(data)
    print(data1)
    
    xs = np.linspace(0, 2 * np.pi, 50)
    ys = np.sin(xs)
    plt.plot(xs, ys)
    
    mask_positive = ys >= 0                        # condition for the blue crosses
    plt.plot(xs[mask_positive], ys[mask_positive], 'bx')    # rendering the blue plots only with filtered values
    mask_negative = (ys < 0)                       # condition for the green dots
    plt.plot(xs[mask_negative], ys[mask_negative], 'go')    # condition applied to xs and ys data sets
    plt.show()