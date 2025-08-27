from FluencyLogisticsOperations import FLO

flo = FLO()

item = flo.client.resource("abc123").get()
items = flo.client.resource.list(limit=100, created_after="2025-08-01")

print(item.head())
print(items.head())
