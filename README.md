# Altheatest4 Instructions

These instructions will be updated as we move through the process. You can see the current status of the testnet at https://althea.zone

If you have any questions, visit our Discord chat: https://discordapp.com/invite/gxJhKZ2

## Joining as a validator

You need to have tokens to become a validator. You can get tokens in the next hard fork by signing up here: https://airtable.com/shrpjZDQYQa3Xd5oe. You can also say hi in https://discordapp.com/invite/gxJhKZ2 and maybe someone will give you some. They are worthless testnet tokens.

These instructions are all for gaiad v0.35.0, which you can get by doing:

### Download and build Gaiad

You must use the exact version specified here. You need Go > 1.12

```
git clone https://github.com/cosmos/cosmos-sdk/
cd cosmos-sdk
git checkout v0.35.0
make tools
make install
```

### Generate your private key using Gaiad

```
# generate a key, set a passphrase and backup the keywords
gaiacli keys add <YOUR_KEY_NAME>

# view your address and pubkey
gaiacli keys list
```

### Creating your validator

Grab the genesis.json file from this repo and put it in `.gaiad/config/genesis.json`

Reset the state with `gaiad unsafe-reset-all`

Now start your validator with:

`gaiad start --p2p.persistent_peers "58B5E7269C70C0B336FAEA6DC573B5BB0B539C3B@althea.zone:26656"`

Now add yourself as a validator:

```
gaiacli tx staking create-validator \
      --amount=100000000ualtg \
      --commission-rate="0.10" \
      --commission-max-rate="0.20" \
      --commission-max-change-rate="0.01" \
      --min-self-delegation="1" \
      --pubkey=$(gaiad tendermint show-validator) \
      --moniker=<YOUR_MONIKER> \
      --chain-id="altheatest4" \
      --from=$(gaiacli keys show <YOUR_KEY_NAME> -a)
```

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
