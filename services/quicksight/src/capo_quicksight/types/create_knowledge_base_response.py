"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_status
    import capo_quicksight.types.knowledge_base_arn
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base_arn: "capo_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    creation_status: "capo_quicksight.types.data_set_status.DataSetStatus"
    """<p>The creation status of the knowledge base.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["capo_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseResponse) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    import capo_quicksight.types.data_set_status

    out["CreationStatus"] = capo_quicksight.types.data_set_status.serialize_json(
        value["creation_status"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseResponse:
    out: CreateKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("CreationStatus") is not None:
        import capo_quicksight.types.data_set_status

        out["creation_status"] = capo_quicksight.types.data_set_status.deserialize_json(
            data["CreationStatus"]
        )
    else:
        import typing

        out["creation_status"] = typing.cast(
            "capo_quicksight.types.data_set_status.DataSetStatus", ""
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
