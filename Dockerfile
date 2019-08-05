FROM fedora
ENV GOPATH=/go
ENV PATH=$PATH:/go/bin
RUN dnf install -y git golang make gcc gcc-c++ which
RUN git clone https://github.com/cosmos/cosmos-sdk && pushd cosmos-sdk && git checkout v0.35.0
RUN pushd cosmos-sdk && make tools && make install
RUN mkdir $HOME/.gaiad/ && mkdir $HOME/.gaiad/config
ADD . /althea-zone
RUN cp /althea-zone/genesis.json $HOME/.gaiad/config
CMD gaiad start --p2p.persistent_peers "20d682e14b3bb1f8dbdb0492ea5f401c0c088163@kilpatrickjustin.me:26656"
