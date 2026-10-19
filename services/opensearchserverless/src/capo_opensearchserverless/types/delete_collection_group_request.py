"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteCollectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_id


class DeleteCollectionGroupRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId"
    """<p>The unique identifier of the collection group to delete.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCollectionGroupRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCollectionGroupRequest:
    out: DeleteCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
