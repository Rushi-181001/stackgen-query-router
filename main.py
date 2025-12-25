from router import Router

def main():
    print("="*50)
    print("StackGen Query Router")
    print("="*50)
    print("\nExamples:")
    print("  1. Show my open pull requests")
    print("  2. What issues are assigned to me?")
    print("  3. What's the weather today?")
    print("\nType 'quit' to exit\n")
    
    router = Router()
    
    while True:
        query = input("Query> ").strip()
        
        if not query:
            continue
        
        if query.lower() == 'quit':
            print("Goodbye!")
            break
        
        answer = router.route_question(query)
        print("\nAnswer: " + answer + "\n")
        print("-"*50 + "\n")

if __name__ == "__main__":
    main()