# Altheatest3 Instructions

These instructions will be updated as we move through the process.

If you have any questions, visit our Discord chat: https://discordapp.com/invite/gxJhKZ2

## Upcoming Hard Fork

_Note: these instructions are for altheatest3 validators. If you're not on that chain, this is a good chance for you to join altheatest4. Sign up here: https://airtable.com/shrpjZDQYQa3Xd5oe to get some tokens, and say hi in https://discordapp.com/invite/gxJhKZ2 to get instructions on getting caught up._

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
gaiacli keys add <your key name>

# view your address and pubkey
gaiacli keys list
```

We will be hard forking the Althea test chain to `altheatest4` on Monday, August 19th at 3pm PDT.

Here are the changes that will be made to the chain's settings and state:

- Reduce governance proposal deposit to 1 ALTG. This will let us do governance proposals.
- Reduce unbonding period to 1 day (86400000000000ns). This will make it easier to take your tokens out of delegation to send them around and stuff.
- Mint 100 new ALTG for anyone who signed up for our validator notification mailing list at https://airtable.com/shrpjZDQYQa3Xd5oe. The newly minted tokens are to give people who weren't in altheatest3 a chance to get some tokens to start validating on altheatest4, and to give the old-timers a little extra worthless testnet pocket change.

Hard forks on Comsos chains are currently a surprisingly manual process. Here are the steps:

1. Everyone waits until the predetermined time.
2. Everyone stops `gaiad`, and exports a new genesis file which will be used to start the new chain.
3. Everyone makes any necessary changes to the new genesis file (at least updating the chain id), and replaces the old genesis file with the new one.
4. Everyone does `gaiad unsafe-reset-all`, and `gaiad start`.
5. Once validators controlling 2/3rds of the voting power on the chain have completed these steps, the chain starts again.

Until step 5, the chain is halted. When the Cosmos hub hard forked from cosmoshub1 to cosmoshub2, this process took around 2 hours. Keep in mind that on the Cosmos hub, most validator operations are someone's full time job and have millions of dollars riding on them. It's likely that our little testnet will be halted for at least as long on Monday.

That being said, I think that a lot of this process can be automated. For future hard forks it might be good to use some kind of script that validators could start days ahead of time, which would wait for the right block, stop the chain, export and modify the genesis file, and start the new chain. Might be good to give that some thought as we go through this process.

## Step-by-step instructions

These are a simplified version of the cosmoshub1 to cosmoshub2 instructions here: https://github.com/cosmos/cosmos-sdk/wiki/Cosmos-Hub-1-Upgrade.

One key difference is that they did the hard fork at a predetermined block, while we will be doing it at a predetermined time.

### Step 1

On or after August 19th, 3pm PDT, check this readme at https://github.com/althea-net/althea-zone for the correct block height to fork at. It will appear below:

```
FORKING BLOCK: 206400
```

### Step 2

Stop any existing `gaiad` process and run `gaiad export --for-zero-height --height=206400 > altheatest3_genesis_export.json`

### Step 3

Run `python3 altheatest3-to-altheatest4.py altheatest3_genesis_export.json > genesis.json` to make the neccesary changes to the genesis file. `altheatest3-to-altheatest4.py` will appear in this repo before August 19th, 3pm PDT.

After this, you should be able to get this hash

```
$ jq -S -c -M '' genesis.json | shasum -a 256
6a58940eb3d113a7139919b6aa2e155a177a1be068c623ecdc2d89b5b3a2b19d
```

Move the genesis file to your .gaiad directory, usually `~/.gaiad/config/genesis.json`.

### Step 4

Run `gaiad unsafe-reset-all` and then `gaiad start --p2p.persistent_peers "20d682e14b3bb1f8dbdb0492ea5f401c0c088163@198.245.51.51:26656"` to hopefully start on the new chain!

You can check the state of the consensus with `curl -s localhost:26657/consensus_state`. You should see some JSON that looks something like this:

```
"round": "0",
"prevotes": [
    "nil-Vote",
    "Vote{1:2B3F7DBECEA4 1/00/1(Prevote) 000000000000 E5158678B215 @ 2019-08-19T22:22:21.144936719Z}",
    "nil-Vote",
    "nil-Vote",
    "Vote{4:3EFFBB4521CE 1/00/1(Prevote) 000000000000 4309AAD1D126 @ 2019-08-19T22:17:37.366381859Z}",
    "nil-Vote",
    "nil-Vote",
    "Vote{7:6F17C91C619F 1/00/1(Prevote) 000000000000 5F56B3A815A6 @ 2019-08-19T22:17:51.138482157Z}",
    "nil-Vote",
    "nil-Vote",
    "nil-Vote",
    "Vote{11:9870294B556F 1/00/1(Prevote) 000000000000 6FD2B9E6E0FD @ 2019-08-19T22:55:16.097209212Z}",
    "Vote{12:A558B0B2A57D 1/00/1(Prevote) 000000000000 A966696548AC @ 2019-08-19T22:37:22.966509726Z}",
    "Vote{13:A797F8942AA6 1/00/1(Prevote) 000000000000 98FBD78DF508 @ 2019-08-19T23:07:00.305851382Z}",
    "Vote{14:A9677737FED1 1/00/1(Prevote) 000000000000 787BB7BEAAF7 @ 2019-08-19T22:22:20.566826479Z}",
    "Vote{15:AFA96C4DF538 1/00/1(Prevote) 000000000000 C026F30F08DA @ 2019-08-19T22:17:41.559706657Z}",
    "nil-Vote",
    "nil-Vote",
    "Vote{18:EC5ADABF5803 1/00/1(Prevote) 000000000000 940BFDEE0A4F @ 2019-08-19T22:22:30.693998577Z}",
    "Vote{19:F8DD3D796B12 1/00/1(Prevote) 000000000000 A0635BF47E46 @ 2019-08-19T23:08:04.191215906Z}"
],
```

Once around 14 or 15 of those slots have a vote (like `Vote{13:A797F8942AA6 1/00/1(Prevote)`), the chain should start making blocks!

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
