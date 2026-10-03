from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider
    import capo_lambda.types.capacity_provider_name
    import capo_lambda.types.capacity_provider_permissions_config
    import capo_lambda.types.capacity_provider_scaling_config
    import capo_lambda.types.capacity_provider_state
    import capo_lambda.types.capacity_provider_telemetry_config
    import capo_lambda.types.capacity_provider_vpc_config
    import capo_lambda.types.create_capacity_provider_request
    import capo_lambda.types.create_capacity_provider_response
    import capo_lambda.types.delete_capacity_provider_request
    import capo_lambda.types.delete_capacity_provider_response
    import capo_lambda.types.function_versions_by_capacity_provider_list_item
    import capo_lambda.types.get_capacity_provider_request
    import capo_lambda.types.get_capacity_provider_response
    import capo_lambda.types.instance_requirements
    import capo_lambda.types.kms_key_arn_non_empty
    import capo_lambda.types.list_capacity_providers_request
    import capo_lambda.types.list_capacity_providers_response
    import capo_lambda.types.list_function_versions_by_capacity_provider_request
    import capo_lambda.types.list_function_versions_by_capacity_provider_response
    import capo_lambda.types.max_fifty_list_items
    import capo_lambda.types.propagate_tags
    import capo_lambda.types.string
    import capo_lambda.types.tags
    import capo_lambda.types.update_capacity_provider_request
    import capo_lambda.types.update_capacity_provider_response
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class CapacityProviderResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def put(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        vpc_config: "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig",
        permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        instance_requirements: Optional[
            "capo_lambda.types.instance_requirements.InstanceRequirements"
        ] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        kms_key_arn: Optional[
            "capo_lambda.types.kms_key_arn_non_empty.KMSKeyArnNonEmpty"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider that manages compute resources for Lambda functions</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider. </p>
            vpc_config: <p>The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.</p>
            permissions_config: <p>The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.</p>
            instance_requirements: <p>The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.</p>
            capacity_provider_scaling_config: <p>The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt data associated with the capacity provider.</p>
            tags: <p>A list of tags to associate with the capacity provider.</p>
            propagate_tags: <p>The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.</p>
            telemetry_config: <p>The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.</p>

        Raises:
            capo_lambda.errors.capacity_provider_limit_exceeded_exception.CapacityProviderLimitExceededException: <p>The maximum number of capacity providers for your account has been exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a> </p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_capacity_provider.create_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name,
            "vpc_config": vpc_config,
            "permissions_config": permissions_config,
        }
        if instance_requirements is not None:
            input_["instance_requirements"] = instance_requirements
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse":
        """<p>Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to retrieve.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_capacity_provider.get_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
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
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Updates the configuration of an existing capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to update.</p>
            capacity_provider_scaling_config: <p>The updated scaling configuration for the capacity provider.</p>
            telemetry_config: <p>The updated telemetry configuration for the capacity provider.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_capacity_provider.update_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to delete.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_capacity_provider.delete_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
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
        config_overrides: Optional[LambdaClientConfig] = None,
        state: Optional[
            "capo_lambda.types.capacity_provider_state.CapacityProviderState"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse":
        """<p>Returns a list of capacity providers in your account.</p>

        Args:
            state: <p>Filter capacity providers by their current state.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of capacity providers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_capacity_providers

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_capacity_providers.list_capacity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_function_versions_by_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse":
        """<p>Returns a list of function versions that are configured to use a specific capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to list function versions for.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function versions to return in the response.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider.list_function_versions_by_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCapacityProviderResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def put(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        vpc_config: "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig",
        permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        instance_requirements: Optional[
            "capo_lambda.types.instance_requirements.InstanceRequirements"
        ] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        kms_key_arn: Optional[
            "capo_lambda.types.kms_key_arn_non_empty.KMSKeyArnNonEmpty"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider that manages compute resources for Lambda functions</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider. </p>
            vpc_config: <p>The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.</p>
            permissions_config: <p>The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.</p>
            instance_requirements: <p>The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.</p>
            capacity_provider_scaling_config: <p>The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt data associated with the capacity provider.</p>
            tags: <p>A list of tags to associate with the capacity provider.</p>
            propagate_tags: <p>The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.</p>
            telemetry_config: <p>The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.</p>

        Raises:
            capo_lambda.errors.capacity_provider_limit_exceeded_exception.CapacityProviderLimitExceededException: <p>The maximum number of capacity providers for your account has been exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a> </p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_capacity_provider

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_capacity_provider.async_create_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name,
            "vpc_config": vpc_config,
            "permissions_config": permissions_config,
        }
        if instance_requirements is not None:
            input_["instance_requirements"] = instance_requirements
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse":
        """<p>Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to retrieve.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_capacity_provider

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_capacity_provider.async_get_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
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
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Updates the configuration of an existing capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to update.</p>
            capacity_provider_scaling_config: <p>The updated scaling configuration for the capacity provider.</p>
            telemetry_config: <p>The updated telemetry configuration for the capacity provider.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_capacity_provider

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_capacity_provider.async_update_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to delete.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_capacity_provider

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_capacity_provider.async_delete_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
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
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        state: Optional[
            "capo_lambda.types.capacity_provider_state.CapacityProviderState"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse":
        """<p>Returns a list of capacity providers in your account.</p>

        Args:
            state: <p>Filter capacity providers by their current state.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of capacity providers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_capacity_providers

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_capacity_providers.async_list_capacity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_function_versions_by_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse":
        """<p>Returns a list of function versions that are configured to use a specific capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to list function versions for.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function versions to return in the response.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider.async_list_function_versions_by_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
