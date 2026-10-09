from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_devops_agent._auth._signers
import capo_devops_agent._auth._sigv4
from capo_devops_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_devops_agent.types.deregister_service_input
    import capo_devops_agent.types.deregister_service_output
    import capo_devops_agent.types.get_service_input
    import capo_devops_agent.types.get_service_output
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.list_services_input
    import capo_devops_agent.types.list_services_output
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.post_register_service_supported_service
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.register_service_input
    import capo_devops_agent.types.register_service_output
    import capo_devops_agent.types.registered_service
    import capo_devops_agent.types.service
    import capo_devops_agent.types.service_details
    import capo_devops_agent.types.service_id
    import capo_devops_agent.types.service_name_input
    import capo_devops_agent.types.tags
    from capo_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from capo_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class ServiceResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def create(
        self,
        service: "capo_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService",
        service_details: "capo_devops_agent.types.service_details.ServiceDetails",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        target_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        exchange_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        name: Optional[
            "capo_devops_agent.types.service_name_input.ServiceNameInput"
        ] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.register_service_output.RegisterServiceOutput":
        """<p>This operation registers the specified service</p>

        Args:
            service_details: <p>Service-specific authorization configuration parameters</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            private_connection_name: <p>The name of the private connection to use for VPC connectivity.</p>
            target_url_private_connection_name: <p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>
            exchange_url_private_connection_name: <p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>
            name: <p>The display name for the service registration.</p>
            tags: <p>Tags to add to the Service at registration time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.register_service_input.RegisterServiceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.register_service_output.RegisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.register_service

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.register_service.register_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.register_service_input.RegisterServiceInput = {
            "service": service,
            "service_details": service_details,
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name
        if target_url_private_connection_name is not None:
            input_["target_url_private_connection_name"] = (
                target_url_private_connection_name
            )
        if exchange_url_private_connection_name is not None:
            input_["exchange_url_private_connection_name"] = (
                exchange_url_private_connection_name
            )
        if name is not None:
            input_["name"] = name
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
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_service_output.GetServiceOutput":
        """<p>Retrieves given service by it's unique identifier</p>

        Args:
            service_id: <p>The unique identifier of the given service.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.get_service_input.GetServiceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.get_service_output.GetServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_service

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_service_input.GetServiceInput = {
            "service_id": service_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput":
        """<p>Deregister a service</p>

        Args:
            service_id: <p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.deregister_service_input.DeregisterServiceInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.deregister_service

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.deregister_service.deregister_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.deregister_service_input.DeregisterServiceInput = {
            "service_id": service_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_services(
        self,
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional["capo_devops_agent.types.service.Service"] = None,
    ) -> "capo_devops_agent.types.list_services_output.ListServicesOutput":
        """<p>List a list of registered service on the account level.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_type: <p>Optional filter to list only services of a specific type.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.list_services_output.ListServicesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_services

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_services_input.ListServicesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_type is not None:
            input_["filter_service_type"] = filter_service_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def create(
        self,
        service: "capo_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService",
        service_details: "capo_devops_agent.types.service_details.ServiceDetails",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        target_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        exchange_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        name: Optional[
            "capo_devops_agent.types.service_name_input.ServiceNameInput"
        ] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.register_service_output.RegisterServiceOutput":
        """<p>This operation registers the specified service</p>

        Args:
            service_details: <p>Service-specific authorization configuration parameters</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            private_connection_name: <p>The name of the private connection to use for VPC connectivity.</p>
            target_url_private_connection_name: <p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>
            exchange_url_private_connection_name: <p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>
            name: <p>The display name for the service registration.</p>
            tags: <p>Tags to add to the Service at registration time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.register_service_input.RegisterServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.register_service_output.RegisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.register_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.register_service.async_register_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.register_service_input.RegisterServiceInput = {
            "service": service,
            "service_details": service_details,
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name
        if target_url_private_connection_name is not None:
            input_["target_url_private_connection_name"] = (
                target_url_private_connection_name
            )
        if exchange_url_private_connection_name is not None:
            input_["exchange_url_private_connection_name"] = (
                exchange_url_private_connection_name
            )
        if name is not None:
            input_["name"] = name
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
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_service_output.GetServiceOutput":
        """<p>Retrieves given service by it's unique identifier</p>

        Args:
            service_id: <p>The unique identifier of the given service.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_service_input.GetServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_service_output.GetServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_service_input.GetServiceInput = {
            "service_id": service_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput":
        """<p>Deregister a service</p>

        Args:
            service_id: <p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.deregister_service_input.DeregisterServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.deregister_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.deregister_service.async_deregister_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.deregister_service_input.DeregisterServiceInput = {
            "service_id": service_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional["capo_devops_agent.types.service.Service"] = None,
    ) -> "capo_devops_agent.types.list_services_output.ListServicesOutput":
        """<p>List a list of registered service on the account level.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_type: <p>Optional filter to list only services of a specific type.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_services_output.ListServicesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_services

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_services_input.ListServicesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_type is not None:
            input_["filter_service_type"] = filter_service_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
