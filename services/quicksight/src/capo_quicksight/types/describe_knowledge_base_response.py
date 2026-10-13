"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base: "capo_quicksight.types.knowledge_base.KnowledgeBase"
    """<p>The knowledge base.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["capo_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.knowledge_base

    out["KnowledgeBase"] = capo_quicksight.types.knowledge_base.serialize_json(
        value["knowledge_base"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeKnowledgeBaseResponse:
    out: DescribeKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBase") is not None:
        import capo_quicksight.types.knowledge_base

        out["knowledge_base"] = capo_quicksight.types.knowledge_base.deserialize_json(
            data["KnowledgeBase"]
        )
    else:
        raise DeserializationError(
            "DescribeKnowledgeBaseResponse.knowledge_base required"
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeKnowledgeBaseResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base" in value:
        import capo_quicksight.types.knowledge_base

        out["knowledge_base"] = capo_quicksight.types.knowledge_base.redact_sensitive(
            value["knowledge_base"]
        )
    return out
