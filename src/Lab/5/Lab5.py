import pandas as pd
import numpy as np

n = 400
stratum_names = ['north Dallas', 'central Dallas', 'south Dallas']
stratum = [1, 2, 3]
p = [0.2, 0.6, 0.4]
N_h = [300000, 400000, 400000]  # strata size
P = 0.418  # ((300000 * 0.20) + (400000 * 0.40) + (400000 * 0.60)) / 1100000


def get_standard_error_estimate_proportion(n, N_h, P):
    # 1- Find the standard error of the estimate of proportion of voters waiting more than 10 minutes for a SRS of
    # 400 voters.
    N = sum(N_h)
    return np.sqrt(P * (1 - P) / n * (1 - (n / N)))


standard_error = get_standard_error_estimate_proportion(n, N_h, P)
print('-------------- a ----------------')
print('Standard Error:', standard_error, '\n\n')


def stratum_sample_size(n):
    # 2- What are the stratum sample sizes for a proportionately allocated stratified sample of size 400?
    sample_pps = pd.DataFrame({'name': stratum_names, 'stratum': stratum, 'p': p, 'N_h': N_h})
    print(sample_pps)
    print(sample_pps['N_h'] / sample_pps['N_h'].sum() * n)
    sample_pps['sample_size'] = [109, 145, 146]
    print(sample_pps)
    return sample_pps


print('-------------- b ----------------')
sample_pps = stratum_sample_size(n)


def get_standard_error_estimate_proportion_stratified(sample_pps):
    # 3- What is the standard error of the estimate of proportion of voters waiting more than 10 minutes for a
    # proportionately allocated stratified sample of 400 voters.
    sample_pps['variance'] = (sample_pps['p'] * (1 - sample_pps['p']) / (sample_pps['sample_size'] - 1) *
                              (1 - (sample_pps['sample_size']) / sample_pps['N_h']))
    sample_pps['weight'] = sample_pps['N_h'] / sample_pps['N_h'].sum()
    print(sample_pps)
    print('Standard Error:', np.sqrt((sample_pps['weight'] ** 2 * sample_pps['variance']).sum()))


print('-------------- c ----------------')
get_standard_error_estimate_proportion_stratified(sample_pps)


def get_stratum_sample_size_neyman(sample_pps):
    # d) What are the stratum sample sizes for a Neyman allocated stratified sample of size 400?

    sample_ney = pd.DataFrame({'name': stratum_names, 'stratum': stratum, 'p': p, 'N_h': N_h})
    print(sample_ney)
    print(sample_pps['p'] / sample_pps['p'].sum() * n)
    sample_ney['sample_size'] = [67, 200, 133]
    print(sample_ney)
    return sample_ney


print('-------------- d ----------------')
sample_ney = get_stratum_sample_size_neyman(sample_pps)


def get_standard_error_neyman_stratified_sample(sample_ney):
    # e) What is the standard error of the estimate of proportion of voters waiting more than 10 minutes for a
    # Neyman allocated stratified sample of 400 voters.

    sample_ney['variance_sample'] = (sample_ney['p'] * (1 - sample_ney['p']) / (sample_ney['sample_size'] - 1) *
                                     (1 - (sample_ney['sample_size']) / sample_ney['N_h']))
    sample_ney['weight'] = sample_ney['N_h'] / sample_ney['N_h'].sum()
    print(sample_ney)
    return np.sqrt((sample_ney['weight'] ** 2 * sample_ney['variance_sample']).sum())


print('-------------- e ----------------')
result = get_standard_error_neyman_stratified_sample(sample_ney)
print('Standard Error:', result)
