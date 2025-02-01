try:
    from utils.template import builder
    from utils.relevance import Relevance
except:
    from template import builder
    from relevance import Relevance
from haystack.components.generators.chat import HuggingFaceAPIChatGenerator
from haystack.utils import Secret
from dotenv import load_dotenv
import os
load_dotenv()
__relevance = Relevance()
api_type = os.getenv("api_type")
model = os.getenv("model_id")
generator = HuggingFaceAPIChatGenerator(api_type=api_type,
                                        api_params={"model": model},
                                        token=Secret.from_env_var("HF_API_TOKEN"))

def agent(question):
    resposne = __relevance.store_relevance(question)
    res = builder.run(query= question, documents=resposne)
    res = res['prompt']
    return generator.run(res)['replies'][0].content  

if __name__ == "__main__":
    print(agent("What is the capital of Nigeria? from en.wikipedia.org/wiki/Nigeria"))

