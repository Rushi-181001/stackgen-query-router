class GitHubAgent:
    """Handles questions about GitHub (pull requests, repos, etc.)"""
    
    def __init__(self):
        # Some fake pull request data
        self.pull_requests = [
            {"number": 1, "title": "Add login feature", "status": "open"},
            {"number": 2, "title": "Fix bug in homepage", "status": "open"},
            {"number": 3, "title": "Update README", "status": "closed"}
        ]
    
    def handle(self, question):
        """Answer GitHub-related questions"""
        question_lower = question.lower()
        
        # Check if they're asking about open PRs
        # Check if they're asking about PRs
        if "pull request" in question_lower or "pr" in question_lower:
            
            # If asking for closed, show closed
            if "closed" in question_lower:
                prs = [pr for pr in self.pull_requests if pr["status"] == "closed"]
                response = f"You have {len(prs)} closed pull requests:\n"
                for pr in prs:
                    response += f"  - PR #{pr['number']}: {pr['title']}\n"
                return response
            
            # If asking for open, show open
            elif "open" in question_lower:
                prs = [pr for pr in self.pull_requests if pr["status"] == "open"]
                response = f"You have {len(prs)} open pull requests:\n"
                for pr in prs:
                    response += f"  - PR #{pr['number']}: {pr['title']}\n"
                return response
            
            # Otherwise show ALL (both open and closed)
            else:
                open_prs = [pr for pr in self.pull_requests if pr["status"] == "open"]
                closed_prs = [pr for pr in self.pull_requests if pr["status"] == "closed"]
                
                response = f"You have {len(self.pull_requests)} total pull requests:\n\n"
                response += f"Open ({len(open_prs)}):\n"
                for pr in open_prs:
                    response += f"  - PR #{pr['number']}: {pr['title']}\n"
                
                response += f"\nClosed ({len(closed_prs)}):\n"
                for pr in closed_prs:
                    response += f"  - PR #{pr['number']}: {pr['title']}\n"
                
                return response

        # Default response
        return "Here are your pull requests: 4 total (2 open, 2 closed)"
        
        