# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getBlockedContactIds())
if int1 == 0:
    print("您沒有封鎖任何好友")
else:
    for cids in yinmo.getBlockedContactIds():
        print("已解除封鎖 " + yinmo.getContact(cids).displayName)
        yinmo.unblockContact(cids)
    print("\n您解除封鎖" + str(int1) + "位好友")
    