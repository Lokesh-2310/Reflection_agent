from langgraph.graph import MessageGraph, END
from langchain_core.messages import HumanMessage
from chain import generate_chain,revisor_chain
from dotenv import load_dotenv
load_dotenv()

graph=MessageGraph()

def generate_node(state):
    return generate_chain.invoke({
        "messages":state
    })
    
def reflect_node(state):
    response=revisor_chain.invoke({"messages":state
    })
    return [HumanMessage(content=response.content)]

def should_continue(state):
    if len(state) == 4:
        return END
    else:
        return "reflect"

graph.add_node("generate",generate_node)
graph.add_node("reflect",reflect_node)
graph.set_entry_point("generate")
graph.add_edge("reflect","generate")
graph.add_conditional_edges("generate",should_continue)

app=graph.compile()


response=app.invoke([HumanMessage(content="What is overfitting?")])
