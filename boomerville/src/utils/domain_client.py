import numpy as np
import pandas as pd
import requests


class DomainClient():
    def __init__(self):
        self.url = 'https://api.domain.com.au/v1/salesResults'
        self.cities = ['Melbourne', 'Sydney', 'Canberra', 'Brisbane', 'Adelaide']
        self.headers = {'X-API-Key': 'key_d0bc84f8d05622330575997936c4398c'} # os.environ['API_KEY']

    def get_city_listings(self, city:str) -> pd.DataFrame:
        url = self.url
        headers = self.headers

        r = requests.get(f'{url}/{city}/listings', headers=headers)
        if r.status_code not in range(200,300):
            return {}
        return pd.DataFrame(r.json())

    def get_all_listings(self) -> pd.DataFrame:
        cities = self.cities

        return pd.concat([self.get_city_listings(city) for city in cities])

    @staticmethod
    def remove_null_ids(df:pd.DataFrame) -> pd.DataFrame:
        return df[~(df['id'] == 0)]

    @staticmethod
    def unpack_geolocation(df:pd.DataFrame) -> pd.DataFrame:
        df['latitude'] = df['geoLocation'].apply(lambda x: np.nan if isinstance(x, float) else x.get('latitude'))
        df['longitude'] = df['geoLocation'].apply(lambda x: np.nan if isinstance(x, float) else x.get('longitude'))
        return df.drop(columns=['geoLocation'])

    @staticmethod
    def rename_columns(df:pd.DataFrame) -> pd.DataFrame:
        df.columns = [
            'agency_id',
            'property_id',
            'property_url',
            'agency_name',
            'agency_url',
            'agent',
            'bathrooms',
            'bedrooms',
            'carspaces',
            'postcode',
            'price',
            'property_type',
            'result',
            'state',
            'street_name',
            'street_number',
            'street_type',
            'suburb',
            'unit_number',
            'latitude',
            'longitude'
            ]
        return df

if __name__ == '__main__':
    client = DomainClient()
