from blockchain import DodoCoin
from wallet import Wallet
from node import Node

dodo = DodoCoin()
node_1 = Node("Node-1", dodo,'')
peter_wallet = Wallet('Peter',node_1)
tony_wallet = Wallet('Tony',node_1)
strange_wallet = Wallet('Strange',node_1)
bruce_wallet = Wallet('Bruce',node_1)
steve_wallet = Wallet('Steve',node_1)
carol_wallet = Wallet('Carol',node_1)
scarlet_wallet = Wallet('Scarlet',node_1)
# nebula_wallet = Wallet('Nebula')
# natasha_wallet = Wallet("Natasha")
# shuri_wallet = Wallet('Shuri')
#print("peter privatekey checking ",peter_wallet.private_key)
# Register each wallet with Blockchain
dodo.register_wallet(peter_wallet.user, peter_wallet.public_key)
dodo.register_wallet(tony_wallet.user, tony_wallet.public_key)
dodo.register_wallet(strange_wallet.user, strange_wallet.public_key)
dodo.register_wallet(bruce_wallet.user, bruce_wallet.public_key)
dodo.register_wallet(steve_wallet.user, steve_wallet.public_key)
dodo.register_wallet(carol_wallet.user, carol_wallet.public_key)
dodo.register_wallet(scarlet_wallet.user, scarlet_wallet.public_key)
# dodo_chain.register_wallet(nebula_wallet.user, nebula_wallet.public_key)
# dodo_chain.register_wallet(natasha_wallet.user, natasha_wallet.public_key)
# dodo_chain.register_wallet(shuri_wallet.user, shuri_wallet.public_key)
#peter_wallet.serialize_private_key()
#peter_wallet.deserialize_private_key()
#tony_wallet.serialize_private_key_to_file("C:\\Users\\OneDrive\\Documents\\project\\C07-Project_01\\C07-Project_01 Shell Code\\dodocoin_3\\")
#tony_wallet.serialize_public_key_to_file("C:\\Users\\OneDrive\\Documents\\project\\C07-Project_01\\C07-Project_01 Shell Code\\dodocoin_3\\")


#node_1 = Node("Node-1", dodo,'')
# node_2 = Node("Node-2", dodo)

# print(node_1)
# print(node_2)

# Show list of registered wallets.
# print("\nList of registered wallets.")
# dodo.list_wallets()
#
transaction = peter_wallet.initiate_transaction(tony_wallet.user, 20)
# node_1.add_new_transaction(transaction)
print("\nList of pending transactions.")
dodo.list_pending_transactions()
node_1.create_new_block()
node_1.show_chain()
print()
node_2 = Node("Node-2", dodo,node_1)
node_2.connect_with_new_node(node_1, True)
print(node_2)
print()


peter_wallet.initiate_transaction(bruce_wallet.user, 25)
# node_1.add_new_transaction(transaction)
bruce_wallet.initiate_transaction(peter_wallet.user, 50)
# node_1.add_new_transaction(transaction)
tony_wallet.initiate_transaction(bruce_wallet.user, 50)
# node_1.add_new_transaction(transaction)
#node_1.create_new_block()
print("\nList of pending transactions.")
dodo.list_pending_transactions()
# transaction = scarlet_wallet.initiate_transaction(peter_wallet.user, 25)
# node_1.add_new_transaction(transaction)
# transaction = carol_wallet.initiate_transaction(steve_wallet.user, 50)
# node_1.add_new_transaction(transaction)
# transaction = steve_wallet.initiate_transaction(bruce_wallet.user, 50)
# node_1.add_new_transaction(transaction)
#
node_1.create_new_block()
# print("\nPrinting blockchain.")
print(node_1)
node_3 = Node("Node-3", dodo, node_1)
node_2.connect_with_new_node(node_1, True)
node_3.connect_with_new_node(node_1, True)
print("this is after adding ttobruce",node_2)
print(node_3)
print()


#print(node_2)
#print(node_3)
print("showing connected nodes here ")
node_1.show_connected_nodes()
node_2.show_connected_nodes()
node_3.show_connected_nodes()



#node_1 = Node("Node_1", dodo,'')
sunil_wallet = Wallet('Sunil', node_2)
harsh_wallet = Wallet('Harsh', node_2)
dodo.register_wallet(sunil_wallet.user, sunil_wallet.public_key)
dodo.register_wallet(harsh_wallet.user, harsh_wallet.public_key)

sunil_wallet.initiate_transaction("Harsh", 50)
sunil_wallet.initiate_transaction("Harsh", 20)

node_2.create_new_block()
node_2.show_chain()

#node_2 = Node("Node_2", dodo, node_1)
#node_2.show_chain()

dodo.update_difficulty_level(3)

harsh_wallet.initiate_transaction("Sunil", 50)
harsh_wallet.initiate_transaction("Sunil", 20)
peter_wallet.initiate_transaction(bruce_wallet.user, 25)
# node_1.add_new_transaction(transaction)
bruce_wallet.initiate_transaction(peter_wallet.user, 50)
# node_1.add_new_transaction(transaction)
tony_wallet.initiate_transaction(bruce_wallet.user, 50)

#node_1.connect_with_new_node(node_2)
node_1.create_new_block()
node_2.connect_with_new_node(node_1, True)
node_3.connect_with_new_node(node_1, True)
node_1.show_chain()
node_2.show_chain()
node_3.show_chain()
