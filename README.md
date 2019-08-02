# Altheatest3 Instructions

These instructions will be updated as we move through the process.

We will start validating the Monday, August 5th, at 5pm PDT.

If you have any questions, visit our Discord chat: https://discordapp.com/invite/gxJhKZ2

At this point, if you haven't gotten your `gentx` in for altheatest3, it is too late. Please stay tuned, we may be able to add you after the chain is started, but you won't be able to tell people that you were a genesis validator on the first Althea test chain.

## Starting the chain

### TEMPORARY PAUSE - THIS GENESIS.JSON WILL NOT WORK.

The reason is that someone's gentx was bad, and the `gaiad collect-gentxs` command for some reason doesn't check for that. We're going to be writing a script to validate all the gentxs and hopefully have a new genesis.json out soon.

It's pretty simple now. Just grab the `genesis.json` file from this repo and put it in `.gaiad/config/genesis.json`

Now start your validator with:

`gaiad start --p2p.persistent_peers "20d682e14b3bb1f8dbdb0492ea5f401c0c088163@198.245.51.51:26656"`

It will wait until Monday the 5th at 5pm PST to start validating.

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
