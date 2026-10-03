"""Generated from Smithy shape ``com.amazonaws.docdbelastic#UpdateClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.auth
    import capo_docdb_elastic.types.password
    import capo_docdb_elastic.types.string_list


class UpdateClusterInput(TypedDict, closed=True):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    auth_type: NotRequired["capo_docdb_elastic.types.auth.Auth"]
    """<p>The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are <code>PLAIN_TEXT</code> or <code>SECRET_ARN</code>.</p>"""
    shard_capacity: NotRequired["int"]
    """<p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>"""
    shard_count: NotRequired["int"]
    """<p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_docdb_elastic.types.string_list.StringList"
    ]
    """<p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>"""
    subnet_ids: NotRequired["capo_docdb_elastic.types.string_list.StringList"]
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    admin_user_password: NotRequired["capo_docdb_elastic.types.password.Password"]
    """<p>The password associated with the elastic cluster administrator. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).</p> <p> <i>Constraints</i>: Must contain from 8 to 100 characters.</p>"""
    client_token: NotRequired["str"]
    """<p>The client token for the elastic cluster.</p>"""
    preferred_maintenance_window: NotRequired["str"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> <i>Default</i>: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p> <i>Valid days</i>: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p> <i>Constraints</i>: Minimum 30-minute window.</p>"""
    backup_retention_period: NotRequired["int"]
    """<p>The number of days for which automatic snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["str"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>backupRetentionPeriod</code>.</p>"""
    shard_instance_count: NotRequired["int"]
    """<p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterInput) -> dict:
    out: dict = {}
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "shard_capacity" in value:
        out["shardCapacity"] = value["shard_capacity"]
    if "shard_count" in value:
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
    if "admin_user_password" in value:
        out["adminUserPassword"] = value["admin_user_password"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "backup_retention_period" in value:
        out["backupRetentionPeriod"] = value["backup_retention_period"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "shard_instance_count" in value:
        out["shardInstanceCount"] = value["shard_instance_count"]
    return out


def deserialize_json(data: dict) -> UpdateClusterInput:
    out: UpdateClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    if data.get("shardCapacity") is not None:
        out["shard_capacity"] = data["shardCapacity"]
    if data.get("shardCount") is not None:
        out["shard_count"] = data["shardCount"]
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
    if data.get("adminUserPassword") is not None:
        out["admin_user_password"] = data["adminUserPassword"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("backupRetentionPeriod") is not None:
        out["backup_retention_period"] = data["backupRetentionPeriod"]
    if data.get("preferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if data.get("shardInstanceCount") is not None:
        out["shard_instance_count"] = data["shardInstanceCount"]
    return out
