from MarketingType import MarketingType
from PropertyType import PropertyType


class PropertyPriceUrlBuilder:
    def __init__(self):
        self.__base = 'https://preisatlas-api.homeday.de/latest'
        self.__resource = 'property_price'
        self.__filter = dict()

    def set_address(self, address):
        self.__filter['address'] = address

    def set_property_type(self, property_type):
        if not isinstance(property_type, PropertyType):
            raise TypeError('property_type must be an instance of PropertyType Enum')
        self.__filter['property_type'] = property_type.name

    def set_marketing_type(self, marketing_type):
        if not isinstance(marketing_type, MarketingType):
            raise TypeError('marketing_type must be an instance of MarketingType Enum')
        self.__filter['marketing_type'] = marketing_type.name

    def get_base(self):
        return self.__base

    def get_resource(self):
        return self.__resource

    def get_filter(self):
        return self.__filter
