from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_statistic_item_list(통계표코드="601Y002")
df.head()

df.to_csv('statistic_item_list.csv')