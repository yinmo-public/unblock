# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
int1 = len(yinmo.getBlockedContactIds())
if int1 == 0:
    print("Blocklist Empty")
else:
    for cids in yinmo.getBlockedContactIds():
        print("Unblock " + yinmo.getContact(cids).displayName)
        yinmo.unblockContact(cids)
    print("\nYou unblock" + str(int1) + "friends")
    