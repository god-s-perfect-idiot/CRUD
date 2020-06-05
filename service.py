import models

def pullusers():
    manageu = models.ManageUser()
    ulist = manageu.getuserlist()
    viewbag = []
    viewbag.append(len(ulist))
    viewbag.extend(ulist)

    return viewbag

def pullsenders(uid):
    manageu = models.ManageUser()
    ulist = manageu.getuserlist()
    for user in ulist:
        if(user[0] == uid):
            ulist.remove(user)
            break
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
    temp=[]
    for transfer in transfers:
        if(uid == transfer[1]):
                temp.append(transfer[3]+" sent "+str(transfer[5])+" credits to "+transfer[4])
        else:
            temp.append(transfer[4]+" recieved "+str(transfer[5])+" credit from "+transfer[3])
    viewbag.extend(temp)
    return viewbag

def pushtransaction(uid1,uid2,credits):
    managet = models.ManageTrs()
    manageu = models.ManageUser()
    user1 = manageu.getuserdetails(uid1)
    user2 = manageu.getuserdetails(uid2)
    if(credits.isdigit()):
        if(int(credits)<=int(user1[0][4])):
            managet.addtrn(uid1,uid2,user1[0][1],user2[0][1],credits)
            manageu.updatecreds(uid1,uid2,credits)
