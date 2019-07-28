# Altheatest3 Instructions

These instructions will be updated as we move through the process.

We'd like to get all gentxs in by Wednesday, July 31st. We will start validating the following Monday, August 5th.

## How to make a gentx

We are currently gathering `gentx` files to create the `genesis.json` file which will be used to start the altheatest3 blockchain.

## Download and build Gaiad

You must use the exact version specified here. You need Go > 1.12

```
git clone https://github.com/cosmos/cosmos-sdk/
cd cosmos-sdk
git checkout v0.35.0
make tools
make install
```

## Generate your private key using Gaiad

```
# generate a key, set a passphrase and backup the keywords
gaiacli keys add <your key name>

# view your address and pubkey
gaiacli keys list
```

## Generate your gentx

```
# Your moniker is the name of your validator that will be publically displayed
gaiad init --chain-id=altheatest3 <moniker>

# We are using ualtg as our base denomination. This is one one millionth of an altg.
# So 100000000ualtg is 100altg, which is what validators are getting at the genesis
# of this testnet.
gaiad add-genesis-account <your address> 100000000ualtg

# Create the gentx
gaiad gentx --name <your key name> --amount 100000000ualtg --ip <your public ip>
```

This will write your genesis transaction to \$HOME/.gaiad/config/gentx/gentx-<gen-tx-hash>.json. This should be the only file in your gentx directory. If you have more than one, delete them and repeat the gentx command above.

Now, just submit a pull request to this repo which puts your gentx in the gentxs folder. Once we have everyone's, we will compile them into a complete `genesis.json`.

# General information on running a validator

## What is a validator?

A validator is sort of like a miner for a proof of stake blockchain. They don't need any special hardware or a large amount of power. Instead validators risk 'staked' tokens. A validator will lock up staking tokens and lose 5% of them if they misbehave.

Misbehaving is defined as

- signing two blocks at the same block height (forking the chain)
- being offline (not signing any blocks) for more than 16 hours without first removing yourself from the validators list
- Losing your private key
- Other conditions that may compromise the security of the chain

Most people will not be validating themselves but “delegating” tokens to a validator. When you delegate your tokens you are adding them to that validators stake and you will split the profits from using your tokens with the validator.

## Do I need anything special to be a validator?

Technically anything that can run a full node can validate, but since there's staked money on the line your concern for the stability and reliability of your validator should be proportinal to the amount of money staked with it. Very professional setups suggest colocating your own physical server and using a ledger to hold the actual validator private key.

You validate or delegate tokens at you're sole risk, we don't make any recomendations in good faith with the hope that they are useful. They don't need any special hardware or a large amount of power. Instead validators risk 'staked' tokens. A validator will lock up staking tokens and lose 5% of them if they misbehave.

Misbehaving is defined as

- signing two blocks at the same block height (forking the chain)
- being offline (not signing any blocks) for more than 16 hours without first removing yourself from the validators list
- Losing your private key
- Other conditions that may compromise the security of the chain

Most people will not be validating themselves but “delegating” tokens to a validator. When you delegate your tokens you are adding them to that validators stake and you will split the profits from using your tokens with the validator.
guarantee of safety in validating.
