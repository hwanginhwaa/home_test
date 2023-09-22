from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_statistic_word(용어="소비자동향지수")
df.head()

df.to_csv('statistic_word.csv')