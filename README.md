# Running a full node on the Althea Blockchain / Cosmos zone

Download and build Gaiad, you must use the exact version specified here. You need Go > 1.12

```
git clone https://github.com/cosmos/cosmos-sdk/
cd cosmos-sdk
git checkout v0.35.0
make tools
make install
```

Now that you have the full node software, Gaiad installed we need to add in the Althea chain
configuraton file (genesis.json) you'll find the latest version of that file in this repository.

```
mkdir ~/.gaiad
mkdir ~/.gaiad/config
cp althea-zone/genesis.json ~/.gaiad/
```

Finally start Gaiad this will hook up to the seed nodes provided and start syncing the chain. After you first
start Gaiad it will remember peers it has seen before, so you don't need the `--p2p.seeds` flag after your first
run.

```
gaiad start --p2p.seeds=f5674655445b64974cd75c809c960965a67e780b@159.65.74.76:26656, 20d682e14b3bb1f8dbdb0492ea5f401c0c088163@kilpatrickjustin.me:26656
```

# Running a validator

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

## Enough jabbering what buttons do I press?

### Genesis validators

Genesis validators are a special case for when a new chain is being started. You create and submit a gentx using `gaiacli gentx` (read the help) which is then added into the `genesis.json` that it used by all parties to start the chain. This is a bit of a back and forth process.

Genesis file is created -> Genesis validators create gentx's using the Genesis file -> A new genesis file is created containing all of those initial validators and their gentx's -> the chain is started.

### Validating on an online chain

To validate on an online chain you must first generate a private key, we will give example commands for generating a key on your own machine. If you have a need for higher security it's recomended that you instead generate a key using the Cosmos Ledger app.

Generate your private key

```
# generate a key, set a passphrase and backup the keywords
gaiacli keys add 0
# view the validator pubkey you have generated this is different from the pubkey you would see
# with gaiacli keys list
gaiad tendermint show_validator
# Generate a transaction to indicate your intention to start staking, you should have gaiad running
# when you do this so that you can publish the transaction.
gaiacli tx staking create-validator --amount 0altg --moniker <your nickname> --pubkey <your key from the last step here> --commission-rate 10 --commission-max-rate 100 --commission-max-change-rate 1 --min-self-delegation 0
```

Once you successfully run the last command you will be running as a validator on the testnet, your node will need to remain online and be delegated some altg in order to start generating validator rewards. Be careful to avoid the bad behavior we talked about previously
