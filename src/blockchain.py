# blockchain.py
# Purpose: Minimal PoA blockchain core.
# - Block and Blockchain classes
# - Simple add_block with authority check
# - Chain validation
#
# Note: This is a POC. Signatures and networking are intentionally minimal/simulated.

import hashlib
import datetime
import json
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#merkle root Le Merkle Root permet de vérifier l'intégrité des transactions d’un bloc sans avoir besoin d'examiner toutes les transactions individuellement
"""
    Classe représentant un bloc de la blockchain.

    Attributes:
        index (int): Position du bloc dans la chaîne
        timestamp (float): Horodatage
        data (dict): Contenu du bloc (logs)
        previous_hash (str): Hash du bloc précédent
        authority_id (str): Identité du créateur
        signature (str): Signature du block
"""

class LogBlock:
    def __init__(self, index, timestamp, previous_hash, data, authority_id, signature):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.authority_id = authority_id
        self.hash = self.compute_hash()
        if self.hash != hashlib.sha256("".encode()).hexdigest():
            logging.debug(f"[BLOCK CREATION SUCCESS] : hash = {self.hash}") 
        else:
            logging.debug(f"[BLOCK CREATION FAILURE]") 

    def compute_hash(self):
            block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.authority_id}"
            return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self, authority):
        self.chain = [self.create_first_block()]
        self.authority = authority
        if len(self.chain) != 0:           
            logging.debug(f"[BLOCKCHAIN CREATION SUCCESS] : taille = {len(self.chain)}") 
        else:
            logging.debug(f"[BLOCKCHAIN CREATION FAILURE]") 
             

    def create_first_block(self):
        first_block = LogBlock(0, time.time(), previous_hash="0", data="GENESIS BLOCK", authority_id="", signature="")
        return first_block
        
    def add_block(self, data, authority_id, signature):
         previous_hash = self.chain[-1].hash
         last_index = len(self.chain)-1
         new_block = LogBlock(last_index+1, time.time(), previous_hash, data, authority_id, signature)
         self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(len(self.chain)-1):
            if self.chain[i+1].previous_hash != self.chain[i].hash:
                return False
        return True