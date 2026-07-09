import google.generativeai as genai

from src.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

print("Loaded API Key:", GOOGLE_API_KEY)


SYSTEM_PROMPT = """
You are IITB Insti-Assist.

Answer ONLY from the provided context.

If the answer cannot be directly supported by the context, reply exactly:

I don't know based on the provided IIT Bombay documents.

Do not use outside knowledge.
Do not infer missing information.
Do not speculate.

If the answer exists, mention the document name and page number.

Keep the answer concise.
"""


def generate_answer(question, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:
        context += f"""
SOURCE: {chunk['source']}
PAGE: {chunk['page']}

{chunk['text']}

----------------------------------------
"""

    prompt = f"""
{SYSTEM_PROMPT}

Retrieved Context:

{context}

Question:
{question}

Answer:
"""
    print("\n" + "=" * 100)
    print("CONTEXT SENT TO GEMINI")
    print("=" * 100)
    print(context)
    print("=" * 100 + "\n")
    response = model.generate_content(prompt)

    return response.text.strip()