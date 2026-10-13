"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.admin_password_source_summary
    import capo_odb.types.autonomous_database_apex
    import capo_odb.types.autonomous_database_connection_strings
    import capo_odb.types.autonomous_database_connection_urls
    import capo_odb.types.autonomous_database_resource_status
    import capo_odb.types.autonomous_maintenance_schedule_type
    import capo_odb.types.compute_model
    import capo_odb.types.customer_contacts
    import capo_odb.types.data_guard_role
    import capo_odb.types.data_safe_status
    import capo_odb.types.database_edition
    import capo_odb.types.database_management_status
    import capo_odb.types.database_standby_summary
    import capo_odb.types.database_tool_list
    import capo_odb.types.database_type
    import capo_odb.types.db_workload
    import capo_odb.types.disaster_recovery_configuration
    import capo_odb.types.disaster_recovery_type
    import capo_odb.types.encryption_summary
    import capo_odb.types.integer_list
    import capo_odb.types.license_model
    import capo_odb.types.long_term_backup_schedule
    import capo_odb.types.net_services_architecture
    import capo_odb.types.open_mode
    import capo_odb.types.operations_insights_status
    import capo_odb.types.permission_level
    import capo_odb.types.refreshable_mode
    import capo_odb.types.refreshable_status
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_pool_summary
    import capo_odb.types.scheduled_operation_details_list
    import capo_odb.types.standby_allowlisted_ips_source
    import capo_odb.types.string_list


class AutonomousDatabaseSummary(TypedDict, closed=True):
    autonomous_database_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Autonomous Database.</p>"""
    autonomous_database_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Autonomous Database.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the Oracle Cloud Infrastructure (OCI) resource anchor associated with the Autonomous Database.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The progress of the current operation on the Autonomous Database, as a percentage.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous Database.</p>"""
    oci_url: NotRequired["str"]
    """<p>The URL for accessing the OCI console page for the Autonomous Database.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database.</p>"""
    db_name: NotRequired["str"]
    """<p>The name of the Autonomous Database.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique identifier of the source from which the Autonomous Database was created.</p>"""
    status: NotRequired[
        "capo_odb.types.autonomous_database_resource_status.AutonomousDatabaseResourceStatus"
    ]
    """<p>The current status of the Autonomous Database.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database, if applicable.</p>"""
    database_type: NotRequired["capo_odb.types.database_type.DatabaseType"]
    """<p>The type of the Autonomous Database, either a regular database or a clone.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version of the Autonomous Database.</p>"""
    db_workload: NotRequired["capo_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""
    character_set: NotRequired["str"]
    """<p>The character set of the Autonomous Database.</p>"""
    ncharacter_set: NotRequired["str"]
    """<p>The national character set of the Autonomous Database.</p>"""
    database_edition: NotRequired["capo_odb.types.database_edition.DatabaseEdition"]
    """<p>The Oracle Database edition of the Autonomous Database.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model that applies to the Autonomous Database.</p>"""
    open_mode: NotRequired["capo_odb.types.open_mode.OpenMode"]
    """<p>The mode in which the Autonomous Database is open, either read-only or read/write.</p>"""
    permission_level: NotRequired["capo_odb.types.permission_level.PermissionLevel"]
    """<p>The permission level of the Autonomous Database.</p>"""
    is_mtls_connection_required: NotRequired["bool"]
    """<p>Indicates whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>"""
    autonomous_maintenance_schedule_type: NotRequired[
        "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
    ]
    """<p>The maintenance schedule type for the Autonomous Database.</p>"""
    net_services_architecture: NotRequired[
        "capo_odb.types.net_services_architecture.NetServicesArchitecture"
    ]
    """<p>The Oracle Net Services architecture of the Autonomous Database, either dedicated or shared.</p>"""
    available_upgrade_versions: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of Oracle Database software versions to which the Autonomous Database can be upgraded.</p>"""
    byol_compute_count_limit: NotRequired["int"]
    """<p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>"""
    connection_string_details: NotRequired[
        "capo_odb.types.autonomous_database_connection_strings.AutonomousDatabaseConnectionStrings"
    ]
    """<p>The connection string details for the Autonomous Database.</p>"""
    service_console_url: NotRequired["str"]
    """<p>The URL for accessing the Oracle service console for the Autonomous Database.</p>"""
    sql_web_developer_url: NotRequired["str"]
    """<p>The URL for accessing Oracle SQL Developer Web for the Autonomous Database.</p>"""
    customer_contacts: NotRequired["capo_odb.types.customer_contacts.CustomerContacts"]
    """<p>The list of customer contacts that receive operational notifications from Oracle for the Autonomous Database.</p>"""
    apex_details: NotRequired[
        "capo_odb.types.autonomous_database_apex.AutonomousDatabaseApex"
    ]
    """<p>The Oracle Application Express (APEX) details for the Autonomous Database.</p>"""
    standby_db: NotRequired[
        "capo_odb.types.database_standby_summary.DatabaseStandbySummary"
    ]
    """<p>The details of the standby Autonomous Database in a cross-Region Oracle Data Guard configuration.</p>"""
    local_standby_db: NotRequired[
        "capo_odb.types.database_standby_summary.DatabaseStandbySummary"
    ]
    """<p>The details of the local standby Autonomous Database in an Oracle Data Guard configuration.</p>"""
    data_safe_status: NotRequired["capo_odb.types.data_safe_status.DataSafeStatus"]
    """<p>The status of the Oracle Data Safe registration for the Autonomous Database.</p>"""
    database_management_status: NotRequired[
        "capo_odb.types.database_management_status.DatabaseManagementStatus"
    ]
    """<p>The status of Oracle Database Management for the Autonomous Database.</p>"""
    operations_insights_status: NotRequired[
        "capo_odb.types.operations_insights_status.OperationsInsightsStatus"
    ]
    """<p>The status of Oracle Operations Insights for the Autonomous Database.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone where the Autonomous Database is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The unique identifier of the Availability Zone where the Autonomous Database is located.</p>"""
    maintenance_target_component: NotRequired["str"]
    """<p>The component on the Autonomous Database that the current maintenance is being applied to.</p>"""
    connection_urls: NotRequired[
        "capo_odb.types.autonomous_database_connection_urls.AutonomousDatabaseConnectionUrls"
    ]
    """<p>The connection URLs for accessing tools and services for the Autonomous Database.</p>"""
    db_tools_details: NotRequired["capo_odb.types.database_tool_list.DatabaseToolList"]
    """<p>The list of database management tools enabled for the Autonomous Database.</p>"""
    scheduled_operations: NotRequired[
        "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
    ]
    """<p>The list of scheduled start and stop times for the Autonomous Database.</p>"""
    resource_pool_leader_id: NotRequired["str"]
    """<p>The unique identifier of the resource pool leader Autonomous Database.</p>"""
    compute_count: NotRequired["float"]
    """<p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), assigned to the Autonomous Database.</p>"""
    compute_model: NotRequired["capo_odb.types.compute_model.ComputeModel"]
    """<p>The compute model of the Autonomous Database, either ECPU or OCPU.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores allocated to the Autonomous Database.</p>"""
    memory_per_oracle_compute_unit_in_g_bs: NotRequired["int"]
    """<p>The amount of memory allocated per Oracle Compute Unit, in GB.</p>"""
    provisionable_cpus: NotRequired["capo_odb.types.integer_list.IntegerList"]
    """<p>The list of CPU core counts that you can provision for the Autonomous Database.</p>"""
    is_auto_scaling_enabled: NotRequired["bool"]
    """<p>Indicates whether automatic scaling of the compute resources is enabled for the Autonomous Database.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size, in terabytes (TB), of the data volume allocated for the Autonomous Database.</p>"""
    data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size, in gigabytes (GB), of the data volume allocated for the Autonomous Database.</p>"""
    used_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The amount of data storage currently in use by the Autonomous Database, in TB.</p>"""
    used_data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of data storage currently in use by the Autonomous Database, in GB.</p>"""
    actual_used_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The actual amount of data storage currently in use by the Autonomous Database, in TB.</p>"""
    allocated_storage_size_in_t_bs: NotRequired["float"]
    """<p>The amount of storage currently allocated to the Autonomous Database, in TB.</p>"""
    in_memory_area_in_g_bs: NotRequired["int"]
    """<p>The size of the in-memory area of the Autonomous Database, in GB.</p>"""
    is_auto_scaling_for_storage_enabled: NotRequired["bool"]
    """<p>Indicates whether automatic scaling of the storage is enabled for the Autonomous Database.</p>"""
    odb_network_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the ODB network associated with the Autonomous Database.</p>"""
    odb_network_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with the Autonomous Database.</p>"""
    private_endpoint: NotRequired["str"]
    """<p>The private endpoint for the Autonomous Database.</p>"""
    private_endpoint_ip: NotRequired["str"]
    """<p>The private endpoint IP address for the Autonomous Database.</p>"""
    private_endpoint_label: NotRequired["str"]
    """<p>The private endpoint label for the Autonomous Database.</p>"""
    allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the Autonomous Database.</p>"""
    standby_allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>"""
    standby_allowlisted_ips_source: NotRequired[
        "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
    ]
    """<p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>"""
    is_local_data_guard_enabled: NotRequired["bool"]
    """<p>Indicates whether local Oracle Data Guard is enabled for the Autonomous Database.</p>"""
    is_remote_data_guard_enabled: NotRequired["bool"]
    """<p>Indicates whether remote Oracle Data Guard is enabled for the Autonomous Database.</p>"""
    local_disaster_recovery_type: NotRequired[
        "capo_odb.types.disaster_recovery_type.DisasterRecoveryType"
    ]
    """<p>The type of local disaster recovery configured for the Autonomous Database.</p>"""
    role: NotRequired["capo_odb.types.data_guard_role.DataGuardRole"]
    """<p>The Oracle Data Guard role of the Autonomous Database.</p>"""
    peer_db_ids: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of unique identifiers of the peer Autonomous Databases.</p>"""
    failed_data_recovery_in_seconds: NotRequired["int"]
    """<p>The amount of time, in seconds, that the data in the Autonomous Database is behind the data in the primary database.</p>"""
    local_adg_auto_failover_max_data_loss_limit: NotRequired["int"]
    """<p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>"""
    remote_disaster_recovery_configuration: NotRequired[
        "capo_odb.types.disaster_recovery_configuration.DisasterRecoveryConfiguration"
    ]
    """<p>The configuration of the remote disaster recovery for the Autonomous Database.</p>"""
    is_refreshable_clone: NotRequired["bool"]
    """<p>Indicates whether the Autonomous Database is a refreshable clone.</p>"""
    refreshable_mode: NotRequired["capo_odb.types.refreshable_mode.RefreshableMode"]
    """<p>The refresh mode of the refreshable clone Autonomous Database.</p>"""
    refreshable_status: NotRequired[
        "capo_odb.types.refreshable_status.RefreshableStatus"
    ]
    """<p>The refresh status of the refreshable clone Autonomous Database.</p>"""
    auto_refresh_frequency_in_seconds: NotRequired["int"]
    """<p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>"""
    auto_refresh_point_lag_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>"""
    is_reconnect_clone_enabled: NotRequired["bool"]
    """<p>Indicates whether reconnecting the refreshable clone to its source Autonomous Database is enabled.</p>"""
    clone_table_space_list: NotRequired["capo_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone for the Autonomous Database.</p>"""
    backup_retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for automatic backups of the Autonomous Database.</p>"""
    long_term_backup_schedule: NotRequired[
        "capo_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
    ]
    """<p>The long-term backup schedule for the Autonomous Database.</p>"""
    is_backup_retention_locked: NotRequired["bool"]
    """<p>Indicates whether the backup retention period of the Autonomous Database is locked.</p>"""
    total_backup_storage_size_in_g_bs: NotRequired["float"]
    """<p>The total amount of backup storage used by the Autonomous Database, in GB.</p>"""
    resource_pool_summary: NotRequired[
        "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
    ]
    """<p>The configuration of the resource pool for the Autonomous Database.</p>"""
    encryption_summary: NotRequired[
        "capo_odb.types.encryption_summary.EncryptionSummary"
    ]
    """<p>The encryption configuration for the Autonomous Database.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database was created.</p>"""
    time_of_last_backup: NotRequired["datetime.datetime"]
    """<p>The date and time of the last backup of the Autonomous Database.</p>"""
    time_maintenance_begin: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the Autonomous Database begins.</p>"""
    time_maintenance_end: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the Autonomous Database ends.</p>"""
    time_local_data_guard_enabled: NotRequired["datetime.datetime"]
    """<p>The date and time when local Oracle Data Guard was enabled for the Autonomous Database.</p>"""
    time_data_guard_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the Oracle Data Guard role of the Autonomous Database last changed.</p>"""
    time_of_last_switchover: NotRequired["datetime.datetime"]
    """<p>The date and time of the last switchover operation for the Autonomous Database.</p>"""
    time_of_last_failover: NotRequired["datetime.datetime"]
    """<p>The date and time of the last failover operation for the Autonomous Database.</p>"""
    time_of_last_refresh: NotRequired["datetime.datetime"]
    """<p>The date and time of the last refresh of the refreshable clone Autonomous Database.</p>"""
    time_of_last_refresh_point: NotRequired["datetime.datetime"]
    """<p>The date and time as of which the data in the refreshable clone Autonomous Database is current.</p>"""
    time_of_next_refresh: NotRequired["datetime.datetime"]
    """<p>The date and time of the next scheduled refresh of the refreshable clone Autonomous Database.</p>"""
    time_of_auto_refresh_start: NotRequired["datetime.datetime"]
    """<p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>"""
    time_deletion_of_free_autonomous_database: NotRequired["datetime.datetime"]
    """<p>The date and time when the inactive Always Free Autonomous Database is scheduled to be automatically deleted.</p>"""
    time_reclamation_of_free_autonomous_database: NotRequired["datetime.datetime"]
    """<p>The date and time when the Always Free Autonomous Database is scheduled to be stopped because of inactivity.</p>"""
    time_disaster_recovery_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the disaster recovery role of the Autonomous Database last changed.</p>"""
    time_until_reconnect_clone_enabled: NotRequired["datetime.datetime"]
    """<p>The date and time until which reconnecting the refreshable clone to its source Autonomous Database is allowed.</p>"""
    next_long_term_backup_time_stamp: NotRequired["datetime.datetime"]
    """<p>The date and time of the next scheduled long-term backup of the Autonomous Database.</p>"""
    time_undeleted: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database was restored after deletion.</p>"""
    admin_password_source_summary: NotRequired[
        "capo_odb.types.admin_password_source_summary.AdminPasswordSourceSummary"
    ]
    """<p>The summary of the admin password source configuration for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseSummary) -> dict:
    out: dict = {}
    if "autonomous_database_id" in value:
        out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "autonomous_database_arn" in value:
        out["autonomousDatabaseArn"] = value["autonomous_database_arn"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "percent_progress" in value:
        out["percentProgress"] = (
            "NaN"
            if value["percent_progress"] != value["percent_progress"]
            else "Infinity"
            if value["percent_progress"] == float("inf")
            else "-Infinity"
            if value["percent_progress"] == float("-inf")
            else value["percent_progress"]
        )
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "status" in value:
        import capo_odb.types.autonomous_database_resource_status

        out["status"] = (
            capo_odb.types.autonomous_database_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "database_type" in value:
        import capo_odb.types.database_type

        out["databaseType"] = capo_odb.types.database_type.serialize_aws_json_1_0(
            value["database_type"]
        )
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "db_workload" in value:
        import capo_odb.types.db_workload

        out["dbWorkload"] = capo_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    if "character_set" in value:
        out["characterSet"] = value["character_set"]
    if "ncharacter_set" in value:
        out["ncharacterSet"] = value["ncharacter_set"]
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
    if "is_mtls_connection_required" in value:
        out["isMtlsConnectionRequired"] = value["is_mtls_connection_required"]
    if "autonomous_maintenance_schedule_type" in value:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomousMaintenanceScheduleType"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.serialize_aws_json_1_0(
                value["autonomous_maintenance_schedule_type"]
            )
        )
    if "net_services_architecture" in value:
        import capo_odb.types.net_services_architecture

        out["netServicesArchitecture"] = (
            capo_odb.types.net_services_architecture.serialize_aws_json_1_0(
                value["net_services_architecture"]
            )
        )
    if "available_upgrade_versions" in value:
        import capo_odb.types.string_list

        out["availableUpgradeVersions"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["available_upgrade_versions"]
            )
        )
    if "byol_compute_count_limit" in value:
        out["byolComputeCountLimit"] = value["byol_compute_count_limit"]
    if "connection_string_details" in value:
        import capo_odb.types.autonomous_database_connection_strings

        out["connectionStringDetails"] = (
            capo_odb.types.autonomous_database_connection_strings.serialize_aws_json_1_0(
                value["connection_string_details"]
            )
        )
    if "service_console_url" in value:
        out["serviceConsoleUrl"] = value["service_console_url"]
    if "sql_web_developer_url" in value:
        out["sqlWebDeveloperUrl"] = value["sql_web_developer_url"]
    if "customer_contacts" in value:
        import capo_odb.types.customer_contacts

        out["customerContacts"] = (
            capo_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts"]
            )
        )
    if "apex_details" in value:
        import capo_odb.types.autonomous_database_apex

        out["apexDetails"] = (
            capo_odb.types.autonomous_database_apex.serialize_aws_json_1_0(
                value["apex_details"]
            )
        )
    if "standby_db" in value:
        import capo_odb.types.database_standby_summary

        out["standbyDb"] = (
            capo_odb.types.database_standby_summary.serialize_aws_json_1_0(
                value["standby_db"]
            )
        )
    if "local_standby_db" in value:
        import capo_odb.types.database_standby_summary

        out["localStandbyDb"] = (
            capo_odb.types.database_standby_summary.serialize_aws_json_1_0(
                value["local_standby_db"]
            )
        )
    if "data_safe_status" in value:
        import capo_odb.types.data_safe_status

        out["dataSafeStatus"] = capo_odb.types.data_safe_status.serialize_aws_json_1_0(
            value["data_safe_status"]
        )
    if "database_management_status" in value:
        import capo_odb.types.database_management_status

        out["databaseManagementStatus"] = (
            capo_odb.types.database_management_status.serialize_aws_json_1_0(
                value["database_management_status"]
            )
        )
    if "operations_insights_status" in value:
        import capo_odb.types.operations_insights_status

        out["operationsInsightsStatus"] = (
            capo_odb.types.operations_insights_status.serialize_aws_json_1_0(
                value["operations_insights_status"]
            )
        )
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "maintenance_target_component" in value:
        out["maintenanceTargetComponent"] = value["maintenance_target_component"]
    if "connection_urls" in value:
        import capo_odb.types.autonomous_database_connection_urls

        out["connectionUrls"] = (
            capo_odb.types.autonomous_database_connection_urls.serialize_aws_json_1_0(
                value["connection_urls"]
            )
        )
    if "db_tools_details" in value:
        import capo_odb.types.database_tool_list

        out["dbToolsDetails"] = (
            capo_odb.types.database_tool_list.serialize_aws_json_1_0(
                value["db_tools_details"]
            )
        )
    if "scheduled_operations" in value:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduledOperations"] = (
            capo_odb.types.scheduled_operation_details_list.serialize_aws_json_1_0(
                value["scheduled_operations"]
            )
        )
    if "resource_pool_leader_id" in value:
        out["resourcePoolLeaderId"] = value["resource_pool_leader_id"]
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
    if "compute_model" in value:
        import capo_odb.types.compute_model

        out["computeModel"] = capo_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "memory_per_oracle_compute_unit_in_g_bs" in value:
        out["memoryPerOracleComputeUnitInGBs"] = value[
            "memory_per_oracle_compute_unit_in_g_bs"
        ]
    if "provisionable_cpus" in value:
        import capo_odb.types.integer_list

        out["provisionableCpus"] = capo_odb.types.integer_list.serialize_aws_json_1_0(
            value["provisionable_cpus"]
        )
    if "is_auto_scaling_enabled" in value:
        out["isAutoScalingEnabled"] = value["is_auto_scaling_enabled"]
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = (
            "NaN"
            if value["data_storage_size_in_t_bs"] != value["data_storage_size_in_t_bs"]
            else "Infinity"
            if value["data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["data_storage_size_in_t_bs"] == float("-inf")
            else value["data_storage_size_in_t_bs"]
        )
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = value["data_storage_size_in_g_bs"]
    if "used_data_storage_size_in_t_bs" in value:
        out["usedDataStorageSizeInTBs"] = (
            "NaN"
            if value["used_data_storage_size_in_t_bs"]
            != value["used_data_storage_size_in_t_bs"]
            else "Infinity"
            if value["used_data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["used_data_storage_size_in_t_bs"] == float("-inf")
            else value["used_data_storage_size_in_t_bs"]
        )
    if "used_data_storage_size_in_g_bs" in value:
        out["usedDataStorageSizeInGBs"] = value["used_data_storage_size_in_g_bs"]
    if "actual_used_data_storage_size_in_t_bs" in value:
        out["actualUsedDataStorageSizeInTBs"] = (
            "NaN"
            if value["actual_used_data_storage_size_in_t_bs"]
            != value["actual_used_data_storage_size_in_t_bs"]
            else "Infinity"
            if value["actual_used_data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["actual_used_data_storage_size_in_t_bs"] == float("-inf")
            else value["actual_used_data_storage_size_in_t_bs"]
        )
    if "allocated_storage_size_in_t_bs" in value:
        out["allocatedStorageSizeInTBs"] = (
            "NaN"
            if value["allocated_storage_size_in_t_bs"]
            != value["allocated_storage_size_in_t_bs"]
            else "Infinity"
            if value["allocated_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["allocated_storage_size_in_t_bs"] == float("-inf")
            else value["allocated_storage_size_in_t_bs"]
        )
    if "in_memory_area_in_g_bs" in value:
        out["inMemoryAreaInGBs"] = value["in_memory_area_in_g_bs"]
    if "is_auto_scaling_for_storage_enabled" in value:
        out["isAutoScalingForStorageEnabled"] = value[
            "is_auto_scaling_for_storage_enabled"
        ]
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "private_endpoint" in value:
        out["privateEndpoint"] = value["private_endpoint"]
    if "private_endpoint_ip" in value:
        out["privateEndpointIp"] = value["private_endpoint_ip"]
    if "private_endpoint_label" in value:
        out["privateEndpointLabel"] = value["private_endpoint_label"]
    if "allowlisted_ips" in value:
        import capo_odb.types.string_list

        out["allowlistedIps"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["allowlisted_ips"]
        )
    if "standby_allowlisted_ips" in value:
        import capo_odb.types.string_list

        out["standbyAllowlistedIps"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["standby_allowlisted_ips"]
            )
        )
    if "standby_allowlisted_ips_source" in value:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standbyAllowlistedIpsSource"] = (
            capo_odb.types.standby_allowlisted_ips_source.serialize_aws_json_1_0(
                value["standby_allowlisted_ips_source"]
            )
        )
    if "is_local_data_guard_enabled" in value:
        out["isLocalDataGuardEnabled"] = value["is_local_data_guard_enabled"]
    if "is_remote_data_guard_enabled" in value:
        out["isRemoteDataGuardEnabled"] = value["is_remote_data_guard_enabled"]
    if "local_disaster_recovery_type" in value:
        import capo_odb.types.disaster_recovery_type

        out["localDisasterRecoveryType"] = (
            capo_odb.types.disaster_recovery_type.serialize_aws_json_1_0(
                value["local_disaster_recovery_type"]
            )
        )
    if "role" in value:
        import capo_odb.types.data_guard_role

        out["role"] = capo_odb.types.data_guard_role.serialize_aws_json_1_0(
            value["role"]
        )
    if "peer_db_ids" in value:
        import capo_odb.types.string_list

        out["peerDbIds"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["peer_db_ids"]
        )
    if "failed_data_recovery_in_seconds" in value:
        out["failedDataRecoveryInSeconds"] = value["failed_data_recovery_in_seconds"]
    if "local_adg_auto_failover_max_data_loss_limit" in value:
        out["localAdgAutoFailoverMaxDataLossLimit"] = value[
            "local_adg_auto_failover_max_data_loss_limit"
        ]
    if "remote_disaster_recovery_configuration" in value:
        import capo_odb.types.disaster_recovery_configuration

        out["remoteDisasterRecoveryConfiguration"] = (
            capo_odb.types.disaster_recovery_configuration.serialize_aws_json_1_0(
                value["remote_disaster_recovery_configuration"]
            )
        )
    if "is_refreshable_clone" in value:
        out["isRefreshableClone"] = value["is_refreshable_clone"]
    if "refreshable_mode" in value:
        import capo_odb.types.refreshable_mode

        out["refreshableMode"] = capo_odb.types.refreshable_mode.serialize_aws_json_1_0(
            value["refreshable_mode"]
        )
    if "refreshable_status" in value:
        import capo_odb.types.refreshable_status

        out["refreshableStatus"] = (
            capo_odb.types.refreshable_status.serialize_aws_json_1_0(
                value["refreshable_status"]
            )
        )
    if "auto_refresh_frequency_in_seconds" in value:
        out["autoRefreshFrequencyInSeconds"] = value[
            "auto_refresh_frequency_in_seconds"
        ]
    if "auto_refresh_point_lag_in_seconds" in value:
        out["autoRefreshPointLagInSeconds"] = value["auto_refresh_point_lag_in_seconds"]
    if "is_reconnect_clone_enabled" in value:
        out["isReconnectCloneEnabled"] = value["is_reconnect_clone_enabled"]
    if "clone_table_space_list" in value:
        import capo_odb.types.integer_list

        out["cloneTableSpaceList"] = capo_odb.types.integer_list.serialize_aws_json_1_0(
            value["clone_table_space_list"]
        )
    if "backup_retention_period_in_days" in value:
        out["backupRetentionPeriodInDays"] = value["backup_retention_period_in_days"]
    if "long_term_backup_schedule" in value:
        import capo_odb.types.long_term_backup_schedule

        out["longTermBackupSchedule"] = (
            capo_odb.types.long_term_backup_schedule.serialize_aws_json_1_0(
                value["long_term_backup_schedule"]
            )
        )
    if "is_backup_retention_locked" in value:
        out["isBackupRetentionLocked"] = value["is_backup_retention_locked"]
    if "total_backup_storage_size_in_g_bs" in value:
        out["totalBackupStorageSizeInGBs"] = (
            "NaN"
            if value["total_backup_storage_size_in_g_bs"]
            != value["total_backup_storage_size_in_g_bs"]
            else "Infinity"
            if value["total_backup_storage_size_in_g_bs"] == float("inf")
            else "-Infinity"
            if value["total_backup_storage_size_in_g_bs"] == float("-inf")
            else value["total_backup_storage_size_in_g_bs"]
        )
    if "resource_pool_summary" in value:
        import capo_odb.types.resource_pool_summary

        out["resourcePoolSummary"] = (
            capo_odb.types.resource_pool_summary.serialize_aws_json_1_0(
                value["resource_pool_summary"]
            )
        )
    if "encryption_summary" in value:
        import capo_odb.types.encryption_summary

        out["encryptionSummary"] = (
            capo_odb.types.encryption_summary.serialize_aws_json_1_0(
                value["encryption_summary"]
            )
        )
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "time_of_last_backup" in value:
        import capo_odb._protocol.serialize

        out["timeOfLastBackup"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_last_backup"]
        )
    if "time_maintenance_begin" in value:
        import capo_odb._protocol.serialize

        out["timeMaintenanceBegin"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_maintenance_begin"]
        )
    if "time_maintenance_end" in value:
        import capo_odb._protocol.serialize

        out["timeMaintenanceEnd"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_maintenance_end"]
        )
    if "time_local_data_guard_enabled" in value:
        import capo_odb._protocol.serialize

        out["timeLocalDataGuardEnabled"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_local_data_guard_enabled"]
        )
    if "time_data_guard_role_changed" in value:
        import capo_odb._protocol.serialize

        out["timeDataGuardRoleChanged"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_data_guard_role_changed"]
        )
    if "time_of_last_switchover" in value:
        import capo_odb._protocol.serialize

        out["timeOfLastSwitchover"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_last_switchover"]
        )
    if "time_of_last_failover" in value:
        import capo_odb._protocol.serialize

        out["timeOfLastFailover"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_last_failover"]
        )
    if "time_of_last_refresh" in value:
        import capo_odb._protocol.serialize

        out["timeOfLastRefresh"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_last_refresh"]
        )
    if "time_of_last_refresh_point" in value:
        import capo_odb._protocol.serialize

        out["timeOfLastRefreshPoint"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_last_refresh_point"]
        )
    if "time_of_next_refresh" in value:
        import capo_odb._protocol.serialize

        out["timeOfNextRefresh"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_next_refresh"]
        )
    if "time_of_auto_refresh_start" in value:
        import capo_odb._protocol.serialize

        out["timeOfAutoRefreshStart"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_auto_refresh_start"]
        )
    if "time_deletion_of_free_autonomous_database" in value:
        import capo_odb._protocol.serialize

        out["timeDeletionOfFreeAutonomousDatabase"] = (
            capo_odb._protocol.serialize.fmt_date_time(
                value["time_deletion_of_free_autonomous_database"]
            )
        )
    if "time_reclamation_of_free_autonomous_database" in value:
        import capo_odb._protocol.serialize

        out["timeReclamationOfFreeAutonomousDatabase"] = (
            capo_odb._protocol.serialize.fmt_date_time(
                value["time_reclamation_of_free_autonomous_database"]
            )
        )
    if "time_disaster_recovery_role_changed" in value:
        import capo_odb._protocol.serialize

        out["timeDisasterRecoveryRoleChanged"] = (
            capo_odb._protocol.serialize.fmt_date_time(
                value["time_disaster_recovery_role_changed"]
            )
        )
    if "time_until_reconnect_clone_enabled" in value:
        import capo_odb._protocol.serialize

        out["timeUntilReconnectCloneEnabled"] = (
            capo_odb._protocol.serialize.fmt_date_time(
                value["time_until_reconnect_clone_enabled"]
            )
        )
    if "next_long_term_backup_time_stamp" in value:
        import capo_odb._protocol.serialize

        out["nextLongTermBackupTimeStamp"] = capo_odb._protocol.serialize.fmt_date_time(
            value["next_long_term_backup_time_stamp"]
        )
    if "time_undeleted" in value:
        import capo_odb._protocol.serialize

        out["timeUndeleted"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_undeleted"]
        )
    if "admin_password_source_summary" in value:
        import capo_odb.types.admin_password_source_summary

        out["adminPasswordSourceSummary"] = (
            capo_odb.types.admin_password_source_summary.serialize_aws_json_1_0(
                value["admin_password_source_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseSummary:
    out: AutonomousDatabaseSummary = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    if data.get("autonomousDatabaseArn") is not None:
        out["autonomous_database_arn"] = data["autonomousDatabaseArn"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("ociUrl") is not None:
        out["oci_url"] = data["ociUrl"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("dbName") is not None:
        out["db_name"] = data["dbName"]
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    if data.get("status") is not None:
        import capo_odb.types.autonomous_database_resource_status

        out["status"] = (
            capo_odb.types.autonomous_database_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("databaseType") is not None:
        import capo_odb.types.database_type

        out["database_type"] = capo_odb.types.database_type.deserialize_aws_json_1_0(
            data["databaseType"]
        )
    if data.get("dbVersion") is not None:
        out["db_version"] = data["dbVersion"]
    if data.get("dbWorkload") is not None:
        import capo_odb.types.db_workload

        out["db_workload"] = capo_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    if data.get("characterSet") is not None:
        out["character_set"] = data["characterSet"]
    if data.get("ncharacterSet") is not None:
        out["ncharacter_set"] = data["ncharacterSet"]
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
    if data.get("isMtlsConnectionRequired") is not None:
        out["is_mtls_connection_required"] = data["isMtlsConnectionRequired"]
    if data.get("autonomousMaintenanceScheduleType") is not None:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomous_maintenance_schedule_type"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.deserialize_aws_json_1_0(
                data["autonomousMaintenanceScheduleType"]
            )
        )
    if data.get("netServicesArchitecture") is not None:
        import capo_odb.types.net_services_architecture

        out["net_services_architecture"] = (
            capo_odb.types.net_services_architecture.deserialize_aws_json_1_0(
                data["netServicesArchitecture"]
            )
        )
    if data.get("availableUpgradeVersions") is not None:
        import capo_odb.types.string_list

        out["available_upgrade_versions"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["availableUpgradeVersions"]
            )
        )
    if data.get("byolComputeCountLimit") is not None:
        out["byol_compute_count_limit"] = data["byolComputeCountLimit"]
    if data.get("connectionStringDetails") is not None:
        import capo_odb.types.autonomous_database_connection_strings

        out["connection_string_details"] = (
            capo_odb.types.autonomous_database_connection_strings.deserialize_aws_json_1_0(
                data["connectionStringDetails"]
            )
        )
    if data.get("serviceConsoleUrl") is not None:
        out["service_console_url"] = data["serviceConsoleUrl"]
    if data.get("sqlWebDeveloperUrl") is not None:
        out["sql_web_developer_url"] = data["sqlWebDeveloperUrl"]
    if data.get("customerContacts") is not None:
        import capo_odb.types.customer_contacts

        out["customer_contacts"] = (
            capo_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContacts"]
            )
        )
    if data.get("apexDetails") is not None:
        import capo_odb.types.autonomous_database_apex

        out["apex_details"] = (
            capo_odb.types.autonomous_database_apex.deserialize_aws_json_1_0(
                data["apexDetails"]
            )
        )
    if data.get("standbyDb") is not None:
        import capo_odb.types.database_standby_summary

        out["standby_db"] = (
            capo_odb.types.database_standby_summary.deserialize_aws_json_1_0(
                data["standbyDb"]
            )
        )
    if data.get("localStandbyDb") is not None:
        import capo_odb.types.database_standby_summary

        out["local_standby_db"] = (
            capo_odb.types.database_standby_summary.deserialize_aws_json_1_0(
                data["localStandbyDb"]
            )
        )
    if data.get("dataSafeStatus") is not None:
        import capo_odb.types.data_safe_status

        out["data_safe_status"] = (
            capo_odb.types.data_safe_status.deserialize_aws_json_1_0(
                data["dataSafeStatus"]
            )
        )
    if data.get("databaseManagementStatus") is not None:
        import capo_odb.types.database_management_status

        out["database_management_status"] = (
            capo_odb.types.database_management_status.deserialize_aws_json_1_0(
                data["databaseManagementStatus"]
            )
        )
    if data.get("operationsInsightsStatus") is not None:
        import capo_odb.types.operations_insights_status

        out["operations_insights_status"] = (
            capo_odb.types.operations_insights_status.deserialize_aws_json_1_0(
                data["operationsInsightsStatus"]
            )
        )
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("maintenanceTargetComponent") is not None:
        out["maintenance_target_component"] = data["maintenanceTargetComponent"]
    if data.get("connectionUrls") is not None:
        import capo_odb.types.autonomous_database_connection_urls

        out["connection_urls"] = (
            capo_odb.types.autonomous_database_connection_urls.deserialize_aws_json_1_0(
                data["connectionUrls"]
            )
        )
    if data.get("dbToolsDetails") is not None:
        import capo_odb.types.database_tool_list

        out["db_tools_details"] = (
            capo_odb.types.database_tool_list.deserialize_aws_json_1_0(
                data["dbToolsDetails"]
            )
        )
    if data.get("scheduledOperations") is not None:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduled_operations"] = (
            capo_odb.types.scheduled_operation_details_list.deserialize_aws_json_1_0(
                data["scheduledOperations"]
            )
        )
    if data.get("resourcePoolLeaderId") is not None:
        out["resource_pool_leader_id"] = data["resourcePoolLeaderId"]
    if data.get("computeCount") is not None:
        out["compute_count"] = float(data["computeCount"])
    if data.get("computeModel") is not None:
        import capo_odb.types.compute_model

        out["compute_model"] = capo_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("memoryPerOracleComputeUnitInGBs") is not None:
        out["memory_per_oracle_compute_unit_in_g_bs"] = data[
            "memoryPerOracleComputeUnitInGBs"
        ]
    if data.get("provisionableCpus") is not None:
        import capo_odb.types.integer_list

        out["provisionable_cpus"] = (
            capo_odb.types.integer_list.deserialize_aws_json_1_0(
                data["provisionableCpus"]
            )
        )
    if data.get("isAutoScalingEnabled") is not None:
        out["is_auto_scaling_enabled"] = data["isAutoScalingEnabled"]
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = float(data["dataStorageSizeInTBs"])
    if data.get("dataStorageSizeInGBs") is not None:
        out["data_storage_size_in_g_bs"] = data["dataStorageSizeInGBs"]
    if data.get("usedDataStorageSizeInTBs") is not None:
        out["used_data_storage_size_in_t_bs"] = float(data["usedDataStorageSizeInTBs"])
    if data.get("usedDataStorageSizeInGBs") is not None:
        out["used_data_storage_size_in_g_bs"] = data["usedDataStorageSizeInGBs"]
    if data.get("actualUsedDataStorageSizeInTBs") is not None:
        out["actual_used_data_storage_size_in_t_bs"] = float(
            data["actualUsedDataStorageSizeInTBs"]
        )
    if data.get("allocatedStorageSizeInTBs") is not None:
        out["allocated_storage_size_in_t_bs"] = float(data["allocatedStorageSizeInTBs"])
    if data.get("inMemoryAreaInGBs") is not None:
        out["in_memory_area_in_g_bs"] = data["inMemoryAreaInGBs"]
    if data.get("isAutoScalingForStorageEnabled") is not None:
        out["is_auto_scaling_for_storage_enabled"] = data[
            "isAutoScalingForStorageEnabled"
        ]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("privateEndpoint") is not None:
        out["private_endpoint"] = data["privateEndpoint"]
    if data.get("privateEndpointIp") is not None:
        out["private_endpoint_ip"] = data["privateEndpointIp"]
    if data.get("privateEndpointLabel") is not None:
        out["private_endpoint_label"] = data["privateEndpointLabel"]
    if data.get("allowlistedIps") is not None:
        import capo_odb.types.string_list

        out["allowlisted_ips"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["allowlistedIps"]
        )
    if data.get("standbyAllowlistedIps") is not None:
        import capo_odb.types.string_list

        out["standby_allowlisted_ips"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["standbyAllowlistedIps"]
            )
        )
    if data.get("standbyAllowlistedIpsSource") is not None:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standby_allowlisted_ips_source"] = (
            capo_odb.types.standby_allowlisted_ips_source.deserialize_aws_json_1_0(
                data["standbyAllowlistedIpsSource"]
            )
        )
    if data.get("isLocalDataGuardEnabled") is not None:
        out["is_local_data_guard_enabled"] = data["isLocalDataGuardEnabled"]
    if data.get("isRemoteDataGuardEnabled") is not None:
        out["is_remote_data_guard_enabled"] = data["isRemoteDataGuardEnabled"]
    if data.get("localDisasterRecoveryType") is not None:
        import capo_odb.types.disaster_recovery_type

        out["local_disaster_recovery_type"] = (
            capo_odb.types.disaster_recovery_type.deserialize_aws_json_1_0(
                data["localDisasterRecoveryType"]
            )
        )
    if data.get("role") is not None:
        import capo_odb.types.data_guard_role

        out["role"] = capo_odb.types.data_guard_role.deserialize_aws_json_1_0(
            data["role"]
        )
    if data.get("peerDbIds") is not None:
        import capo_odb.types.string_list

        out["peer_db_ids"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["peerDbIds"]
        )
    if data.get("failedDataRecoveryInSeconds") is not None:
        out["failed_data_recovery_in_seconds"] = data["failedDataRecoveryInSeconds"]
    if data.get("localAdgAutoFailoverMaxDataLossLimit") is not None:
        out["local_adg_auto_failover_max_data_loss_limit"] = data[
            "localAdgAutoFailoverMaxDataLossLimit"
        ]
    if data.get("remoteDisasterRecoveryConfiguration") is not None:
        import capo_odb.types.disaster_recovery_configuration

        out["remote_disaster_recovery_configuration"] = (
            capo_odb.types.disaster_recovery_configuration.deserialize_aws_json_1_0(
                data["remoteDisasterRecoveryConfiguration"]
            )
        )
    if data.get("isRefreshableClone") is not None:
        out["is_refreshable_clone"] = data["isRefreshableClone"]
    if data.get("refreshableMode") is not None:
        import capo_odb.types.refreshable_mode

        out["refreshable_mode"] = (
            capo_odb.types.refreshable_mode.deserialize_aws_json_1_0(
                data["refreshableMode"]
            )
        )
    if data.get("refreshableStatus") is not None:
        import capo_odb.types.refreshable_status

        out["refreshable_status"] = (
            capo_odb.types.refreshable_status.deserialize_aws_json_1_0(
                data["refreshableStatus"]
            )
        )
    if data.get("autoRefreshFrequencyInSeconds") is not None:
        out["auto_refresh_frequency_in_seconds"] = data["autoRefreshFrequencyInSeconds"]
    if data.get("autoRefreshPointLagInSeconds") is not None:
        out["auto_refresh_point_lag_in_seconds"] = data["autoRefreshPointLagInSeconds"]
    if data.get("isReconnectCloneEnabled") is not None:
        out["is_reconnect_clone_enabled"] = data["isReconnectCloneEnabled"]
    if data.get("cloneTableSpaceList") is not None:
        import capo_odb.types.integer_list

        out["clone_table_space_list"] = (
            capo_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    if data.get("backupRetentionPeriodInDays") is not None:
        out["backup_retention_period_in_days"] = data["backupRetentionPeriodInDays"]
    if data.get("longTermBackupSchedule") is not None:
        import capo_odb.types.long_term_backup_schedule

        out["long_term_backup_schedule"] = (
            capo_odb.types.long_term_backup_schedule.deserialize_aws_json_1_0(
                data["longTermBackupSchedule"]
            )
        )
    if data.get("isBackupRetentionLocked") is not None:
        out["is_backup_retention_locked"] = data["isBackupRetentionLocked"]
    if data.get("totalBackupStorageSizeInGBs") is not None:
        out["total_backup_storage_size_in_g_bs"] = float(
            data["totalBackupStorageSizeInGBs"]
        )
    if data.get("resourcePoolSummary") is not None:
        import capo_odb.types.resource_pool_summary

        out["resource_pool_summary"] = (
            capo_odb.types.resource_pool_summary.deserialize_aws_json_1_0(
                data["resourcePoolSummary"]
            )
        )
    if data.get("encryptionSummary") is not None:
        import capo_odb.types.encryption_summary

        out["encryption_summary"] = (
            capo_odb.types.encryption_summary.deserialize_aws_json_1_0(
                data["encryptionSummary"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("timeOfLastBackup") is not None:
        import datetime

        out["time_of_last_backup"] = datetime.datetime.fromisoformat(
            data["timeOfLastBackup"].replace("Z", "+00:00")
        )
    if data.get("timeMaintenanceBegin") is not None:
        import datetime

        out["time_maintenance_begin"] = datetime.datetime.fromisoformat(
            data["timeMaintenanceBegin"].replace("Z", "+00:00")
        )
    if data.get("timeMaintenanceEnd") is not None:
        import datetime

        out["time_maintenance_end"] = datetime.datetime.fromisoformat(
            data["timeMaintenanceEnd"].replace("Z", "+00:00")
        )
    if data.get("timeLocalDataGuardEnabled") is not None:
        import datetime

        out["time_local_data_guard_enabled"] = datetime.datetime.fromisoformat(
            data["timeLocalDataGuardEnabled"].replace("Z", "+00:00")
        )
    if data.get("timeDataGuardRoleChanged") is not None:
        import datetime

        out["time_data_guard_role_changed"] = datetime.datetime.fromisoformat(
            data["timeDataGuardRoleChanged"].replace("Z", "+00:00")
        )
    if data.get("timeOfLastSwitchover") is not None:
        import datetime

        out["time_of_last_switchover"] = datetime.datetime.fromisoformat(
            data["timeOfLastSwitchover"].replace("Z", "+00:00")
        )
    if data.get("timeOfLastFailover") is not None:
        import datetime

        out["time_of_last_failover"] = datetime.datetime.fromisoformat(
            data["timeOfLastFailover"].replace("Z", "+00:00")
        )
    if data.get("timeOfLastRefresh") is not None:
        import datetime

        out["time_of_last_refresh"] = datetime.datetime.fromisoformat(
            data["timeOfLastRefresh"].replace("Z", "+00:00")
        )
    if data.get("timeOfLastRefreshPoint") is not None:
        import datetime

        out["time_of_last_refresh_point"] = datetime.datetime.fromisoformat(
            data["timeOfLastRefreshPoint"].replace("Z", "+00:00")
        )
    if data.get("timeOfNextRefresh") is not None:
        import datetime

        out["time_of_next_refresh"] = datetime.datetime.fromisoformat(
            data["timeOfNextRefresh"].replace("Z", "+00:00")
        )
    if data.get("timeOfAutoRefreshStart") is not None:
        import datetime

        out["time_of_auto_refresh_start"] = datetime.datetime.fromisoformat(
            data["timeOfAutoRefreshStart"].replace("Z", "+00:00")
        )
    if data.get("timeDeletionOfFreeAutonomousDatabase") is not None:
        import datetime

        out["time_deletion_of_free_autonomous_database"] = (
            datetime.datetime.fromisoformat(
                data["timeDeletionOfFreeAutonomousDatabase"].replace("Z", "+00:00")
            )
        )
    if data.get("timeReclamationOfFreeAutonomousDatabase") is not None:
        import datetime

        out["time_reclamation_of_free_autonomous_database"] = (
            datetime.datetime.fromisoformat(
                data["timeReclamationOfFreeAutonomousDatabase"].replace("Z", "+00:00")
            )
        )
    if data.get("timeDisasterRecoveryRoleChanged") is not None:
        import datetime

        out["time_disaster_recovery_role_changed"] = datetime.datetime.fromisoformat(
            data["timeDisasterRecoveryRoleChanged"].replace("Z", "+00:00")
        )
    if data.get("timeUntilReconnectCloneEnabled") is not None:
        import datetime

        out["time_until_reconnect_clone_enabled"] = datetime.datetime.fromisoformat(
            data["timeUntilReconnectCloneEnabled"].replace("Z", "+00:00")
        )
    if data.get("nextLongTermBackupTimeStamp") is not None:
        import datetime

        out["next_long_term_backup_time_stamp"] = datetime.datetime.fromisoformat(
            data["nextLongTermBackupTimeStamp"].replace("Z", "+00:00")
        )
    if data.get("timeUndeleted") is not None:
        import datetime

        out["time_undeleted"] = datetime.datetime.fromisoformat(
            data["timeUndeleted"].replace("Z", "+00:00")
        )
    if data.get("adminPasswordSourceSummary") is not None:
        import capo_odb.types.admin_password_source_summary

        out["admin_password_source_summary"] = (
            capo_odb.types.admin_password_source_summary.deserialize_aws_json_1_0(
                data["adminPasswordSourceSummary"]
            )
        )
    return out


def redact_sensitive(value: AutonomousDatabaseSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_contacts" in value:
        import capo_odb.types.customer_contacts

        out["customer_contacts"] = capo_odb.types.customer_contacts.redact_sensitive(
            value["customer_contacts"]
        )
    return out
