from router import Router

def test_route_to_github_agent():
    router = Router()
    query = "How many open pull requests do I have on GitHub?"
    response = router.route_question(query)
    assert "pull request" in response.lower()

def test_route_to_linear_agent():
    router = Router()
    query = "Show me my assigned issues in Linear."
    response = router.route_question(query)
    assert "issues" in response.lower()

def test_route_to_no_agent():
    router = Router()
    query = "What is the weather today?"
    response = router.route_question(query)
    assert response == "I cannot answer this question"
