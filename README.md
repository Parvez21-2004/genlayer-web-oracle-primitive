# GenLayer Intelligent Contract: Optimistic Web Oracle Primitive

A production-ready standalone Intelligent Contract primitive built on GenLayer that brings off-chain web data on-chain using multi-validator AI execution and equivalence consensus.

## 🌟 Overview
This contract acts as an AI-powered oracle. It accepts a web source URL and a natural language query, fetches the web payload, and uses GenLayer's non-deterministic LLM consensus to verify facts before storing them permanently in contract state.

## ⚡ How GenLayer Consensus Is Used
- **Web Retrieval (`gl.web.get`):** Validators fetch external data independently.
- **LLM Reasoning (`gl.llm.generate`):** Each validator processes the unstructured HTML/text using an LLM.
- **Equivalence Principle:** GenLayer compares output outputs from multiple validators to achieve consensus before committing state updates.

## 🧪 How to Test in GenLayer Studio
1. Open [GenLayer Studio](https://studio.genlayer.com).
2. Create a new contract file and paste `contract.py`.
3. Deploy the contract using the Bradbury Testnet.
4. Call `resolve_and_verify_fact` with test parameters:
   - `fact_id`: `"fact_001"`
   - `source_url`: `"https://en.wikipedia.org/wiki/Ethereum"`
   - `query_prompt`: `"What is Ethereum?"`
5. Read the finalized state using `get_verified_fact("fact_001")`.
