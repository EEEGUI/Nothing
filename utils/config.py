import numpy as np

class Config(object):

    ##  File Path ##

    TRAIN_PATH = 'data/train.csv'
    TEST_PATH = 'data/test.csv'
    HISTORY_PATH = 'data/historical_transactions.csv'
    MERCHANTS_PATH = 'data/merchants.csv'
    NEW_MERCHANT_TRANSACTIONS_PATH = 'data/new_merchant_transactions.csv'


    ##  DataSet ##
    LABEL_COL_NAME = 'target'
    PARSE_DATE = 'purchase_date'
    NROWS = 2000
    KEY = 'card_id'

    HISTORY_TAG = 'hist'



    ## Feature engineer ##
    HISTORY_AGG_FUNC = {
        'category_1': ['nunique'],
        'category_2': ['mean'],
        'category_3': ['nunique'],
        'merchant_id': ['nunique'],
        'merchant_category_id': ['nunique'],
        'state_id': ['nunique'],
        'city_id': ['nunique'],
        'subsector_id': ['nunique'],
        'purchase_amount': ['sum', 'mean', 'max', 'min', 'std'],
        'installments': ['sum', 'mean', 'max', 'min', 'std'],
        'purchase_date': [np.ptp, 'min', 'max'],
        'month_lag': ['mean', 'max', 'min', 'std'],
    }


