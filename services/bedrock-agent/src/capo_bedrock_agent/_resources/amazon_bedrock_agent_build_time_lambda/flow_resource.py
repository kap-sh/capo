from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_flow_request
    import capo_bedrock_agent.types.create_flow_response
    import capo_bedrock_agent.types.delete_flow_request
    import capo_bedrock_agent.types.delete_flow_response
    import capo_bedrock_agent.types.flow_definition
    import capo_bedrock_agent.types.flow_description
    import capo_bedrock_agent.types.flow_execution_role_arn
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.flow_name
    import capo_bedrock_agent.types.flow_summary
    import capo_bedrock_agent.types.get_flow_request
    import capo_bedrock_agent.types.get_flow_response
    import capo_bedrock_agent.types.included_data
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.list_flows_request
    import capo_bedrock_agent.types.list_flows_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.prepare_flow_request
    import capo_bedrock_agent.types.prepare_flow_response
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_flow_request
    import capo_bedrock_agent.types.update_flow_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class FlowResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse":
        """<p>Creates a prompt flow that you can use to send an input through various steps to yield an output. Configure nodes, each of which corresponds to a step of the flow, and create connections between the nodes to create paths to different outputs. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and connections between nodes in the flow.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_flow_request.CreateFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow.create_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_flow_request.CreateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition
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
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_flow_response.GetFlowResponse":
        """<p>Retrieves information about a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_flow_request.GetFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_flow_response.GetFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow.get_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_flow_request.GetFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse":
        """<p>Modifies a flow. Include both fields that you want to keep and fields that you want to change. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and the connections between the nodes in the flow.</p>
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow.update_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
            "flow_identifier": flow_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse":
        """<p>Deletes a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow.delete_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

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
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse":
        """<p>Returns a list of flows and information about each flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_flows_request.ListFlowsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows.list_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_flows_request.ListFlowsRequest = {}
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

    def prepare_flow(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse":
        """<p>Prepares the <code>DRAFT</code> version of a flow so that it can be invoked. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow.prepare_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest = {
            "flow_identifier": flow_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFlowResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse":
        """<p>Creates a prompt flow that you can use to send an input through various steps to yield an output. Configure nodes, each of which corresponds to a step of the flow, and create connections between the nodes to create paths to different outputs. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and connections between nodes in the flow.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_flow_request.CreateFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow.async_create_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_flow_request.CreateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition
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
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_flow_response.GetFlowResponse":
        """<p>Retrieves information about a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_flow_request.GetFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_flow_response.GetFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow.async_get_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_flow_request.GetFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse":
        """<p>Modifies a flow. Include both fields that you want to keep and fields that you want to change. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and the connections between the nodes in the flow.</p>
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow.async_update_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
            "flow_identifier": flow_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse":
        """<p>Deletes a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow.async_delete_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

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
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse":
        """<p>Returns a list of flows and information about each flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_flows_request.ListFlowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows.async_list_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_flows_request.ListFlowsRequest = {}
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

    async def prepare_flow(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse":
        """<p>Prepares the <code>DRAFT</code> version of a flow so that it can be invoked. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow.async_prepare_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest = {
            "flow_identifier": flow_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
