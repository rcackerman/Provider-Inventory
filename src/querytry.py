from google.appengine.api import users
from google.appengine.ext import db

def list_provs():
  provs = Providers.all()
  for prov in provs:
    print prov.pAgency
  return provs
    
def list_addresses(agency):
  addrs = []
  addresses = db.Query(Providers).filter('pAgency =', agency)
  for addr in addresses:
    print prov.pAddress
  return None

providers = list_provs()
for provider in providers:
  print list_addresses(provider)