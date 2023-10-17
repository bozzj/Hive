from beem.account import Account
from beem import Hive
from beem.nodelist import NodeList
nodelist = NodeList()
nodelist.update_nodes()
hive = Hive()
print()
print ('Please input a Hive username:')
acc = str(input())
account = Account(acc, blockchain_instance=hive)
print()
print("accounts muting", acc, ":")
print('\n\.join(map(str,account.get_muters(raw_name_list=True, limit=100))))
print()
