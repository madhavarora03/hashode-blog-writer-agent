from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict

from tools import tools

load_dotenv()


# Define state
class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = init_chat_model(model_provider="openai", model="gpt-4.1")
llm = llm.bind_tools(tools=tools)


def chatbot(state: State) -> State:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# Graph builder
tool_node = ToolNode(tools=tools)

builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)


def create_chat_graph(checkpointer):
    return builder.compile(checkpointer=checkpointer)
