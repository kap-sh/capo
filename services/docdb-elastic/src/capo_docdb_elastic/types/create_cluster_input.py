"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CreateClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.auth
    import capo_docdb_elastic.types.password
    import capo_docdb_elastic.types.string_list
    import capo_docdb_elastic.types.tag_map


class CreateClusterInput(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of the new elastic cluster. This parameter is stored as a lowercase string.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p> <i>Example</i>: <code>my-cluster</code> </p>"""
    auth_type: "capo_docdb_elastic.types.auth.Auth"
    """<p>The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are <code>PLAIN_TEXT</code> or <code>SECRET_ARN</code>.</p>"""
    admin_user_name: "str"
    """<p>The name of the Amazon DocumentDB elastic clusters administrator.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must be from 1 to 63 letters or numbers.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot be a reserved word.</p> </li> </ul>"""
    admin_user_password: "capo_docdb_elastic.types.password.Password"
    """<p>The password for the Amazon DocumentDB elastic clusters administrator. The password can contain any printable ASCII characters.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must contain from 8 to 100 characters.</p> </li> <li> <p>Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).</p> </li> </ul>"""
    shard_capacity: "int"
    """<p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>"""
    shard_count: "int"
    """<p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_docdb_elastic.types.string_list.StringList"
    ]
    """<p>A list of EC2 VPC security groups to associate with the new elastic cluster.</p>"""
    subnet_ids: NotRequired["capo_docdb_elastic.types.string_list.StringList"]
    """<p>The Amazon EC2 subnet IDs for the new elastic cluster.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The KMS key identifier to use to encrypt the new elastic cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.</p> <p>If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.</p>"""
    client_token: NotRequired["str"]
    """<p>The client token for the elastic cluster.</p>"""
    preferred_maintenance_window: NotRequired["str"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> <i>Default</i>: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p> <i>Valid days</i>: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p> <i>Constraints</i>: Minimum 30-minute window.</p>"""
    tags: NotRequired["capo_docdb_elastic.types.tag_map.TagMap"]
    """<p>The tags to be assigned to the new elastic cluster.</p>"""
    backup_retention_period: NotRequired["int"]
    """<p>The number of days for which automatic snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["str"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>backupRetentionPeriod</code>.</p>"""
    shard_instance_count: NotRequired["int"]
    """<p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterInput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    out["authType"] = value["auth_type"]
    out["adminUserName"] = value["admin_user_name"]
    out["adminUserPassword"] = value["admin_user_password"]
    out["shardCapacity"] = value["shard_capacity"]
    out["shardCount"] = value["shard_count"]
    if "vpc_security_group_ids" in value:
        import capo_docdb_elastic.types.string_list

        out["vpcSecurityGroupIds"] = (
            capo_docdb_elastic.types.string_list.serialize_json(
                value["vpc_security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_docdb_elastic.types.string_list

        out["subnetIds"] = capo_docdb_elastic.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "tags" in value:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    if "backup_retention_period" in value:
        out["backupRetentionPeriod"] = value["backup_retention_period"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "shard_instance_count" in value:
        out["shardInstanceCount"] = value["shard_instance_count"]
    return out


def deserialize_json(data: dict) -> CreateClusterInput:
    out: CreateClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("CreateClusterInput.cluster_name required")
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    else:
        raise DeserializationError("CreateClusterInput.auth_type required")
    if data.get("adminUserName") is not None:
        out["admin_user_name"] = data["adminUserName"]
    else:
        raise DeserializationError("CreateClusterInput.admin_user_name required")
    if data.get("adminUserPassword") is not None:
        out["admin_user_password"] = data["adminUserPassword"]
    else:
        raise DeserializationError("CreateClusterInput.admin_user_password required")
    if data.get("shardCapacity") is not None:
        out["shard_capacity"] = data["shardCapacity"]
    else:
        raise DeserializationError("CreateClusterInput.shard_capacity required")
    if data.get("shardCount") is not None:
        out["shard_count"] = data["shardCount"]
    else:
        raise DeserializationError("CreateClusterInput.shard_count required")
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["vpc_security_group_ids"] = (
            capo_docdb_elastic.types.string_list.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    if data.get("subnetIds") is not None:
        import capo_docdb_elastic.types.string_list

        out["subnet_ids"] = capo_docdb_elastic.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("tags") is not None:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    if data.get("backupRetentionPeriod") is not None:
        out["backup_retention_period"] = data["backupRetentionPeriod"]
    if data.get("preferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if data.get("shardInstanceCount") is not None:
        out["shard_instance_count"] = data["shardInstanceCount"]
    return out
