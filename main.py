# vim:fileencoding=utf-8

import math
import itertools
import Member
import Memoca

RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
BLUE="\033[94m"
ENDC="\033[0m"
UNDER="\033[4m"


def bonus(m):
    return math.floor((100 + (int(m.getLove()) -1) / 254 * 100) * 10) / 1000

def power(m, c):
    return math.floor(int(c.getATK()) * (1 if m.identity() != c.identity() and m.identity() != ("0", "0") else \
                                         bonus(m)))

def selfpower(m):
    return power(m, m.getCard(0))+power(m, m.getCard(1))

def selfmemoca(lst, m):
    return sorted(lst, key=lambda x: x.identity() != m.identity())[0:idcount(lst, m)]

def whosememoca(c, m):
    return sorted(m, key=lambda x: x.identity() != c.identity())[0]

def idcount(lst, m):
    cnt=0
    for i in lst:
        if i.identity() == m.identity():
            cnt += 1
    return cnt


card=[]
mem=[]
dummy_card=Memoca.Memoca()
rare={"SR":1, "uSR":2, "UR":3, "EXR":4}

f=open("memoca.csv", "r")
for i in f:
    i=i.replace("\n", "").split(",")
    card.append(Memoca.Memoca(i))
f.flush()
f.close()

f=open("member.csv", "r")
for i in f:
    i=i.replace("\n", "").split(",")
    mem.append(Member.Member(i))
    for i in range(2):
        mem[-1].setCard(dummy_card, i)

f.flush()
f.close()

front=[mem[0], mem[1], mem[2], mem[3], mem[4]]

sorted(mem, key=lambda x: x.identity() != ("0", "1"))[0].setLove("179")


for i, j in itertools.product(range(len(mem)), range(len(card))):
    if(mem[i].identity() == card[j].identity()):
        if int(mem[i].getCard(0).getATK()) == 0:
            mem[i].setCard(card[j], 0)
        else:
            if rare[mem[i].getCard(0).getRare()] < rare[card[j].getRare()]:
                mem[i].setCard(mem[i].getCard(0), 1)
                mem[i].setCard(card[j], 0)
            else:
                mem[i].setCard(card[j], 1)

front = sorted(mem, key=lambda x: selfpower(x)*-1)[:5]

cand = sorted(card, key=lambda x: int(x.getATK())*-1)

for i in front:
    for j, k in itertools.product(i.getCard(), cand):
        if k==j:
            cand.remove(j)

assist_card = sorted(cand, key=lambda x: int(x.getATK())*-1)
total_assist=0
assist_prob=0
for i in assist_card[:10]:
    total_assist += int(i.getATK())
    assist_prob += 0.5*(int(i.getConv())+1)
assist_card[:10] = sorted(cand, key=lambda x: (int(x.getATK()) + math.floor(total_assist/5)*0.5*(int(x.getConv())+1)/100) * -1)
for i in assist_card[10:]:
    if int(assist_card[9].getATK()) + math.floor(total_assist/5)*0.5*(int(assist_card[9].getConv())+1)/100 <\
       int(i.getATK()) + math.floor((total_assist-int(assist_card[9].getATK())+int(i.getATK()))/5)*0.5*(int(i.getConv())+1)/100:
        total_assist += int(i.getATK()) - int(assist[9].getATK())
        assist_card[9] = i
        assist_card[:10] = sorted(assist_card[:10], key=lambda x: (int(x.getATK()) + math.floor(total_assist/5)*0.5+(int(x.getConv())+1)/100) * -1)

assist_card = assist_card[:10]
for i in sorted(cand, key=lambda x: int(x.getATK()) * bonus(whosememoca(x, mem)) * -1)[:10]:
    assist_card.append(i)

assist_card = list(set(assist_card))

assist_cand=[]
for i in assist_card:
    assist_cand.append(whosememoca(i, mem))

assist_cand = list(set(assist_cand))

assist_lst=[]
for i in range(5):
    assist_lst.append([assist_cand[i]] + assist_cand[i].getCard())

count=0
total_assist=0
for i in list(itertools(assist_cand, 5)):
    if count%100 == 0:
        print("\r" + "{:5d}".format(count) + "/" + str(len(itertools(assist_cand, 5))) + "\t",end="")
    for j in i:
        total_assist += selfpower(j)
    i = sorted(i, key=lambda x: (int(x.getCard(1)) + math.floor(total_assist/5)*0.5*(int(x.getCard(1).getConv())+1)/100) * -1)
    for j in assist_card:
        print("",end="")
#いま必要なもの：そのカードを他のメンバーが持ってるかの判定
#   アシストメンバー用のATK評価

"""
assist = sorted(cand, key=lambda x: int(x.getATK())*-1)
total_assist=0
assist_prob=0
for i in assist[:10]:
    total_assist += int(i.getATK())
    assist_prob += 0.5*(int(i.getConv())+1)
assist[:10] = sorted(cand, key=lambda x: (int(x.getATK()) + math.floor(total_assist/5)*0.5*(int(x.getConv())+1)/100) * -1)
for i in assist[10:]:
    if int(assist[9].getATK()) + math.floor(total_assist/5)*0.5*(int(assist[9].getConv())+1)/100 <\
       int(i.getATK()) + math.floor((total_assist-int(assist[9].getATK())+int(i.getATK()))/5)*0.5*(int(i.getConv())+1)/100:
        total_assist += int(i.getATK()) - int(assist[9].getATK())
        assist[9] = i
        assist[:10] = sorted(assist[:10], key=lambda x: (int(x.getATK()) + math.floor(total_assist/5)*0.5+(int(x.getConv())+1)/100) * -1)
"""



"""
total_atk=0
for i in front:
    total_atk += selfpower(i)
    print(YELLOW + ("　　" + i.getName())[-6:] + " ATK:"+ UNDER + "{:>6d}".format(selfpower(i)) + ENDC +
          "\tbonus: " + "{:03.3f}".format(bonus(i)))
    for j in range(2):
        print("\t" + "{:6d}".format(power(i, i.getCard(j))) + "{:>4}".format(i.getCard(j).getRare()) +
              ((" +" + i.getCard(j).getConv()) if i.getCard(j).getConv() != "0" else "") +
              "\t" + i.getCard(j).getName())
print("total_atk: " + YELLOW + UNDER + str(total_atk) + ENDC)
"""

