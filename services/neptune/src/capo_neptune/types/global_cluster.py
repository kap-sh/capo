"""Generated from Smithy shape ``com.amazonaws.neptune#GlobalCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.failover_state
    import capo_neptune.types.global_cluster_identifier
    import capo_neptune.types.global_cluster_member_list
    import capo_neptune.types.string
    import capo_neptune.types.tag_list


class GlobalCluster(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.</p>"""
    global_cluster_resource_id: NotRequired["capo_neptune.types.string.String"]
    """<p>An immutable identifier for the global database that is unique within all regions. This identifier is found in CloudTrail log entries whenever the KMS key for the DB cluster is accessed.</p>"""
    global_cluster_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the global database.</p>"""
    status: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the current state of this global database.</p>"""
    engine: NotRequired["capo_neptune.types.string.String"]
    """<p>The Neptune database engine used by the global database (<code>"neptune"</code>).</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The Neptune engine version used by the global database.</p>"""
    database_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The default database name within the new global database cluster.</p>"""
    storage_encrypted: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>The storage encryption setting for the global database.</p>"""
    deletion_protection: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>The deletion protection setting for the global database.</p>"""
    global_cluster_members: NotRequired[
        "capo_neptune.types.global_cluster_member_list.GlobalClusterMemberList"
    ]
    """<p>A list of cluster ARNs and instance ARNs for all the DB clusters that are part of the global database.</p>"""
    failover_state: NotRequired["capo_neptune.types.failover_state.FailoverState"]
    """<p>A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster (Neptune global database). This object is empty unless the <code>SwitchoverGlobalCluster</code> or <code>FailoverGlobalCluster</code> operation was called on this global cluster.</p>"""
    tag_list: NotRequired["capo_neptune.types.tag_list.TagList"]
    """<p>A list of global cluster tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalCluster, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "global_cluster_resource_id" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterResourceId",
                str(value["global_cluster_resource_id"]),
            )
        )
    if "global_cluster_arn" in value:
        pairs.append(
            (f"{key_prefix}GlobalClusterArn", str(value["global_cluster_arn"]))
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "database_name" in value:
        pairs.append((f"{key_prefix}DatabaseName", str(value["database_name"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "global_cluster_members" in value:
        import capo_neptune.types.global_cluster_member_list

        capo_neptune.types.global_cluster_member_list.serialize_query(
            value["global_cluster_members"], pairs, f"{key_prefix}GlobalClusterMembers"
        )
    if "failover_state" in value:
        import capo_neptune.types.failover_state

        capo_neptune.types.failover_state.serialize_query(
            value["failover_state"], pairs, f"{key_prefix}FailoverState"
        )
    if "tag_list" in value:
        import capo_neptune.types.tag_list

        capo_neptune.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> GlobalCluster:
    out: GlobalCluster = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_global_cluster_resource_id = el.find("GlobalClusterResourceId")
    if child_global_cluster_resource_id is not None:
        out["global_cluster_resource_id"] = str(
            child_global_cluster_resource_id.text or ""
        )
    child_global_cluster_arn = el.find("GlobalClusterArn")
    if child_global_cluster_arn is not None:
        out["global_cluster_arn"] = str(child_global_cluster_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_global_cluster_members = el.find("GlobalClusterMembers")
    if child_global_cluster_members is not None:
        import capo_neptune.types.global_cluster_member_list

        out["global_cluster_members"] = (
            capo_neptune.types.global_cluster_member_list.deserialize_query(
                child_global_cluster_members
            )
        )
    child_failover_state = el.find("FailoverState")
    if child_failover_state is not None:
        import capo_neptune.types.failover_state

        out["failover_state"] = capo_neptune.types.failover_state.deserialize_query(
            child_failover_state
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_neptune.types.tag_list

        out["tag_list"] = capo_neptune.types.tag_list.deserialize_query(child_tag_list)
    return out
