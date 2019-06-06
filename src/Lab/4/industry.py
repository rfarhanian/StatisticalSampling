import pandas as pd
import warnings


def init_data():
    warnings.simplefilter('ignore')
    return pd.read_csv('data/industry.csv')


def proportion_allocation(sales, sample_size):
    df = pd.DataFrame()
    df['stratum'] = sales.groupby(['stratum'], as_index=False).count()['stratum']
    df['no_of_units'] = sales.groupby(['stratum'], as_index=False).count()['UnitId']
    df['N_h/N'] = df['no_of_units'] / sales['UnitId'].count()
    df[str(sample_size) + '*N_h/N'] = df['N_h/N'] * sample_size
    df['sample_size'] = df[str(sample_size) + '*N_h/N'].round()
    # df['sample_size'][2] = df['sample_size'][2] + 1
    return df


def neyman_allocation(sales, prop_alloc, sample_size):
    df = pd.DataFrame()
    df['stratum'] = prop_alloc['stratum']
    df['N_h*S_h'] = sales.groupby(['stratum'], as_index=False).std()['Sales'] * prop_alloc['no_of_units']
    df['N_h*S_h/sum(N_h*S_h)'] = df['N_h*S_h'] / df['N_h*S_h'].sum()
    df[str(sample_size) + '*N_h*S_h/sum(N_h*S_h)'] = sample_size * df['N_h*S_h/sum(N_h*S_h)']
    df['sample_size'] = df[str(sample_size) + '*N_h*S_h/sum(N_h*S_h)'].round()
    return df


def neyman_allocation_substituting_sum_measure_size_product_stratum_size_and_std(sales, prop_alloc, sample_size):
    df = pd.DataFrame()
    df['stratum'] = prop_alloc['stratum']
    df['MOS_h'] = sales.groupby(['stratum'], as_index=False).sum()['mos']
    df['MOS_h/total MOS_h'] = df['MOS_h'] / df['MOS_h'].sum()
    df[str(sample_size) + '*MOS_h/total MOS_h'] = sample_size * df['MOS_h/total MOS_h']
    df['sample_size'] = df[str(sample_size) + '*MOS_h/total MOS_h'].round()
    return df


def main(sample_size):
    sales = init_data()
    prop_alloc = proportion_allocation(sales, sample_size)
    print('proportion_allocation\n\n', prop_alloc, '\n')
    print('neyman_allocation\n\n', neyman_allocation(sales, prop_alloc, sample_size), '\n')
    print('neyman_allocation_substituting_sum_measure_size_product_stratum_size_and_std\n\n',
          neyman_allocation_substituting_sum_measure_size_product_stratum_size_and_std(sales, prop_alloc, sample_size))


main(50)
