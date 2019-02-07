# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
for cids in yinmo.getBlockedContactIds():
    yinmo.unblockContact(cids)
    print("已解除封鎖1位好友")