import unittest
import time
import hashlib
from blockchain import LogBlock

class TestCreation(unittest.TestCase):
    
    # Teste la somme de deux nombres positifs
    def test_valid_hash(self):
        localtime = time.time()
        block = LogBlock(0, localtime, previous_hash="ROOT HASH", data="", authority_id="AUTHORITY", signature="signed")
        block_string = f"0ROOT HASH{localtime}AUTHORITY" 
        self.assertEqual(block.hash, hashlib.sha256(block_string.encode()).hexdigest()) 

# Cette ligne permet d'exécuter les tests si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()
