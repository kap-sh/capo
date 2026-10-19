"""Generated from Smithy shape ``com.amazonaws.pcs#GetQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.queue_identifier


class GetQueueRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the queue.</p>"""
    queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier"
    """<p>The name or ID of the queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueIdentifier"] = value["queue_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueRequest:
    out: GetQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("queueIdentifier") is not None:
        out["queue_identifier"] = data["queueIdentifier"]
    else:
        out["queue_identifier"] = ""
    return out
