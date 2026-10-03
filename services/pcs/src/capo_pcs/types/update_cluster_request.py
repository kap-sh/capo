"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.update_cluster_slurm_configuration_request
    import capo_pcs.types.update_scheduler_request


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster to update.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.update_cluster_slurm_configuration_request.UpdateClusterSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    scheduler: NotRequired[
        "capo_pcs.types.update_scheduler_request.UpdateSchedulerRequest"
    ]
    """<p>The scheduler configuration to update for the cluster. Use this to update the scheduler version. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html">Updating the scheduler version on a cluster</a> in the <i>PCS User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "slurm_configuration" in value:
        import capo_pcs.types.update_cluster_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.update_cluster_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "scheduler" in value:
        import capo_pcs.types.update_scheduler_request

        out["scheduler"] = (
            capo_pcs.types.update_scheduler_request.serialize_aws_json_1_0(
                value["scheduler"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("UpdateClusterRequest.cluster_identifier required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.update_cluster_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.update_cluster_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("scheduler") is not None:
        import capo_pcs.types.update_scheduler_request

        out["scheduler"] = (
            capo_pcs.types.update_scheduler_request.deserialize_aws_json_1_0(
                data["scheduler"]
            )
        )
    return out
