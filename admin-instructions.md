# Get a genesis.json

gaiad init --chain-id=<your chain id>

# repeat for each validator

gaiad add-genesis-account <validator address> 100000000ualtg

# repeat for each account

gaiad add-genesis-account <account address> 100000000ualtg

# Add gentxs into .gaiad/config/gentx if not already added

# Add in correct constants by looking at cosmos launch cosmoshub1 genesis

# Set not_bonded_tokens to total number of tokens in existence (bonded_tokens is set dynamically at chain start)

# Make sure to set up one validator that can be used as persistent peer

# Give genesis.json to validators and have them run gaiad start --p2p.persistent_peers "c8f1f5f9cbecdbc22c67205d569143f7e99e6ab5@159.65.74.76:26656" <- change to your persistent peer
