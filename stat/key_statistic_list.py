from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_key_statistic_list()
df.head()

df.to_csv('key_statistic_list.csv')