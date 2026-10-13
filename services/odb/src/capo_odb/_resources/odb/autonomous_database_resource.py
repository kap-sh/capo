from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Any, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.admin_password_source
    import capo_odb.types.admin_password_source_configuration_input
    import capo_odb.types.autonomous_database_peer_summary
    import capo_odb.types.autonomous_database_summary
    import capo_odb.types.autonomous_maintenance_schedule_type
    import capo_odb.types.create_autonomous_database_input
    import capo_odb.types.create_autonomous_database_output
    import capo_odb.types.create_autonomous_database_wallet_input
    import capo_odb.types.create_autonomous_database_wallet_output
    import capo_odb.types.customer_contacts
    import capo_odb.types.database_edition
    import capo_odb.types.database_tool_list
    import capo_odb.types.db_workload
    import capo_odb.types.delete_autonomous_database_input
    import capo_odb.types.delete_autonomous_database_output
    import capo_odb.types.encryption_key_configuration_input
    import capo_odb.types.encryption_key_provider_input
    import capo_odb.types.failover_autonomous_database_input
    import capo_odb.types.failover_autonomous_database_output
    import capo_odb.types.general_input_string
    import capo_odb.types.get_autonomous_database_input
    import capo_odb.types.get_autonomous_database_output
    import capo_odb.types.get_autonomous_database_wallet_details_input
    import capo_odb.types.get_autonomous_database_wallet_details_output
    import capo_odb.types.license_model
    import capo_odb.types.list_autonomous_database_clones_input
    import capo_odb.types.list_autonomous_database_clones_output
    import capo_odb.types.list_autonomous_database_peers_input
    import capo_odb.types.list_autonomous_database_peers_output
    import capo_odb.types.list_autonomous_databases_input
    import capo_odb.types.list_autonomous_databases_output
    import capo_odb.types.long_term_backup_schedule
    import capo_odb.types.open_mode
    import capo_odb.types.permission_level
    import capo_odb.types.reboot_autonomous_database_input
    import capo_odb.types.reboot_autonomous_database_output
    import capo_odb.types.refreshable_mode
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_pool_summary
    import capo_odb.types.restore_autonomous_database_input
    import capo_odb.types.restore_autonomous_database_output
    import capo_odb.types.scheduled_operation_details_list
    import capo_odb.types.sensitive_string
    import capo_odb.types.shrink_autonomous_database_input
    import capo_odb.types.shrink_autonomous_database_output
    import capo_odb.types.source_configuration
    import capo_odb.types.source_type
    import capo_odb.types.standby_allowlisted_ips_source
    import capo_odb.types.start_autonomous_database_input
    import capo_odb.types.start_autonomous_database_output
    import capo_odb.types.stop_autonomous_database_input
    import capo_odb.types.stop_autonomous_database_output
    import capo_odb.types.string_list
    import capo_odb.types.switchover_autonomous_database_input
    import capo_odb.types.switchover_autonomous_database_output
    import capo_odb.types.transportable_tablespace
    import capo_odb.types.update_autonomous_database_input
    import capo_odb.types.update_autonomous_database_output
    import capo_odb.types.wallet_password_source
    import capo_odb.types.wallet_password_source_configuration_input
    import capo_odb.types.wallet_type
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class AutonomousDatabaseResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        character_set: Optional[str] = None,
        ncharacter_set: Optional[str] = None,
        db_version: Optional[str] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        transportable_tablespace: Optional[
            "capo_odb.types.transportable_tablespace.TransportableTablespace"
        ] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        source: Optional["capo_odb.types.source_type.SourceType"] = None,
        source_configuration: Optional[
            "capo_odb.types.source_configuration.SourceConfiguration"
        ] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput":
        """<p>Creates a new Autonomous Database.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to be used for the Autonomous Database.</p>
            display_name: <p>The user-friendly name for the Autonomous Database. The name does not have to be unique.</p>
            db_name: <p>The name of the Autonomous Database. The name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters. Special characters are not permitted. The name must be unique in the Amazon Web Services account.</p>
            admin_password: <p>The password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), to assign to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            character_set: <p>The character set to use for the Autonomous Database.</p>
            ncharacter_set: <p>The national character set to use for the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from Oracle Cloud Infrastructure (OCI) for the Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            transportable_tablespace: <p>The transportable tablespace configuration to use when creating the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            source: <p>The source from which to create the Autonomous Database, such as a clone, backup, or cross-Region copy.</p>
            source_configuration: <p>The configuration details for the source used to create the Autonomous Database.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.create_autonomous_database.create_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_input

            return capo_odb.types.create_autonomous_database_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAutonomousDatabase", redact_input=_redact_input),
        )
        input_: capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput = {}
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if license_model is not None:
            input_["license_model"] = license_model
        if character_set is not None:
            input_["character_set"] = character_set
        if ncharacter_set is not None:
            input_["ncharacter_set"] = ncharacter_set
        if db_version is not None:
            input_["db_version"] = db_version
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if transportable_tablespace is not None:
            input_["transportable_tablespace"] = transportable_tablespace
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if source is not None:
            input_["source"] = source
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput":
        """<p>Gets information about a specific Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.get_autonomous_database.get_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.get_autonomous_database_output

            return capo_odb.types.get_autonomous_database_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAutonomousDatabase", redact_output=_redact_output),
        )
        input_: capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        db_version: Optional[str] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        is_refreshable_clone: Optional[bool] = None,
        is_disconnect_peer: Optional[bool] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        local_adg_auto_failover_max_data_loss_limit: Optional[int] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        long_term_backup_schedule: Optional[
            "capo_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
        ] = None,
        open_mode: Optional["capo_odb.types.open_mode.OpenMode"] = None,
        permission_level: Optional[
            "capo_odb.types.permission_level.PermissionLevel"
        ] = None,
        refreshable_mode: Optional[
            "capo_odb.types.refreshable_mode.RefreshableMode"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        peer_db_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        auto_refresh_frequency_in_seconds: Optional[int] = None,
        auto_refresh_point_lag_in_seconds: Optional[int] = None,
        time_of_auto_refresh_start: Optional[datetime.datetime] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
    ) -> "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput":
        """<p>Updates the properties of an Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to update.</p>
            admin_password: <p>The new password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of ECPUs or OCPUs, to assign to the Autonomous Database.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            display_name: <p>The new user-friendly name for the Autonomous Database.</p>
            db_name: <p>The new name of the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            is_refreshable_clone: <p>Specifies whether the Autonomous Database is a refreshable clone.</p>
            is_disconnect_peer: <p>Specifies whether to disconnect the Autonomous Database from its peer database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            local_adg_auto_failover_max_data_loss_limit: <p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from OCI for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            long_term_backup_schedule: <p>The long-term backup schedule for the Autonomous Database.</p>
            open_mode: <p>The mode in which to open the Autonomous Database, either read-only or read/write.</p>
            permission_level: <p>The permission level of the Autonomous Database.</p>
            refreshable_mode: <p>The refresh mode of the refreshable clone Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            peer_db_id: <p>The unique identifier of the peer Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            auto_refresh_frequency_in_seconds: <p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>
            auto_refresh_point_lag_in_seconds: <p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>
            time_of_auto_refresh_start: <p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.update_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.update_autonomous_database.update_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput",
        ) -> dict[str, Any]:
            import capo_odb.types.update_autonomous_database_input

            return capo_odb.types.update_autonomous_database_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAutonomousDatabase", redact_input=_redact_input),
        )
        input_: capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if db_version is not None:
            input_["db_version"] = db_version
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if license_model is not None:
            input_["license_model"] = license_model
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if is_refreshable_clone is not None:
            input_["is_refreshable_clone"] = is_refreshable_clone
        if is_disconnect_peer is not None:
            input_["is_disconnect_peer"] = is_disconnect_peer
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if local_adg_auto_failover_max_data_loss_limit is not None:
            input_["local_adg_auto_failover_max_data_loss_limit"] = (
                local_adg_auto_failover_max_data_loss_limit
            )
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if long_term_backup_schedule is not None:
            input_["long_term_backup_schedule"] = long_term_backup_schedule
        if open_mode is not None:
            input_["open_mode"] = open_mode
        if permission_level is not None:
            input_["permission_level"] = permission_level
        if refreshable_mode is not None:
            input_["refreshable_mode"] = refreshable_mode
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if peer_db_id is not None:
            input_["peer_db_id"] = peer_db_id
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if auto_refresh_frequency_in_seconds is not None:
            input_["auto_refresh_frequency_in_seconds"] = (
                auto_refresh_frequency_in_seconds
            )
        if auto_refresh_point_lag_in_seconds is not None:
            input_["auto_refresh_point_lag_in_seconds"] = (
                auto_refresh_point_lag_in_seconds
            )
        if time_of_auto_refresh_start is not None:
            input_["time_of_auto_refresh_start"] = time_of_auto_refresh_start
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput":
        """<p>Deletes the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.delete_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.delete_autonomous_database.delete_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutonomousDatabase")
        )
        input_: capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
    ):
        """<p>Returns information about the Autonomous Databases owned by your Amazon Web Services account in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_databases

            output, http_response = (
                capo_odb._operations.odb.list_autonomous_databases.list_autonomous_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.list_autonomous_databases_output

            return capo_odb.types.list_autonomous_databases_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAutonomousDatabases", redact_output=_redact_output),
        )
        input_: capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_autonomous_database_wallet(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        wallet_type: Optional["capo_odb.types.wallet_type.WalletType"] = None,
        password: Optional["capo_odb.types.sensitive_string.SensitiveString"] = None,
        password_source: Optional[
            "capo_odb.types.wallet_password_source.WalletPasswordSource"
        ] = None,
        password_source_configuration: Optional[
            "capo_odb.types.wallet_password_source_configuration_input.WalletPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput":
        """<p>Creates a new wallet for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to create a wallet for.</p>
            wallet_type: <p>The type of wallet to create, either a regional wallet or an instance wallet.</p>
            password: <p>The password to encrypt the keys inside the wallet.</p>
            password_source: <p>The source of the password for encrypting the wallet. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            password_source_configuration: <p>The configuration of the password source for the Autonomous Database wallet.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database_wallet

            output, http_response = (
                capo_odb._operations.odb.create_autonomous_database_wallet.create_autonomous_database_wallet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_wallet_input

            return (
                capo_odb.types.create_autonomous_database_wallet_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_wallet_output

            return capo_odb.types.create_autonomous_database_wallet_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutonomousDatabaseWallet",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if wallet_type is not None:
            input_["wallet_type"] = wallet_type
        if password is not None:
            input_["password"] = password
        if password_source is not None:
            input_["password_source"] = password_source
        if password_source_configuration is not None:
            input_["password_source_configuration"] = password_source_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def failover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput":
        """<p>Initiates a failover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to fail over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to fail over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.failover_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.failover_autonomous_database.failover_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("FailoverAutonomousDatabase")
        )
        input_: capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_autonomous_database_wallet_details(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput":
        """<p>Gets the wallet details for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve wallet details for.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database_wallet_details

            output, http_response = (
                capo_odb._operations.odb.get_autonomous_database_wallet_details.get_autonomous_database_wallet_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAutonomousDatabaseWalletDetails")
        )
        input_: capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_autonomous_database_clones(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput":
        """<p>Lists the clones of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the source Autonomous Database whose clones you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_clones

            output, http_response = (
                capo_odb._operations.odb.list_autonomous_database_clones.list_autonomous_database_clones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.list_autonomous_database_clones_output

            return (
                capo_odb.types.list_autonomous_database_clones_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutonomousDatabaseClones", redact_output=_redact_output
            ),
        )
        input_: capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_autonomous_database_peers(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput":
        """<p>Lists the peer databases of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose peer databases you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_peers

            output, http_response = (
                capo_odb._operations.odb.list_autonomous_database_peers.list_autonomous_database_peers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutonomousDatabasePeers")
        )
        input_: capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        is_online_reboot: Optional[bool] = None,
    ) -> "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput":
        """<p>Reboots the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to reboot.</p>
            is_online_reboot: <p>Specifies whether to perform an online reboot of the Autonomous Database without interrupting active connections.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.reboot_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.reboot_autonomous_database.reboot_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootAutonomousDatabase")
        )
        input_: capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if is_online_reboot is not None:
            input_["is_online_reboot"] = is_online_reboot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        timestamp: datetime.datetime,
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput":
        """<p>Restores the specified Autonomous Database to a point in time.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to restore.</p>
            timestamp: <p>The date and time to which to restore the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.restore_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.restore_autonomous_database.restore_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreAutonomousDatabase")
        )
        input_: capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id,
            "timestamp": timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def shrink_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput":
        """<p>Shrinks the storage of the specified Autonomous Database to reclaim unused space.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to shrink.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.shrink_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.shrink_autonomous_database.shrink_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ShrinkAutonomousDatabase")
        )
        input_: capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> (
        "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
    ):
        """<p>Starts the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.start_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.start_autonomous_database.start_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartAutonomousDatabase")
        )
        input_: capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput":
        """<p>Stops the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.stop_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.stop_autonomous_database.stop_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopAutonomousDatabase")
        )
        input_: capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def switchover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput":
        """<p>Performs a switchover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to switch over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to switch over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput]",
        ) -> OperationResponse[
            "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.switchover_autonomous_database

            output, http_response = (
                capo_odb._operations.odb.switchover_autonomous_database.switchover_autonomous_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SwitchoverAutonomousDatabase")
        )
        input_: capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAutonomousDatabaseResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        character_set: Optional[str] = None,
        ncharacter_set: Optional[str] = None,
        db_version: Optional[str] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        transportable_tablespace: Optional[
            "capo_odb.types.transportable_tablespace.TransportableTablespace"
        ] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        source: Optional["capo_odb.types.source_type.SourceType"] = None,
        source_configuration: Optional[
            "capo_odb.types.source_configuration.SourceConfiguration"
        ] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput":
        """<p>Creates a new Autonomous Database.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to be used for the Autonomous Database.</p>
            display_name: <p>The user-friendly name for the Autonomous Database. The name does not have to be unique.</p>
            db_name: <p>The name of the Autonomous Database. The name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters. Special characters are not permitted. The name must be unique in the Amazon Web Services account.</p>
            admin_password: <p>The password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), to assign to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            character_set: <p>The character set to use for the Autonomous Database.</p>
            ncharacter_set: <p>The national character set to use for the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from Oracle Cloud Infrastructure (OCI) for the Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            transportable_tablespace: <p>The transportable tablespace configuration to use when creating the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            source: <p>The source from which to create the Autonomous Database, such as a clone, backup, or cross-Region copy.</p>
            source_configuration: <p>The configuration details for the source used to create the Autonomous Database.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_autonomous_database.async_create_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_input

            return capo_odb.types.create_autonomous_database_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAutonomousDatabase", redact_input=_redact_input),
        )
        input_: capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput = {}
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if license_model is not None:
            input_["license_model"] = license_model
        if character_set is not None:
            input_["character_set"] = character_set
        if ncharacter_set is not None:
            input_["ncharacter_set"] = ncharacter_set
        if db_version is not None:
            input_["db_version"] = db_version
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if transportable_tablespace is not None:
            input_["transportable_tablespace"] = transportable_tablespace
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if source is not None:
            input_["source"] = source
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput":
        """<p>Gets information about a specific Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_autonomous_database.async_get_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.get_autonomous_database_output

            return capo_odb.types.get_autonomous_database_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAutonomousDatabase", redact_output=_redact_output),
        )
        input_: capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        db_version: Optional[str] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        is_refreshable_clone: Optional[bool] = None,
        is_disconnect_peer: Optional[bool] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        local_adg_auto_failover_max_data_loss_limit: Optional[int] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        long_term_backup_schedule: Optional[
            "capo_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
        ] = None,
        open_mode: Optional["capo_odb.types.open_mode.OpenMode"] = None,
        permission_level: Optional[
            "capo_odb.types.permission_level.PermissionLevel"
        ] = None,
        refreshable_mode: Optional[
            "capo_odb.types.refreshable_mode.RefreshableMode"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        peer_db_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        auto_refresh_frequency_in_seconds: Optional[int] = None,
        auto_refresh_point_lag_in_seconds: Optional[int] = None,
        time_of_auto_refresh_start: Optional[datetime.datetime] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
    ) -> "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput":
        """<p>Updates the properties of an Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to update.</p>
            admin_password: <p>The new password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of ECPUs or OCPUs, to assign to the Autonomous Database.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            display_name: <p>The new user-friendly name for the Autonomous Database.</p>
            db_name: <p>The new name of the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            is_refreshable_clone: <p>Specifies whether the Autonomous Database is a refreshable clone.</p>
            is_disconnect_peer: <p>Specifies whether to disconnect the Autonomous Database from its peer database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            local_adg_auto_failover_max_data_loss_limit: <p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from OCI for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            long_term_backup_schedule: <p>The long-term backup schedule for the Autonomous Database.</p>
            open_mode: <p>The mode in which to open the Autonomous Database, either read-only or read/write.</p>
            permission_level: <p>The permission level of the Autonomous Database.</p>
            refreshable_mode: <p>The refresh mode of the refreshable clone Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            peer_db_id: <p>The unique identifier of the peer Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            auto_refresh_frequency_in_seconds: <p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>
            auto_refresh_point_lag_in_seconds: <p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>
            time_of_auto_refresh_start: <p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.update_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_autonomous_database.async_update_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput",
        ) -> dict[str, Any]:
            import capo_odb.types.update_autonomous_database_input

            return capo_odb.types.update_autonomous_database_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAutonomousDatabase", redact_input=_redact_input),
        )
        input_: capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if db_version is not None:
            input_["db_version"] = db_version
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if license_model is not None:
            input_["license_model"] = license_model
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if is_refreshable_clone is not None:
            input_["is_refreshable_clone"] = is_refreshable_clone
        if is_disconnect_peer is not None:
            input_["is_disconnect_peer"] = is_disconnect_peer
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if local_adg_auto_failover_max_data_loss_limit is not None:
            input_["local_adg_auto_failover_max_data_loss_limit"] = (
                local_adg_auto_failover_max_data_loss_limit
            )
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if long_term_backup_schedule is not None:
            input_["long_term_backup_schedule"] = long_term_backup_schedule
        if open_mode is not None:
            input_["open_mode"] = open_mode
        if permission_level is not None:
            input_["permission_level"] = permission_level
        if refreshable_mode is not None:
            input_["refreshable_mode"] = refreshable_mode
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if peer_db_id is not None:
            input_["peer_db_id"] = peer_db_id
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if auto_refresh_frequency_in_seconds is not None:
            input_["auto_refresh_frequency_in_seconds"] = (
                auto_refresh_frequency_in_seconds
            )
        if auto_refresh_point_lag_in_seconds is not None:
            input_["auto_refresh_point_lag_in_seconds"] = (
                auto_refresh_point_lag_in_seconds
            )
        if time_of_auto_refresh_start is not None:
            input_["time_of_auto_refresh_start"] = time_of_auto_refresh_start
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput":
        """<p>Deletes the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.delete_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_autonomous_database.async_delete_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutonomousDatabase")
        )
        input_: capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
    ):
        """<p>Returns information about the Autonomous Databases owned by your Amazon Web Services account in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_databases

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_databases.async_list_autonomous_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.list_autonomous_databases_output

            return capo_odb.types.list_autonomous_databases_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAutonomousDatabases", redact_output=_redact_output),
        )
        input_: capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_autonomous_database_wallet(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        wallet_type: Optional["capo_odb.types.wallet_type.WalletType"] = None,
        password: Optional["capo_odb.types.sensitive_string.SensitiveString"] = None,
        password_source: Optional[
            "capo_odb.types.wallet_password_source.WalletPasswordSource"
        ] = None,
        password_source_configuration: Optional[
            "capo_odb.types.wallet_password_source_configuration_input.WalletPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput":
        """<p>Creates a new wallet for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to create a wallet for.</p>
            wallet_type: <p>The type of wallet to create, either a regional wallet or an instance wallet.</p>
            password: <p>The password to encrypt the keys inside the wallet.</p>
            password_source: <p>The source of the password for encrypting the wallet. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            password_source_configuration: <p>The configuration of the password source for the Autonomous Database wallet.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database_wallet

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_autonomous_database_wallet.async_create_autonomous_database_wallet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_wallet_input

            return (
                capo_odb.types.create_autonomous_database_wallet_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.create_autonomous_database_wallet_output

            return capo_odb.types.create_autonomous_database_wallet_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutonomousDatabaseWallet",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if wallet_type is not None:
            input_["wallet_type"] = wallet_type
        if password is not None:
            input_["password"] = password
        if password_source is not None:
            input_["password_source"] = password_source
        if password_source_configuration is not None:
            input_["password_source_configuration"] = password_source_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput":
        """<p>Initiates a failover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to fail over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to fail over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.failover_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.failover_autonomous_database.async_failover_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("FailoverAutonomousDatabase")
        )
        input_: capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_autonomous_database_wallet_details(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput":
        """<p>Gets the wallet details for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve wallet details for.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database_wallet_details

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_autonomous_database_wallet_details.async_get_autonomous_database_wallet_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAutonomousDatabaseWalletDetails")
        )
        input_: capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_database_clones(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput":
        """<p>Lists the clones of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the source Autonomous Database whose clones you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_clones

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_clones.async_list_autonomous_database_clones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput",
        ) -> dict[str, Any]:
            import capo_odb.types.list_autonomous_database_clones_output

            return (
                capo_odb.types.list_autonomous_database_clones_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutonomousDatabaseClones", redact_output=_redact_output
            ),
        )
        input_: capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_database_peers(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput":
        """<p>Lists the peer databases of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose peer databases you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_peers

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_peers.async_list_autonomous_database_peers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutonomousDatabasePeers")
        )
        input_: capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        is_online_reboot: Optional[bool] = None,
    ) -> "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput":
        """<p>Reboots the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to reboot.</p>
            is_online_reboot: <p>Specifies whether to perform an online reboot of the Autonomous Database without interrupting active connections.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.reboot_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.reboot_autonomous_database.async_reboot_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootAutonomousDatabase")
        )
        input_: capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if is_online_reboot is not None:
            input_["is_online_reboot"] = is_online_reboot

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        timestamp: datetime.datetime,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput":
        """<p>Restores the specified Autonomous Database to a point in time.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to restore.</p>
            timestamp: <p>The date and time to which to restore the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.restore_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.restore_autonomous_database.async_restore_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreAutonomousDatabase")
        )
        input_: capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id,
            "timestamp": timestamp,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def shrink_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput":
        """<p>Shrinks the storage of the specified Autonomous Database to reclaim unused space.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to shrink.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.shrink_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.shrink_autonomous_database.async_shrink_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ShrinkAutonomousDatabase")
        )
        input_: capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> (
        "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
    ):
        """<p>Starts the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.start_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.start_autonomous_database.async_start_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartAutonomousDatabase")
        )
        input_: capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput":
        """<p>Stops the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.stop_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.stop_autonomous_database.async_stop_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopAutonomousDatabase")
        )
        input_: capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def switchover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput":
        """<p>Performs a switchover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to switch over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to switch over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.switchover_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.switchover_autonomous_database.async_switchover_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SwitchoverAutonomousDatabase")
        )
        input_: capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
