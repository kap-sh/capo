"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.snapshot_type
    import capo_docdb_elastic.types.status
    import capo_docdb_elastic.types.string_list


class ClusterSnapshot(TypedDict, closed=True):
    subnet_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    snapshot_name: "str"
    """<p>The name of the elastic cluster snapshot.</p>"""
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""
    snapshot_creation_time: "str"
    """<p>The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    cluster_creation_time: "str"
    """<p>The time when the elastic cluster was created in Universal Coordinated Time (UTC).</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster snapshot.</p>"""
    vpc_security_group_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>"""
    admin_user_name: "str"
    """<p>The name of the elastic cluster administrator.</p>"""
    kms_key_id: "str"
    """<p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region. </p>"""
    snapshot_type: NotRequired["capo_docdb_elastic.types.snapshot_type.SnapshotType"]
    """<p>The type of cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all cluster snapshots that you have manually created for your Amazon Web Services account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshot) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.string_list

    out["subnetIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["subnet_ids"]
    )
    out["snapshotName"] = value["snapshot_name"]
    out["snapshotArn"] = value["snapshot_arn"]
    out["snapshotCreationTime"] = value["snapshot_creation_time"]
    out["clusterArn"] = value["cluster_arn"]
    out["clusterCreationTime"] = value["cluster_creation_time"]
    out["status"] = value["status"]
    import capo_docdb_elastic.types.string_list

    out["vpcSecurityGroupIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["vpc_security_group_ids"]
    )
    out["adminUserName"] = value["admin_user_name"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "snapshot_type" in value:
        out["snapshotType"] = value["snapshot_type"]
    return out


def deserialize_json(data: dict) -> ClusterSnapshot:
    out: ClusterSnapshot = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["subnet_ids"] = capo_docdb_elastic.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("snapshotArn") is not None:
        out["snapshot_arn"] = data["snapshotArn"]
    else:
        out["snapshot_arn"] = ""
    if data.get("snapshotCreationTime") is not None:
        out["snapshot_creation_time"] = data["snapshotCreationTime"]
    else:
        out["snapshot_creation_time"] = ""
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("clusterCreationTime") is not None:
        out["cluster_creation_time"] = data["clusterCreationTime"]
    else:
        out["cluster_creation_time"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["vpc_security_group_ids"] = (
            capo_docdb_elastic.types.string_list.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        out["vpc_security_group_ids"] = []
    if data.get("adminUserName") is not None:
        out["admin_user_name"] = data["adminUserName"]
    else:
        out["admin_user_name"] = ""
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("snapshotType") is not None:
        out["snapshot_type"] = data["snapshotType"]
    return out
