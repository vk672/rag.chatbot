def export_response_to_file(query, response):
    with open("data/report.txt", "a") as f:
        f.write(f"Query: {query}\nResponse: {response}\n{'-'*60}\n")
