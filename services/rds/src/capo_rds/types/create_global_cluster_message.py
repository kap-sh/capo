"""Generated from Smithy shape ``com.amazonaws.rds#CreateGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.global_cluster_identifier
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier for this global database cluster. This parameter is stored as a lowercase string.</p>"""
    source_db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) to use as the primary cluster of the global database.</p> <p>If you provide a value for this parameter, don't specify values for the following settings because Amazon Aurora uses the values from the specified source DB cluster:</p> <ul> <li> <p> <code>DatabaseName</code> </p> </li> <li> <p> <code>Engine</code> </p> </li> <li> <p> <code>EngineVersion</code> </p> </li> <li> <p> <code>StorageEncrypted</code> </p> </li> </ul>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to use for this global database cluster.</p> <p>Valid Values: <code>aurora-mysql | aurora-postgresql</code> </p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>SourceDBClusterIdentifier</code> is specified. In this case, Amazon Aurora uses the engine of the source DB cluster.</p> </li> </ul>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The engine version to use for this global database cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>SourceDBClusterIdentifier</code> is specified. In this case, Amazon Aurora uses the engine version of the source DB cluster.</p> </li> </ul>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this global database cluster.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your global cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, creating the global cluster will fail if the DB major version is past its end of standard support date.</p> </note> <p>This setting only applies to Aurora PostgreSQL-based global databases.</p> <p>You can use this setting to enroll your global cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your global cluster past the end of standard support for that engine version. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the new global database cluster. The global database can't be deleted when deletion protection is enabled.</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name for your database of up to 64 alphanumeric characters. If you don't specify a name, Amazon Aurora doesn't create a database in the global database cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>SourceDBClusterIdentifier</code> is specified. In this case, Amazon Aurora uses the database name from the source DB cluster.</p> </li> </ul>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable storage encryption for the new global database cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>SourceDBClusterIdentifier</code> is specified. In this case, Amazon Aurora uses the setting from the source DB cluster.</p> </li> </ul>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the global cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "source_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterIdentifier",
                str(value["source_db_cluster_identifier"]),
            )
        )
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
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
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
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateGlobalClusterMessage:
    out: CreateGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_source_db_cluster_identifier = el.find("SourceDBClusterIdentifier")
    if child_source_db_cluster_identifier is not None:
        out["source_db_cluster_identifier"] = str(
            child_source_db_cluster_identifier.text or ""
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
