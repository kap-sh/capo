from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.delete_source_server_request
    import capo_drs.types.delete_source_server_response
    import capo_drs.types.describe_recovery_snapshots_request
    import capo_drs.types.describe_recovery_snapshots_request_filters
    import capo_drs.types.describe_recovery_snapshots_response
    import capo_drs.types.describe_source_servers_request
    import capo_drs.types.describe_source_servers_request_filters
    import capo_drs.types.describe_source_servers_response
    import capo_drs.types.disconnect_source_server_request
    import capo_drs.types.ec2_instance_type
    import capo_drs.types.get_launch_configuration_request
    import capo_drs.types.get_replication_configuration_request
    import capo_drs.types.internet_protocol
    import capo_drs.types.launch_configuration
    import capo_drs.types.launch_disposition
    import capo_drs.types.launch_into_instance_properties
    import capo_drs.types.licensing
    import capo_drs.types.pagination_token
    import capo_drs.types.pit_policy
    import capo_drs.types.positive_integer
    import capo_drs.types.recovery_mode
    import capo_drs.types.recovery_snapshot
    import capo_drs.types.recovery_snapshots_order
    import capo_drs.types.replication_configuration
    import capo_drs.types.replication_configuration_data_plane_routing
    import capo_drs.types.replication_configuration_default_large_staging_disk_type
    import capo_drs.types.replication_configuration_ebs_encryption
    import capo_drs.types.replication_configuration_replicated_disks
    import capo_drs.types.replication_servers_security_groups_i_ds
    import capo_drs.types.retry_data_replication_request
    import capo_drs.types.small_bounded_string
    import capo_drs.types.source_server
    import capo_drs.types.source_server_id
    import capo_drs.types.start_recovery_request
    import capo_drs.types.start_recovery_request_source_servers
    import capo_drs.types.start_recovery_response
    import capo_drs.types.start_replication_request
    import capo_drs.types.start_replication_response
    import capo_drs.types.stop_replication_request
    import capo_drs.types.stop_replication_response
    import capo_drs.types.strictly_positive_integer
    import capo_drs.types.subnet_id
    import capo_drs.types.tags_map
    import capo_drs.types.target_instance_type_right_sizing_method
    import capo_drs.types.update_launch_configuration_request
    import capo_drs.types.update_replication_configuration_request
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class SourceServerResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def delete(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single Source Server by ID. The Source Server must be disconnected first.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> OperationResponse[
            "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_server

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_source_server.delete_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceServer")
        )
        input_: capo_drs.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
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
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Lists all Source Servers or multiple Source Servers filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Servers.</p>
            max_results: <p>Maximum number of Source Servers to retrieve.</p>
            next_token: <p>The token of the next Source Server to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers.describe_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_source_servers_response

            return capo_drs.types.describe_source_servers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceServers", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def describe_recovery_snapshots(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "capo_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse":
        """<p>Lists all Recovery Snapshots for a single Source Server.</p>

        Args:
            source_server_id: <p>Filter Recovery Snapshots by Source Server ID.</p>
            filters: <p>A set of filters by which to return Recovery Snapshots.</p>
            order: <p>The sorted ordering by which to return Recovery Snapshots.</p>
            max_results: <p>Maximum number of Recovery Snapshots to retrieve.</p>
            next_token: <p>The token of the next Recovery Snapshot to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots.describe_recovery_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeRecoverySnapshots")
        )
        input_: capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if order is not None:
            input_["order"] = order
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

    def disconnect_source_server(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to disconnect.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest]",
        ) -> OperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server.disconnect_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_drs.types.source_server

            return capo_drs.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisconnectSourceServer", redact_output=_redact_output),
        )
        input_: capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Gets a LaunchConfiguration, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration.get_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLaunchConfiguration")
        )
        input_: capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Gets a ReplicationConfiguration, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Serve for this Replication Configuration.r</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration.get_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration

            return capo_drs.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetReplicationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retry_data_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>WARNING: RetryDataReplication is deprecated. Causes the data replication initiation sequence to begin immediately upon next Handshake for the specified Source Server ID, regardless of when the previous initiation started. This command will work only if the Source Server is stalled or is in a DISCONNECTED or STOPPED state. </p>

        Args:
            source_server_id: <p>The ID of the Source Server whose data replication should be retried.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> OperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication.retry_data_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_drs.types.source_server

            return capo_drs.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("RetryDataReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.start_replication_response.StartReplicationResponse":
        """<p>Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to start replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.start_replication_request.StartReplicationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_replication_response.StartReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_replication.start_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.start_replication_response.StartReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_replication_response

            return capo_drs.types.start_replication_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.stop_replication_response.StopReplicationResponse":
        """<p>Stops replication for a Source Server. This action would make the Source Server unprotected, delete its existing snapshots and stop billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to stop replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.stop_replication_request.StopReplicationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.stop_replication_response.StopReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.stop_replication.stop_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.stop_replication_response.StopReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.stop_replication_response

            return capo_drs.types.stop_replication_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StopReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_instance_properties: Optional[
            "capo_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
        ] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Updates a LaunchConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
            name: <p>The name of the launch configuration.</p>
            launch_disposition: <p>The state of the Recovery Instance in EC2 after the recovery operation.</p>
            target_instance_type_right_sizing_method: <p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>
            copy_private_ip: <p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>
            copy_tags: <p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>
            licensing: <p>The licensing configuration to be used for this launch configuration.</p>
            post_launch_enabled: <p>Whether we want to enable post-launch actions for the Source Server.</p>
            launch_into_instance_properties: <p>Launch into existing instance properties.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration.update_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLaunchConfiguration")
        )
        input_: capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
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
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_instance_properties is not None:
            input_["launch_into_instance_properties"] = launch_into_instance_properties
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update a ReplicationConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server for this Replication Configuration.</p>
            name: <p>The name of the Replication Configuration.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            replicated_disks: <p>The configuration of the disks of the Source Server to be replicated.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration.update_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.update_replication_configuration_request

            return capo_drs.types.update_replication_configuration_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration

            return capo_drs.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfiguration",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
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
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_recovery(
        self,
        source_servers: "capo_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        is_drill: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_recovery_response.StartRecoveryResponse":
        """<p>Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.</p>

        Args:
            source_servers: <p>The Source Servers that we want to start a Recovery Job for.</p>
            is_drill: <p>Whether this Source Server Recovery operation is a drill or not.</p>
            tags: <p>The tags to be associated with the Recovery Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.start_recovery_request.StartRecoveryRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_recovery_response.StartRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_recovery

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_recovery.start_recovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_recovery_request.StartRecoveryRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_request

            return capo_drs.types.start_recovery_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.start_recovery_response.StartRecoveryResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_response

            return capo_drs.types.start_recovery_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecovery",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_recovery_request.StartRecoveryRequest = {
            "source_servers": source_servers
        }
        if is_drill is not None:
            input_["is_drill"] = is_drill
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSourceServerResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def delete(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single Source Server by ID. The Source Server must be disconnected first.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_server

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_source_server.async_delete_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceServer")
        )
        input_: capo_drs.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
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
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Lists all Source Servers or multiple Source Servers filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Servers.</p>
            max_results: <p>Maximum number of Source Servers to retrieve.</p>
            next_token: <p>The token of the next Source Server to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers.async_describe_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_source_servers_response

            return capo_drs.types.describe_source_servers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceServers", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_recovery_snapshots(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "capo_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse":
        """<p>Lists all Recovery Snapshots for a single Source Server.</p>

        Args:
            source_server_id: <p>Filter Recovery Snapshots by Source Server ID.</p>
            filters: <p>A set of filters by which to return Recovery Snapshots.</p>
            order: <p>The sorted ordering by which to return Recovery Snapshots.</p>
            max_results: <p>Maximum number of Recovery Snapshots to retrieve.</p>
            next_token: <p>The token of the next Recovery Snapshot to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots.async_describe_recovery_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeRecoverySnapshots")
        )
        input_: capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if order is not None:
            input_["order"] = order
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

    async def disconnect_source_server(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to disconnect.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest]",
        ) -> AsyncOperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server.async_disconnect_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_drs.types.source_server

            return capo_drs.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisconnectSourceServer", redact_output=_redact_output),
        )
        input_: capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Gets a LaunchConfiguration, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration.async_get_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLaunchConfiguration")
        )
        input_: capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Gets a ReplicationConfiguration, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Serve for this Replication Configuration.r</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration.async_get_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration

            return capo_drs.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetReplicationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_data_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>WARNING: RetryDataReplication is deprecated. Causes the data replication initiation sequence to begin immediately upon next Handshake for the specified Source Server ID, regardless of when the previous initiation started. This command will work only if the Source Server is stalled or is in a DISCONNECTED or STOPPED state. </p>

        Args:
            source_server_id: <p>The ID of the Source Server whose data replication should be retried.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> AsyncOperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication.async_retry_data_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.source_server.SourceServer",
        ) -> dict[str, Any]:
            import capo_drs.types.source_server

            return capo_drs.types.source_server.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("RetryDataReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.start_replication_response.StartReplicationResponse":
        """<p>Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to start replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_replication_request.StartReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_replication_response.StartReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.start_replication_response.StartReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_replication_response

            return capo_drs.types.start_replication_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.stop_replication_response.StopReplicationResponse":
        """<p>Stops replication for a Source Server. This action would make the Source Server unprotected, delete its existing snapshots and stop billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to stop replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.stop_replication_request.StopReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.stop_replication_response.StopReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.stop_replication_response.StopReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.stop_replication_response

            return capo_drs.types.stop_replication_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StopReplication", redact_output=_redact_output),
        )
        input_: capo_drs.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_instance_properties: Optional[
            "capo_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
        ] = None,
        recovery_mode: Optional["capo_drs.types.recovery_mode.RecoveryMode"] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Updates a LaunchConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
            name: <p>The name of the launch configuration.</p>
            launch_disposition: <p>The state of the Recovery Instance in EC2 after the recovery operation.</p>
            target_instance_type_right_sizing_method: <p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>
            copy_private_ip: <p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>
            copy_tags: <p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>
            licensing: <p>The licensing configuration to be used for this launch configuration.</p>
            post_launch_enabled: <p>Whether we want to enable post-launch actions for the Source Server.</p>
            launch_into_instance_properties: <p>Launch into existing instance properties.</p>
            recovery_mode: <p>Recovery mode.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration.async_update_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateLaunchConfiguration")
        )
        input_: capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
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
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_instance_properties is not None:
            input_["launch_into_instance_properties"] = launch_into_instance_properties
        if recovery_mode is not None:
            input_["recovery_mode"] = recovery_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update a ReplicationConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server for this Replication Configuration.</p>
            name: <p>The name of the Replication Configuration.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            replicated_disks: <p>The configuration of the disks of the Source Server to be replicated.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration.async_update_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.update_replication_configuration_request

            return capo_drs.types.update_replication_configuration_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_drs.types.replication_configuration.ReplicationConfiguration",
        ) -> dict[str, Any]:
            import capo_drs.types.replication_configuration

            return capo_drs.types.replication_configuration.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateReplicationConfiguration",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
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
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recovery(
        self,
        source_servers: "capo_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        is_drill: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_recovery_response.StartRecoveryResponse":
        """<p>Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.</p>

        Args:
            source_servers: <p>The Source Servers that we want to start a Recovery Job for.</p>
            is_drill: <p>Whether this Source Server Recovery operation is a drill or not.</p>
            tags: <p>The tags to be associated with the Recovery Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_recovery_request.StartRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_recovery_response.StartRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_recovery

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_recovery.async_start_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_recovery_request.StartRecoveryRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_request

            return capo_drs.types.start_recovery_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.start_recovery_response.StartRecoveryResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_recovery_response

            return capo_drs.types.start_recovery_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecovery",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_recovery_request.StartRecoveryRequest = {
            "source_servers": source_servers
        }
        if is_drill is not None:
            input_["is_drill"] = is_drill
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
