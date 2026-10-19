"""Generated from Smithy shape ``com.amazonaws.pcs#RegisterComputeNodeGroupInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.bootstrap_id
    import capo_pcs.types.cluster_identifier


class RegisterComputeNodeGroupInstanceRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster to register the compute node group instance in.</p>"""
    bootstrap_id: "capo_pcs.types.bootstrap_id.BootstrapId"
    """<p>The client-generated token to allow for retries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterComputeNodeGroupInstanceRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["bootstrapId"] = value["bootstrap_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterComputeNodeGroupInstanceRequest:
    out: RegisterComputeNodeGroupInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("bootstrapId") is not None:
        out["bootstrap_id"] = data["bootstrapId"]
    else:
        out["bootstrap_id"] = ""
    return out
