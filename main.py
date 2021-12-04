import time
import requests
import csv

url_1 = '''https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken'''

response_b = requests.get(url_1).json()['result']


with open('graf.csv', mode='a', encoding='utf-8') as w_file:

    file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')


    def pars(q):

        url = 'https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&startblock=0&endblock=99999999&page=1&offset=10&tag='+ str(q) + '&boolean=true&apikey=CN887PAS9VREPY3ANBM7W12V9WWJZ9WHFQ'

        response = requests.get(url).json()['result']
        s = [response['timestamp'], [a['from'] for a in response['transactions']]]

        b = (int(s[0], 16))
        b_t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(b))
        if len(s[1]) > 0:
            file_writer.writerow([b_t[:10], len(s[1])])
    print('If you want to parse diapason - input 1, if you want to start parsing from a specific block to the last one - input 0: ')
    k = input()

    if k == 1:
        p = input('enter the starting block number: ')
        l = input('enter the ending block number: ')
        while True:
            for y in range(int(p, int(l))):
                pars(hex(y))
                print(y)
                p = y
            time.sleep(60)
    else:

        j = input('enter the starting block number: ')
        while True:
            for i in range(int(j), int(response_b, 16)):
                pars(hex(i))
                print(i)
                j = i
            time.sleep(60)
