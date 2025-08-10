# 🗂️ AI-Powered Task Manager (MCP Server + Claude Desktop Integration)

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MCP](https://img.shields.io/badge/MCP-FastMCP-orange)
![Local](https://img.shields.io/badge/deployment-local-lightgrey)
![Claude Desktop](https://img.shields.io/badge/AI-Claude%20Desktop-8A2BE2)

Ever wished your **AI assistant** could actually **manage your tasks** instead of just talking about them?
That’s exactly what I built — and it runs 100% locally for privacy and speed.

A **locally deployed MCP server** for managing your daily tasks with **Claude Desktop integration**.  
Get a **privacy-first**, **AI-assisted** task management system that runs entirely on your machine.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| ✅ **Add Tasks** | Create tasks with custom priorities & due dates |
| 📋 **List Tasks** | View all or filter by `pending` / `done` |
| ✔️ **Mark Complete** | Search by name & mark as done |
| ⏰ **Smart Reminders** | Alerts for today, tomorrow & overdue tasks |
| 📅 **Today's Tasks** | Quick access to tasks due today |
| 🔒 **Local Privacy** | Runs entirely on your device — no cloud storage |
| 🤖 **AI Integration** | Seamless interaction with Claude Desktop |

---

## 📦 Installation

### **Prerequisites**
- Python **3.7+**
- **MCP FastMCP** library
- **Claude Desktop** installed

### **Setup**
```bash
uv install mcp
git clone https://github.com/arnav1827/MCP_1.git
cd MCP_1
uv run mcp install server.py
```

## **File Structure**
```txt
[Task] : Complete project report
[Priority] : High
[Due] : 2024-12-15
[Status] : Pending
----
[Task] : Buy groceries
[Priority] : Medium
[Due] : None
[Status] : Done
----
```

## **Task Lifecycle**
```css
New Task → [Status: Pending] → Mark Done → [Status: Done]
```

## **🛠 Error Handling**

  - Creates task file if missing
  - Checks date formats
  - Handles empty files
  - Validates required fields

## **Note**
  - Every function is documented with clear in-code comments explaining its purpose, parameters, and logic flow — making the codebase easy to maintain and extend.
  - It is necessary which not only help readers but also the LLMs when the interact with these functions as they add further information to every LLM call
