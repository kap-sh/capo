from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.action_category
    import capo_mgn.types.action_description
    import capo_mgn.types.action_id
    import capo_mgn.types.action_name
    import capo_mgn.types.arn
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.boot_mode
    import capo_mgn.types.bounded_string
    import capo_mgn.types.change_server_life_cycle_state_request
    import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle
    import capo_mgn.types.delete_source_server_request
    import capo_mgn.types.delete_source_server_response
    import capo_mgn.types.describe_source_servers_request
    import capo_mgn.types.describe_source_servers_request_filters
    import capo_mgn.types.describe_source_servers_response
    import capo_mgn.types.disconnect_from_service_request
    import capo_mgn.types.document_version
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.finalize_cutover_request
    import capo_mgn.types.fqdn_for_action_framework
    import capo_mgn.types.get_launch_configuration_request
    import capo_mgn.types.get_replication_configuration_request
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.launch_configuration
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.licensing
    import capo_mgn.types.list_source_server_actions_request
    import capo_mgn.types.list_source_server_actions_response
    import capo_mgn.types.mark_as_archived_request
    import capo_mgn.types.max_results_type
    import capo_mgn.types.operating_system_string
    import capo_mgn.types.order_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.pause_replication_request
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.put_source_server_action_request
    import capo_mgn.types.remove_source_server_action_request
    import capo_mgn.types.remove_source_server_action_response
    import capo_mgn.types.replication_configuration
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_configuration_replicated_disks
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.replication_type
    import capo_mgn.types.resume_replication_request
    import capo_mgn.types.retry_data_replication_request
    import capo_mgn.types.small_bounded_string
    import capo_mgn.types.source_server
    import capo_mgn.types.source_server_action_document
    import capo_mgn.types.source_server_actions_request_filters
    import capo_mgn.types.source_server_connector_action
    import capo_mgn.types.source_server_id
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.start_cutover_request
    import capo_mgn.types.start_cutover_request_source_server_i_ds
    import capo_mgn.types.start_cutover_response
    import capo_mgn.types.start_replication_request
    import capo_mgn.types.start_test_request
    import capo_mgn.types.start_test_request_source_server_i_ds
    import capo_mgn.types.start_test_response
    import capo_mgn.types.stop_replication_request
    import capo_mgn.types.storage_configuration
    import capo_mgn.types.strictly_positive_integer
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tag_value
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_instance_type_right_sizing_method
    import capo_mgn.types.terminate_target_instances_request
    import capo_mgn.types.terminate_target_instances_request_source_server_i_ds
    import capo_mgn.types.terminate_target_instances_response
    import capo_mgn.types.update_launch_configuration_request
    import capo_mgn.types.update_replication_configuration_request
    import capo_mgn.types.update_source_server_replication_type_request
    import capo_mgn.types.update_source_server_request
    import capo_mgn.types.user_provided_id
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class SourceServerResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def update(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        connector_action: Optional[
            "capo_mgn.types.source_server_connector_action.SourceServerConnectorAction"
        ] = None,
        user_provided_id: Optional[
            "capo_mgn.types.user_provided_id.UserProvidedId"
        ] = None,
        fqdn_for_action_framework: Optional[
            "capo_mgn.types.fqdn_for_action_framework.FqdnForActionFramework"
        ] = None,
        platform: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Update Source Server.</p>

        Args:
            account_id: <p>Update Source Server request account ID.</p>
            source_server_id: <p>Update Source Server request source server ID.</p>
            connector_action: <p>Update Source Server request connector action.</p>
            user_provided_id: <p>Update Source Server request user provided ID.</p>
            fqdn_for_action_framework: <p>Update Source Server request FQDN for action framework.</p>
            platform: <p>Update Source Server request platform operating system.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_source_server_request.UpdateSourceServerRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_source_server.update_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateSourceServer", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_source_server_request.UpdateSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id
        if connector_action is not None:
            input_["connector_action"] = connector_action
        if user_provided_id is not None:
            input_["user_provided_id"] = user_provided_id
        if fqdn_for_action_framework is not None:
            input_["fqdn_for_action_framework"] = fqdn_for_action_framework
        if platform is not None:
            input_["platform"] = platform

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single source server by ID.</p>

        Args:
            source_server_id: <p>Request to delete Source Server from service by Server ID.</p>
            account_id: <p>Request to delete Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_source_server

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_source_server.delete_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceServer")
        )
        input_: capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> (
        "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Retrieves all SourceServers or multiple SourceServers by ID.</p>

        Args:
            filters: <p>Request to filter Source Servers list.</p>
            max_results: <p>Request to filter Source Servers list by maximum results.</p>
            next_token: <p>Request to filter Source Servers list by next token.</p>
            account_id: <p>Request to filter Source Servers list by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_source_servers.describe_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_source_servers_response

            return capo_mgn.types.describe_source_servers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceServers", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def change_server_life_cycle_state(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        life_cycle: "capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows the user to set the SourceServer.LifeCycle.state property for specific Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER. This command only works if the Source Server is already launchable (dataReplicationInfo.lagDuration is not null.)</p>

        Args:
            source_server_id: <p>The request to change the source server migration lifecycle state by source server ID.</p>
            life_cycle: <p>The request to change the source server migration lifecycle state.</p>
            account_id: <p>The request to change the source server migration account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.change_server_life_cycle_state

            output, http_response = (
                capo_mgn._operations.application_migration_service.change_server_life_cycle_state.change_server_life_cycle_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ChangeServerLifeCycleState", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest = {
            "source_server_id": source_server_id,
            "life_cycle": life_cycle,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disconnect_from_service(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Disconnects specific Source Servers from Application Migration Service. Data replication is stopped immediately. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. If the agent on the source server has not been prevented from communicating with Application Migration Service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to disconnect Source Server from service by Server ID.</p>
            account_id: <p>Request to disconnect Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.disconnect_from_service

            output, http_response = (
                capo_mgn._operations.application_migration_service.disconnect_from_service.disconnect_from_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisconnectFromService", redact_output=_redact_output),
        )
        input_: capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def finalize_cutover(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be changed to DISCONNECTED; The SourceServer.lifeCycle.state will be changed to CUTOVER; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to finalize Cutover by Source Server ID.</p>
            account_id: <p>Request to finalize Cutover by Source Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.finalize_cutover

            output, http_response = (
                capo_mgn._operations.application_migration_service.finalize_cutover.finalize_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("FinalizeCutover", redact_output=_redact_output),
        )
        input_: capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Lists all LaunchConfigurations available, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>Request to get Launch Configuration information by Source Server ID.</p>
            account_id: <p>Request to get Launch Configuration information by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_launch_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_launch_configuration.get_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLaunchConfiguration")
        )
        input_: capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Lists all ReplicationConfigurations, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>Request to get Replication Configuration by Source Server ID.</p>
            account_id: <p>Request to get Replication Configuration by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_replication_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_replication_configuration.get_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration

            return capo_mgn.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetReplicationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_source_server_actions(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse":
        """<p>List source server post migration custom actions.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            filters: <p>Filters to apply when listing source server post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing source server post migration custom actions.</p>
            next_token: <p>Next token to use when listing source server post migration custom actions.</p>
            account_id: <p>Account ID to return when listing source server post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_source_server_actions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_source_server_actions.list_source_server_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSourceServerActions")
        )
        input_: capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def mark_as_archived(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Archives specific Source Servers by setting the SourceServer.isArchived property to true for specified SourceServers by ID. This command only works for SourceServers with a lifecycle state that equals DISCONNECTED or CUTOVER.</p>

        Args:
            source_server_id: <p>Mark as archived by Source Server ID.</p>
            account_id: <p>Mark as archived by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.mark_as_archived

            output, http_response = (
                capo_mgn._operations.application_migration_service.mark_as_archived.mark_as_archived(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("MarkAsArchived", redact_output=_redact_output),
        )
        input_: capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def pause_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Pause Replication.</p>

        Args:
            source_server_id: <p>Pause Replication Request source server ID.</p>
            account_id: <p>Pause Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.pause_replication_request.PauseReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.pause_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.pause_replication.pause_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PauseReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.pause_replication_request.PauseReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_name: "capo_mgn.types.action_name.ActionName",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server_action_document.SourceServerActionDocument":
        """<p>Put source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            action_name: <p>Source server post migration custom action name.</p>
            document_identifier: <p>Source server post migration custom action document identifier.</p>
            order: <p>Source server post migration custom action order.</p>
            action_id: <p>Source server post migration custom action ID.</p>
            document_version: <p>Source server post migration custom action document version.</p>
            active: <p>Source server post migration custom action active status.</p>
            timeout_seconds: <p>Source server post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Source server post migration custom action must succeed for cutover.</p>
            parameters: <p>Source server post migration custom action parameters.</p>
            external_parameters: <p>Source server post migration custom action external parameters.</p>
            description: <p>Source server post migration custom action description.</p>
            category: <p>Source server post migration custom action category.</p>
            account_id: <p>Source server post migration custom account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.source_server_action_document.SourceServerActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_source_server_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.put_source_server_action.put_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutSourceServerAction")
        )
        input_: capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse":
        """<p>Remove source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID of the post migration custom action to remove.</p>
            action_id: <p>Source server post migration custom action ID to remove.</p>
            account_id: <p>Source server post migration account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_source_server_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.remove_source_server_action.remove_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveSourceServerAction")
        )
        input_: capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_id": action_id,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Resume Replication.</p>

        Args:
            source_server_id: <p>Resume Replication Request source server ID.</p>
            account_id: <p>Resume Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.resume_replication_request.ResumeReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.resume_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.resume_replication.resume_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ResumeReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.resume_replication_request.ResumeReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retry_data_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Causes the data replication initiation sequence to begin immediately upon next Handshake for specified SourceServer IDs, regardless of when the previous initiation started. This command will not work if the SourceServer is not stalled or is in a DISCONNECTED or STOPPED state.</p>

        Args:
            source_server_id: <p>Retry data replication for Source Server ID.</p>
            account_id: <p>Retry data replication for Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.retry_data_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.retry_data_replication.retry_data_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("RetryDataReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Start replication for source server irrespective of its replication type.</p>

        Args:
            source_server_id: <p>ID of source server on which to start replication.</p>
            account_id: <p>Account ID on which to start replication.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_replication_request.StartReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.start_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_replication.start_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Stop Replication.</p>

        Args:
            source_server_id: <p>Stop Replication Request source server ID.</p>
            account_id: <p>Stop Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.stop_replication_request.StopReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.stop_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.stop_replication.stop_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StopReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Updates multiple LaunchConfigurations by Source Server ID.</p> <note> <p>bootMode valid values are <code>LEGACY_BIOS | UEFI | USE_SOURCE</code> </p> </note>

        Args:
            source_server_id: <p>Update Launch configuration by Source Server ID request.</p>
            name: <p>Update Launch configuration name request.</p>
            launch_disposition: <p>Update Launch configuration launch disposition request.</p>
            target_instance_type_right_sizing_method: <p>Update Launch configuration Target instance right sizing request.</p>
            copy_private_ip: <p>Update Launch configuration copy Private IP request.</p>
            copy_tags: <p>Update Launch configuration copy Tags request.</p>
            licensing: <p>Update Launch configuration licensing request.</p>
            boot_mode: <p>Update Launch configuration boot mode request.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration map auto tagging MPE ID.</p>
            account_id: <p>Update Launch configuration Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_launch_configuration.update_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLaunchConfiguration")
        )
        input_: capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update multiple ReplicationConfigurations by Source Server ID.</p>

        Args:
            source_server_id: <p>Update replication configuration Source Server ID request.</p>
            name: <p>Update replication configuration name request.</p>
            staging_area_subnet_id: <p>Update replication configuration Staging Area subnet request.</p>
            associate_default_security_group: <p>Update replication configuration associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration Replication Server Security Groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration use default large Staging Disk type request.</p>
            replicated_disks: <p>Update replication configuration replicated disks request.</p>
            ebs_encryption: <p>Update replication configuration EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration data plane routing request.</p>
            create_public_ip: <p>Update replication configuration create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration use Fips Endpoint.</p>
            account_id: <p>Update replication configuration Account ID request.</p>
            internet_protocol: <p>Update replication configuration internet protocol.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration store snapshot on local zone.</p>
            storage_configuration: <p>Update replication configuration storage configuration.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_replication_configuration.update_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_replication_configuration_request

            return capo_mgn.types.update_replication_configuration_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration

            return capo_mgn.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfiguration",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if account_id is not None:
            input_["account_id"] = account_id
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_source_server_replication_type(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        replication_type: "capo_mgn.types.replication_type.ReplicationType",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows you to change between the AGENT_BASED replication type and the SNAPSHOT_SHIPPING replication type. </p> <p>SNAPSHOT_SHIPPING should be used for agentless replication.</p>

        Args:
            source_server_id: <p>ID of source server on which to update replication type.</p>
            replication_type: <p>Replication type to which to update source server.</p>
            account_id: <p>Account ID on which to update replication type.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server_replication_type

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_source_server_replication_type.update_source_server_replication_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateSourceServerReplicationType", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest = {
            "source_server_id": source_server_id,
            "replication_type": replication_type,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_cutover(
        self,
        source_server_i_ds: "capo_mgn.types.start_cutover_request_source_server_i_ds.StartCutoverRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_cutover_response.StartCutoverResponse":
        """<p>Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING_OVER.</p>

        Args:
            source_server_i_ds: <p>Start Cutover by Source Server IDs.</p>
            tags: <p>Start Cutover by Tags.</p>
            account_id: <p>Start Cutover by Account IDs</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_cutover_request.StartCutoverRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_cutover_response.StartCutoverResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_cutover

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_cutover.start_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_cutover_request.StartCutoverRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_cutover_request

            return capo_mgn.types.start_cutover_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_cutover_response.StartCutoverResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_cutover_response

            return capo_mgn.types.start_cutover_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartCutover", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_cutover_request.StartCutoverRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_test(
        self,
        source_server_i_ds: "capo_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_test_response.StartTestResponse":
        """<p>Launches a Test Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartTest and changes the SourceServer.lifeCycle.state property to TESTING.</p>

        Args:
            source_server_i_ds: <p>Start Test for Source Server IDs.</p>
            tags: <p>Start Test by Tags.</p>
            account_id: <p>Start Test for Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_test_request.StartTestRequest]",
        ) -> OperationResponse["capo_mgn.types.start_test_response.StartTestResponse"]:
            import capo_mgn._operations.application_migration_service.start_test

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_test.start_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_test_request.StartTestRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_test_request

            return capo_mgn.types.start_test_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_test_response.StartTestResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_test_response

            return capo_mgn.types.start_test_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartTest", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_test_request.StartTestRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_target_instances(
        self,
        source_server_i_ds: "capo_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse":
        """<p>Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING_OVER, or CUTOVER.</p>

        Args:
            source_server_i_ds: <p>Terminate Target instance by Source Server IDs.</p>
            tags: <p>Terminate Target instance by Tags.</p>
            account_id: <p>Terminate Target instance by Account ID</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.terminate_target_instances

            output, http_response = (
                capo_mgn._operations.application_migration_service.terminate_target_instances.terminate_target_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.terminate_target_instances_request

            return capo_mgn.types.terminate_target_instances_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.terminate_target_instances_response

            return capo_mgn.types.terminate_target_instances_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "TerminateTargetInstances",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSourceServerResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def update(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        connector_action: Optional[
            "capo_mgn.types.source_server_connector_action.SourceServerConnectorAction"
        ] = None,
        user_provided_id: Optional[
            "capo_mgn.types.user_provided_id.UserProvidedId"
        ] = None,
        fqdn_for_action_framework: Optional[
            "capo_mgn.types.fqdn_for_action_framework.FqdnForActionFramework"
        ] = None,
        platform: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Update Source Server.</p>

        Args:
            account_id: <p>Update Source Server request account ID.</p>
            source_server_id: <p>Update Source Server request source server ID.</p>
            connector_action: <p>Update Source Server request connector action.</p>
            user_provided_id: <p>Update Source Server request user provided ID.</p>
            fqdn_for_action_framework: <p>Update Source Server request FQDN for action framework.</p>
            platform: <p>Update Source Server request platform operating system.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_source_server_request.UpdateSourceServerRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_source_server.async_update_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateSourceServer", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_source_server_request.UpdateSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id
        if connector_action is not None:
            input_["connector_action"] = connector_action
        if user_provided_id is not None:
            input_["user_provided_id"] = user_provided_id
        if fqdn_for_action_framework is not None:
            input_["fqdn_for_action_framework"] = fqdn_for_action_framework
        if platform is not None:
            input_["platform"] = platform

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single source server by ID.</p>

        Args:
            source_server_id: <p>Request to delete Source Server from service by Server ID.</p>
            account_id: <p>Request to delete Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_source_server

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_source_server.async_delete_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceServer")
        )
        input_: capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> (
        "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Retrieves all SourceServers or multiple SourceServers by ID.</p>

        Args:
            filters: <p>Request to filter Source Servers list.</p>
            max_results: <p>Request to filter Source Servers list by maximum results.</p>
            next_token: <p>Request to filter Source Servers list by next token.</p>
            account_id: <p>Request to filter Source Servers list by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_source_servers

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_source_servers.async_describe_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_source_servers_response

            return capo_mgn.types.describe_source_servers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceServers", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def change_server_life_cycle_state(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        life_cycle: "capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows the user to set the SourceServer.LifeCycle.state property for specific Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER. This command only works if the Source Server is already launchable (dataReplicationInfo.lagDuration is not null.)</p>

        Args:
            source_server_id: <p>The request to change the source server migration lifecycle state by source server ID.</p>
            life_cycle: <p>The request to change the source server migration lifecycle state.</p>
            account_id: <p>The request to change the source server migration account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.change_server_life_cycle_state

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.change_server_life_cycle_state.async_change_server_life_cycle_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ChangeServerLifeCycleState", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest = {
            "source_server_id": source_server_id,
            "life_cycle": life_cycle,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_from_service(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Disconnects specific Source Servers from Application Migration Service. Data replication is stopped immediately. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. If the agent on the source server has not been prevented from communicating with Application Migration Service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to disconnect Source Server from service by Server ID.</p>
            account_id: <p>Request to disconnect Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.disconnect_from_service

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.disconnect_from_service.async_disconnect_from_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisconnectFromService", redact_output=_redact_output),
        )
        input_: capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def finalize_cutover(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be changed to DISCONNECTED; The SourceServer.lifeCycle.state will be changed to CUTOVER; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to finalize Cutover by Source Server ID.</p>
            account_id: <p>Request to finalize Cutover by Source Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.finalize_cutover

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.finalize_cutover.async_finalize_cutover(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("FinalizeCutover", redact_output=_redact_output),
        )
        input_: capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Lists all LaunchConfigurations available, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>Request to get Launch Configuration information by Source Server ID.</p>
            account_id: <p>Request to get Launch Configuration information by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_launch_configuration

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.get_launch_configuration.async_get_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLaunchConfiguration")
        )
        input_: capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Lists all ReplicationConfigurations, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>Request to get Replication Configuration by Source Server ID.</p>
            account_id: <p>Request to get Replication Configuration by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_replication_configuration

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.get_replication_configuration.async_get_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration

            return capo_mgn.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetReplicationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_source_server_actions(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse":
        """<p>List source server post migration custom actions.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            filters: <p>Filters to apply when listing source server post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing source server post migration custom actions.</p>
            next_token: <p>Next token to use when listing source server post migration custom actions.</p>
            account_id: <p>Account ID to return when listing source server post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_source_server_actions

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_source_server_actions.async_list_source_server_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSourceServerActions")
        )
        input_: capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def mark_as_archived(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Archives specific Source Servers by setting the SourceServer.isArchived property to true for specified SourceServers by ID. This command only works for SourceServers with a lifecycle state that equals DISCONNECTED or CUTOVER.</p>

        Args:
            source_server_id: <p>Mark as archived by Source Server ID.</p>
            account_id: <p>Mark as archived by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.mark_as_archived

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.mark_as_archived.async_mark_as_archived(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("MarkAsArchived", redact_output=_redact_output),
        )
        input_: capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def pause_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Pause Replication.</p>

        Args:
            source_server_id: <p>Pause Replication Request source server ID.</p>
            account_id: <p>Pause Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.pause_replication_request.PauseReplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.pause_replication

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.pause_replication.async_pause_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PauseReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.pause_replication_request.PauseReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_name: "capo_mgn.types.action_name.ActionName",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server_action_document.SourceServerActionDocument":
        """<p>Put source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            action_name: <p>Source server post migration custom action name.</p>
            document_identifier: <p>Source server post migration custom action document identifier.</p>
            order: <p>Source server post migration custom action order.</p>
            action_id: <p>Source server post migration custom action ID.</p>
            document_version: <p>Source server post migration custom action document version.</p>
            active: <p>Source server post migration custom action active status.</p>
            timeout_seconds: <p>Source server post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Source server post migration custom action must succeed for cutover.</p>
            parameters: <p>Source server post migration custom action parameters.</p>
            external_parameters: <p>Source server post migration custom action external parameters.</p>
            description: <p>Source server post migration custom action description.</p>
            category: <p>Source server post migration custom action category.</p>
            account_id: <p>Source server post migration custom account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.source_server_action_document.SourceServerActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_source_server_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.put_source_server_action.async_put_source_server_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutSourceServerAction")
        )
        input_: capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse":
        """<p>Remove source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID of the post migration custom action to remove.</p>
            action_id: <p>Source server post migration custom action ID to remove.</p>
            account_id: <p>Source server post migration account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_source_server_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.remove_source_server_action.async_remove_source_server_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveSourceServerAction")
        )
        input_: capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_id": action_id,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Resume Replication.</p>

        Args:
            source_server_id: <p>Resume Replication Request source server ID.</p>
            account_id: <p>Resume Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.resume_replication_request.ResumeReplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.resume_replication

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.resume_replication.async_resume_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ResumeReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.resume_replication_request.ResumeReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_data_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Causes the data replication initiation sequence to begin immediately upon next Handshake for specified SourceServer IDs, regardless of when the previous initiation started. This command will not work if the SourceServer is not stalled or is in a DISCONNECTED or STOPPED state.</p>

        Args:
            source_server_id: <p>Retry data replication for Source Server ID.</p>
            account_id: <p>Retry data replication for Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.retry_data_replication

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.retry_data_replication.async_retry_data_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("RetryDataReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Start replication for source server irrespective of its replication type.</p>

        Args:
            source_server_id: <p>ID of source server on which to start replication.</p>
            account_id: <p>Account ID on which to start replication.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_replication_request.StartReplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.start_replication

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Stop Replication.</p>

        Args:
            source_server_id: <p>Stop Replication Request source server ID.</p>
            account_id: <p>Stop Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.stop_replication_request.StopReplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.stop_replication

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StopReplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Updates multiple LaunchConfigurations by Source Server ID.</p> <note> <p>bootMode valid values are <code>LEGACY_BIOS | UEFI | USE_SOURCE</code> </p> </note>

        Args:
            source_server_id: <p>Update Launch configuration by Source Server ID request.</p>
            name: <p>Update Launch configuration name request.</p>
            launch_disposition: <p>Update Launch configuration launch disposition request.</p>
            target_instance_type_right_sizing_method: <p>Update Launch configuration Target instance right sizing request.</p>
            copy_private_ip: <p>Update Launch configuration copy Private IP request.</p>
            copy_tags: <p>Update Launch configuration copy Tags request.</p>
            licensing: <p>Update Launch configuration licensing request.</p>
            boot_mode: <p>Update Launch configuration boot mode request.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration map auto tagging MPE ID.</p>
            account_id: <p>Update Launch configuration Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_launch_configuration.async_update_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLaunchConfiguration")
        )
        input_: capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update multiple ReplicationConfigurations by Source Server ID.</p>

        Args:
            source_server_id: <p>Update replication configuration Source Server ID request.</p>
            name: <p>Update replication configuration name request.</p>
            staging_area_subnet_id: <p>Update replication configuration Staging Area subnet request.</p>
            associate_default_security_group: <p>Update replication configuration associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration Replication Server Security Groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration use default large Staging Disk type request.</p>
            replicated_disks: <p>Update replication configuration replicated disks request.</p>
            ebs_encryption: <p>Update replication configuration EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration data plane routing request.</p>
            create_public_ip: <p>Update replication configuration create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration use Fips Endpoint.</p>
            account_id: <p>Update replication configuration Account ID request.</p>
            internet_protocol: <p>Update replication configuration internet protocol.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration store snapshot on local zone.</p>
            storage_configuration: <p>Update replication configuration storage configuration.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_replication_configuration.async_update_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_replication_configuration_request

            return capo_mgn.types.update_replication_configuration_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_mgn.types.replication_configuration

            return capo_mgn.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfiguration",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if account_id is not None:
            input_["account_id"] = account_id
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_source_server_replication_type(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        replication_type: "capo_mgn.types.replication_type.ReplicationType",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows you to change between the AGENT_BASED replication type and the SNAPSHOT_SHIPPING replication type. </p> <p>SNAPSHOT_SHIPPING should be used for agentless replication.</p>

        Args:
            source_server_id: <p>ID of source server on which to update replication type.</p>
            replication_type: <p>Replication type to which to update source server.</p>
            account_id: <p>Account ID on which to update replication type.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server_replication_type

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_source_server_replication_type.async_update_source_server_replication_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_mgn.types.source_server

            return capo_mgn.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateSourceServerReplicationType", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest = {
            "source_server_id": source_server_id,
            "replication_type": replication_type,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_cutover(
        self,
        source_server_i_ds: "capo_mgn.types.start_cutover_request_source_server_i_ds.StartCutoverRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_cutover_response.StartCutoverResponse":
        """<p>Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING_OVER.</p>

        Args:
            source_server_i_ds: <p>Start Cutover by Source Server IDs.</p>
            tags: <p>Start Cutover by Tags.</p>
            account_id: <p>Start Cutover by Account IDs</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_cutover_request.StartCutoverRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.start_cutover_response.StartCutoverResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_cutover

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_cutover.async_start_cutover(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_cutover_request.StartCutoverRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_cutover_request

            return capo_mgn.types.start_cutover_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_cutover_response.StartCutoverResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_cutover_response

            return capo_mgn.types.start_cutover_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartCutover", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_cutover_request.StartCutoverRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_test(
        self,
        source_server_i_ds: "capo_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_test_response.StartTestResponse":
        """<p>Launches a Test Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartTest and changes the SourceServer.lifeCycle.state property to TESTING.</p>

        Args:
            source_server_i_ds: <p>Start Test for Source Server IDs.</p>
            tags: <p>Start Test by Tags.</p>
            account_id: <p>Start Test for Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_test_request.StartTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.start_test_response.StartTestResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_test

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_test.async_start_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_test_request.StartTestRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_test_request

            return capo_mgn.types.start_test_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.start_test_response.StartTestResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_test_response

            return capo_mgn.types.start_test_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartTest", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.start_test_request.StartTestRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_target_instances(
        self,
        source_server_i_ds: "capo_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse":
        """<p>Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING_OVER, or CUTOVER.</p>

        Args:
            source_server_i_ds: <p>Terminate Target instance by Source Server IDs.</p>
            tags: <p>Terminate Target instance by Tags.</p>
            account_id: <p>Terminate Target instance by Account ID</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.terminate_target_instances

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.terminate_target_instances.async_terminate_target_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.terminate_target_instances_request

            return capo_mgn.types.terminate_target_instances_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.terminate_target_instances_response

            return capo_mgn.types.terminate_target_instances_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "TerminateTargetInstances",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
