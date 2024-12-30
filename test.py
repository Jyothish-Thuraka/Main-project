
from langchain_community.llms import CTransformers
#import CTransformers
def web_search_assistant(query):
    # Initialize the LLM
    llm = CTransformers(
        model='model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.5  # Slightly increased temperature for more creative responses
        }
    )
    
    # Create a template for web search assistance
    prompt_template = f"""You are a helpful web search assistant. Please help with the following query:
    
Query: {query}

"""

    # Get the response from the model
    response = llm.predict(prompt_template)
    return response

# Example usage
def main():
    while True:
        user_query = input("\nEnter your search query (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break
            
        print("\nAssistant Response:")
        response = web_search_assistant(user_query)
        print(response)

if __name__ == "__main__":
    main()
