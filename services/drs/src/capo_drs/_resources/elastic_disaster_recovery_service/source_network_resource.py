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
    import capo_drs.types.account_id
    import capo_drs.types.associate_source_network_stack_request
    import capo_drs.types.associate_source_network_stack_response
    import capo_drs.types.aws_region
    import capo_drs.types.cfn_stack_name
    import capo_drs.types.create_source_network_request
    import capo_drs.types.create_source_network_response
    import capo_drs.types.delete_source_network_request
    import capo_drs.types.delete_source_network_response
    import capo_drs.types.describe_source_networks_request
    import capo_drs.types.describe_source_networks_request_filters
    import capo_drs.types.describe_source_networks_response
    import capo_drs.types.export_source_network_cfn_template_request
    import capo_drs.types.export_source_network_cfn_template_response
    import capo_drs.types.pagination_token
    import capo_drs.types.source_network
    import capo_drs.types.source_network_id
    import capo_drs.types.start_source_network_recovery_request
    import capo_drs.types.start_source_network_recovery_request_network_entries
    import capo_drs.types.start_source_network_recovery_response
    import capo_drs.types.start_source_network_replication_request
    import capo_drs.types.start_source_network_replication_response
    import capo_drs.types.stop_source_network_replication_request
    import capo_drs.types.stop_source_network_replication_response
    import capo_drs.types.strictly_positive_integer
    import capo_drs.types.tags_map
    import capo_drs.types.vpc_id
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class SourceNetworkResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "capo_drs.types.vpc_id.VpcID",
        origin_account_id: "capo_drs.types.account_id.AccountID",
        origin_region: "capo_drs.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse":
        """<p>Create a new Source Network resource for a provided VPC ID.</p>

        Args:
            vpc_id: <p>Which VPC ID to protect.</p>
            origin_account_id: <p>Account containing the VPC to protect.</p>
            origin_region: <p>Region containing the VPC to protect.</p>
            tags: <p>A set of tags to be associated with the Source Network resource.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.create_source_network_request.CreateSourceNetworkRequest]",
        ) -> OperationResponse[
            "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_source_network

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.create_source_network.create_source_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_source_network_request.CreateSourceNetworkRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_source_network_request

            return capo_drs.types.create_source_network_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateSourceNetwork", redact_input=_redact_input),
        )
        input_: capo_drs.types.create_source_network_request.CreateSourceNetworkRequest = {
            "vpc_id": vpc_id,
            "origin_account_id": origin_account_id,
            "origin_region": origin_region,
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

    def delete(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse":
        """<p>Delete Source Network resource.</p>

        Args:
            source_network_id: <p>ID of the Source Network to delete.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest]",
        ) -> OperationResponse[
            "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_network

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_source_network.delete_source_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceNetwork")
        )
        input_: capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest = {
            "source_network_id": source_network_id
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
            "capo_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse":
        """<p>Lists all Source Networks or multiple Source Networks filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Networks.</p>
            max_results: <p>Maximum number of Source Networks to retrieve.</p>
            next_token: <p>The token of the next Source Networks to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks.describe_source_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_source_networks_response

            return capo_drs.types.describe_source_networks_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceNetworks", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest = {}
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

    def associate_source_network_stack(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        cfn_stack_name: "capo_drs.types.cfn_stack_name.CfnStackName",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse":
        """<p>Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network. Can be used for reverting to previously deployed CloudFormation stacks.</p>

        Args:
            source_network_id: <p>The Source Network ID to associate with CloudFormation template.</p>
            cfn_stack_name: <p>CloudFormation template to associate with a Source Network.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest]",
        ) -> OperationResponse[
            "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack.associate_source_network_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.associate_source_network_stack_request

            return (
                capo_drs.types.associate_source_network_stack_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.associate_source_network_stack_response

            return (
                capo_drs.types.associate_source_network_stack_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateSourceNetworkStack",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest = {
            "source_network_id": source_network_id,
            "cfn_stack_name": cfn_stack_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_source_network_cfn_template(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse":
        """<p>Export the Source Network CloudFormation template to an S3 bucket.</p>

        Args:
            source_network_id: <p>The Source Network ID to export its CloudFormation template to an S3 bucket.</p>

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
            req: "OperationRequest[capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest]",
        ) -> OperationResponse[
            "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template.export_source_network_cfn_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportSourceNetworkCfnTemplate")
        )
        input_: capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest = {
            "source_network_id": source_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse":
        """<p>Starts replication for a Source Network. This action would make the Source Network protected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to replicate.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication.start_source_network_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_replication_response

            return capo_drs.types.start_source_network_replication_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartSourceNetworkReplication", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse":
        """<p>Stops replication for a Source Network. This action would make the Source Network unprotected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to stop replication.</p>

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
            req: "OperationRequest[capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest]",
        ) -> OperationResponse[
            "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication.stop_source_network_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.stop_source_network_replication_response

            return capo_drs.types.stop_source_network_replication_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StopSourceNetworkReplication", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_source_network_recovery(
        self,
        source_networks: "capo_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        deploy_as_new: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse":
        """<p>Deploy VPC for the specified Source Network and modify launch templates to use this network. The VPC will be deployed using a dedicated CloudFormation stack.</p>

        Args:
            source_networks: <p>The Source Networks that we want to start a Recovery Job for.</p>
            deploy_as_new: <p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>
            tags: <p>The tags to be associated with the Source Network recovery Job.</p>

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
            req: "OperationRequest[capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest]",
        ) -> OperationResponse[
            "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery.start_source_network_recovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_recovery_request

            return (
                capo_drs.types.start_source_network_recovery_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_recovery_response

            return (
                capo_drs.types.start_source_network_recovery_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartSourceNetworkRecovery",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest = {
            "source_networks": source_networks
        }
        if deploy_as_new is not None:
            input_["deploy_as_new"] = deploy_as_new
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSourceNetworkResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "capo_drs.types.vpc_id.VpcID",
        origin_account_id: "capo_drs.types.account_id.AccountID",
        origin_region: "capo_drs.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse":
        """<p>Create a new Source Network resource for a provided VPC ID.</p>

        Args:
            vpc_id: <p>Which VPC ID to protect.</p>
            origin_account_id: <p>Account containing the VPC to protect.</p>
            origin_region: <p>Region containing the VPC to protect.</p>
            tags: <p>A set of tags to be associated with the Source Network resource.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_source_network_request.CreateSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_source_network

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_source_network.async_create_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.create_source_network_request.CreateSourceNetworkRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.create_source_network_request

            return capo_drs.types.create_source_network_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateSourceNetwork", redact_input=_redact_input),
        )
        input_: capo_drs.types.create_source_network_request.CreateSourceNetworkRequest = {
            "vpc_id": vpc_id,
            "origin_account_id": origin_account_id,
            "origin_region": origin_region,
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

    async def delete(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse":
        """<p>Delete Source Network resource.</p>

        Args:
            source_network_id: <p>ID of the Source Network to delete.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_network

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_source_network.async_delete_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSourceNetwork")
        )
        input_: capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest = {
            "source_network_id": source_network_id
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
            "capo_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse":
        """<p>Lists all Source Networks or multiple Source Networks filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Networks.</p>
            max_results: <p>Maximum number of Source Networks to retrieve.</p>
            next_token: <p>The token of the next Source Networks to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks.async_describe_source_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_source_networks_response

            return capo_drs.types.describe_source_networks_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeSourceNetworks", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest = {}
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

    async def associate_source_network_stack(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        cfn_stack_name: "capo_drs.types.cfn_stack_name.CfnStackName",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse":
        """<p>Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network. Can be used for reverting to previously deployed CloudFormation stacks.</p>

        Args:
            source_network_id: <p>The Source Network ID to associate with CloudFormation template.</p>
            cfn_stack_name: <p>CloudFormation template to associate with a Source Network.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack.async_associate_source_network_stack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.associate_source_network_stack_request

            return (
                capo_drs.types.associate_source_network_stack_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.associate_source_network_stack_response

            return (
                capo_drs.types.associate_source_network_stack_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateSourceNetworkStack",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest = {
            "source_network_id": source_network_id,
            "cfn_stack_name": cfn_stack_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_source_network_cfn_template(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse":
        """<p>Export the Source Network CloudFormation template to an S3 bucket.</p>

        Args:
            source_network_id: <p>The Source Network ID to export its CloudFormation template to an S3 bucket.</p>

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
            req: "AsyncOperationRequest[capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template.async_export_source_network_cfn_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportSourceNetworkCfnTemplate")
        )
        input_: capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse":
        """<p>Starts replication for a Source Network. This action would make the Source Network protected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to replicate.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication.async_start_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_replication_response

            return capo_drs.types.start_source_network_replication_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartSourceNetworkReplication", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse":
        """<p>Stops replication for a Source Network. This action would make the Source Network unprotected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to stop replication.</p>

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
            req: "AsyncOperationRequest[capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication.async_stop_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.stop_source_network_replication_response

            return capo_drs.types.stop_source_network_replication_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StopSourceNetworkReplication", redact_output=_redact_output
            ),
        )
        input_: capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_source_network_recovery(
        self,
        source_networks: "capo_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        deploy_as_new: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse":
        """<p>Deploy VPC for the specified Source Network and modify launch templates to use this network. The VPC will be deployed using a dedicated CloudFormation stack.</p>

        Args:
            source_networks: <p>The Source Networks that we want to start a Recovery Job for.</p>
            deploy_as_new: <p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>
            tags: <p>The tags to be associated with the Source Network recovery Job.</p>

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
            req: "AsyncOperationRequest[capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery.async_start_source_network_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_recovery_request

            return (
                capo_drs.types.start_source_network_recovery_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.start_source_network_recovery_response

            return (
                capo_drs.types.start_source_network_recovery_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartSourceNetworkRecovery",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest = {
            "source_networks": source_networks
        }
        if deploy_as_new is not None:
            input_["deploy_as_new"] = deploy_as_new
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
