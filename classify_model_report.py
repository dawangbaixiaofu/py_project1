import math
import pandas as pd


class Solution:
    @staticmethod
    def report_model(model, x_val, y_val):
        if type(x_val) == pd.DataFrame:
            x_val = x_val.reset_index(drop=True)
        y_val = y_val.reset_index(drop=True)
        row_num, col_num = 0, 0
        bins = 20
        y_predict = model.predict_proba(x_val)[:, 1]
        nrows = x_val.shape[0]
        lis = [(y_predict[i], y_val[i]) for i in range(nrows)]
        ks_lis = sorted(lis, key=lambda x: x[0], reversed=True)
        bin_num = int(nrows / bins + 1)
        bad = sum([1 for (p, y) in ks_lis if y > 0.5])
        good = sum([1 for (p, y) in ks_lis if y <= 0.5])
        bad_cnt, good_cnt = 0, 0
        KS = []
        BAD = []
        GOOD = []
        BAD_CNT = []
        GOOD_CNT = []
        BAD_PCTG = []
        BAD_RATE = []
        dct_report = {}

        for j in range(bins):
            ds = ks_lis[j * bin_num:min((j + 1) * bin_num, nrows)]
            bad1 = sum([1 for (p, y) in ds if y > 0.5])
            good1 = sum([1 for (p, y) in ds if y <= 0.5])
            bad_cnt += bad1
            good_cnt += good1
            bad_pctg = round(bad_cnt / bad, 3)
            bad_rate = round(bad1 / (bad1 + good1), 3)
            ks = round(math.fabs((bad_cnt / bad) - (good_cnt / good)), 3)
            KS.append(ks)
            BAD.append(bad1)
            GOOD.append(good1)
            BAD_CNT.append(bad_cnt)
            GOOD_CNT.append(good_cnt)
            BAD_PCTG.append(bad_pctg)
            BAD_RATE.append(bad_rate)
        dct_report['KS'] = KS
        dct_report['负样本个数'] = BAD
        dct_report['正样本个数'] = GOOD
        dct_report['负样本累积个数'] = BAD_CNT
        dct_report['正样本累积个数'] = GOOD_CNT
        dct_report['捕获率'] = BAD_PCTG
        dct_report['负样本占比'] = BAD_RATE
        val_report = pd.DataFrame(dct_report)
        return val_report

    @staticmethod
    def report(y_prob, y_val):
        row_num, col_num = 0, 0
        bins = 20
        nrows = len(y_val)
        bin_num = int(nrows / bins + 1)
        lis = [(y_prob[i], y_val[i]) for i in range(nrows)]
        ks_lis = sorted(lis, key=lambda x: x[0], reversed=True)
        bad = sum([1 for x in y_val if y_val > 0.5])
        good = sum([1 for x in y_val if y_val <= 0.5])
        bad_cnt, good_cnt = 0, 0
        KS = []
        BAD = []
        GOOD = []
        BAD_CNT = []
        GOOD_CNT = []
        BAD_PCTG = []
        BAD_RATE = []
        dct_report = {}

        for j in range(bins):
            ds = ks_lis[j * bin_num:min((j + 1) * bin_num, nrows)]
            good1 = sum([1 for x in ds if x[1] > 0.5])
            bad1 = sum([1 for x in ds if x[1] <= 0.5])
            good_cnt += good1
            bad_cnt += bad1
            bad_rate = round(bad1 / (bad1 + good1), 3)
            bad_pactg = round(bad_cnt / bad, 3)
            ks = round(math.fabs(bad_cnt / bad - good_cnt / good), 3)
            KS.append(ks)
            GOOD.append(good1)
            BAD.append(bad1)
            GOOD_CNT.append(good_cnt)
            BAD_CNT.append(bad_cnt)
            BAD_PCTG.append(bad_pactg)
            BAD_RATE.append(bad_rate)
        dct_report['KS'] = KS
        dct_report['正样本个数'] = GOOD
        dct_report['负样本个数'] = BAD
        dct_report['累积正样本个数'] = GOOD_CNT
        dct_report['累积负样本分数'] = BAD_CNT
        dct_report['负样本占比'] = BAD_RATE
        dct_report['负样本捕获率'] = BAD_PCTG
        val_report = pd.DataFrame(dct_report)
        return val_report
