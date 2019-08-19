import argparse
import json
import sys

parser = argparse.ArgumentParser(
    description="Convert altheatest3 genesis file to altheatest4")

parser.add_argument(
    'exported_genesis',
    help='exported genesis.json file',
    type=argparse.FileType('r'), default=sys.stdin,
)

args = parser.parse_args()

genesis = json.loads(args.exported_genesis.read())

# New genesis time
genesis['genesis_time'] = '2019-08-19T21:00:00Z'

# New chain id
genesis['chain_id'] = 'altheatest4'

# Change deposit amount to 1 ALTG
genesis['app_state']['gov']['deposit_params']['min_deposit'][0]['amount'] = '1000000'

# Change unbonding period to 1 day
genesis['app_state']['staking']['params']['unbonding_time'] = '86400000000000'

accounts = genesis['app_state']['accounts']


def search(list, key, value):
    for item in list:
        if item[key] == value:
            return item


total_new_tokens_minted = 0


def mint_ualtg_for(accounts, address, amount):
    global total_new_tokens_minted
    total_new_tokens_minted = total_new_tokens_minted + amount
    for account in accounts:
        if account['address'] == address:
            # If the account exists, add coins
            account['coins'][0]['amount'] = str(int(
                account['coins'][0]['amount']) + amount)
            break

    # If the account does not yet exist, create it
    accounts.append({
        "address": address,
        "coins": [
            {
                "denom": "ualtg",
                "amount": str(amount)
            }
        ],
        "sequence_number": "1",
        "account_number": "0",
        "original_vesting": None,
        "delegated_free": None,
        "delegated_vesting": None,
        "start_time": "0",
        "end_time": "0"
    },)


# rourke750
mint_ualtg_for(
    accounts, 'cosmos1l6gf409w0lnnw43k0z0uxewhpj039mjg8ztz5q', 100000000)
# meow
mint_ualtg_for(
    accounts, 'cosmos1ftal9qkrvm5vq28my6al3ajsyny46gp97fv0z9', 100000000)
# asoltys
mint_ualtg_for(
    accounts, 'cosmos1z6s8unktt0em3cnuw6dakewufmeap0y6m964sv', 100000000)
# xcipher
mint_ualtg_for(
    accounts, 'cosmos1q7lmehnlwe9faa53jtq2f2jucwudr2dcrfqv3p', 100000000)
# blitmore
mint_ualtg_for(
    accounts, 'cosmos1z8tl0rcp8kz9v3tyra4q44zyg337k7geulkh0f', 100000000)
# novy
mint_ualtg_for(
    accounts, 'cosmos1m53wwcst7l4psdh8uph2eq74jmqjx85xh3fss3', 100000000)
# ka4ok
mint_ualtg_for(
    accounts, 'cosmos14lsedpygn54ch58sl0rr2dz5jxgasue8tke37p', 100000000)
# dasheng
mint_ualtg_for(
    accounts, 'cosmos1mqyutur58fx0pfdtpfh34f62w6x9vk2fnd56qg', 100000000)
# POS-Bakerz
mint_ualtg_for(
    accounts, 'cosmos1v0z8fxddwa6ftlfeawuwrq677vgk76v2w3v3mc', 100000000)
# browep
mint_ualtg_for(
    accounts, 'cosmos13fkdunuukj0tylpslcqshnz6f6tm9vr0a6drfn', 100000000)
# okeanus
mint_ualtg_for(
    accounts, 'cosmos1v5c3v8802wtrw06jakk00smtqyvw99xahug9gl', 100000000)
# Chainflow
mint_ualtg_for(
    accounts, 'cosmos1jj7lcjxm43yh43u4m6s83h7f0vc2l8a3jte63w', 100000000)
# y3v63n
mint_ualtg_for(
    accounts, 'cosmos1cytt9ru6a48j4un4gn5355lgmqankl0l8e7u49', 100000000)
# UbikCapital
mint_ualtg_for(
    accounts, 'cosmos1ymy58lrqvrxwa7mnrtaqfl24dv2c5jm7uyx7y9', 100000000)
# nuevax
mint_ualtg_for(
    accounts, 'cosmos170zkcgge9w4vj2zqu2jvx37jlfwr2w8t9hsyy4', 100000000)
# blockshane
mint_ualtg_for(
    accounts, 'cosmos1me6xrxj80cp4smrmy2mwaan67spnsen9s0xtg4', 100000000)
# Figment Networks
mint_ualtg_for(
    accounts, 'cosmos15at47see52v0rv70q4xqcxwa6dhw6ecurjj44x', 100000000)

# Add new tokens into not_bonded_tokens
genesis['app_state']['staking']['pool']['not_bonded_tokens'] = str(int(
    genesis['app_state']['staking']['pool']['not_bonded_tokens']) + total_new_tokens_minted)

print(json.dumps(genesis, indent=True))
