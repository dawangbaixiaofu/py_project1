import pandas as pd
import numpy as np


class Solution:
    @staticmethod
    def row_unique(df: pd.DataFrame, cols: list) -> pd.DataFrame:
        for row in range(len(df)):
            dic = dict()
            for col in cols:
                element = df.loc[row, col]
                if element in dic.keys():
                    dic[element] += 1
                    df.loc[row, col] = np.nan
                else:
                    dic[element] = 1


if __name__ == '__main__':
    data = {
        'Feature': [1, 2, 3, 4],
        'error1': ['overlaps', 'No error', 'overlaps', 'invalid'],
        'error2': ['overlaps', np.nan, 'invalid', 'overlaps'],
        'error3': ['overlaps', np.nan, 'invalid', 'overlaps'],
        'error4': ['overlaps', np.nan, np.nan, np.nan]
    }
    df = pd.DataFrame(data)
    df1 = df.copy()
    cols = ['error1', 'error2', 'error3', 'error4']
    Solution().row_unique(df1, cols)

    # 一种更加简洁的实现
    df[cols] = df[cols].apply(lambda x:pd.Series(x.unique()), axis=1).reindex(np.arange(len(cols)),axis=1)
    print(df1,'\n',df)

