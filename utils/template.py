from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage

system = ChatMessage.from_system(''' 1. You are a Professional who analyse internet pages to provide relevant information to users.\n 
    You are given a query: {{query}}, Think step by step to response to the query, and provide a response.\n
    You should only response that is relevant to the query from the Context provided below.\n
    Context:
    {% for document in documents %}
        content: {{document.content}} from url: {{document.url}}
    {% endfor %}
    
    2. Condition: 
    * The response should be relevant to the query. If the query is not relevant, you should respond "I'm sorry, I don't know the answer to that question."\n
    * You should response with your reasoning and provide a response that is concise and accurate.
    * provide the response in the format: Reasoning: <Your reasoning>, Response: <Your response>
    Example format of response:
        Reasoning:"The capital of Nigeria is Abuja. I found this information from en.wikipedia.org/wiki/Nigeria"
        Response: "The capital of Nigeria is Abuja"
    3. If the query is relevant, you should provide a response that is concise and accurate.
    
    Respoonse:
    ''')
user_2 = ChatMessage.from_user("Please provide a response to the query, Assume I cannot see the context, provide the response in the format: Reasoning: <Your reasoning>, Response: <Your response>, by thinking step by step to response to the query")

template = [system, user_2]

builder = ChatPromptBuilder(template=template, required_variables= ['query', 'documents'])
