"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.admin_password_source
    import capo_odb.types.admin_password_source_configuration_input
    import capo_odb.types.autonomous_maintenance_schedule_type
    import capo_odb.types.customer_contacts
    import capo_odb.types.database_edition
    import capo_odb.types.database_tool_list
    import capo_odb.types.db_workload
    import capo_odb.types.encryption_key_configuration_input
    import capo_odb.types.encryption_key_provider_input
    import capo_odb.types.general_input_string
    import capo_odb.types.license_model
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_pool_summary
    import capo_odb.types.scheduled_operation_details_list
    import capo_odb.types.sensitive_string
    import capo_odb.types.source_configuration
    import capo_odb.types.source_type
    import capo_odb.types.standby_allowlisted_ips_source
    import capo_odb.types.string_list
    import capo_odb.types.transportable_tablespace


class CreateAutonomousDatabaseInput(TypedDict, closed=True):
    odb_network_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the ODB network to be used for the Autonomous Database.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The user-friendly name for the Autonomous Database. The name does not have to be unique.</p>"""
    db_name: NotRequired["str"]
    """<p>The name of the Autonomous Database. The name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters. Special characters are not permitted. The name must be unique in the Amazon Web Services account.</p>"""
    admin_password: NotRequired["capo_odb.types.sensitive_string.SensitiveString"]
    """<p>The password for the <code>ADMIN</code> user of the Autonomous Database.</p>"""
    compute_count: NotRequired["float"]
    """<p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), to assign to the Autonomous Database.</p>"""
    data_storage_size_in_t_bs: NotRequired["int"]
    """<p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>"""
    data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>"""
    db_workload: NotRequired["capo_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""
    is_auto_scaling_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>"""
    is_auto_scaling_for_storage_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Autonomous Database.</p>"""
    character_set: NotRequired["str"]
    """<p>The character set to use for the Autonomous Database.</p>"""
    ncharacter_set: NotRequired["str"]
    """<p>The national character set to use for the Autonomous Database.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version to use for the Autonomous Database.</p>"""
    database_edition: NotRequired["capo_odb.types.database_edition.DatabaseEdition"]
    """<p>The Oracle Database edition to apply to the Autonomous Database.</p>"""
    standby_allowlisted_ips_source: NotRequired[
        "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
    ]
    """<p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>"""
    autonomous_maintenance_schedule_type: NotRequired[
        "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
    ]
    """<p>The maintenance schedule type for the Autonomous Database.</p>"""
    backup_retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for automatic backups of the Autonomous Database.</p>"""
    byol_compute_count_limit: NotRequired["float"]
    """<p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores to allocate to the Autonomous Database.</p>"""
    customer_contacts_to_send_to_oci: NotRequired[
        "capo_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The list of customer contacts to receive operational notifications from Oracle Cloud Infrastructure (OCI) for the Autonomous Database.</p>"""
    private_endpoint_ip: NotRequired["str"]
    """<p>The private endpoint IP address for the Autonomous Database.</p>"""
    private_endpoint_label: NotRequired["str"]
    """<p>The private endpoint label for the Autonomous Database.</p>"""
    resource_pool_leader_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the resource pool leader Autonomous Database.</p>"""
    resource_pool_summary: NotRequired[
        "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
    ]
    """<p>The configuration of the resource pool for the Autonomous Database.</p>"""
    scheduled_operations: NotRequired[
        "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
    ]
    """<p>The list of scheduled start and stop times for the Autonomous Database.</p>"""
    standby_allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>"""
    allowlisted_ips: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the Autonomous Database.</p>"""
    transportable_tablespace: NotRequired[
        "capo_odb.types.transportable_tablespace.TransportableTablespace"
    ]
    """<p>The transportable tablespace configuration to use when creating the Autonomous Database.</p>"""
    is_backup_retention_locked: NotRequired["bool"]
    """<p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>"""
    is_local_data_guard_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>"""
    is_mtls_connection_required: NotRequired["bool"]
    """<p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>"""
    db_tools_details: NotRequired["capo_odb.types.database_tool_list.DatabaseToolList"]
    """<p>The list of database management tools to enable for the Autonomous Database.</p>"""
    source: NotRequired["capo_odb.types.source_type.SourceType"]
    """<p>The source from which to create the Autonomous Database, such as a clone, backup, or cross-Region copy.</p>"""
    source_configuration: NotRequired[
        "capo_odb.types.source_configuration.SourceConfiguration"
    ]
    """<p>The configuration details for the source used to create the Autonomous Database.</p>"""
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
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A client-provided token to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the Autonomous Database. Each tag is a key-value pair with no predefined name, type, or namespace.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseInput) -> dict:
    out: dict = {}
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
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
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = value["data_storage_size_in_g_bs"]
    if "db_workload" in value:
        import capo_odb.types.db_workload

        out["dbWorkload"] = capo_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    if "is_auto_scaling_enabled" in value:
        out["isAutoScalingEnabled"] = value["is_auto_scaling_enabled"]
    if "is_auto_scaling_for_storage_enabled" in value:
        out["isAutoScalingForStorageEnabled"] = value[
            "is_auto_scaling_for_storage_enabled"
        ]
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "character_set" in value:
        out["characterSet"] = value["character_set"]
    if "ncharacter_set" in value:
        out["ncharacterSet"] = value["ncharacter_set"]
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "database_edition" in value:
        import capo_odb.types.database_edition

        out["databaseEdition"] = capo_odb.types.database_edition.serialize_aws_json_1_0(
            value["database_edition"]
        )
    if "standby_allowlisted_ips_source" in value:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standbyAllowlistedIpsSource"] = (
            capo_odb.types.standby_allowlisted_ips_source.serialize_aws_json_1_0(
                value["standby_allowlisted_ips_source"]
            )
        )
    if "autonomous_maintenance_schedule_type" in value:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomousMaintenanceScheduleType"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.serialize_aws_json_1_0(
                value["autonomous_maintenance_schedule_type"]
            )
        )
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
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customerContactsToSendToOCI"] = (
            capo_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    if "private_endpoint_ip" in value:
        out["privateEndpointIp"] = value["private_endpoint_ip"]
    if "private_endpoint_label" in value:
        out["privateEndpointLabel"] = value["private_endpoint_label"]
    if "resource_pool_leader_id" in value:
        out["resourcePoolLeaderId"] = value["resource_pool_leader_id"]
    if "resource_pool_summary" in value:
        import capo_odb.types.resource_pool_summary

        out["resourcePoolSummary"] = (
            capo_odb.types.resource_pool_summary.serialize_aws_json_1_0(
                value["resource_pool_summary"]
            )
        )
    if "scheduled_operations" in value:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduledOperations"] = (
            capo_odb.types.scheduled_operation_details_list.serialize_aws_json_1_0(
                value["scheduled_operations"]
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
    if "transportable_tablespace" in value:
        import capo_odb.types.transportable_tablespace

        out["transportableTablespace"] = (
            capo_odb.types.transportable_tablespace.serialize_aws_json_1_0(
                value["transportable_tablespace"]
            )
        )
    if "is_backup_retention_locked" in value:
        out["isBackupRetentionLocked"] = value["is_backup_retention_locked"]
    if "is_local_data_guard_enabled" in value:
        out["isLocalDataGuardEnabled"] = value["is_local_data_guard_enabled"]
    if "is_mtls_connection_required" in value:
        out["isMtlsConnectionRequired"] = value["is_mtls_connection_required"]
    if "db_tools_details" in value:
        import capo_odb.types.database_tool_list

        out["dbToolsDetails"] = (
            capo_odb.types.database_tool_list.serialize_aws_json_1_0(
                value["db_tools_details"]
            )
        )
    if "source" in value:
        import capo_odb.types.source_type

        out["source"] = capo_odb.types.source_type.serialize_aws_json_1_0(
            value["source"]
        )
    if "source_configuration" in value:
        import capo_odb.types.source_configuration

        out["sourceConfiguration"] = (
            capo_odb.types.source_configuration.serialize_aws_json_1_0(
                value["source_configuration"]
            )
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseInput:
    out: CreateAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("dbName") is not None:
        out["db_name"] = data["dbName"]
    if data.get("adminPassword") is not None:
        out["admin_password"] = data["adminPassword"]
    if data.get("computeCount") is not None:
        out["compute_count"] = float(data["computeCount"])
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if data.get("dataStorageSizeInGBs") is not None:
        out["data_storage_size_in_g_bs"] = data["dataStorageSizeInGBs"]
    if data.get("dbWorkload") is not None:
        import capo_odb.types.db_workload

        out["db_workload"] = capo_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    if data.get("isAutoScalingEnabled") is not None:
        out["is_auto_scaling_enabled"] = data["isAutoScalingEnabled"]
    if data.get("isAutoScalingForStorageEnabled") is not None:
        out["is_auto_scaling_for_storage_enabled"] = data[
            "isAutoScalingForStorageEnabled"
        ]
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("characterSet") is not None:
        out["character_set"] = data["characterSet"]
    if data.get("ncharacterSet") is not None:
        out["ncharacter_set"] = data["ncharacterSet"]
    if data.get("dbVersion") is not None:
        out["db_version"] = data["dbVersion"]
    if data.get("databaseEdition") is not None:
        import capo_odb.types.database_edition

        out["database_edition"] = (
            capo_odb.types.database_edition.deserialize_aws_json_1_0(
                data["databaseEdition"]
            )
        )
    if data.get("standbyAllowlistedIpsSource") is not None:
        import capo_odb.types.standby_allowlisted_ips_source

        out["standby_allowlisted_ips_source"] = (
            capo_odb.types.standby_allowlisted_ips_source.deserialize_aws_json_1_0(
                data["standbyAllowlistedIpsSource"]
            )
        )
    if data.get("autonomousMaintenanceScheduleType") is not None:
        import capo_odb.types.autonomous_maintenance_schedule_type

        out["autonomous_maintenance_schedule_type"] = (
            capo_odb.types.autonomous_maintenance_schedule_type.deserialize_aws_json_1_0(
                data["autonomousMaintenanceScheduleType"]
            )
        )
    if data.get("backupRetentionPeriodInDays") is not None:
        out["backup_retention_period_in_days"] = data["backupRetentionPeriodInDays"]
    if data.get("byolComputeCountLimit") is not None:
        out["byol_compute_count_limit"] = float(data["byolComputeCountLimit"])
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("customerContactsToSendToOCI") is not None:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContactsToSendToOCI"]
            )
        )
    if data.get("privateEndpointIp") is not None:
        out["private_endpoint_ip"] = data["privateEndpointIp"]
    if data.get("privateEndpointLabel") is not None:
        out["private_endpoint_label"] = data["privateEndpointLabel"]
    if data.get("resourcePoolLeaderId") is not None:
        out["resource_pool_leader_id"] = data["resourcePoolLeaderId"]
    if data.get("resourcePoolSummary") is not None:
        import capo_odb.types.resource_pool_summary

        out["resource_pool_summary"] = (
            capo_odb.types.resource_pool_summary.deserialize_aws_json_1_0(
                data["resourcePoolSummary"]
            )
        )
    if data.get("scheduledOperations") is not None:
        import capo_odb.types.scheduled_operation_details_list

        out["scheduled_operations"] = (
            capo_odb.types.scheduled_operation_details_list.deserialize_aws_json_1_0(
                data["scheduledOperations"]
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
    if data.get("transportableTablespace") is not None:
        import capo_odb.types.transportable_tablespace

        out["transportable_tablespace"] = (
            capo_odb.types.transportable_tablespace.deserialize_aws_json_1_0(
                data["transportableTablespace"]
            )
        )
    if data.get("isBackupRetentionLocked") is not None:
        out["is_backup_retention_locked"] = data["isBackupRetentionLocked"]
    if data.get("isLocalDataGuardEnabled") is not None:
        out["is_local_data_guard_enabled"] = data["isLocalDataGuardEnabled"]
    if data.get("isMtlsConnectionRequired") is not None:
        out["is_mtls_connection_required"] = data["isMtlsConnectionRequired"]
    if data.get("dbToolsDetails") is not None:
        import capo_odb.types.database_tool_list

        out["db_tools_details"] = (
            capo_odb.types.database_tool_list.deserialize_aws_json_1_0(
                data["dbToolsDetails"]
            )
        )
    if data.get("source") is not None:
        import capo_odb.types.source_type

        out["source"] = capo_odb.types.source_type.deserialize_aws_json_1_0(
            data["source"]
        )
    if data.get("sourceConfiguration") is not None:
        import capo_odb.types.source_configuration

        out["source_configuration"] = (
            capo_odb.types.source_configuration.deserialize_aws_json_1_0(
                data["sourceConfiguration"]
            )
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateAutonomousDatabaseInput) -> dict[str, Any]:
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
