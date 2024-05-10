import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv
load_dotenv()


class ChromaDB:
    __client = chromadb.PersistentClient(path=os.getenv("CHROMADB_PATH"))
    __openai_ef = OpenAIEmbeddingFunction(api_key=os.getenv(
        "OPENAI_API_KEY"), model_name="text-embedding-3-small")

    @staticmethod
    def get_or_create_collection():
        return ChromaDB.__client.get_or_create_collection(name=os.getenv("CHROMADB_NAME"), embedding_function=ChromaDB.__openai_ef)

    @staticmethod
    def get_collection():
        return ChromaDB.__client.get_collection(name=os.getenv("CHROMADB_NAME"))
