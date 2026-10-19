"""Generated from Smithy shape ``com.amazonaws.odb#UpdateAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.admin_password_source
    import capo_odb.types.admin_password_source_configuration_input
    import capo_odb.types.autonomous_maintenance_schedule_type
    import capo_odb.types.customer_contacts
    import capo_odb.types.database_edition
    import capo_odb.types.database_tool_list
    import capo_odb.types.db_workload
    import capo_odb.types.encryption_key_configuration_input
    import capo_odb.types.encryption_key_provider_input
    import capo_odb.types.license_model
    import capo_odb.types.long_term_backup_schedule
    import capo_odb.types.open_mode
    import capo_odb.types.permission_level
    import capo_odb.types.refreshable_mode
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_pool_summary
    import capo_odb.types.scheduled_operation_details_list
    import capo_odb.types.sensitive_string
    import capo_odb.types.standby_allowlisted_ips_source
    import capo_odb.types.string_list


class UpdateAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to update.</p>"""
    admin_password: NotRequired["capo_odb.types.sensitive_string.SensitiveString"]
    """<p>The new password for the <code>ADMIN</code> user of the Autonomous Database.</p>"""
    compute_count: NotRequired["float"]
    """<p>The compute capacity, in number of ECPUs or OCPUs, to assign to the Autonomous Database.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores to allocate to the Autonomous Database.</p>"""
    data_storage_size_in_t_bs: NotRequired["int"]
    """<p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>"""
    data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The new user-friendly name for the Autonomous Database.</p>"""
    db_name: NotRequired["str"]
    """<p>The new name of the Autonomous Database.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version to use for the Autonomous Database.</p>"""
    db_workload: NotRequired["capo_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""
    db_tools_details: NotRequired["capo_odb.types.database_tool_list.DatabaseToolList"]
    """<p>The list of database management tools to enable for the Autonomous Database.</p>"""
    database_edition: NotRequired["capo_odb.types.database_edition.DatabaseEdition"]
    """<p>The Oracle Database edition to apply to the Autonomous Database.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Autonomous Database.</p>"""
    is_auto_scaling_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>"""
    is_auto_scaling_for_storage_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>"""
    is_backup_retention_locked: NotRequired["bool"]
    """<p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>"""
    is_local_data_guard_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>"""
    is_mtls_connection_required: NotRequired["bool"]
    """<p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>"""
    is_refreshable_clone: NotRequired["bool"]
    """<p>Specifies whether the Autonomous Database is a refreshable clone.</p>"""
    is_disconnect_peer: NotRequired["bool"]
    """<p>Specifies whether to disconnect the Autonomous Database from its peer database.</p>"""
    backup_retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for automatic backups of the Autonomous Database.</p>"""
    byol_compute_count_limit: NotRequired["float"]
    """<p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>"""
    local_adg_auto_failover_max_data_loss_limit: NotRequired["int"]
    """<p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>"""
    autonomous_maintenance_schedule_type: NotRequired[
        "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
    ]
    """<p>The maintenance schedule type for the Autonomous Database.</p>"""
    customer_contacts_to_send_to_oci: NotRequired[
        "capo_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The list of customer contacts to receive operational notifications from OCI for the Autonomous Database.</p>"""
    scheduled_operations: NotRequired[
        "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
    ]
    """<p>The list of scheduled start and stop times for the Autonomous Database.</p>"""
    long_term_backup_schedule: NotRequired[
        "capo_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
    ]
    """<p>The long-term backup schedule for the Autonomous Database.</p>"""
    open_mode: NotRequired["capo_odb.types.open_mode.OpenMode"]
    """<p>The mode in which to open the Autonomous Database, either read-only or read/write.</p>"""
    permission_level: NotRequired["capo_odb.types.permission_level.PermissionLevel"]
    """<p>The permission level of the Autonomous Database.</p>"""
    refreshable_mode: NotRequired["capo_odb.types.refreshable_mode.RefreshableMode"]
    """<p>The refresh mode of the refreshable clone Autonomous Database.</p>"""
    private_endpoint_ip: NotRequired["str"]
    """<p>The private endpoint IP address for the Autonomous Database.</p>"""
    private_endpoint_label: NotRequired["str"]
    """<p>The private endpoint label for the Autonomous Database.</p>"""
    peer_db_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the peer Autonomous Database.</p>"""
    resource_pool_leader_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the resource pool leader Autonomous Database.</p>"""
    resource_pool_summary: NotRequired[
        "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
    ]
    """<p>The configuration of the resource pool for the Autonomous Database.</p>"""
    standby_allowlisted_ips_source: NotRequired[
        "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
    ]
    """<p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>"""
    standby_allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>"""
    allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the Autonomous Database.</p>"""
    auto_refresh_frequency_in_seconds: NotRequired["int"]
    """<p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>"""
    auto_refresh_point_lag_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>"""
    time_of_auto_refresh_start: NotRequired["datetime.datetime"]
    """<p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>"""
    encryption_key_provider: NotRequired[
        "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
    ]
    """<p>The provider of the encryption key to use for the Autonomous Database.</p>"""
    encryption_key_configuration: NotRequired[
        "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
    ]
    """<p>The configuration of the encryption key to use for the Autonomous Database.</p>"""
    admin_password_source: NotRequired[
        "capo_odb.types.admin_password_source.AdminPasswordSource"
    ]
    """<p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>"""
    admin_password_source_configuration: NotRequired[
        "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
    ]
    """<p>The configuration of the admin password source for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "admin_password" in value:
        out["adminPassword"] = value["admin_password"]
    if "compute_count" in value:
        out["computeCount"] = (
            "NaN"
            if value["compute_count"] != value["compute_count"]
            else "Infinity"
            if value["compute_count"] == float("inf")
            else "-Infinity"
            if value["compute_count"] == float("-inf")
            else value["compute_count"]
        )
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = value["data_storage_size_in_g_bs"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "db_workload" in value:
        import capo_odb.types.db_workload

        out["dbWorkload"] = capo_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    if "db_tools_details" in value:
        import capo_odb.types.database_tool_list

        out["dbToolsDetails"] = (
            capo_odb.types.database_tool_list.serialize_aws_json_1_0(
                value["db_tools_details"]
            )
        )
    if "database_edition" in value:
        import capo_odb.types.database_edition

        out["databaseEdition"] = capo_odb.types.database_edition.serialize_aws_json_1_0(
            value["database_edition"]
        )
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "is_auto_scaling_enabled" in value:
        out["isAutoScalingEnabled"] = value["is_auto_scaling_enabled"]
    if "is_auto_scaling_for_storage_enabled" in value:
        out["isAutoScalingForStorageEnabled"] = value[
            "is_auto_scaling_for_storage_enabled"
        ]
    if "is_backup_retention_locked" in value:
        out["isBackupRetentionLocked"] = value["is_backup_retention_locked"]
    if "is_local_data_guard_enabled" in value:
        out["isLocalDataGuardEnabled"] = value["is_local_data_guard_enabled"]
    if "is_mtls_connection_required" in value:
        out["isMtlsConnectionRequired"] = value["is_mtls_connection_required"]
    if "is_refreshable_clone" in value:
        out["isRefreshableClone"] = value["is_refreshable_clone"]
    if "is_disconnect_peer" in value:
        out["isDisconnectPeer"] = value["is_disconnect_peer"]
    if "backup_retention_period_in_days" in value:
        out["backupRetentionPeriodInDays"] = value["backup_retention_period_in_days"]
    if "byol_compute_count_limit" in value:
        out["byolComputeCountLimit"] = (
            "NaN"
            if value["byol_compute_count_limit"] != value["byol_compute_count_limit"]
            else "Infinity"
            if value["byol_compute_count_limit"] == float("inf")
            else "-Infinity"
            if value["byol_compute_count_limit"] == float("-inf")
            else value["byol_compute_count_limit"]
        )
    if "local_adg_auto_failover_max_data_loss_limit" in value:
        out["localAdgAutoFailoverMaxDataLossLimit"] = value[
            "local_adg_auto_failover_max_data_loss_limit"
        ]
    if "autonomous_maintenance_schedule_type" in value:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomousMaintenanceScheduleType"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.serialize_aws_json_1_0(
                value["autonomous_maintenance_schedule_type"]
            )
        )
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customerContactsToSendToOCI"] = (
            capo_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    if "scheduled_operations" in value:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduledOperations"] = (
            capo_odb.types.scheduled_operation_details_list.serialize_aws_json_1_0(
                value["scheduled_operations"]
            )
        )
    if "long_term_backup_schedule" in value:
        import capo_odb.types.long_term_backup_schedule

        out["longTermBackupSchedule"] = (
            capo_odb.types.long_term_backup_schedule.serialize_aws_json_1_0(
                value["long_term_backup_schedule"]
            )
        )
    if "open_mode" in value:
        import capo_odb.types.open_mode

        out["openMode"] = capo_odb.types.open_mode.serialize_aws_json_1_0(
            value["open_mode"]
        )
    if "permission_level" in value:
        import capo_odb.types.permission_level

        out["permissionLevel"] = capo_odb.types.permission_level.serialize_aws_json_1_0(
            value["permission_level"]
        )
    if "refreshable_mode" in value:
        import capo_odb.types.refreshable_mode

        out["refreshableMode"] = capo_odb.types.refreshable_mode.serialize_aws_json_1_0(
            value["refreshable_mode"]
        )
    if "private_endpoint_ip" in value:
        out["privateEndpointIp"] = value["private_endpoint_ip"]
    if "private_endpoint_label" in value:
        out["privateEndpointLabel"] = value["private_endpoint_label"]
    if "peer_db_id" in value:
        out["peerDbId"] = value["peer_db_id"]
    if "resource_pool_leader_id" in value:
        out["resourcePoolLeaderId"] = value["resource_pool_leader_id"]
    if "resource_pool_summary" in value:
        import capo_odb.types.resource_pool_summary

        out["resourcePoolSummary"] = (
            capo_odb.types.resource_pool_summary.serialize_aws_json_1_0(
                value["resource_pool_summary"]
            )
        )
    if "standby_allowlisted_ips_source" in value:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standbyAllowlistedIpsSource"] = (
            capo_odb.types.standby_allowlisted_ips_source.serialize_aws_json_1_0(
                value["standby_allowlisted_ips_source"]
            )
        )
    if "standby_allowlisted_ips" in value:
        import capo_odb.types.string_list

        out["standbyAllowlistedIps"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["standby_allowlisted_ips"]
            )
        )
    if "allowlisted_ips" in value:
        import capo_odb.types.string_list

        out["allowlistedIps"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["allowlisted_ips"]
        )
    if "auto_refresh_frequency_in_seconds" in value:
        out["autoRefreshFrequencyInSeconds"] = value[
            "auto_refresh_frequency_in_seconds"
        ]
    if "auto_refresh_point_lag_in_seconds" in value:
        out["autoRefreshPointLagInSeconds"] = value["auto_refresh_point_lag_in_seconds"]
    if "time_of_auto_refresh_start" in value:
        import capo_odb._protocol.serialize

        out["timeOfAutoRefreshStart"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_auto_refresh_start"]
        )
    if "encryption_key_provider" in value:
        import capo_odb.types.encryption_key_provider_input

        out["encryptionKeyProvider"] = (
            capo_odb.types.encryption_key_provider_input.serialize_aws_json_1_0(
                value["encryption_key_provider"]
            )
        )
    if "encryption_key_configuration" in value:
        import capo_odb.types.encryption_key_configuration_input

        out["encryptionKeyConfiguration"] = (
            capo_odb.types.encryption_key_configuration_input.serialize_aws_json_1_0(
                value["encryption_key_configuration"]
            )
        )
    if "admin_password_source" in value:
        import capo_odb.types.admin_password_source

        out["adminPasswordSource"] = (
            capo_odb.types.admin_password_source.serialize_aws_json_1_0(
                value["admin_password_source"]
            )
        )
    if "admin_password_source_configuration" in value:
        import capo_odb.types.admin_password_source_configuration_input

        out["adminPasswordSourceConfiguration"] = (
            capo_odb.types.admin_password_source_configuration_input.serialize_aws_json_1_0(
                value["admin_password_source_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutonomousDatabaseInput:
    out: UpdateAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("adminPassword") is not None:
        out["admin_password"] = data["adminPassword"]
    if data.get("computeCount") is not None:
        out["compute_count"] = float(data["computeCount"])
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if data.get("dataStorageSizeInGBs") is not None:
        out["data_storage_size_in_g_bs"] = data["dataStorageSizeInGBs"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("dbName") is not None:
        out["db_name"] = data["dbName"]
    if data.get("dbVersion") is not None:
        out["db_version"] = data["dbVersion"]
    if data.get("dbWorkload") is not None:
        import capo_odb.types.db_workload

        out["db_workload"] = capo_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    if data.get("dbToolsDetails") is not None:
        import capo_odb.types.database_tool_list

        out["db_tools_details"] = (
            capo_odb.types.database_tool_list.deserialize_aws_json_1_0(
                data["dbToolsDetails"]
            )
        )
    if data.get("databaseEdition") is not None:
        import capo_odb.types.database_edition

        out["database_edition"] = (
            capo_odb.types.database_edition.deserialize_aws_json_1_0(
                data["databaseEdition"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("isAutoScalingEnabled") is not None:
        out["is_auto_scaling_enabled"] = data["isAutoScalingEnabled"]
    if data.get("isAutoScalingForStorageEnabled") is not None:
        out["is_auto_scaling_for_storage_enabled"] = data[
            "isAutoScalingForStorageEnabled"
        ]
    if data.get("isBackupRetentionLocked") is not None:
        out["is_backup_retention_locked"] = data["isBackupRetentionLocked"]
    if data.get("isLocalDataGuardEnabled") is not None:
        out["is_local_data_guard_enabled"] = data["isLocalDataGuardEnabled"]
    if data.get("isMtlsConnectionRequired") is not None:
        out["is_mtls_connection_required"] = data["isMtlsConnectionRequired"]
    if data.get("isRefreshableClone") is not None:
        out["is_refreshable_clone"] = data["isRefreshableClone"]
    if data.get("isDisconnectPeer") is not None:
        out["is_disconnect_peer"] = data["isDisconnectPeer"]
    if data.get("backupRetentionPeriodInDays") is not None:
        out["backup_retention_period_in_days"] = data["backupRetentionPeriodInDays"]
    if data.get("byolComputeCountLimit") is not None:
        out["byol_compute_count_limit"] = float(data["byolComputeCountLimit"])
    if data.get("localAdgAutoFailoverMaxDataLossLimit") is not None:
        out["local_adg_auto_failover_max_data_loss_limit"] = data[
            "localAdgAutoFailoverMaxDataLossLimit"
        ]
    if data.get("autonomousMaintenanceScheduleType") is not None:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomous_maintenance_schedule_type"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.deserialize_aws_json_1_0(
                data["autonomousMaintenanceScheduleType"]
            )
        )
    if data.get("customerContactsToSendToOCI") is not None:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContactsToSendToOCI"]
            )
        )
    if data.get("scheduledOperations") is not None:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduled_operations"] = (
            capo_odb.types.scheduled_operation_details_list.deserialize_aws_json_1_0(
                data["scheduledOperations"]
            )
        )
    if data.get("longTermBackupSchedule") is not None:
        import capo_odb.types.long_term_backup_schedule

        out["long_term_backup_schedule"] = (
            capo_odb.types.long_term_backup_schedule.deserialize_aws_json_1_0(
                data["longTermBackupSchedule"]
            )
        )
    if data.get("openMode") is not None:
        import capo_odb.types.open_mode

        out["open_mode"] = capo_odb.types.open_mode.deserialize_aws_json_1_0(
            data["openMode"]
        )
    if data.get("permissionLevel") is not None:
        import capo_odb.types.permission_level

        out["permission_level"] = (
            capo_odb.types.permission_level.deserialize_aws_json_1_0(
                data["permissionLevel"]
            )
        )
    if data.get("refreshableMode") is not None:
        import capo_odb.types.refreshable_mode

        out["refreshable_mode"] = (
            capo_odb.types.refreshable_mode.deserialize_aws_json_1_0(
                data["refreshableMode"]
            )
        )
    if data.get("privateEndpointIp") is not None:
        out["private_endpoint_ip"] = data["privateEndpointIp"]
    if data.get("privateEndpointLabel") is not None:
        out["private_endpoint_label"] = data["privateEndpointLabel"]
    if data.get("peerDbId") is not None:
        out["peer_db_id"] = data["peerDbId"]
    if data.get("resourcePoolLeaderId") is not None:
        out["resource_pool_leader_id"] = data["resourcePoolLeaderId"]
    if data.get("resourcePoolSummary") is not None:
        import capo_odb.types.resource_pool_summary

        out["resource_pool_summary"] = (
            capo_odb.types.resource_pool_summary.deserialize_aws_json_1_0(
                data["resourcePoolSummary"]
            )
        )
    if data.get("standbyAllowlistedIpsSource") is not None:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standby_allowlisted_ips_source"] = (
            capo_odb.types.standby_allowlisted_ips_source.deserialize_aws_json_1_0(
                data["standbyAllowlistedIpsSource"]
            )
        )
    if data.get("standbyAllowlistedIps") is not None:
        import capo_odb.types.string_list

        out["standby_allowlisted_ips"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["standbyAllowlistedIps"]
            )
        )
    if data.get("allowlistedIps") is not None:
        import capo_odb.types.string_list

        out["allowlisted_ips"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["allowlistedIps"]
        )
    if data.get("autoRefreshFrequencyInSeconds") is not None:
        out["auto_refresh_frequency_in_seconds"] = data["autoRefreshFrequencyInSeconds"]
    if data.get("autoRefreshPointLagInSeconds") is not None:
        out["auto_refresh_point_lag_in_seconds"] = data["autoRefreshPointLagInSeconds"]
    if data.get("timeOfAutoRefreshStart") is not None:
        import datetime

        out["time_of_auto_refresh_start"] = datetime.datetime.fromisoformat(
            data["timeOfAutoRefreshStart"].replace("Z", "+00:00")
        )
    if data.get("encryptionKeyProvider") is not None:
        import capo_odb.types.encryption_key_provider_input

        out["encryption_key_provider"] = (
            capo_odb.types.encryption_key_provider_input.deserialize_aws_json_1_0(
                data["encryptionKeyProvider"]
            )
        )
    if data.get("encryptionKeyConfiguration") is not None:
        import capo_odb.types.encryption_key_configuration_input

        out["encryption_key_configuration"] = (
            capo_odb.types.encryption_key_configuration_input.deserialize_aws_json_1_0(
                data["encryptionKeyConfiguration"]
            )
        )
    if data.get("adminPasswordSource") is not None:
        import capo_odb.types.admin_password_source

        out["admin_password_source"] = (
            capo_odb.types.admin_password_source.deserialize_aws_json_1_0(
                data["adminPasswordSource"]
            )
        )
    if data.get("adminPasswordSourceConfiguration") is not None:
        import capo_odb.types.admin_password_source_configuration_input

        out["admin_password_source_configuration"] = (
            capo_odb.types.admin_password_source_configuration_input.deserialize_aws_json_1_0(
                data["adminPasswordSourceConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateAutonomousDatabaseInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "admin_password" in value:
        out["admin_password"] = "*** Sensitive Data Redacted ***"
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.redact_sensitive(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    return out
