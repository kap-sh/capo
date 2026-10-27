"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_id


class UpdateCollectionGroupRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId"
    """<p>The unique identifier of the collection group to update.</p>"""
    description: NotRequired["str"]
    """<p>A new description for the collection group.</p>"""
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs). Updates to capacity limits are not incremental. Any field not specified resets to its default value.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionGroupRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionGroupRequest:
    out: UpdateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("capacityLimits") is not None:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
