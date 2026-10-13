"""Generated from Smithy shape ``com.amazonaws.rds#ClusterPendingModifiedValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.certificate_details
    import capo_rds.types.integer_optional
    import capo_rds.types.pending_cloudwatch_logs_exports
    import capo_rds.types.rds_custom_cluster_configuration
    import capo_rds.types.sensitive_string
    import capo_rds.types.string


class ClusterPendingModifiedValues(TypedDict, closed=True):
    pending_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.pending_cloudwatch_logs_exports.PendingCloudwatchLogsExports"
    ]
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DBClusterIdentifier value for the DB cluster.</p>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The master credentials for the DB cluster.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine version.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type for the DB cluster.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The allocated storage size in gibibytes (GiB) for all database engines except Amazon Aurora. For Aurora, <code>AllocatedStorage</code> always returns 1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.</p>"""
    rds_custom_cluster_configuration: NotRequired[
        "capo_rds.types.rds_custom_cluster_configuration.RdsCustomClusterConfiguration"
    ]
    """<p>Reserved for future use.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The Provisioned IOPS (I/O operations per second) value. This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    certificate_details: NotRequired[
        "capo_rds.types.certificate_details.CertificateDetails"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterPendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pending_cloudwatch_logs_exports" in value:
        import capo_rds.types.pending_cloudwatch_logs_exports

        capo_rds.types.pending_cloudwatch_logs_exports.serialize_query(
            value["pending_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}PendingCloudwatchLogsExports",
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
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
    if "rds_custom_cluster_configuration" in value:
        import capo_rds.types.rds_custom_cluster_configuration

        capo_rds.types.rds_custom_cluster_configuration.serialize_query(
            value["rds_custom_cluster_configuration"],
            pairs,
            f"{key_prefix}RdsCustomClusterConfiguration",
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "certificate_details" in value:
        import capo_rds.types.certificate_details

        capo_rds.types.certificate_details.serialize_query(
            value["certificate_details"], pairs, f"{key_prefix}CertificateDetails"
        )


def deserialize_query(el: Element) -> ClusterPendingModifiedValues:
    out: ClusterPendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_pending_cloudwatch_logs_exports = el.find("PendingCloudwatchLogsExports")
    if child_pending_cloudwatch_logs_exports is not None:
        import capo_rds.types.pending_cloudwatch_logs_exports

        out["pending_cloudwatch_logs_exports"] = (
            capo_rds.types.pending_cloudwatch_logs_exports.deserialize_query(
                child_pending_cloudwatch_logs_exports
            )
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
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
    child_rds_custom_cluster_configuration = el.find("RdsCustomClusterConfiguration")
    if child_rds_custom_cluster_configuration is not None:
        import capo_rds.types.rds_custom_cluster_configuration

        out["rds_custom_cluster_configuration"] = (
            capo_rds.types.rds_custom_cluster_configuration.deserialize_query(
                child_rds_custom_cluster_configuration
            )
        )
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_certificate_details = el.find("CertificateDetails")
    if child_certificate_details is not None:
        import capo_rds.types.certificate_details

        out["certificate_details"] = (
            capo_rds.types.certificate_details.deserialize_query(
                child_certificate_details
            )
        )
    return out


def redact_sensitive(value: ClusterPendingModifiedValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "master_user_password" in value:
        out["master_user_password"] = "*** Sensitive Data Redacted ***"
    return out
