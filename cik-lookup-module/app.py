import requests

class RetrieveSecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = {}
        self.tickerdict = {}
        self.load_data()

    def load_data(self):
        try:
            header = {'user-agent' : 'MLT CP 25 hmu200000@utdallas.edu'}
            response = requests.get(self.fileurl, headers=header)
            response.raise_for_status()

            self.company_data = response.json()
            for company in self.company_data.values():
                cik = company['cik_str']
                ticker = company['ticker']
                name = company['title']

                if cik and ticker and name:
                    self.namedict[name.lower()] = (cik, name, ticker)
                    self.tickerdict[ticker.lower()] = (cik, name, ticker)
                else:
                    print(f"Skipping incomplete data for: {company}")

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
        except ValueError as e:
            print(f"Error parsing JSON data: {e}")

    def name_to_cik(self, company_name):
        return self.namedict.get(company_name.lower())
    
    def ticker_to_cik(self, ticker):
        return self.tickerdict.get(ticker.lower())
se = RetrieveSecEdgar('https://www.sec.gov/files/company_tickers.json')
print(se.name_to_cik('Apple Inc.'))
print(se.ticker_to_cik('AAPL'))