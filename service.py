import models

def pullusers():
    manageu = models.ManageUser()
    ulist = manageu.getuserlist()
    viewbag = []
    viewbag.append(len(ulist))
    viewbag.extend(ulist)

    return viewbag

def pulluser(uid):
    manageu = models.ManageUser()
    user = manageu.getuserdetails(uid)
    viewbag = user
    return viewbag

def pulltransactions(uid):
    managet = models.ManageTrs()
    transfers = managet.gettrn(uid)
    viewbag = []
    viewbag.append(len(transfers))
    viewbag.extend(transfers)
    return viewbag

def pushtransaction(uid1,uid2,credits):
    managet = models.ManageTrs()
    manageu = models.ManageUser()
    user1 = manageu.getuserdetails(uid1)
    user2 = manageu.getuserdetails(uid2)
    managet.addtrn(uid1,uid2,user1[0][1],user2[0][1],credits)
    manageu.updatecreds(uid1,uid2,credits)
