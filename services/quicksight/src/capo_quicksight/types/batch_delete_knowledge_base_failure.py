"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_id


class BatchDeleteKnowledgeBaseFailure(TypedDict, closed=True):
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the knowledge base that failed to be deleted.</p>"""
    error_code: "str"
    """<p>The error code for the deletion failure.</p>"""
    error_message: "str"
    """<p>The error message for the deletion failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseFailure) -> dict:
    out: dict = {}
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteKnowledgeBaseFailure:
    out: BatchDeleteKnowledgeBaseFailure = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
