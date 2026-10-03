"""Generated from Smithy shape ``com.amazonaws.rds#GlobalCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.failover_state
    import capo_rds.types.global_cluster_identifier
    import capo_rds.types.global_cluster_member_list
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.tag_list


class GlobalCluster(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database cluster.</p>"""
    global_cluster_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services <a href="https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?id=docs_gateway#partition">partition</a>-unique, immutable identifier for the global database cluster. This identifier is found in Amazon Web Services CloudTrail log entries whenever the Amazon Web Services KMS key for the DB cluster is accessed.</p>"""
    global_cluster_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the global database cluster.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the current state of this global database cluster.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The Aurora database engine used by the global database cluster.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for the global cluster.</p> <p>For more information, see CreateGlobalCluster.</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The default database name within the new global database cluster.</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>The storage encryption setting for the global database cluster.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the global database cluster. Possible values:</p> <ul> <li> <p> <code>none</code> - The global database cluster is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The global database cluster is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The global database cluster is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>The deletion protection setting for the new global database cluster.</p>"""
    global_cluster_members: NotRequired[
        "capo_rds.types.global_cluster_member_list.GlobalClusterMemberList"
    ]
    """<p>The list of primary and secondary clusters within the global database cluster.</p>"""
    endpoint: NotRequired["capo_rds.types.string.String"]
    """<p> The writer endpoint for the new global database cluster. This endpoint always points to the writer DB instance in the current primary cluster. </p>"""
    failover_state: NotRequired["capo_rds.types.failover_state.FailoverState"]
    """<p>A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster (Aurora global database). This object is empty unless the <code>SwitchoverGlobalCluster</code> or <code>FailoverGlobalCluster</code> operation was called on this global cluster.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]


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
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )
    if "database_name" in value:
        pairs.append((f"{key_prefix}DatabaseName", str(value["database_name"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "global_cluster_members" in value:
        import capo_rds.types.global_cluster_member_list

        capo_rds.types.global_cluster_member_list.serialize_query(
            value["global_cluster_members"], pairs, f"{key_prefix}GlobalClusterMembers"
        )
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "failover_state" in value:
        import capo_rds.types.failover_state

        capo_rds.types.failover_state.serialize_query(
            value["failover_state"], pairs, f"{key_prefix}FailoverState"
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
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
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_global_cluster_members = el.find("GlobalClusterMembers")
    if child_global_cluster_members is not None:
        import capo_rds.types.global_cluster_member_list

        out["global_cluster_members"] = (
            capo_rds.types.global_cluster_member_list.deserialize_query(
                child_global_cluster_members
            )
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_failover_state = el.find("FailoverState")
    if child_failover_state is not None:
        import capo_rds.types.failover_state

        out["failover_state"] = capo_rds.types.failover_state.deserialize_query(
            child_failover_state
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out
