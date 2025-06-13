import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict

load_dotenv()

# Define state
class GraphState(TypedDict):
    messages: list
    current_step: str

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define nodes
def generate_response(state: GraphState):
    messages = state["messages"]
    response = llm.invoke(messages[-1])
    return {
        "messages": messages + [response],
        "current_step": "completed"
    }

# Build graph
workflow = StateGraph(GraphState)
workflow.add_node("generate", generate_response)
workflow.set_entry_point("generate")
workflow.add_edge("generate", END)

app = workflow.compile()

def display_graph_html(app, filename="graph.html"):
    try:
        mermaid_code = app.get_graph().draw_mermaid()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>LangGraph Visualization</title>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.6.1/mermaid.min.js"></script>
        </head>
        <body>
            <h1>My LangGraph</h1>
            <div class="mermaid">
                {mermaid_code}
            </div>
            <script>
                mermaid.initialize({{startOnLoad: true}});
            </script>
        </body>
        </html>
        """
        
        with open(filename, "w") as f:
            f.write(html_content)
        print(f"Graph saved as HTML: {filename}")
        print(f"Open this file in your browser to view the graph")
        
    except Exception as e:
        print(f"Error creating HTML: {e}")


# Test your graph
if __name__ == "__main__":
    initial_state = {
        "messages": ["What is LangGraph?"],
        "current_step": "starting"
    }
    
    result = app.invoke(initial_state)
    print("Response:", result["messages"][-1].content)

    # Create HTML version
    display_graph_html(app)
