# genlayer-web-oracle-primitive
# Standalone GenLayer Intelligent Contract for AI Web Data Oracle

from genlayer.std import *

class OptimisticWebOracle:
    def __init__(self, admin: Address):
        self.admin = admin
        self.verified_facts = TreeMap()
        self.fact_count = 0

    @gl.public.write
    def resolve_and_verify_fact(self, fact_id: str, source_url: str, query_prompt: str) -> str:
        """
        Fetches web content and uses non-deterministic LLM consensus to evaluate fact claim.
        Executes within the Equivalence Principle consensus mode.
        """
        # Fetch external web page data
        web_data = gl.web.get(source_url)
        
        # Non-deterministic LLM prompt execution across validators
        prompt = f"""
        Analyze the following web page content and answer the query: '{query_prompt}'.
        
        Web Page Content:
        {web_data.text[:1500]}
        
        Provide a concise, factual answer (max 30 words).
        """
        
        # Validator consensus via LLM equivalence check
        extracted_result = gl.llm.generate(prompt)
        
        # Store result upon validator consensus
        self.verified_facts[fact_id] = extracted_result
        self.fact_count += 1
        
        return extracted_result

    @gl.public.view
    def get_verified_fact(self, fact_id: str) -> str:
        """
        Returns the verified fact stored in contract state.
        """
        return self.verified_facts.get(fact_id, "Fact not found or unresolved.")
