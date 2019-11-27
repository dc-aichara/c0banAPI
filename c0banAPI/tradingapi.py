import requests
import json
import pandas as pd
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

Price_URL = 'https://c0bantrade.jp/top/ajax/price.json'
Order_URL = 'https://c0bantrade.jp/top/ajax/orderbook.json'
Contract_URL = 'https://c0bantrade.jp/top/ajax/contractlist.json'
c0ban_URL = 'https://c0bantrade.jp/c0ban.json'


class c0banTrade:

    def __init__(self, price_url=Price_URL, order_url=Order_URL, contract_url=Contract_URL, c0ban_url=c0ban_URL):
        self.price_url = price_url
        self.order_url = order_url
        self.contract_url = contract_url
        self.c0ban_url = c0ban_url
        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

        self.headers = {'user_agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
                        'X-Requested-With': 'XMLHttpRequest'}
        self.payload = {"source_currency": "CBN", "target_currency": "JPY"}

    def __request(self, url):
        try:
            try:
                response = self.session.post(url, data=self.payload, headers=self.headers, timeout=self.request_timeout)
                response.raise_for_status()
                content = json.loads(response.content.decode('utf-8'))
                return content['data']
            except:
                response = self.session.get(url, timeout=self.request_timeout)
                response.raise_for_status()
                content = json.loads(response.content.decode('utf-8'))
                return content['CBN_JPY']
        except Exception as e:
            raise

    def mean_price(self):
        """
        c0ban mean price at c0bantrade.jp
        :return: float
        """
        cmp = self.__request(self.price_url)["current_price"]
        return float(cmp)

    def ask_price(self):
        """
        Lowest sell price at c0bantrade.jp
        :return: float
        """
        cap = self.__request(self.price_url)['sell_price']
        return float(cap)

    def bid_price(self):
        """
        Highest buy price price at c0bantrade.jp
        :return: float
        """
        cbp = self.__request(self.price_url)['buy_price']
        return float(cbp)

    def price_spread(self):
        """
        c0ban price spread (difference of ask and bid)
        :return: float
        """
        data = self.__request(self.price_url)
        spread = float(data["sell_price"]) - float(data["buy_price"])
        return spread

    def trading_volume_24h(self):
        """
        24 hours trading volume of c0ban on c0bantrade
        :return: float
        """
        tv = self.__request(self.price_url)["volume"]
        return float(tv)

    def quoted_volume_24h(self):
        """
        Total quoted volume on c0bantrade in last 24 hours.
        :return: float
        """
        qv = self.__request(self.c0ban_url)["quoteVolume"]
        return float(qv)

    def trading_price_volume_data(self):
        """
        All trading data
        :return: json
        """
        ts = self.__request(self.price_url)
        return ts

    def percent_price_change_3h(self):
        """
        c0ban price percent change in last 3 hours.
        :return: float
        """
        ppc = self.__request(self.c0ban_url)["percentchange"]
        return float(ppc)

    def price_low_3h(self):
        """
        Lowest c0ban price in last 3 hours.
        :return: float
        """
        pl = self.__request(self.c0ban_url)["low24hr"]
        return float(pl)

    def price_high_3h(self):
        """
        Highest c0ban price in last 3 hours.
        :return: float
        """
        ph = self.__request(self.c0ban_url)["high24hr"]
        return float(ph)

    def order_book(self):
        """
        Order book is a table which contains trader count, order price,
         and order volume sum by type of the order (sell or buy).
        :return: pandas DataFrame
        """
        content = self.__request(self.order_url)
        sell = content['sell']
        buy = content['buy']
        sell_data = {'count': [], 'sum_order_quantity': [], 'price_rate': []}
        buy_data = {'count': [], 'sum_order_quantity': [], 'price_rate': []}

        for item1, item2 in zip(sell, buy):
            for key in sell_data.keys():
                sell_data[key].append(item1[key])
                buy_data[key].append(item2[key])

        df_sell = pd.DataFrame(data=sell_data)

        df_sell.rename(columns={'count': 'seller_count', 'sum_order_quantity': 'sell_order_sum'}, inplace=True)

        df_buy = pd.DataFrame(data=buy_data)

        df_buy.rename(columns={'count': 'buyer_count', 'sum_order_quantity': 'buy_order_sum'}, inplace=True)

        df_order = pd.concat([df_sell, df_buy], axis=0, sort=False)

        df_order.fillna(0, inplace=True)

        for col in df_order.columns:
            try:
                df_order[col] = df_order[col].astype(float).astype(int)
            except:
                pass
        return df_order

    def trading_history(self):
        """
        This function returns lasted 100 transactions on c0bantrade.
        :return: pandas DataFrame
        """
        content = self.__request(self.contract_url)
        data = {'concluded_timestamp': [],
                'enforcement_criteria': [],
                'trade_order_kind': [],
                'price_rate': [],
                'concluded_order_quantity': [],
                'concluded_currency_amount': []}

        for item in content:
            for key in data.keys():
                data[key].append(item[key])

        df = pd.DataFrame(data=data)

        df['concluded_timestamp'] = pd.to_datetime(df['concluded_timestamp'])

        for col in df.columns[1:]:
            df[col] = df[col].astype(float).astype(int)

        df.rename(columns={'concluded_timestamp': 'timestamp',
                           'enforcement_criteria': 'limit_business',
                           'trade_order_kind': 'sell_buy',
                           'price_rate': 'rate',
                           'concluded_order_quantity': 'volume',
                           'concluded_currency_amount': 'amount'},
                  inplace=True)

        df['limit_business'] = df['limit_business'].apply(lambda x: 'limit' if x == 1 else 'business')
        df['sell_buy'] = df['sell_buy'].apply(lambda x: 'sell' if x == 1 else 'buy')
        return df

