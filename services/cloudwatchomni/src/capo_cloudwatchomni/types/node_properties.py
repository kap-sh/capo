"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.node_category


class NodeProperties(TypedDict, closed=True):
    region: NotRequired["str"]
    """The region the node runs in. Falls back to the region the telemetry was ingested from when the node does not report one."""
    cloud_provider: NotRequired["str"]
    """The cloud provider hosting the node, resolved from the reported provider, platform, or vendor namespace, and defaulting to "aws"."""
    source_account_id: NotRequired["str"]
    """The account that produced the telemetry this node was discovered from."""
    namespace: NotRequired["str"]
    """The logical service grouping the node belongs to. This is not a metric namespace."""
    category: NotRequired["capo_cloudwatchomni.types.node_category.NodeCategory"]
    """What kind of thing the node is, coarser than nodeType."""
    stage: NotRequired["str"]
    """The node's deployment environment. A node may be observed in several; this is the highest-precedence one. Match any of them with NodeFilters.stage."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeProperties) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    if "source_account_id" in value:
        out["sourceAccountId"] = value["source_account_id"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "category" in value:
        import capo_cloudwatchomni.types.node_category

        out["category"] = capo_cloudwatchomni.types.node_category.serialize_cbor(
            value["category"]
        )
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_cbor(data: dict) -> NodeProperties:
    out: NodeProperties = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    if data.get("sourceAccountId") is not None:
        out["source_account_id"] = data["sourceAccountId"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("category") is not None:
        import capo_cloudwatchomni.types.node_category

        out["category"] = capo_cloudwatchomni.types.node_category.deserialize_cbor(
            data["category"]
        )
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    return out
