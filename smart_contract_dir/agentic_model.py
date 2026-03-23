# agentic_model.py

"""
Goal: Package agent interactions as transactions

Smart contracts can check agent behavior or override malicious outputs when system limits are crossed
"""

import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545' 

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address)) 

web3.eth.defaultAccount = web3.eth.accounts[0]

# Setting the default account (so we don't need 
#to set the "from" for every transaction call)

# Path to the compiled contract JSON file
compiled_contract_path = '/Users/homepro/agentic-cybersecurity-architecture/agentic-cybersecurity-architecture/smart_contract_dir/build/contracts/agentic_smart_contract.json' 

# Deployed contract address (see `migrate` command output: 
# `contract address`)
# Do Not Copy from here, contract address will be different 
# for different contracts.
deployed_contract_address = '0x21B63026F42894d0645FbE4CBC5d5F85C0F0E22D'

# load contract info as JSON
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  
    
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']

# Fetching deployed contract reference
contract = web3.eth.contract(
    address = deployed_contract_address, abi = contract_abi)


class AgenticSecurityAgent:
    def __init__(self):
        self.memory = []
        self.trust_threshold = 0.8

    def sense(self, input_data):
        print("Collecting telemetry...") #automated process of collecting data from distributed/remote sources
        return {"anomaly_score": 0.9, "source": "API-Gateway"}

    def reflect(self, data):
        print("Reflecting on context...")
        if data["anomaly_score"] > self.trust_threshold:
            return "High Threat"
        return "Normal"

    def act(self, decision):
        print(f"Taking action based on decision: {decision}")
        if decision == "High Threat":
            return "Initiate containment"
        return "Allow flow"

if __name__ == "__main__":
    agent = AgenticSecurityAgent()
    data = agent.sense(None)
    decision = agent.reflect(data)
    action = agent.act(decision)
    print(f"Response: {action}")

    # Calling contract function (this is not persisted 
    # to the blockchain)
    output = contract.functions.packaging_actions(
        str(data),
        str(decision),
        str(action)
    ).transact()

    print(output)
