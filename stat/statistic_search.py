from PublicDataReader import Ecos

service_key = "SV4A93SRKYG5CY6T11V3"
api = Ecos(service_key)
df = api.get_statistic_search(통계표코드="200Y001", 주기="A", 검색시작일자="2015", 검색종료일자="2021")
df.head()

df.to_csv('statistic_search.csv')