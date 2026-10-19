"""Generated from Smithy shape ``com.amazonaws.docdbelastic#RestoreClusterFromSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.string_list
    import capo_docdb_elastic.types.tag_map


class RestoreClusterFromSnapshotInput(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of the elastic cluster.</p>"""
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_docdb_elastic.types.string_list.StringList"
    ]
    """<p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>"""
    subnet_ids: NotRequired["capo_docdb_elastic.types.string_list.StringList"]
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The KMS key identifier to use to encrypt the new Amazon DocumentDB elastic clusters cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.</p> <p>If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.</p>"""
    tags: NotRequired["capo_docdb_elastic.types.tag_map.TagMap"]
    """<p>A list of the tag names to be assigned to the restored elastic cluster, in the form of an array of key-value pairs in which the key is the tag name and the value is the key value.</p>"""
    shard_capacity: NotRequired["int"]
    """<p>The capacity of each shard in the new restored elastic cluster.</p>"""
    shard_instance_count: NotRequired["int"]
    """<p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreClusterFromSnapshotInput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
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
    if "tags" in value:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    if "shard_capacity" in value:
        out["shardCapacity"] = value["shard_capacity"]
    if "shard_instance_count" in value:
        out["shardInstanceCount"] = value["shard_instance_count"]
    return out


def deserialize_json(data: dict) -> RestoreClusterFromSnapshotInput:
    out: RestoreClusterFromSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
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
    if data.get("tags") is not None:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    if data.get("shardCapacity") is not None:
        out["shard_capacity"] = data["shardCapacity"]
    if data.get("shardInstanceCount") is not None:
        out["shard_instance_count"] = data["shardInstanceCount"]
    return out
