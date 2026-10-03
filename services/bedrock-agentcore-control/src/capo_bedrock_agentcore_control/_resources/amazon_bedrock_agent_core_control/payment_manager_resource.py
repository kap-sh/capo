from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_payment_manager_request
    import capo_bedrock_agentcore_control.types.create_payment_manager_response
    import capo_bedrock_agentcore_control.types.delete_payment_manager_request
    import capo_bedrock_agentcore_control.types.delete_payment_manager_response
    import capo_bedrock_agentcore_control.types.get_payment_manager_request
    import capo_bedrock_agentcore_control.types.get_payment_manager_response
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.list_payment_managers_request
    import capo_bedrock_agentcore_control.types.list_payment_managers_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payment_manager_name
    import capo_bedrock_agentcore_control.types.payment_manager_summary
    import capo_bedrock_agentcore_control.types.payments_authorizer_type
    import capo_bedrock_agentcore_control.types.payments_description
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_payment_manager_request
    import capo_bedrock_agentcore_control.types.update_payment_manager_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class PaymentManagerResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName",
        authorizer_type: "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse":
        """<p>Creates a new payment manager in your Amazon Web Services account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the payment manager.</p>
            description: <p>A description of the payment manager.</p>
            authorizer_type: <p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the payment manager.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to assign to the payment manager.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for encrypting sensitive payment manager data at rest. If you don't specify a key, the data is encrypted with an Amazon Web Services owned key.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager.create_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest = {
            "name": name,
            "authorizer_type": authorizer_type,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse":
        """<p>Retrieves information about a specific payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager.get_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
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
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse":
        """<p>Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to update.</p>
            description: <p>The updated description of the payment manager.</p>
            authorizer_type: <p>The updated authorizer type for the payment manager.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the payment manager.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            kms_key_arn: <p>The updated Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt sensitive payment manager data at rest.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager.update_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse":
        """<p>Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager.delete_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }
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

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse":
        """<p>Lists all payment managers in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers.list_payment_managers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest = {}
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


class AsyncPaymentManagerResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName",
        authorizer_type: "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse":
        """<p>Creates a new payment manager in your Amazon Web Services account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the payment manager.</p>
            description: <p>A description of the payment manager.</p>
            authorizer_type: <p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the payment manager.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to assign to the payment manager.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for encrypting sensitive payment manager data at rest. If you don't specify a key, the data is encrypted with an Amazon Web Services owned key.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager.async_create_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest = {
            "name": name,
            "authorizer_type": authorizer_type,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse":
        """<p>Retrieves information about a specific payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager.async_get_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
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
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse":
        """<p>Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to update.</p>
            description: <p>The updated description of the payment manager.</p>
            authorizer_type: <p>The updated authorizer type for the payment manager.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the payment manager.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            kms_key_arn: <p>The updated Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt sensitive payment manager data at rest.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager.async_update_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse":
        """<p>Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager.async_delete_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse":
        """<p>Lists all payment managers in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers.async_list_payment_managers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest = {}
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
