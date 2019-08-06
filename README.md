# Altheatest3 Instructions

These instructions will be updated as we move through the process.

We will start validating the Monday, August 5th, at 5pm PDT.

If you have any questions, visit our Discord chat: https://discordapp.com/invite/gxJhKZ2

At this point, if you haven't gotten your `gentx` in for altheatest3, it is too late. Please stay tuned, we may be able to add you after the chain is started, but you won't be able to tell people that you were a genesis validator on the first Althea test chain.

## New plan: Centralized Start

Unfortunately, we were one validator short of having a quorum to start the chain. After an hour of cliff-hangers trying to get one more person on, we decided to go with a centralized start. Justin started his validator and everyone else added a new `genesis.json` with only Justin as a starting validator. Then they ran the commands below to add themselves once the chain was running. It's up now, and you can see it at: https://althea.zone/#/staking/validators/.

### Joining

NOTE: This will only work if you were included in the genesis.json, went through the gentx process, etc.

Grab the `genesis.json` file from this repo and put it in `.gaiad/config/genesis.json`

Reset the state with `gaiad unsafe-reset-all`

Now start your validator with:

`gaiad start --p2p.persistent_peers "20d682e14b3bb1f8dbdb0492ea5f401c0c088163@198.245.51.51:26656"`

Now add yourself as a validator:

```
gaiacli tx staking create-validator \
      --amount=100000000ualtg \
      --commission-rate="0.10" \
      --commission-max-rate="0.20" \
      --commission-max-change-rate="0.01" \
      --min-self-delegation="1" \
      --pubkey=$(gaiad tendermint show-validator) \
      --moniker=<YOUR MONIKER> \
      --chain-id="altheatest3" \
      --from=$(gaiacli keys show <YOUR KEY NAME> -a)
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
