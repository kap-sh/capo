"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCitation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list


class AgenticRetrieveCitation(TypedDict, closed=True):
    start_index: "int"
    """<p>Character offset start in the answer text.</p>"""
    end_index: "int"
    """<p>Character offset end (exclusive) in the answer text.</p>"""
    references: "capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list.AgenticRetrieveCitationReferenceList"
    """<p>References to results that support this span.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCitation) -> dict:
    out: dict = {}
    out["startIndex"] = value["start_index"]
    out["endIndex"] = value["end_index"]
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list

    out["references"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list.serialize_json(
            value["references"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveCitation:
    out: AgenticRetrieveCitation = {}  # type: ignore[typeddict-item]
    if data.get("startIndex") is not None:
        out["start_index"] = data["startIndex"]
    else:
        out["start_index"] = 0
    if data.get("endIndex") is not None:
        out["end_index"] = data["endIndex"]
    else:
        out["end_index"] = 0
    if data.get("references") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list

        out["references"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference_list.deserialize_json(
                data["references"]
            )
        )
    else:
        out["references"] = []
    return out
