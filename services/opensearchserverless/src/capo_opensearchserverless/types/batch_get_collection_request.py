"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_ids
    import capo_opensearchserverless.types.collection_names


class BatchGetCollectionRequest(TypedDict, closed=True):
    ids: NotRequired["capo_opensearchserverless.types.collection_ids.CollectionIds"]
    """<p>A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the <a href="https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html">ListCollections</a> API.</p>"""
    names: NotRequired[
        "capo_opensearchserverless.types.collection_names.CollectionNames"
    ]
    """<p>A list of collection names. You can't provide names and IDs in the same request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_opensearchserverless.types.collection_ids

        out["ids"] = (
            capo_opensearchserverless.types.collection_ids.serialize_aws_json_1_0(
                value["ids"]
            )
        )
    if "names" in value:
        import capo_opensearchserverless.types.collection_names

        out["names"] = (
            capo_opensearchserverless.types.collection_names.serialize_aws_json_1_0(
                value["names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionRequest:
    out: BatchGetCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_opensearchserverless.types.collection_ids

        out["ids"] = (
            capo_opensearchserverless.types.collection_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    if data.get("names") is not None:
        import capo_opensearchserverless.types.collection_names

        out["names"] = (
            capo_opensearchserverless.types.collection_names.deserialize_aws_json_1_0(
                data["names"]
            )
        )
    return out
