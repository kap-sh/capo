"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.index_name
    import capo_opensearchserverless.types.index_schema


class CreateIndexRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection in which to create the index.</p>"""
    index_name: "capo_opensearchserverless.types.index_name.IndexName"
    """<p>The name of the index to create. Index names must be lowercase and can't begin with underscores (_) or hyphens (-).</p>"""
    index_schema: NotRequired[
        "capo_opensearchserverless.types.index_schema.IndexSchema"
    ]
    """<p>The JSON schema definition for the index, including field mappings and settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIndexRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["indexName"] = value["index_name"]
    if "index_schema" in value:
        out["indexSchema"] = value["index_schema"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        out["index_name"] = ""
    if data.get("indexSchema") is not None:
        out["index_schema"] = data["indexSchema"]
    return out
