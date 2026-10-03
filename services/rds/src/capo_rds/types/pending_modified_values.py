"""Generated from Smithy shape ``com.amazonaws.rds#PendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.automation_mode
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.pending_cloudwatch_logs_exports
    import capo_rds.types.processor_feature_list
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class PendingModifiedValues(TypedDict, closed=True):
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the compute and memory capacity class for the DB instance.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The allocated storage size for the DB instance specified in gibibytes (GiB).</p>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The master credentials for the DB instance.</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port for the DB instance.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained.</p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the Single-AZ DB instance will change to a Multi-AZ deployment.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine version.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model for the DB instance.</p> <p>Valid values: <code>license-included</code> | <code>bring-your-own-license</code> | <code>general-public-license</code> | <code>bring-your-own-media</code> </p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The Provisioned IOPS value for the DB instance.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput of the DB instance.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The database identifier for the DB instance.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type of the DB instance.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the CA certificate for the DB instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The DB subnet group for the DB instance.</p>"""
    pending_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.pending_cloudwatch_logs_exports.PendingCloudwatchLogsExports"
    ]
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p>"""
    automation_mode: NotRequired["capo_rds.types.automation_mode.AutomationMode"]
    """<p>The automation mode of the RDS Custom DB instance: <code>full</code> or <code>all-paused</code>. If <code>full</code>, the DB instance automates monitoring and instance recovery. If <code>all-paused</code>, the instance pauses automation for the duration set by <code>--resume-full-automation-mode-minutes</code>.</p>"""
    resume_full_automation_mode_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance will change to the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE). </p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.&gt;</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine of the DB instance.</p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>The additional storage volume modifications that are pending for the DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "pending_cloudwatch_logs_exports" in value:
        import capo_rds.types.pending_cloudwatch_logs_exports

        capo_rds.types.pending_cloudwatch_logs_exports.serialize_query(
            value["pending_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}PendingCloudwatchLogsExports",
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
        )
    if "automation_mode" in value:
        import capo_rds.types.automation_mode

        capo_rds.types.automation_mode.serialize_query(
            value["automation_mode"], pairs, f"{key_prefix}AutomationMode"
        )
    if "resume_full_automation_mode_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["resume_full_automation_mode_time"],
            pairs,
            f"{key_prefix}ResumeFullAutomationModeTime",
        )
    if "multi_tenant" in value:
        pairs.append(
            (f"{key_prefix}MultiTenant", "true" if value["multi_tenant"] else "false")
        )
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "additional_storage_volumes" in value:
        import capo_rds.types.additional_storage_volumes_list

        capo_rds.types.additional_storage_volumes_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )


def deserialize_query(el: Element) -> PendingModifiedValues:
    out: PendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_pending_cloudwatch_logs_exports = el.find("PendingCloudwatchLogsExports")
    if child_pending_cloudwatch_logs_exports is not None:
        import capo_rds.types.pending_cloudwatch_logs_exports

        out["pending_cloudwatch_logs_exports"] = (
            capo_rds.types.pending_cloudwatch_logs_exports.deserialize_query(
                child_pending_cloudwatch_logs_exports
            )
        )
    child_processor_features = el.find("ProcessorFeatures")
    if child_processor_features is not None:
        import capo_rds.types.processor_feature_list

        out["processor_features"] = (
            capo_rds.types.processor_feature_list.deserialize_query(
                child_processor_features
            )
        )
    child_automation_mode = el.find("AutomationMode")
    if child_automation_mode is not None:
        import capo_rds.types.automation_mode

        out["automation_mode"] = capo_rds.types.automation_mode.deserialize_query(
            child_automation_mode
        )
    child_resume_full_automation_mode_time = el.find("ResumeFullAutomationModeTime")
    if child_resume_full_automation_mode_time is not None:
        import capo_rds.types.t_stamp

        out["resume_full_automation_mode_time"] = (
            capo_rds.types.t_stamp.deserialize_query(
                child_resume_full_automation_mode_time
            )
        )
    child_multi_tenant = el.find("MultiTenant")
    if child_multi_tenant is not None:
        out["multi_tenant"] = (child_multi_tenant.text or "").lower() == "true"
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    return out
