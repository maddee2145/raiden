from ethereum.utils import big_endian_to_int, sha3, int_to_big_endian, privtoaddr
#from ethereum.keys import privtoaddr
from bitcoin import encode_pubkey, N, P
from IPython.core import ultratb
import sys


def ishash(h):
    return isinstance(h, bytes) and len(h) == 32


def isaddress(a):
    return isinstance(a, bytes) and len(a) == 20


def pex(h):
    return str(h).encode('hex')[:8]

def lpex(lst):
    return [pex(l) for l in lst]


def activate_ultratb():
    sys.excepthook = ultratb.VerboseTB(call_pdb=True, tb_offset=6)