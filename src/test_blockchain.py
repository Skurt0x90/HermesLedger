import unittest
import time
import hashlib
from blockchain import LogBlock, Blockchain

class TestBlockchain(unittest.TestCase):
    
    
    def test_block_creation(self):
        localtime = time.time()
        block = LogBlock(0, localtime, previous_hash="ROOT HASH", data="", authority_id="AUTHORITY", signature="signed")
        block_string = f"0ROOT HASH{localtime}AUTHORITY" 
        self.assertEqual(block.hash, hashlib.sha256(block_string.encode()).hexdigest()) 

    
    def test_blockchain_creation(self):
        blockchain = Blockchain("authority")
        self.assertEqual(len(blockchain.chain), 1) and self.assertEqual(blockchain.chain[0].data, "GENESIS BLOCK")

    def test_add_block(self):
        blockchain = Blockchain("authority")
        length_before = len(blockchain.chain)
        blockchain.add_block("NEW BLOCK", "AUTHORITY", "SIGNATURE")
        self.assertEqual(blockchain.chain[-1].data, "NEW BLOCK") and self.assertEqual(len(blockchain.chain), length_before+1)

    def test_chain_validation_true(self):
        blockchain = Blockchain("authority")
        blockchain.add_block("NEW BLOCK", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK2", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK3", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK4", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK5", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK6", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK7", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK8", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK9", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK10", "AUTHORITY", "SIGNATURE")
        self.assertEqual(blockchain.is_chain_valid(), True)

    def test_chain_validation_false(self):
        blockchain = Blockchain("authority")
        blockchain.add_block("NEW BLOCK", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK2", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK3", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK4", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK5", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK6", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK7", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK8", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK9", "AUTHORITY", "SIGNATURE")
        blockchain.add_block("BLOCK10", "AUTHORITY", "SIGNATURE")
        blockchain.chain[2].hash = "fakehash"
        self.assertEqual(blockchain.is_chain_valid(), False)


# Cette ligne permet d'exécuter les tests si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()
