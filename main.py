import pandas as pd



def load_data_dict():
    data_dict = {}

    
    ## basic formatting
    data_dict['holidays_events'] = pd.read_csv('data_season/holidays_events.csv')
  
    data_dict['oil'] = pd.read_csv('data_season/oil.csv')
  
    data_dict['stores'] = pd.read_csv('data_season/stores.csv')
  
    data_dict['sample_subs'] = pd.read_csv('data_season/sample_submission.csv')
  
    data_dict['transactions'] = pd.read_csv('data_season/transactions.csv')
    
    data_dict['sales'] = pd.read_csv('data_season/train.csv', parse_dates=['date'])
    data_dict['sales'] = data_dict['sales'].set_index('date')
    data_dict['sales'] = data_dict['sales'].set_index(['store_nbr', 'family'], append=True)

    data_dict['avg'] = data_dict['sales'].groupby('date').mean()

    data_dict['test'] = pd.read_csv('data_season/test.csv')
    data_dict['test'] = data_dict['test'].set_index('date')
    data_dict['test'] = data_dict['test'].set_index(['store_nbr', 'family'], append=True)  

    data_dict['test_avg'] = data_dict['test'].groupby('date').mean()

    return data_dict


if __name__ == '__main__':
    data_dict = load_data_dict()