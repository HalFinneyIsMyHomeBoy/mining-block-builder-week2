#from collections import OrderedDict
import collections
from collections import defaultdict
import statistics
import time
import copy
from typing import NamedTuple


#https://github.com/btcfoss-career/block-builder-HalFinneyIsMyHomeBoy

dataList = []

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.parents = parents
        self.weight = int(weight)


def parse_mempool_csv():
    """Parse the CSV file and return a list of MempoolTransactions."""
    with open('mempool.csv', mode ='r') as f:
        return [MempoolTransaction(*line.strip().split(',')) for line in f.readlines()]
        
def has_duplicates(lst):
    seen = set()
    dups = set()
    for item in lst:
        if item in seen:
            dups.add(item)
            #return True
        seen.add(item)
    if(len(dups) > 0):
        return True
    else:
        return False

def find_duplicates_by_attribute(obj_list, attribute_name):
    seen = set()
    duplicates = set()

    for obj in obj_list:
        value = getattr(obj, attribute_name)
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates

data = ()
data = parse_mempool_csv()
start_time = time.time()


data.sort(key=lambda x: (x.weight, -x.fee))

txCanidatesObjects = []
txCanidatesTxids = []


weightLimit = 4000000
count = 1
totalFee = 0
totalWeight = 0


def GetTxCandidates(hashMap: dict):
    # hashMap = {}
    # hashMap = data
    weightLimit = 4000000
    totalFee = 0
    totalWeight = 0 
    count = 1
    for count in range(1000):
        for item in hashMap:
            if((totalWeight + item.weight) <= weightLimit): # check if this one will put it over weight
                percentage = (item.weight / item.fee) * 100  # get weight to fee percentage
                if(percentage <= count):
                    if(item.txid not in txCanidatesTxids):

                        totalFee += item.fee
                        totalWeight += item.weight

                        candidate = MempoolTransaction(item.txid, item.fee, item.weight, item.parents)                
                        txCanidatesObjects.append(candidate)
                        txCanidatesTxids.append(item.txid)

    return hashMap
                                        #if(len(find_duplicates_by_attribute(txCanidates, 'txid')) < 1):
    #txSeen.append(item)

# for item in sorted_set:
#     if((totalWeight + item.weight) <= weightLimit):
#             #if hasattr(txCanidates, "txid") and getattr(txCanidates, "txid") == item.txid:
#         #if(len(find_duplicates_by_attribute(txCanidates, 'txid')) < 1):
#         if(item.txid not in txCanidates):
#             totalFee += item.fee
#             totalWeight += item.weight
#             txCanidates.append(item.txid)
# txSeen.append(item)
# fees = 0
# for x in hashMap:
#     fees += x.fee

hashMap = {}
hashMap = data
hashMap = GetTxCandidates(hashMap)



for tx in txCanidatesObjects:
    totalFee += tx.fee
    totalWeight += tx.weight



print('Weight filled - ' + str(totalWeight))
print('Fees Earned - ' + str(totalFee))
print('TXs - ' + str(len(txCanidatesObjects)))
print("--- %s seconds ---" % (time.time() - start_time))
if has_duplicates(txCanidatesTxids):
    print("There are duplicates in the list.")
else:
    print("There are no duplicates in the list.")

with open('block.txt','w+') as file:
    for tx in txCanidatesObjects:
        file.write(tx.txid)
        file.write('\n')


# def sortParents():
#     if(len(item.parents) > 0):
#         splitParents = item.parents.split(',')  
#         for parent in splitParents:
#             exists = next((True for x in hashMap if x.txid==parent), False)

#             #exists = any(item.txid == parent for x.txid in data)
#             if (exists):
#                 if(parent not in txParents['parent']):
#                     txParents['parent'].append(parent)
#                     totalFee += item.fee
#                     totalWeight += item.weight
#                     txCanidates['txid'].append(item.txid)
#                     txCanidates['weight'].append(item.weight)
#                     txCanidates['fee'].append(item.fee)
#                     txCanidates['parents'].append(item.parents)

#     else:
#         print('')
#     return 



#duplicate_values = find_duplicates_by_attribute(txCanidates, 'txid')

#dups = [values for key, values in txCanidates['txid'] if len(values) > 1]

# Sample set of tuples




# seen = set()
# dupes = []

# dataset = set(data)
# if dataset.count(txid) > 1:
#     print('dup')




# for x in data:
#     if x in seen:
#         dupes.append(x)
#     else:
#         seen.add(x)

#thingDict = dict(data)
# result = [key for key, values in data.items()
#                               if len(values) > 1]

# for obj in sorted(data):
#     print(obj.weight)

# #sortedDict.sort(key=len)
# for obj in sortedDict:
#     print(str(obj.txid))

