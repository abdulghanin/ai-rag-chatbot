from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

# تحميل نموذج الذكاء الاصطناعي
llm = OllamaLLM(model="llama3")

# نموذج embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# تحميل قاعدة البيانات
vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

# إنشاء retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

# قالب البرومبت
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""
)

# وظيفة RAG
def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = prompt_template.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response
if __name__ == "__main__":

    question = input("Ask a question: ")

    answer = ask_question(question)

    print("\nAnswer:\n")
    print(answer)