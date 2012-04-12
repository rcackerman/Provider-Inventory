from google.appengine.api import users
from google.appengine.ext import db

class Providers(db.Model):
	"""Provider Information DB"""
	pDomain = db.StringProperty()
	pType = db.StringProperty()
	pAgency = db.StringProperty()
	pSite = db.StringProperty()
	progamName = db.StringProperty()
	pAddress = db.StringProperty()
	pAddress2 = db.StringProperty()
	pCity = db.StringProperty()
	pState = db.StringProperty()
	pZip = db.StringProperty()
	pPhone = db.StringProperty()
	pEmail = db.StringProperty()
	pNotes = db.TextProperty()
	Owner = db.UserProperty()

	def list_provs(self):
		self.providers = []
		self.provs = Providers.all()
		for prov in self.provs:
			self.providers.append(prov.pAgency)
                print self.providers
		return self.providers
	
	def list_addresses(self, providers):
	    print providers
		self.addrs = []
		self.addresses = db.Query(Providers).filter('pAgency =', provider)
		for addr in self.addresses:
			addrs.append(addr.pAddress)
		return addrs
		
Providers.list_addresses()