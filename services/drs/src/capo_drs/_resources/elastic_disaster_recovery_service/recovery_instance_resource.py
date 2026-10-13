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
    import capo_drs.types.bounded_string
    import capo_drs.types.delete_recovery_instance_request
    import capo_drs.types.describe_recovery_instances_request
    import capo_drs.types.describe_recovery_instances_request_filters
    import capo_drs.types.describe_recovery_instances_response
    import capo_drs.types.disconnect_recovery_instance_request
    import capo_drs.types.get_failback_replication_configuration_request
    import capo_drs.types.get_failback_replication_configuration_response
    import capo_drs.types.internet_protocol
    import capo_drs.types.pagination_token
    import capo_drs.types.positive_integer
    import capo_drs.types.recovery_instance
    import capo_drs.types.recovery_instance_id
    import capo_drs.types.recovery_instances_for_termination_request
    import capo_drs.types.reverse_replication_request
    import capo_drs.types.reverse_replication_response
    import capo_drs.types.start_failback_launch_request
    import capo_drs.types.start_failback_launch_response
    import capo_drs.types.start_failback_request_recovery_instance_i_ds
    import capo_drs.types.stop_failback_request
    import capo_drs.types.strictly_positive_integer
    import capo_drs.types.tags_map
    import capo_drs.types.terminate_recovery_instances_request
    import capo_drs.types.terminate_recovery_instances_response
    import capo_drs.types.update_failback_replication_configuration_request
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class RecoveryInstanceResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_instances_request_filters.DescribeRecoveryInstancesRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse":
        """<p>Lists all Recovery Instances or multiple Recovery Instances by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Recovery Instances.</p>
            max_results: <p>Maximum number of Recovery Instances to retrieve.</p>
            next_token: <p>The token of the next Recovery Instance to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances.describe_recovery_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_recovery_instances_response

            return capo_drs.types.describe_recovery_instances_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeRecoveryInstances", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest = {}
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

    def delete_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> None:
        """<p>Deletes a single Recovery Instance by ID. This deletes the Recovery Instance resource from Elastic Disaster Recovery. The Recovery Instance must be disconnected first in order to delete it.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to be deleted.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest]",
        ) -> OperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance.delete_recovery_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRecoveryInstance")
        )
        input_: capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disconnect_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> None:
        """<p>Disconnect a Recovery Instance from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Recovery Instance will be terminated / deleted within 90 minutes. If the agent on the Recovery Instance has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the Recovery Instance will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to disconnect.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest]",
        ) -> OperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance.disconnect_recovery_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisconnectRecoveryInstance")
        )
        input_: capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse":
        """<p>Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance whose failback replication configuration should be returned.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration.get_failback_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFailbackReplicationConfiguration")
        )
        input_: capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reverse_replication(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.reverse_replication_response.ReverseReplicationResponse":
        """<p>Start replication to origin / target region - applies only to protected instances that originated in EC2. For recovery instances on target region - starts replication back to origin region. For failback instances on origin region - starts replication to target region to re-protect them. </p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance that we want to reverse the replication for.</p>

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
            req: "OperationRequest[capo_drs.types.reverse_replication_request.ReverseReplicationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.reverse_replication_response.ReverseReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.reverse_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.reverse_replication.reverse_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ReverseReplication")
        )
        input_: capo_drs.types.reverse_replication_request.ReverseReplicationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_failback(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> None:
        """<p>Stops the failback process for a specified Recovery Instance. This changes the Failback State of the Recovery Instance back to FAILBACK_NOT_STARTED.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance we want to stop failback for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.stop_failback_request.StopFailbackRequest]",
        ) -> OperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_failback

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.stop_failback.stop_failback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopFailback")
        )
        input_: capo_drs.types.stop_failback_request.StopFailbackRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        name: Optional["capo_drs.types.bounded_string.BoundedString"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        use_private_ip: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> None:
        """<p>Allows you to update the failback replication configuration of a Recovery Instance by ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance.</p>
            name: <p>The name of the Failback Replication Configuration.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.</p>
            use_private_ip: <p>Whether to use Private IP for the failback replication of the Recovery Instance.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration.update_failback_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFailbackReplicationConfiguration")
        )
        input_: capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }
        if name is not None:
            input_["name"] = name
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if use_private_ip is not None:
            input_["use_private_ip"] = use_private_ip
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_failback_launch(
        self,
        recovery_instance_i_ds: "capo_drs.types.start_failback_request_recovery_instance_i_ds.StartFailbackRequestRecoveryInstanceIDs",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse":
        """<p>Initiates a Job for launching the machine that is being failed back to from the specified Recovery Instance. This will run conversion on the failback client and will reboot your machine, thus completing the failback process.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instance whose failback launch we want to request.</p>
            tags: <p>The tags to be associated with the failback launch Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch.start_failback_launch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_failback_launch_request

            return capo_drs.types.start_failback_launch_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_failback_launch_response

            return capo_drs.types.start_failback_launch_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartFailbackLaunch",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_recovery_instances(
        self,
        recovery_instance_i_ds: "capo_drs.types.recovery_instances_for_termination_request.RecoveryInstancesForTerminationRequest",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse":
        """<p>Initiates a Job for terminating the EC2 resources associated with the specified Recovery Instances, and then will delete the Recovery Instances from the Elastic Disaster Recovery service.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instances that should be terminated.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest]",
        ) -> OperationResponse[
            "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances.terminate_recovery_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.terminate_recovery_instances_response

            return (
                capo_drs.types.terminate_recovery_instances_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "TerminateRecoveryInstances", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRecoveryInstanceResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_instances_request_filters.DescribeRecoveryInstancesRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse":
        """<p>Lists all Recovery Instances or multiple Recovery Instances by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Recovery Instances.</p>
            max_results: <p>Maximum number of Recovery Instances to retrieve.</p>
            next_token: <p>The token of the next Recovery Instance to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances.async_describe_recovery_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_recovery_instances_response

            return capo_drs.types.describe_recovery_instances_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeRecoveryInstances", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest = {}
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

    async def delete_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Deletes a single Recovery Instance by ID. This deletes the Recovery Instance resource from Elastic Disaster Recovery. The Recovery Instance must be disconnected first in order to delete it.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to be deleted.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance.async_delete_recovery_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRecoveryInstance")
        )
        input_: capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Disconnect a Recovery Instance from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Recovery Instance will be terminated / deleted within 90 minutes. If the agent on the Recovery Instance has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the Recovery Instance will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to disconnect.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance.async_disconnect_recovery_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisconnectRecoveryInstance")
        )
        input_: capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse":
        """<p>Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance whose failback replication configuration should be returned.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration.async_get_failback_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFailbackReplicationConfiguration")
        )
        input_: capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reverse_replication(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.reverse_replication_response.ReverseReplicationResponse":
        """<p>Start replication to origin / target region - applies only to protected instances that originated in EC2. For recovery instances on target region - starts replication back to origin region. For failback instances on origin region - starts replication to target region to re-protect them. </p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance that we want to reverse the replication for.</p>

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
            req: "AsyncOperationRequest[capo_drs.types.reverse_replication_request.ReverseReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.reverse_replication_response.ReverseReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.reverse_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.reverse_replication.async_reverse_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ReverseReplication")
        )
        input_: capo_drs.types.reverse_replication_request.ReverseReplicationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_failback(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Stops the failback process for a specified Recovery Instance. This changes the Failback State of the Recovery Instance back to FAILBACK_NOT_STARTED.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance we want to stop failback for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.stop_failback_request.StopFailbackRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_failback

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_failback.async_stop_failback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopFailback")
        )
        input_: capo_drs.types.stop_failback_request.StopFailbackRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.bounded_string.BoundedString"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        use_private_ip: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> None:
        """<p>Allows you to update the failback replication configuration of a Recovery Instance by ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance.</p>
            name: <p>The name of the Failback Replication Configuration.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.</p>
            use_private_ip: <p>Whether to use Private IP for the failback replication of the Recovery Instance.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration.async_update_failback_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFailbackReplicationConfiguration")
        )
        input_: capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }
        if name is not None:
            input_["name"] = name
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if use_private_ip is not None:
            input_["use_private_ip"] = use_private_ip
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_failback_launch(
        self,
        recovery_instance_i_ds: "capo_drs.types.start_failback_request_recovery_instance_i_ds.StartFailbackRequestRecoveryInstanceIDs",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse":
        """<p>Initiates a Job for launching the machine that is being failed back to from the specified Recovery Instance. This will run conversion on the failback client and will reboot your machine, thus completing the failback process.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instance whose failback launch we want to request.</p>
            tags: <p>The tags to be associated with the failback launch Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch.async_start_failback_launch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_failback_launch_request

            return capo_drs.types.start_failback_launch_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_failback_launch_response

            return capo_drs.types.start_failback_launch_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartFailbackLaunch",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_recovery_instances(
        self,
        recovery_instance_i_ds: "capo_drs.types.recovery_instances_for_termination_request.RecoveryInstancesForTerminationRequest",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse":
        """<p>Initiates a Job for terminating the EC2 resources associated with the specified Recovery Instances, and then will delete the Recovery Instances from the Elastic Disaster Recovery service.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instances that should be terminated.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances.async_terminate_recovery_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.terminate_recovery_instances_response

            return (
                capo_drs.types.terminate_recovery_instances_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "TerminateRecoveryInstances", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
