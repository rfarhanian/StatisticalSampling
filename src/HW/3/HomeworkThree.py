import pandas as pd

# pat_encounters = pd.read_csv('data/patient_encounters.csv', delimiter=';')
#
# # count of encounters by each patNum
# pat_visits = pat_encounters[['DOS','patNum']].groupby('patNum').count().rename(columns={'DOS':'count'})
#
# # random sample of 20 encounters with replacement, merged with the count of encouters by patNum
# pps_sample = pat_encounters.sample(n=20, replace=True).merge(pat_visits, left_on='patNum', right_index=True)
#
# # calculating weights
# pps_sample['weight'] = pat_encounters.DOS.count() / pps_sample['count']
#
# pps_sample


hypothetical_roster_data = pd.read_csv('data/class_roster.csv')
print("--------Hypothetical Roster Data------")
print(hypothetical_roster_data)
print("------------------")
srs_class_sample = hypothetical_roster_data.sample(n=5, replace=False)
print("Simple Random Sample: \n\n", srs_class_sample)

all = hypothetical_roster_data.Texas.count()
texan_data = hypothetical_roster_data[hypothetical_roster_data.Texas == "Y"]
non_texan_data = hypothetical_roster_data[hypothetical_roster_data.Texas == "N"]
n_Texas = texan_data.count() / all * 5
n_non_Texas = non_texan_data.count() / all * 5

texas_startum_size = n_Texas.Texas.round()
non_texas_stratum_size = n_non_Texas.Texas.round()

print("-------------------------")
print("Texan Stratum n: ", texas_startum_size)
print("Non-Texan Stratum n: ", non_texas_stratum_size)
print("-------------------------")

texan_stratum_class_sample = texan_data.sample(n=int(texas_startum_size), replace=False)

non_texan_stratum_class_sample = non_texan_data.sample(n=int(non_texas_stratum_size), replace=False)

print("All Samples:\n\n", pd.concat([texan_stratum_class_sample, non_texan_stratum_class_sample]))
print("-------------------------")
