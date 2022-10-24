#!/usr/bin/env python3
"""
Random IPv6 address for a specified subnet
"""

from random import seed, getrandbits
from ipaddress import IPv6Network, IPv6Address

""" 
Install Multiping module
    pip install multiping
"""
from multiping import MultiPing

print("IPv6 subnet (Ex: 2001:db8:acad:2::/64): ")
subnet = input()
seed()
network = IPv6Network(subnet)
address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))
print(address)

mp = MultiPing([str(address)])
mp.send()
responses, no_responses = mp.receive(1)
if responses:
    print("reachable: %s" % responses)

if no_responses:
    print("unreachable: %s" % no_responses)
