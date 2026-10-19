"""Generated from Smithy shape ``com.amazonaws.docdbelastic#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.auth
    import capo_docdb_elastic.types.shard_list
    import capo_docdb_elastic.types.status
    import capo_docdb_elastic.types.string_list


class Cluster(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of the elastic cluster.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster.</p>"""
    cluster_endpoint: "str"
    """<p>The URL used to connect to the elastic cluster.</p>"""
    create_time: "str"
    """<p>The time when the elastic cluster was created in Universal Coordinated Time (UTC).</p>"""
    admin_user_name: "str"
    """<p>The name of the elastic cluster administrator.</p>"""
    auth_type: "capo_docdb_elastic.types.auth.Auth"
    """<p>The authentication type for the elastic cluster.</p>"""
    shard_capacity: "int"
    """<p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>"""
    shard_count: "int"
    """<p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>"""
    vpc_security_group_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>A list of EC2 VPC security groups associated with thie elastic cluster.</p>"""
    subnet_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    preferred_maintenance_window: "str"
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p>"""
    kms_key_id: "str"
    """<p>The KMS key identifier to use to encrypt the elastic cluster.</p>"""
    shards: NotRequired["capo_docdb_elastic.types.shard_list.ShardList"]
    """<p>The total number of shards in the cluster.</p>"""
    backup_retention_period: NotRequired["int"]
    """<p>The number of days for which automatic snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["str"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by <code>backupRetentionPeriod</code>.</p>"""
    shard_instance_count: NotRequired["int"]
    """<p>The number of replica instances applying to all shards in the cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cluster) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    out["clusterEndpoint"] = value["cluster_endpoint"]
    out["createTime"] = value["create_time"]
    out["adminUserName"] = value["admin_user_name"]
    out["authType"] = value["auth_type"]
    out["shardCapacity"] = value["shard_capacity"]
    out["shardCount"] = value["shard_count"]
    import capo_docdb_elastic.types.string_list

    out["vpcSecurityGroupIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["vpc_security_group_ids"]
    )
    import capo_docdb_elastic.types.string_list

    out["subnetIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["subnet_ids"]
    )
    out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "shards" in value:
        import capo_docdb_elastic.types.shard_list

        out["shards"] = capo_docdb_elastic.types.shard_list.serialize_json(
            value["shards"]
        )
    if "backup_retention_period" in value:
        out["backupRetentionPeriod"] = value["backup_retention_period"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "shard_instance_count" in value:
        out["shardInstanceCount"] = value["shard_instance_count"]
    return out


def deserialize_json(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("clusterEndpoint") is not None:
        out["cluster_endpoint"] = data["clusterEndpoint"]
    else:
        out["cluster_endpoint"] = ""
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = ""
    if data.get("adminUserName") is not None:
        out["admin_user_name"] = data["adminUserName"]
    else:
        out["admin_user_name"] = ""
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    else:
        out["auth_type"] = ""
    if data.get("shardCapacity") is not None:
        out["shard_capacity"] = data["shardCapacity"]
    else:
        out["shard_capacity"] = 0
    if data.get("shardCount") is not None:
        out["shard_count"] = data["shardCount"]
    else:
        out["shard_count"] = 0
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["vpc_security_group_ids"] = (
            capo_docdb_elastic.types.string_list.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        out["vpc_security_group_ids"] = []
    if data.get("subnetIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["subnet_ids"] = capo_docdb_elastic.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    else:
        out["preferred_maintenance_window"] = ""
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("shards") is not None:
        import capo_docdb_elastic.types.shard_list

        out["shards"] = capo_docdb_elastic.types.shard_list.deserialize_json(
            data["shards"]
        )
    if data.get("backupRetentionPeriod") is not None:
        out["backup_retention_period"] = data["backupRetentionPeriod"]
    if data.get("preferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if data.get("shardInstanceCount") is not None:
        out["shard_instance_count"] = data["shardInstanceCount"]
    return out
