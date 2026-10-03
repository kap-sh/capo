"""Generated from Smithy shape ``com.amazonaws.memorydb#ACL``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.acl_cluster_name_list
    import capo_memorydb.types.acl_pending_changes
    import capo_memorydb.types.string
    import capo_memorydb.types.user_name_list


class ACL(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the Access Control List</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>Indicates ACL status. Can be "creating", "active", "modifying", "deleting".</p>"""
    user_names: NotRequired["capo_memorydb.types.user_name_list.UserNameList"]
    """<p>The list of user names that belong to the ACL.</p>"""
    minimum_engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The minimum engine version supported for the ACL</p>"""
    pending_changes: NotRequired[
        "capo_memorydb.types.acl_pending_changes.ACLPendingChanges"
    ]
    """<p>A list of updates being applied to the ACL.</p>"""
    clusters: NotRequired[
        "capo_memorydb.types.acl_cluster_name_list.ACLClusterNameList"
    ]
    """<p>A list of clusters associated with the ACL.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the ACL</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACL) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "user_names" in value:
        import capo_memorydb.types.user_name_list

        out["UserNames"] = capo_memorydb.types.user_name_list.serialize_aws_json_1_1(
            value["user_names"]
        )
    if "minimum_engine_version" in value:
        out["MinimumEngineVersion"] = value["minimum_engine_version"]
    if "pending_changes" in value:
        import capo_memorydb.types.acl_pending_changes

        out["PendingChanges"] = (
            capo_memorydb.types.acl_pending_changes.serialize_aws_json_1_1(
                value["pending_changes"]
            )
        )
    if "clusters" in value:
        import capo_memorydb.types.acl_cluster_name_list

        out["Clusters"] = (
            capo_memorydb.types.acl_cluster_name_list.serialize_aws_json_1_1(
                value["clusters"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ACL:
    out: ACL = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("UserNames") is not None:
        import capo_memorydb.types.user_name_list

        out["user_names"] = capo_memorydb.types.user_name_list.deserialize_aws_json_1_1(
            data["UserNames"]
        )
    if data.get("MinimumEngineVersion") is not None:
        out["minimum_engine_version"] = data["MinimumEngineVersion"]
    if data.get("PendingChanges") is not None:
        import capo_memorydb.types.acl_pending_changes

        out["pending_changes"] = (
            capo_memorydb.types.acl_pending_changes.deserialize_aws_json_1_1(
                data["PendingChanges"]
            )
        )
    if data.get("Clusters") is not None:
        import capo_memorydb.types.acl_cluster_name_list

        out["clusters"] = (
            capo_memorydb.types.acl_cluster_name_list.deserialize_aws_json_1_1(
                data["Clusters"]
            )
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out
