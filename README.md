# logic-gate-verification
Automated Framework for Validating LLM Reasoning Chains via Symbolic Logic and n8n Orchestration.
graph TD
    A[LLM Output / JSON] --> B{n8n Orchestrator}
    B --> C[Python Symbolic Filter]
    B --> D[Heuristic Auditor]
    C --> E{Logic Consistency Check}
    D --> E
    E -->|FAIL| F[Refine/Regenerate]
    E -->|PASS| G[High-Fidelity Training Data]
    
    subgraph "The Validation Layer"
    C
    D
    E
    end
