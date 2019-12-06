# -*- coding: utf-8 -*-
__author__ = 'AbyssViper'

import requests
from api.common import get_base_headers
from utils import *

# Nat Static Map (Port mapping -> static mapping)
# rule_operate include edit and add.
rule_operate = "/goform/formNatStaticMap"
rule_del = "/goform/formNatStaticMapDel"
rule_enable = "/goform/formConfigNatMapEnable"


# Control port mapping open or close.
# Parm value 1 mean open, 0 mean close.
def port_enable(rule_id, value):
    data = {
        "IDs": rule_id,
        "ConfigEnables": value
    }

    response = requests.post(request_api(rule_enable), data, headers=get_base_headers())
    return response


# Parm port_list format: [(Protocols, OutPortS, OutPortE, InnerPortS, InnerPortE), ...]
# Protocols: TCP-1, UDP-2, TCP/UDP-3
# PortS mean PortStart, PortE mean PortEnd
# Action: add, update
def operate_mapping(action, enable, rule_id, interface, inner_ip, port_rules):
    port_rule_keys = ["Protocols[%s]", "OutPortS[%s]", "OutPortE[%s]", "InnerPortS[%s]", "InnerPortE[%s]"]

    data = {
        "Action": action,
        "ConfigEnables": enable,
        "IDs": rule_id,
        "NatBinds": interface,
        "IPs": inner_ip,
        "PortNums": len(port_rules)
    }

    if action == "update":
        data.pop("Action")

    for rule_index, port_rule in enumerate(port_rules):
        for key_index, rule_value in enumerate(port_rule_keys):
            data[rule_value % rule_index] = port_rule[key_index]

    response = requests.post(request_api(rule_operate), data, headers=get_base_headers())
    return response


def edit_mapping(old_rule_id, new_rule_id):
    pass


# Delete rule from port mapping.
# Parm need a list, e.g. [id1, id2, id3....]
def del_mapping(rule_ids):
    key_word = "delstr"
    data = {
        key_word: ""
    }
    for rule_id in rule_ids:
        data[key_word] += str(rule_id) + ","

    data[key_word] = data[key_word][:-1]

    response = requests.post(request_api(rule_del), data, headers=get_base_headers())
    return response


if __name__ == '__main__':
    pass

    """
        Edit and add demo.
    """
    # result = operate_mapping(
    #     "update",
    #     1,
    #     443,
    #     "WAN1",
    #     "192.168.1.233",
    #     [(1, 443, 443, 443, 443), (3, 28443, 28443, 443, 443)]
    # )
    #
    # print(result.status_code)
    # print(result.content)
