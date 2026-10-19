"""Generated from Smithy shape ``com.amazonaws.pcs#DeleteQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.queue_identifier
    import capo_pcs.types.sb_client_token


class DeleteQueueRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the queue.</p>"""
    queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier"
    """<p>The name or ID of the queue to delete.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueIdentifier"] = value["queue_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteQueueRequest:
    out: DeleteQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("queueIdentifier") is not None:
        out["queue_identifier"] = data["queueIdentifier"]
    else:
        out["queue_identifier"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
