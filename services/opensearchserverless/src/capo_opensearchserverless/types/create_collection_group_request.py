"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.serverless_generation
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags


class CreateCollectionGroupRequest(TypedDict, closed=True):
    name: "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    """<p>The name of the collection group.</p>"""
    standby_replicas: "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
    """<p>Indicates whether standby replicas should be used for a collection group.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection group.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>"""
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>"""
    generation: NotRequired[
        "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["standbyReplicas"] = value["standby_replicas"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "generation" in value:
        out["generation"] = value["generation"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionGroupRequest:
    out: CreateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("standbyReplicas") is not None:
        out["standby_replicas"] = data["standbyReplicas"]
    else:
        out["standby_replicas"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("capacityLimits") is not None:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if data.get("generation") is not None:
        out["generation"] = data["generation"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
