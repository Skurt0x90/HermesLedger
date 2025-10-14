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

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#merkle root Le Merkle Root permet de vérifier l'intégrité des transactions d’un bloc sans avoir besoin d'examiner toutes les transactions individuellement
class LogBlock:
    def __init__(self, index, timestamp, previous_hash, data, authority_id, signature):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.authority_id = authority_id
        self.hash = self.compute_hash()
        if self.hash != hashlib.sha256("".encode()).hexdigest():
            logging.debug(f"[CREATION SUCCESS] : hash = {self.hash}")  # Affiche les valeurs de a et b au niveau DEBUG

    def compute_hash(self):
            block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.authority_id}"
            return hashlib.sha256(block_string.encode()).hexdigest()

