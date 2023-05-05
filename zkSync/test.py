import csv
import os

from eth_keys import keys
from eth_utils import to_checksum_address


def generate_wallets(num_wallets):
    wallet_list = []

    for _ in range(num_wallets):
        private_key = keys.PrivateKey(os.urandom(32))
        public_key = private_key.public_key
        wallet_address = to_checksum_address(public_key.to_checksum_address())

        wallet_list.append((wallet_address, private_key.to_hex()))

    return wallet_list

def save_wallets(wallet_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['wallet_address', 'private_key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for wallet_address, private_key in wallet_list:
            writer.writerow({'wallet_address': wallet_address, 'private_key': private_key})

if __name__ == '__main__':
    num_wallets = 10
    output_filename = 'wallets.csv'

    wallet_list = generate_wallets(num_wallets)
    save_wallets(wallet_list, output_filename)

