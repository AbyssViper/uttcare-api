# -*- coding: utf-8 -*-
__author__ = 'AbyssViper'

import time
from api.nat_map_api import *

# Demo test
if __name__ == '__main__':
    del_mapping([443])

    operate_mapping(
        "add",
        1,
        443,
        "WAN1",
        "192.168.1.233",
        [(3, 443, 443, 443, 443)]
    )

    time.sleep(10)

    port_enable(443, 0)
