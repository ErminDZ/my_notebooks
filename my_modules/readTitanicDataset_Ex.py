def test():
    import pandas as pd
    data = pd.read_csv('./my_data/titanic_train.csv')
    #print('her: ', data)
    
    new_data = pd.DataFrame(data)
    #print('her : ', new_data)
    
    df_new_data = new_data.set_index('PassengerId')
    #print('Her :',df_new_data)
    
    df_new_data = new_data.sort_values('Fare', ascending = False)
    #print('Her : ',df_new_data)
    
    