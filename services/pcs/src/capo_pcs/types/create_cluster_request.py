"""Generated from Smithy shape ``com.amazonaws.pcs#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.cluster_name
    import capo_pcs.types.cluster_slurm_configuration_request
    import capo_pcs.types.networking_request
    import capo_pcs.types.request_tag_map
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.scheduler_request
    import capo_pcs.types.size


class CreateClusterRequest(TypedDict, closed=True):
    cluster_name: "capo_pcs.types.cluster_name.ClusterName"
    """<p>A name to identify the cluster. Example: <code>MyCluster</code> </p>"""
    scheduler: "capo_pcs.types.scheduler_request.SchedulerRequest"
    """<p>The cluster management and job scheduling software associated with the cluster.</p>"""
    size: "capo_pcs.types.size.Size"
    """<p>A value that determines the maximum number of compute nodes in the cluster and the maximum number of jobs (active and queued).</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>"""
    networking: "capo_pcs.types.networking_request.NetworkingRequest"
    """<p>The networking configuration used to set up the cluster's control plane.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.cluster_slurm_configuration_request.ClusterSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    tags: NotRequired["capo_pcs.types.request_tag_map.RequestTagMap"]
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateClusterRequest) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    import capo_pcs.types.scheduler_request

    out["scheduler"] = capo_pcs.types.scheduler_request.serialize_aws_json_1_0(
        value["scheduler"]
    )
    import capo_pcs.types.size

    out["size"] = capo_pcs.types.size.serialize_aws_json_1_0(value["size"])
    import capo_pcs.types.networking_request

    out["networking"] = capo_pcs.types.networking_request.serialize_aws_json_1_0(
        value["networking"]
    )
    if "slurm_configuration" in value:
        import capo_pcs.types.cluster_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.cluster_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("scheduler") is not None:
        import capo_pcs.types.scheduler_request

        out["scheduler"] = capo_pcs.types.scheduler_request.deserialize_aws_json_1_0(
            data["scheduler"]
        )
    else:
        raise DeserializationError("CreateClusterRequest.scheduler required")
    if data.get("size") is not None:
        import capo_pcs.types.size

        out["size"] = capo_pcs.types.size.deserialize_aws_json_1_0(data["size"])
    else:
        import typing

        out["size"] = typing.cast("capo_pcs.types.size.Size", "")
    if data.get("networking") is not None:
        import capo_pcs.types.networking_request

        out["networking"] = capo_pcs.types.networking_request.deserialize_aws_json_1_0(
            data["networking"]
        )
    else:
        raise DeserializationError("CreateClusterRequest.networking required")
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.cluster_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.cluster_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
