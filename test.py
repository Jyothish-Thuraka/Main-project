
# from langchain_community.llms import CTransformers
# #import CTransformers
# def web_search_assistant(query):
#     # Initialize the LLM
#     llm = CTransformers(
#         model='model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={
#             'max_new_tokens': 256,
#             'temperature': 0.5  # Slightly increased temperature for more creative responses
#         }
#     )
    
#     # Create a template for web search assistance
#     prompt_template = f"""You are a helpful web search assistant. Please help with the following query:
    
# Query: {query}

# """

#     # Get the response from the model
#     response = llm.predict(prompt_template)
#     return response

# # Example usage
# def main():
#     while True:
#         user_query = input("\nEnter your search query (or 'quit' to exit): ")
#         if user_query.lower() == 'quit':
#             break
            
#         print("\nAssistant Response:")
#         response = web_search_assistant(user_query)
#         print(response)

# if __name__ == "__main__":
#     main()


# import smtplib
# from engine.config import password
# import pywhatkit as pwk
# def sendEmail(re_mail,message):

#     pwk.send_mail("jyothishalways@gmail.com", password,"",message,re_mail,)
# re_mail="alwaysjyothish@gmail.com"
# message="hello"
# sendEmail(re_mail, message)

# import datetime
# query="what is time"

# if "time" in query:
#              now_time=datetime.datetime.now().strftime("%H:%M:%S")
#              print("the time is "+now_time)

# import pyautogui


# def spotifyAutomation():
#         query="Spotify"
#         #speak(f"Opening Spotify")  
#         query = query.replace("open", "")
#         pyautogui.press("super")
#         pyautogui.typewrite(query)
#         pyautogui.sleep(2)
#         pyautogui.press("enter")
#         pyautogui.sleep(7)
#         pyautogui.press("space")
# spotifyAutomation()

import subprocess


subprocess.call([r'dev.bat'])