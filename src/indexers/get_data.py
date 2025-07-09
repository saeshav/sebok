import os

async def get_doc_data(embeddings):
    # FIXED: Get the correct path to the data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # src/indexers/
    data_dir = os.path.join(script_dir, 'data')              # src/indexers/data/
    
    print(f"Loading documents from: {data_dir}")
    
    # Document 1: PerksPlus Program
    doc1_path = os.path.join(data_dir, 'Contoso_Electronics_PerkPlus_Program.md')
    print(f"Loading: {doc1_path}")
    print(f"File exists: {os.path.exists(doc1_path)}")
    
    with open(doc1_path, 'r', encoding='utf-8') as file:
        raw_description1 = file.read()
    doc1 = {
        "docId": "1",
        "docTitle": "Contoso_Electronics_PerkPlus_Program",
        "description": raw_description1,
        "descriptionVector": await get_embedding_vector(raw_description1, embeddings=embeddings),
    }
    
    # Document 2: Company Overview
    doc2_path = os.path.join(data_dir, 'Contoso_Electronics_Company_Overview.md')
    print(f"Loading: {doc2_path}")
    print(f"File exists: {os.path.exists(doc2_path)}")
    
    with open(doc2_path, 'r', encoding='utf-8') as file:
        raw_description2 = file.read()
    doc2 = {
        "docId": "2",
        "docTitle": "Contoso_Electronics_Company_Overview",
        "description": raw_description2,
        "descriptionVector": await get_embedding_vector(raw_description2, embeddings=embeddings),
    }
    
    # Document 3: Plan Benefits
    doc3_path = os.path.join(data_dir, 'Contoso_Electronics_Plan_Benefits.md')
    print(f"Loading: {doc3_path}")
    print(f"File exists: {os.path.exists(doc3_path)}")
    
    with open(doc3_path, 'r', encoding='utf-8') as file:
        raw_description3 = file.read()
    doc3 = {
        "docId": "3",
        "docTitle": "Contoso_Electronics_Plan_Benefits",
        "description": raw_description3,
        "descriptionVector": await get_embedding_vector(raw_description3, embeddings=embeddings),
    }

    print(f"✅ Successfully loaded {len([doc1, doc2, doc3])} documents")
    return [doc1, doc2, doc3]


async def get_embedding_vector(text: str, embeddings):
    result = await embeddings.create_embeddings(text)
    if (result.status != 'success' or not result.output):
        if result.status == 'error':
            raise Exception(f"Failed to generate embeddings for description: <{text[:200]+'...'}>\n\nError: {result.output}")
        raise Exception(f"Failed to generate embeddings for description: <{text[:200]+'...'}>")
    
    return result.output[0]