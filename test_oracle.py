import pytest
from genlayer.testing import direct_vm

def test_oracle_fact_resolution():
    # Setup test VM sender
    admin_address = "0x0000000000000000000000000000000000000001"
    
    # Deploy contract in direct mode
    oracle = direct_vm.deploy("contract.py", admin_address)
    
    # Mock external web response
    direct_vm.mock_web("https://example.com/news", "GenLayer mainnet launch announcement")
    
    # Mock LLM consensus output
    direct_vm.mock_llm("Analyze the following web page", "GenLayer announced mainnet release.")
    
    # Execute contract method
    result = oracle.resolve_and_verify_fact("news_01", "https://example.com/news", "What was announced?")
    
    assert "GenLayer" in result
    assert oracle.get_verified_fact("news_01") == result
