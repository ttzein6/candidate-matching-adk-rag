from google.adk.agents import Agent

from .tools.add_data import add_data
from .tools.create_corpus import create_corpus
from .tools.delete_corpus import delete_corpus
from .tools.delete_document import delete_document
from .tools.get_corpus_info import get_corpus_info
from .tools.list_corpora import list_corpora
from .tools.rag_query import rag_query
import prompt as prompt
root_agent = Agent(
    name="CandidateMatchingAgent",
    # Using Gemini 2.5 Flash for best performance with RAG operations
    model="gemini-2.5-flash-preview-05-20",
    description="AI-Powered Candidate Matching RAG Agent",
    tools=[
        rag_query,
        list_corpora,
        create_corpus,
        add_data,
        get_corpus_info,
        delete_corpus,
        delete_document,
    ],
    instruction=prompt.AGENT_INSTRUCTION,
)
