# Hashnode Blog Writer Agent

This project is an **AI-powered blog writing assistant** built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and [OpenAI models](https://platform.openai.com/).  
It can generate, refine, and publish blog posts to **Hashnode** with human-in-the-loop capabilities.

---

## 🚀 Features
- Interactive chatbot flow powered by LangGraph
- Blog post generation in **Markdown**
- Uses **Tavily Search** for real-time web information
- Human-in-the-loop interruptions for assistance
- **One-click publishing** to Hashnode via GraphQL API
- MongoDB checkpointing for conversation memory
- Devcontainer setup with Docker Compose (includes MongoDB, Neo4j, Qdrant, Valkey)

---

## 📂 Project Structure
```
madhavarora03-hashode-blog-writer-agent/
├── requirements.txt        # Python dependencies
├── src/
│   ├── graph.py            # LangGraph state and flow definition
│   ├── main.py             # CLI entry point for chatbot
│   ├── prompt.py           # System prompt & few-shot examples
│   └── tools.py            # Tools: publish, human assistance, web search
└── .devcontainer/
    ├── devcontainer.json   # VS Code devcontainer setup
    ├── docker-compose.yaml # Multi-service environment
    └── Dockerfile          # Python base image
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/madhavarora03/madhavarora03-hashode-blog-writer-agent.git
cd madhavarora03-hashode-blog-writer-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory with the following:
```env
OPENAI_API_KEY=your_openai_api_key
HASHNODE_API_ENDPOINT=https://gql.hashnode.com
HASHNODE_API_KEY=your_hashnode_api_key
HASHNODE_PUBLICATION_ID=your_publication_id
```

### 4. Run with Docker (Devcontainer)
```bash
docker-compose -f .devcontainer/docker-compose.yaml up -d
```

### 5. Start the Agent
```bash
python src/main.py
```

---

## 💡 Usage
- Enter a **title and keywords** to generate a blog post.
- The agent will:
  1. Search the web (if needed)
  2. Generate blog content in Markdown
  3. Ask for your feedback
  4. Publish to Hashnode when approved

---

## 🧰 Tools
- **publish_article** → Publishes the final blog to Hashnode
- **human_assistance** → Requests user input during interruptions
- **search_tool (Tavily)** → Retrieves up-to-date web content

---

## 🗄️ Services in Devcontainer
- **MongoDB** → Conversation checkpoints
- **Qdrant** → Vector database (optional)
- **Valkey** → In-memory store
- **Neo4j** → Graph database

---

## 📜 License
MIT License

---

## ✨ Author
Developed by **Madhav Arora**
