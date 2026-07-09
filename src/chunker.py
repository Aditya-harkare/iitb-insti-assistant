from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)


def chunk_documents(documents):

    chunks = []

    for doc in documents:

        for page in doc["pages"]:

            split_chunks = splitter.split_text(page["text"])

            for i, chunk in enumerate(split_chunks):

                chunks.append({

                    "text": chunk,

                    "source": doc["source"],

                    "page": page["page"],

                    "chunk_id": i

                })

    return chunks