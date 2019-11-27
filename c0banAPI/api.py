import requests
import json

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class c0banAPI:

    __API_URL_BASE = 'https://insight-beta.c0ban.com/insight-api-c0ban/'

    def __init__(self, api_base_url=__API_URL_BASE):
        self.api_base_url = api_base_url
        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def __request(self, url):
        try:
            response = self.session.get(url, timeout=self.request_timeout)
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            raise

    def get_transaction_pages_of_address(self, wallet_address):
        """
        Get number of pages of transactions of a wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: Number of transaction pages (int)
        """

        api_url = '{0}txs?address={1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["pagesTotal"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_transactions_of_address(self, wallet_address, max_page_num):
        """
        Get transactions of intended wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :param max_page_num: Maximum number of pages (int)
        :return: transactions (json)
        """
        api_url = '{0}txs?address={1}&pageNum={2}'.format(self.api_base_url, wallet_address, max_page_num)
        try:
            return self.__request(api_url)["txs"]
        except Exception as e:
            print(e)
            print('Please check inputs!!')

    def get_all_transactions_of_address(self, wallet_address):
        """
        Get all transactions of a wallet address"
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: All transactions of given wallet address (list)
        """

        # Get page numbers

        api_url = '{0}txs?address={1}'.format(self.api_base_url, wallet_address)
        try:
            page_num = self.__request(api_url)["pagesTotal"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

        # Get transactions

        transactions =[]
        for i in range(0, page_num):
            api_url = '{0}txs?address={1}&pageNum={2}'.format(self.api_base_url, wallet_address, i)
            transactions.append(self.__request(api_url)["txs"])
        return transactions

    def get_txids_of_address(self, wallet_address):
        """
        Get all transaction IDs related to a particular wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: list of transaction ids
        """

        api_url = '{0}addr/{1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["transactions"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_balance_of_address(self, wallet_address):
        """
        Get balance of a particular wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: balance of wallet address (float)
        """

        api_url = '{0}addr/{1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["balance"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_received_amount_of_address(self, wallet_address):
        """
        Get total received amount of a particular wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: amount in RYOs (float)
        """

        api_url = '{0}addr/{1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["totalReceived"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_sent_amount_of_address(self, wallet_address):
        """
        Get total sent amount of a particular wallet address
        :param wallet_address: wallet address on c0ban blockchain (str)
        :return: sent amount in RYOs (float)
        """
        api_url = '{0}addr/{1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["totalSent"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_transaction_count_of_address(self, wallet_address):
        """
        Get number of transactions of a particular wallet address
        :param wallet_address:wallet address on c0ban blockchain (str)
        :return: list of transactions
        """
        api_url = '{0}addr/{1}'.format(self.api_base_url, wallet_address)
        try:
            return self.__request(api_url)["txApperances"]
        except:
            return print('Invalid wallet address. Please check wallet address again.')

    def get_transaction_of_txid(self, txid):
        """
        Get all transactions of a transaction id
        :param txid: transaction id (str)
        :return: transactions of given transaction id (json)
        """
        api_url = '{0}tx/{1}'.format(self.api_base_url, txid)
        try:
            return self.__request(api_url)
        except:
            return print('Invalid transaction id.')

    def get_blocks(self):

        """Get latest 200 blocks on c0ban blockchain
        :return: latest 200 blocks information (json)
        """

        api_url = '{0}blocks'.format(self.api_base_url)
        return self.__request(api_url)["blocks"]

    def get_block(self, block_height):
        """
        Get any block information by block height
        :param block_height: block height (int)
        :return: block information (json)
        """
        # Get block hash

        api_url = '{0}block-index/{1}'.format(self.api_base_url, block_height)

        try:
            block_hash = self.__request(api_url)["blockHash"]
        except:
            api_url = '{}status?q=getInfo'.format(self.api_base_url)
            current_height = self.__request(api_url)["info"]["blocks"]
            return print('{0} block height not yet reached! Current block height is {1}.'.format(block_height, current_height))

        # Get block

        api_url = '{0}block/{1}'.format(self.api_base_url, block_hash)
        return self.__request(api_url)

    def get_latest_block_height(self):
        """
        Get latest block height
        :return: current block height (int)
        """
        api_url = '{}status?q=getInfo'.format(self.api_base_url)
        return self.__request(api_url)["info"]["blocks"]

    def get_latest_block_difficulty(self):
        """
        Get current difficulty of c0ban blockchain
        :return: current difficulty (float)
        """

        api_url = '{}status?q=getInfo'.format(self.api_base_url)
        return self.__request(api_url)["info"]["difficulty"]

    def get_block_difficullty(self, block_height):
        """
        Get block difficulty at desired block height
        :param block_height: block height (int)
        :return: block difficulty (float)
        """
        api_url = '{0}block-index/{1}'.format(self.api_base_url, block_height)

        try:

            block_hash = self.__request(api_url)["blockHash"]
        except:
            api_url = '{}status?q=getInfo'.format(self.api_base_url)
            current_height = self.__request(api_url)["info"]["blocks"]
            return print('{0} block height not yet reached! Current block height is {1}.'.format(block_height, current_height))

        api_url = '{0}block/{1}'.format(self.api_base_url, block_hash)
        return self.__request(api_url)['difficulty']

    def get_transaction_count_of_block(self, block_height):
        """
        Get number of transactions of a block on c0ban blockchain
        :param block_height: block height (int)
        :return: Number of transactions (int)
        """

        api_url = '{0}block-index/{1}'.format(self.api_base_url, block_height)

        try:

            block_hash = self.__request(api_url)["blockHash"]
        except:
            api_url = '{}status?q=getInfo'.format(self.api_base_url)
            current_height = self.__request(api_url)["info"]["blocks"]
            return print('{0} block height not yet reached! Current block height is {1}.'.format(block_height, current_height))

        api_url = '{0}block/{1}'.format(self.api_base_url, block_hash)
        return len(self.__request(api_url)["tx"])

    def get_block_reward(self, block_height):
        """
        Get block reward for mining
        :param block_height: block height (int)
        :return: block reward (int)
        """
        api_url = '{0}block-index/{1}'.format(self.api_base_url, block_height)

        try:

            block_hash = self.__request(api_url)["blockHash"]
        except:
            api_url = '{}status?q=getInfo'.format(self.api_base_url)
            current_height = self.__request(api_url)["info"]["blocks"]
            return print('{0} block height not yet reached! Current block height is {1}.'.format(block_height, current_height))

        api_url = '{0}block/{1}'.format(self.api_base_url, block_hash)
        return self.__request(api_url)["reward"]

    def get_block_miner_address(self, block_height):
        """
        Get block miner address
        :param block_height: block height (int)
        :return: miner address (str)
        """
        api_url = '{0}block-index/{1}'.format(self.api_base_url, block_height)

        try:

            block_hash = self.__request(api_url)["blockHash"]

        except:
            api_url = '{}status?q=getInfo'.format(self.api_base_url)
            current_height = self.__request(api_url)["info"]["blocks"]

            return print(
                '{0} block height not yet reached! Current block height is {1}.'.format(block_height, current_height))

        api_url = '{0}block/{1}'.format(self.api_base_url, block_hash)
        miner_txid = self.__request(api_url)["tx"][0]

        api_url = '{0}tx/{1}'.format(self.api_base_url, miner_txid)
        return self.__request(api_url)["vout"][0]["scriptPubKey"]["addresses"][0]

