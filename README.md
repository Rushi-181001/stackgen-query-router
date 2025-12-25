# StackGen Query Router (Python Track)

## Overview

This project is a **simple query router** built in Python, designed to route user questions to the appropriate agent depending on intent of the input.

There are **two mock agents** implemented in this task:

1. **GitHubAgent** – Handles questions about pull requests, repositories, and commits.
2. **LinearAgent** – Handles questions about issues, tasks, and assignments.

If a question does not match any agent, the router will politely respond:

```
"I cannot answer this question"
```


## How It Works

1. **Router**

   * The `Router` class is responsible for determining which agent should handle a query.
   * Keyword-based intent detection is used (e.g., `"pull request"` → `GitHubAgent`).
   * This keeps the system simple and easy to extend for future agents as we can extend just by adding agents files.

2. **Agents**

   * `GitHubAgent` and `LinearAgent` are completely **self-contained**.
   * Each agent has mocked data to simulate real responses .
   * Agents decide **what** response to give based on the nature of the query provided.

3. **CLI Interface**

   * Users interact with the system through a simple **command-line interface**.
   * Example queries:
  
     ```
     Show my open pull requests
     What issues are assigned to me?
     What's the weather today?
     ```
   * Type `quit` to exit the program.

---

## Project Structure

```
project/
│── main.py              # CLI entry point
│── router.py            # Routes questions to its reaponsible agent
│── agents/
│   ├── github_agent.py  # GitHubAgent
│   └── linear_agent.py  # LinearAgent
│── tests/
│   └── test_router.py   # Unit tests for router
│── README.md
```

--- 

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd project
```

2. Run the CLI:

```bash
python main.py
```

3. Type your query and press Enter. Example:

```
Query> Show my open pull requests

or

Query> Show my closed pull requests

```

4. To exit, type:

```
quit
```

---

## Running Tests

This project includes simple unit tests using **pytest**.

1. Install pytest (if not already installed):

```bash
pip install pytest
```

2. Run tests:

```bash
pytest
```

You should see output indicating all tests passed.

---

## Assumptions & Design Choices

* In this assignment **Keyword-based routing** is implemented .

  * In a production system, a proper NLP intent classifier would be ideal as it can be more accurate in understanding which agent is best for that particular input query.
* Each agent is **independent** to allow easy extension (easy to add more agents in future).
* Mock data is hard-coded to simulate realistic responses.
* CLI was chosen for simplicity and easy demonstration of routing behavior.
* Minor logging (`print` statements) is included to show routing decisions, making it easy to understand why a question went to a certain agent.

---

## Example Interaction

```
==================================================
StackGen Query Router
==================================================

Examples:
  1. Show my open pull requests
  2. What issues are assigned to me?
  3. What's the weather today?

Type 'quit' to exit

Query> show my closed pr     
→ Routing to GitHubAgent (found keyword: 'pr')

Answer: You have 1 closed pull requests:
  - PR #3: Update README


--------------------------------------------------

Query>

---

## Notes


* Tests cover **all main routing scenarios** (GitHub, Linear, and unknown queries).
