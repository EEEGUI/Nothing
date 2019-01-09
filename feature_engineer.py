from utils import dataset
from utils import config
import pandas as pd


class EloData(dataset.DataSet):
    def __init__(self, df_train, df_test, label_col_name):
        super(EloData, self).__init__(df_train, df_test, label_col_name)

    @staticmethod
    def aggregate(df, key, agg_config, col_tag):
        """
        df group by key and the aggregate with agg_config
        :param df:
        :param key:
        :param agg_config: dict, eg: {"colname": ["mean", "std", ...]}
        :param col_tag: string, a tag of the df
        :return:
        """
        agg_df = df.groupby([key]).agg(agg_config)
        # change the columns of ("colname", "mean") to "colname_mean"
        agg_df.columns = ['_'.join(col).strip() for col in agg_df.columns.values]
        agg_df.reset_index(inplace=True)

        count_key_df = df.groupby(key).size().reset_index(name='%s_count' % key)

        df = pd.merge(count_key_df, agg_df, on=key, how='left')

        df.columns = [col_tag + '_' + c if c != key else c for c in df.columns]

        return df


if __name__ == '__main__':
    config = config.Config()
    df_train = pd.read_csv(config.TRAIN_PATH)
    df_test = pd.read_csv(config.TEST_PATH)
    df_history = pd.read_csv(config.HISTORY_PATH, parse_dates=[config.PARSE_DATE], nrows=config.NROWS)

    elo_data = EloData(df_train, df_test, config.LABEL_COL_NAME)
    print(elo_data.aggregate(df_history, config.KEY, config.HISTORY_AGG_FUNC, config.HISTORY_TAG))





