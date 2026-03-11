import sympy
import json

class LogicGateValidator:
    """
    Logic-Gate-v1: Deterministic Validation Kernel.
    Designed for high-precision auditing of LLM outputs in STEM datasets.
    """
    def __init__(self):
        self.version = "1.0.0-alpha"
        self.engine = "Symbolic-Logic-v1"

    def verify_symbolic_step(self, llm_step, reference_logic):
        """
        Calculates the symbolic difference between LLM output and Ground Truth.
        Returns 'VALIDATED' only if the logical identity is preserved (Difference = 0).
        """
        try:
            # Converting raw strings to symbolic expressions
            # This is where we catch "Hallucinated Logic"
            expr_llm = sympy.simplify(llm_step)
            expr_ref = sympy.simplify(reference_logic)
            
            # The core deterministic check: (A - B) must be 0 for identity
            discrepancy = sympy.simplify(expr_llm - expr_ref)
            
            if discrepancy == 0:
                return {
                    "status": "VALIDATED",
                    "integrity_score": 1.0,
                    "method": self.engine
                }
            else:
                return {
                    "status": "REJECTED",
                    "error_type": "Logical_Inconsistency",
                    "discrepancy_found": str(discrepancy)
                }
        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Parsing Error: {str(e)}"
            }

def run_technical_demo():
    validator = LogicGateValidator()
    
    print(f"--- [Logic-Gate-v1] Audit Session Initialized ---")
    print(f"Target: Identifying LLM Hallucinations in Algebra\n")

    # Scenario 1: Common AI Hallucination
    # LLM claims (x+1)^2 is x^2 + 1
    print(f"Step 1: Auditing claim '(x + 1)^2 = x^2 + 1' ...")
    audit_1 = validator.verify_symbolic_step("x**2 + 1", "(x + 1)**2")
    print(f"Result: {audit_1['status']} | Reason: {audit_1.get('error_type', 'N/A')}")
    print(f"Discrepancy: {audit_1.get('discrepancy_found', 'None')}\n")

    # Scenario 2: Valid Logic
    # LLM claims (x-y)(x+y) is x^2 - y^2
    print(f"Step 2: Auditing claim '(x - y)(x + y) = x^2 - y^2' ...")
    audit_2 = validator.verify_symbolic_step("x**2 - y**2", "(x - y)*(x + y)")
    print(f"Result: {audit_2['status']} | Integrity: {audit_2.get('integrity_score', 0)}")

    print(f"\n--- Audit Session Completed ---")

if __name__ == "__main__":
    run_technical_demo()
