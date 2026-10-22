"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_field_text


class RetrievalInstructionContent(TypedDict, closed=True):
    retrieval_guidance: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_field_text.RetrievalInstructionFieldText"
    ]
    """<p>How to interpret and decompose the question, and what to prioritise when searching.</p>"""
    persona: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_field_text.RetrievalInstructionFieldText"
    ]
    """<p>Who the assistant is: identity, tone and language.</p>"""
    answer_format: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_field_text.RetrievalInstructionFieldText"
    ]
    """<p>How the answer is structured, including how sources are cited.</p>"""
    answer_policy: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_field_text.RetrievalInstructionFieldText"
    ]
    """<p>Whether and how to answer: how strongly an answer must be supported, and what to do with questions outside scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionContent) -> dict:
    out: dict = {}
    if "retrieval_guidance" in value:
        out["retrievalGuidance"] = value["retrieval_guidance"]
    if "persona" in value:
        out["persona"] = value["persona"]
    if "answer_format" in value:
        out["answerFormat"] = value["answer_format"]
    if "answer_policy" in value:
        out["answerPolicy"] = value["answer_policy"]
    return out


def deserialize_json(data: dict) -> RetrievalInstructionContent:
    out: RetrievalInstructionContent = {}  # type: ignore[typeddict-item]
    if data.get("retrievalGuidance") is not None:
        out["retrieval_guidance"] = data["retrievalGuidance"]
    if data.get("persona") is not None:
        out["persona"] = data["persona"]
    if data.get("answerFormat") is not None:
        out["answer_format"] = data["answerFormat"]
    if data.get("answerPolicy") is not None:
        out["answer_policy"] = data["answerPolicy"]
    return out
