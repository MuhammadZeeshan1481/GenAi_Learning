class AgentProtocolWrapper:
    def call_agent(self, agent_func, *args, **kwargs):
        try:
            result = agent_func(*args, **kwargs)
            return {"status": "success", "output": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
