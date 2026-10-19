"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveGeneratedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list


class AgenticRetrieveGeneratedResponse(TypedDict, closed=True):
    answer: "str"
    """<p>The generated answer text.</p>"""
    citations: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list.AgenticRetrieveCitationList"
    ]
    """<p>Citations mapping spans of the answer to supporting results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveGeneratedResponse) -> dict:
    out: dict = {}
    out["answer"] = value["answer"]
    if "citations" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list

        out["citations"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list.serialize_json(
                value["citations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveGeneratedResponse:
    out: AgenticRetrieveGeneratedResponse = {}  # type: ignore[typeddict-item]
    if data.get("answer") is not None:
        out["answer"] = data["answer"]
    else:
        out["answer"] = ""
    if data.get("citations") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list

        out["citations"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation_list.deserialize_json(
                data["citations"]
            )
        )
    return out
