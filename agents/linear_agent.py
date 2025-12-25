class LinearAgent:
    """Handles questions about Linear (issues, tasks, etc.)"""
    
    def __init__(self):
        # Some fake issue data
        self.issues = [
            {"id": 101, "title": "Design new homepage", "assigned": True},
            {"id": 102, "title": "Fix login bug", "assigned": True},
            {"id": 103, "title": "Write documentation", "assigned": False},
            {"id": 104, "title": "Update API docs", "assigned": False}
        ]
    
    def handle(self, question):
        # Answer Linear-related questions
        question_lower = question.lower()
        
        # Checking if the query question asking about issues
        if "issue" in question_lower or "task" in question_lower:
            
            # If asking for unassigned,shows unassigned task information
            if "unassigned" in question_lower:
                issues = [issue for issue in self.issues if not issue["assigned"]]
                response = f"You have {len(issues)} unassigned issues:\n"
                for issue in issues:
                    response += f"  - Issue #{issue['id']}: {issue['title']}\n"
                return response
            
            # If asking for assigned, shows assigned task information
            elif "assigned" in question_lower or "my" in question_lower:
                issues = [issue for issue in self.issues if issue["assigned"]]
                response = f"You have {len(issues)} issues assigned to you:\n"
                for issue in issues:
                    response += f"  - Issue #{issue['id']}: {issue['title']}\n"
                return response
            
            # Otherwise show ALL (both assigned and unassigned)
            else:
                assigned = [issue for issue in self.issues if issue["assigned"]]
                unassigned = [issue for issue in self.issues if not issue["assigned"]]
                
                response = f"You have {len(self.issues)} total issues:\n\n"
                response += f"Assigned to you ({len(assigned)}):\n"
                for issue in assigned:
                    response += f"  - Issue #{issue['id']}: {issue['title']}\n"
                
                response += f"\nUnassigned ({len(unassigned)}):\n"
                for issue in unassigned:
                    response += f"  - Issue #{issue['id']}: {issue['title']}\n"
                
                return response
                
        return "Here are your issues: 4 total (2 assigned, 2 unassigned)"
        
    
