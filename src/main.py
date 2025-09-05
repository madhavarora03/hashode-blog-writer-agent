from typing import cast

from langchain_core.runnables.config import RunnableConfig
from langgraph.checkpoint.mongodb import MongoDBSaver
from rich.console import Console

from graph import State, create_chat_graph
from prompt import SYSTEM_PROMPT

console = Console()

if __name__ == "__main__":
    DB_URI = "mongodb://admin:admin@mongodb:27017"
    config = {"configurable": {"thread_id": "1024"}}

    with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
        graph = create_chat_graph(checkpointer)

        while True:
            user_input = console.input("> ")
            state = State(
                messages=[{"role": "system", "content": SYSTEM_PROMPT},
                          {"role": "user", "content": user_input}]
            )
            for event in graph.stream(
                state,
                config=cast(RunnableConfig, config),
                stream_mode="values"
            ):
                if "messages" in event:
                    event["messages"][-1].pretty_print()
