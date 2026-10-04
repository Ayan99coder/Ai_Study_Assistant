from langchain_core.runnables import RunnableBranch, RunnableLambda

from chains.All_chains import (
    explanation_chain,
    quiz_chain,
    notes_chain
)

condition_runnable = RunnableBranch(

    (
        lambda x: x["output_type"] == "Explain Topic",
        explanation_chain
    ),

    (
        lambda x: x["output_type"] == "Generate Quiz",
        quiz_chain
    ),

    (
        lambda x: x["output_type"] == "Generate Notes",
        notes_chain
    ),

    RunnableLambda(
        lambda x: "Could not find output type"
    )
)