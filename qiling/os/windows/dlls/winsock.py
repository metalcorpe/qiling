#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import socket

from qiling import Qiling
from qiling.os.windows.api import *
from qiling.os.windows.fncc import *
from qiling.os.windows.structs import *

WSAAPI = STDCALL

# u_long ntohl(
#   u_long netlong
# );
@winsdkapi(cc=WSAAPI, params={
    "netlong" : ULONG
})
def hook_ntohl(ql: Qiling, address: int, params):
    print(params)
    ret = socket.htonl(params["netlong"])
    print(ret)

    return ret

# u_long ntohs(
#   u_long netlong
# );
@winsdkapi(cc=WSAAPI, params={
    "netlong" : ULONG
})
def hook_ntohs(ql: Qiling, address: int, params):
    print(params)
    ret = socket.ntohs(params["netlong"])
    print(ret)

    return ret
