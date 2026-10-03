"""Generated from Smithy shape ``com.amazonaws.neptune#ClusterPendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.integer_optional
    import capo_neptune.types.pending_cloudwatch_logs_exports
    import capo_neptune.types.string


class ClusterPendingModifiedValues(TypedDict, closed=True):
    pending_cloudwatch_logs_exports: NotRequired[
        "capo_neptune.types.pending_cloudwatch_logs_exports.PendingCloudwatchLogsExports"
    ]
    """<p>This <code>PendingCloudwatchLogsExports</code> structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.</p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The DBClusterIdentifier value for the DB cluster.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The database engine version.</p>"""
    backup_retention_period: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The pending change in storage type for the DB cluster. Valid Values:</p> <ul> <li> <p> <b> <code>standard</code> </b> – ( <i>the default</i> ) Configures cost-effective database storage for applications with moderate to small I/O usage.</p> </li> <li> <p> <b> <code>iopt1</code> </b> – Enables <a href="https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage">I/O-Optimized storage</a> that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.</p> <p>Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.</p> </li> </ul>"""
    allocated_storage: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>The allocated storage size in gibibytes (GiB) for database engines. For Neptune, <code>AllocatedStorage</code> always returns 1, because Neptune DB cluster storage size isn't fixed, but instead automatically adjusts as needed.</p>"""
    iops: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>The Provisioned IOPS (I/O operations per second) value. This setting is only for Multi-AZ DB clusters.</p>"""
    network_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The pending change in network type for the DB cluster.</p> <p>Valid Values: <code>IPV4</code>, <code>DUAL</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterPendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pending_cloudwatch_logs_exports" in value:
        import capo_neptune.types.pending_cloudwatch_logs_exports

        capo_neptune.types.pending_cloudwatch_logs_exports.serialize_query(
            value["pending_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}PendingCloudwatchLogsExports",
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))


def deserialize_query(el: Element) -> ClusterPendingModifiedValues:
    out: ClusterPendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_pending_cloudwatch_logs_exports = el.find("PendingCloudwatchLogsExports")
    if child_pending_cloudwatch_logs_exports is not None:
        import capo_neptune.types.pending_cloudwatch_logs_exports

        out["pending_cloudwatch_logs_exports"] = (
            capo_neptune.types.pending_cloudwatch_logs_exports.deserialize_query(
                child_pending_cloudwatch_logs_exports
            )
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    return out
