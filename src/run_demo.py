# run_demo.py
# Purpose: Small demo that creates a shared Blockchain instance and simulates 3 authority nodes
# adding log entries. Use this to quickly test the POC locally.
import time
from blockchain import LogBlock

def main():
    # Create shared blockchain (POC: single in-memory chain shared by nodes)
    block = LogBlock(0, time.time(), previous_hash="ROOT HASH", data="", authority_id="AUTHORITY", signature="signed")

if __name__ == "__main__":
    main()

