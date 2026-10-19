"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.index_name


class DeleteIndexRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection containing the index to delete.</p>"""
    index_name: "capo_opensearchserverless.types.index_name.IndexName"
    """<p>The name of the index to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIndexRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["indexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIndexRequest:
    out: DeleteIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        out["index_name"] = ""
    return out
