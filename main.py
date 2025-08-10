from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta
import os

mcp = FastMCP("AI To-Do-Manager")
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.txt')

# Function to check whether the tasks file exist or not
def ensure_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            f.write('')
            
@mcp.tool()
def add_task(task : str, priority : str = "Medium", due : str = None) -> str:
    """Add a new task to the tasks list.
    
       Args:
            task (str): The task to be added.
            priority (str): The priority of the task. Default is Medium.
            due (str): The due date of the task. Default is None.
       
       Returns:
            str: The task ID.
    """
    
    ensure_file()
    due_date = due or 'None'
    with open(TASKS_FILE, 'a') as f:
        f.write(f"[Task] : {task}\n[Priority] : {priority}\n[Due] : {due_date}\n[Status] : Pending\n----\n")
    return f"Task '{task}' added successfully !"

@mcp.tool()
def list_tasks(show : str = 'all') -> str:
    """List all the tasks.
    Args:
         show (str): Filter tasks ('all', 'pending', or 'done')
    
    Returns:
         str: List of filtered tasks
    """

    ensure_file()
    with open(TASKS_FILE, 'r') as f:
        tasks = f.read().strip().split("----")
        
    filtered = []
    
    for task in tasks:
        if not task.strip():
            continue
        
        status = [line for line in task.split('\n') if line.startswith("[Status] :")][0].split(":")[1].strip().lower()
        
        if show == 'all':
            filtered.append(task.strip())
        elif show == 'pending' and status == 'pending':
            filtered.append(task.strip())
        elif show == 'done' and status == 'done':
            filtered.append(task.strip())
            
    return "\n---\n".join(filtered) if filtered else "No tasks found."

@mcp.tool()
def mark_done(task_name : str) -> str:
    """Mark a task as done by matching its name.
    
    Args:
         task_name (str) : Name of the task to mark as done.
         
    Returns:
         str : Success or Error message
    """
    
    ensure_file()
    with open(TASKS_FILE, 'r') as f:
        tasks = f.read().strip().split("----")
    
    updated_tasks = []
    found = False
    
    for task in tasks:
        if not task.strip():
            continue
    
        if task_name.lower() in task.lower() and "[Status] : Pending" in task:
            task = task.replace("[Status] : Pending", "[Status] : Done")
            found = True
        updated_tasks.append(task.strip())
        
    if found:
        with open(TASKS_FILE, 'w') as f:
            f.write("\n----\n".join(updated_tasks))
            if updated_tasks:
                f.write("\n----\n")
        return f"Task updated successfully!"
    else:
        return f"Task not found."
            

@mcp.tool()
def check_reminders() -> str:
    """
    Check for tasks that are due today, tomorrow, or overdue.
    """
    
    ensure_file()
    today = datetime.now().date()
    tomorrow = today + timedelta(days = 1)
    
    with open(TASKS_FILE, "r") as f:
        tasks = f.read().strip().split("----")
    
    reminders = []
    
    for task in tasks:
        if not task.strip():
            continue
        
        lines = task.strip().split("\n")
        due_lines = [line for line in lines if line.startswith("[Due] :")]
        status_lines = [line for line in lines if line.startswith("[Status] :")]
        task_lines = [line for line in lines if line.startswith("[Task] :")]
        
        if not due_lines or not status_lines or not task_lines:
            continue
                
        due_str = due_lines[0].split(":", 1)[1].strip()
        status = status_lines[0].split(":", 1)[1].strip()
        task_name = task_lines[0].split(":", 1)[1].strip()
        
        if due_str != "None" and status == "Pending":
            try:
                due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
                if due_date == today:
                    reminders.append(f"⚠️ Due TODAY: {task_name}")
                elif due_date == tomorrow:
                    reminders.append(f"⏳ Due TOMORROW: {task_name}")
                elif due_date < today:
                    reminders.append(f"❌ OVERDUE: {task_name}")
            except ValueError:
                continue

    return "\n".join(reminders) if reminders else "No upcoming or overdue tasks."
  
@mcp.resource("tasks://today")
def get_today_tasks() -> str:
    """Get tasks for today."""
    
    ensure_file()
    today = datetime.now().strftime("%Y-%m-%d")
    
    with open(TASKS_FILE, 'r') as f:
        tasks = f.read().strip().split("----")
        
    today_tasks = [task.strip() for task in tasks if task.strip() and f'[Due] : {today}' in task]
    
    return "\n---\n".join(today_tasks) if today_tasks else "No tasks found."