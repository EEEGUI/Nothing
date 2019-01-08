import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, Imputer


class DataSet(object):
    def __init__(self, df_train, df_test, label_col_name):
        """
        :param df_train:DataFrame, contain the column of label
        :param df_test: Dataframe, don't contain label
        :param label_col_name: string, the name of label
        """
        self.label_name = label_col_name
        self.len_train = len(df_train)
        self.len_test = len(df_test)
        self.label = df_train[label_col_name]

        df_train = self.drop_cols(df_train, [label_col_name])

        self.df_all = pd.concat([df_train, df_test], ignore_index=True)

    def merge_data(self, on_key, df_other, agg_config):
        """
        apply agg_config on df_other and then merge df_other with self.df_all on key
        :param on_key: the key(id) in both df_all and df_other
        :param df_other:
        :param agg_config: dict, eg: {"colname": ["mean", "std", ...]}
        :return:
        """
        pass

    def min_max_scale(self, cols_to_scale):
        """
        scale self.df
        :param cols_to_scale: list of cols to scale
        :return:
        """
        scale = MinMaxScaler()

        scale.fit(self.df_all.loc[:, cols_to_scale])
        self.df_all.loc[:, cols_to_scale] = scale.transform(self.df_all.loc[:, cols_to_scale])

    def fill_nan(self, dict_strategy):
        """
        fill the nan of self.df_all by different strategy
        :param dict_strategy: dict, key:col name, value:strategy; strategy include "mean", "median", "most_frequent",
                                int value
        :return:
        """
        for key in dict_strategy:
            if type(dict_strategy[key]) is str:
                imputer = Imputer(strategy=dict_strategy[key])
                imputer.fit(self.df_all.loc[key])
                self.df_all.loc[key] = imputer.transform(self.df_all.loc[key])
            elif type(dict_strategy[key]) is int:
                self.df_all.loc[key].fillna(dict_strategy[key])
            else:
                print("strategy error")
                pass

    def label_encoding(self, cols_to_encode):
        """
        encoding the col with two class
        :param cols_to_encode: list of cols to encode
        :return:
        """
        le = LabelEncoder()
        le.fit(self.df_all.loc[cols_to_encode])
        self.df_all.loc[cols_to_encode] = le.transform(self.df_all.loc[cols_to_encode])

    def process_datetime(self, cols_of_datetime):
        """
        get the year, month, day, weekday from the datetime cols
        :param cols_of_datetime: cols with the type of datetime
        :return:
        """
        pass

    @staticmethod
    def drop_cols(df, list_cols):
        """
        del list_cols from df
        :param df:
        :param list_cols: list, cols to delete
        :return: df without list_cols
        """
        return df.drop(labels=list_cols, axis=1)

    def makeup_feature(self):
        """
        makeup new feature from the original feature
        please override this function
        :return:
        """
        pass

    def get_df_train(self):
        """
        get train data set from the concat of train and test
        :return:
        """
        return self.df_all.loc[:self.len_train, :]

    def get_df_test(self):
        """
        get test data set from the concat of train and label
        :return:
        """
        return self.df_all.loc[self.len_train:, :]

    def get_label(self):
        """
        :return:
        """
        return self.label

    def process(self):
        """
        pipline to process the data set
        override this function
        :return:
        """
        pass
