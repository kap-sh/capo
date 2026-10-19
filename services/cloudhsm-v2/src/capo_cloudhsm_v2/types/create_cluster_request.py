"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_arn
    import capo_cloudhsm_v2.types.backup_retention_policy
    import capo_cloudhsm_v2.types.cluster_mode
    import capo_cloudhsm_v2.types.hsm_type
    import capo_cloudhsm_v2.types.network_type
    import capo_cloudhsm_v2.types.subnet_ids
    import capo_cloudhsm_v2.types.tag_list


class CreateClusterRequest(TypedDict, closed=True):
    backup_retention_policy: NotRequired[
        "capo_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
    ]
    """<p>A policy that defines how the service retains backups.</p>"""
    hsm_type: "capo_cloudhsm_v2.types.hsm_type.HsmType"
    """<p>The type of HSM to use in the cluster. The allowed values are <code>hsm1.medium</code> and <code>hsm2m.medium</code>.</p>"""
    source_backup_id: NotRequired["capo_cloudhsm_v2.types.backup_arn.BackupArn"]
    """<p>The identifier (ID) or the Amazon Resource Name (ARN) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID or ARN, use <a>DescribeBackups</a>. <i>If using a backup in another account, the full ARN must be supplied.</i> </p>"""
    subnet_ids: "capo_cloudhsm_v2.types.subnet_ids.SubnetIds"
    """<p>The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:</p> <ul> <li> <p>All subnets must be in the same virtual private cloud (VPC).</p> </li> <li> <p>You can specify only one subnet per Availability Zone.</p> </li> </ul>"""
    network_type: NotRequired["capo_cloudhsm_v2.types.network_type.NetworkType"]
    """<p>The NetworkType to create a cluster with. The allowed values are <code>IPV4</code> and <code>DUALSTACK</code>. </p>"""
    tag_list: NotRequired["capo_cloudhsm_v2.types.tag_list.TagList"]
    """<p>Tags to apply to the CloudHSM cluster during creation.</p>"""
    mode: NotRequired["capo_cloudhsm_v2.types.cluster_mode.ClusterMode"]
    """<p>The mode to use in the cluster. The allowed values are <code>FIPS</code> and <code>NON_FIPS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "backup_retention_policy" in value:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["BackupRetentionPolicy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.serialize_aws_json_1_1(
                value["backup_retention_policy"]
            )
        )
    out["HsmType"] = value["hsm_type"]
    if "source_backup_id" in value:
        out["SourceBackupId"] = value["source_backup_id"]
    import capo_cloudhsm_v2.types.subnet_ids

    out["SubnetIds"] = capo_cloudhsm_v2.types.subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    if "network_type" in value:
        import capo_cloudhsm_v2.types.network_type

        out["NetworkType"] = capo_cloudhsm_v2.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    if "tag_list" in value:
        import capo_cloudhsm_v2.types.tag_list

        out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    if "mode" in value:
        import capo_cloudhsm_v2.types.cluster_mode

        out["Mode"] = capo_cloudhsm_v2.types.cluster_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("BackupRetentionPolicy") is not None:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["backup_retention_policy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.deserialize_aws_json_1_1(
                data["BackupRetentionPolicy"]
            )
        )
    if data.get("HsmType") is not None:
        out["hsm_type"] = data["HsmType"]
    else:
        out["hsm_type"] = ""
    if data.get("SourceBackupId") is not None:
        out["source_backup_id"] = data["SourceBackupId"]
    if data.get("SubnetIds") is not None:
        import capo_cloudhsm_v2.types.subnet_ids

        out["subnet_ids"] = capo_cloudhsm_v2.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("NetworkType") is not None:
        import capo_cloudhsm_v2.types.network_type

        out["network_type"] = (
            capo_cloudhsm_v2.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    if data.get("TagList") is not None:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    if data.get("Mode") is not None:
        import capo_cloudhsm_v2.types.cluster_mode

        out["mode"] = capo_cloudhsm_v2.types.cluster_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    return out
