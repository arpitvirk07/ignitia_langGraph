from typing import TypedDict
from langgraph.graph import StateGraph

from agents.ideation import ideation_agent
from agents.validation import validation_agent
from agents.branding import branding_agent


# ✅ Proper State Definition
class SystemState(TypedDict):
    idea: str
    concept: str
    analysis: str
    branding: str


workflow = StateGraph(SystemState)

# ✅ Nodes
def ideation_step(state: SystemState):
    return {"concept": ideation_agent(state["idea"])}

def market_step(state: SystemState):
    return {"analysis": validation_agent(state["concept"])}

def branding_step(state: SystemState):
    return {"branding": branding_agent(state["analysis"])}

workflow.add_node("ideation", ideation_step)
workflow.add_node("market", market_step)
workflow.add_node("branding", branding_step)

# ✅ Path Flow
workflow.set_entry_point("ideation")
workflow.add_edge("ideation", "market")
workflow.add_edge("market", "branding")
workflow.set_finish_point("branding")

# ✅ Compile
ignitia_graph = workflow.compile()
