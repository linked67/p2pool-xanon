from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

 xanon=math.Object(
        PARENT=networks.nets['xanon'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        IDENTIFIER='4d8baad93fedb9f6'.decode('hex'),
        PREFIX='fb7eeb0576bdf90a'.decode('hex'),
        P2P_PORT=7879,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7878,
        BOOTSTRAP_ADDRS='p2poolcoin.com ca.p2poolcoin.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-xanon',
        VERSION_CHECK=lambda v: True,
    ),



)
for net_name, net in nets.iteritems():
    net.NAME = net_name
