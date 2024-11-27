from .agents_base import AgentBase

class SantizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SantizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
            {"role": "system", "content": "You are an AI assistant that sanitizes medical data by removing Protected Health Information (PHI)."},
            {
                "role": "user",
                "content": (
                    "Remove all PHI form the following datat:\n\n"
                    f"{medical_data}\n\nSantize Data:"
                )
            }
        ]
        Santize_data = self.call_openai(messages, max_tokens=300)
        return Santize_data