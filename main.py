
import requests

from PropertyType import PropertyType
from MarketingType import MarketingType
from PropertyPriceUrlBuilder import PropertyPriceUrlBuilder
from UrlBuilder import UrlBuilder

if __name__ == '__main__':
    ppub = PropertyPriceUrlBuilder()
    ppub.set_address('Eisenbahnstraße 18B Hanau')
    ppub.set_property_type(PropertyType.apartment)
    ppub.set_marketing_type(MarketingType.rent)
    url = UrlBuilder(ppub).build()
    r = requests.get(url)
    obj = r.json()

    print(obj['property']['price'])
