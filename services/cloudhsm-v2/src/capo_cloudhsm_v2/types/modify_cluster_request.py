"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_retention_policy
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.hsm_type


class ModifyClusterRequest(TypedDict, closed=True):
    hsm_type: NotRequired["capo_cloudhsm_v2.types.hsm_type.HsmType"]
    """<p>The desired HSM type of the cluster.</p>"""
    backup_retention_policy: NotRequired[
        "capo_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
    ]
    """<p>A policy that defines how the service retains backups.</p>"""
    cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that you want to modify. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterRequest) -> dict:
    out: dict = {}
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "backup_retention_policy" in value:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["BackupRetentionPolicy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.serialize_aws_json_1_1(
                value["backup_retention_policy"]
            )
        )
    out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterRequest:
    out: ModifyClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("HsmType") is not None:
        out["hsm_type"] = data["HsmType"]
    if data.get("BackupRetentionPolicy") is not None:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["backup_retention_policy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.deserialize_aws_json_1_1(
                data["BackupRetentionPolicy"]
            )
        )
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    else:
        out["cluster_id"] = ""
    return out
