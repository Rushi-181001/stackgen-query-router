from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent

class Router:
    """Decides which agent should handle each question"""
    
    def __init__(self):
        # Create our agents
        self.github_agent = GitHubAgent()
        self.linear_agent = LinearAgent()
        
        # Keywords that indicate GitHub questions
        self.github_keywords = ["pull request", "pr", "commit", "repository", "repo", "merge"]
        
        # Keywords that indicate Linear questions
        self.linear_keywords = ["issue", "ticket", "task", "assigned", "project", "unassigned"]
    
    def route_question(self, question):
        """Figure out which agent should answer this question"""
        question_lower = question.lower()
        
        # Check if it's a GitHub question
        for keyword in self.github_keywords:
            if keyword in question_lower:
                print(f"→ Routing to GitHubAgent (found keyword: '{keyword}')")
                answer = self.github_agent.handle(question)
                return answer
        
        # Check if it's a Linear question
        for keyword in self.linear_keywords:
            if keyword in question_lower:
                print(f"→ Routing to LinearAgent (found keyword: '{keyword}')")
                answer = self.linear_agent.handle(question)
                return answer
        
        # If no keywords match, we can't answer
        print("→ No matching agent found")
        return "I cannot answer this question"