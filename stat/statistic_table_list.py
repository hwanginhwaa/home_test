from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_statistic_table_list()
df.head()

df.to_csv('statistic_table_list.csv')