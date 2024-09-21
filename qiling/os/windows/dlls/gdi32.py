#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from qiling.os.windows.fncc import *
from qiling.os.const import *
from qiling.os.windows.utils import *
from qiling.os.windows.const import *
from qiling.const import *
from qiling.os.windows.structs import *
from .const import *

dllname = 'gdi32_dll'

# HENHMETAFILE GetEnhMetaFileW(
#   LPCWSTR lpName
# );
@winsdkapi(cc=STDCALL)
def hook_GetEnhMetaFileW(ql, address, params):
    ret = 0
    return

# DWORD GetFontData(
#   HDC   hdc,
#   DWORD dwTable,
#   DWORD dwOffset,
#   PVOID pvBuffer,
#   DWORD cjBuffer
# );
@winsdkapi(cc=STDCALL)
def hook_GetEnhMetaFileW(ql, address, params):
    # ret = 0
    return 2
