# Privasee RAG project Documentation

Mels Hakobyan

### Step 1. Installation

Python version - 3.12.3

The virtual environment is included in the rar file (privasee_env directory) you can run the following commands inside the root directory.

Windows

```bash
cd privasee_env
cd Scripts
activate
```

Linux

```bash
cd privasee_env
source bin/activate
```

Mac

```bash
cd privasee_env
source bin/activate
```

Alternatively you can create your own virtual environment and install all the dependencies by running

```bash
pip install -r requirements.txt
```

requirements.txt is located in privasee/privasee dir.

If that approach fails you can install all used dependencies manually, here is the list of dependencies and their versions

```bash
pip install langchain==0.2.11 langchain-community==0.2.10 langchain-core==0.2.23 langchain-experimental==0.0.63 langchain-openai==0.1.17 langchain-text-splitters==0.2.2 PyMuPDF==1.24.9 chromadb==0.5.5
```

### Step 2. Config

There is a config file named [config.py](http://config.py) in privasee/privasee, open the file in the editor and add your OpenAI key and organization

```python
openai_api_key = "sk-proj-youropenaiapikey"
openai_organization = "org-youropenaiorganization"
gpt_model = "gpt-4-turbo"
fi_api_key = "your_fi_api_key"
```

save the file and close

### Step 2.1 Computing ChromaDB embeddings (Optional)

The project folder also contains the chroma files, in case it fails to deliver results you can compute the embeddings from scratch manually, open [utils.py](http://utils.py) file in your editor located at privasee/privasee/ai, run

```bash
python utils.py
```

if it fails due to path issues you can edit the file on the very bottom and copy the full path on your computer and paste in the code here

```python
if __name__ == "__main__":
    create_vector_databases(r'privasee\GDPR_Art_1_to_21_split\text')
    vdb = VectorDB(collection='GDPR_Art_1_to_21_full')
    vdb.join_all_collections()
```

change this part privasee\GDPR_Art_1_to_21_split\text with the full path

### Step 3. Running the project

In privasee/privasee there is a [main.py](http://main.py) file run

```bash
python main.py
```

All of the data used for RAG is already self contained and pre-computed so the application will start

## Description of the solutions

- First of all I split the original PDF into separate articles 1-21, then I converted all PDFs into txt files (all the code could be found in privasee/privasee/pdf_parsing/utils.py).
- Then I performed semantic chunking on all txt files and vectorized them to store in ChromaDB, each article in separate collection.
    - Also I joined all chunks together into one collection in case chunks from several articles are needed.
- The model has two helper models
    - one determines which article is best suitable to answer the question (if none apply returns None and I perform a search in the full document)
    - other one modifies the question in a way that it will be easier to perform a semantic search in the vector database

## Ideas for improvement

- Make it more robust to edge case bugs and implement try-catch blocks
- Try agentic chunking
- Implement short cut requests like FAQ and pre-build answers. The argument is that mostly users ask the same questions and there is no need to compute all the answers on the fly and we can just give them a quick FAQ-like questions recommendations
