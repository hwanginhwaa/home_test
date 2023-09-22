from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_statistic_meta(데이터명="경제심리지수")
df.head()

df.to_csv('get_statistic_meta.csv')