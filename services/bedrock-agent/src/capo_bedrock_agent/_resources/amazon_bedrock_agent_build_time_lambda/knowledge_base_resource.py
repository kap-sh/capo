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
    import capo_bedrock_agent.types.agent_knowledge_base_summary
    import capo_bedrock_agent.types.associate_agent_knowledge_base_request
    import capo_bedrock_agent.types.associate_agent_knowledge_base_response
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_knowledge_base_request
    import capo_bedrock_agent.types.create_knowledge_base_response
    import capo_bedrock_agent.types.delete_knowledge_base_request
    import capo_bedrock_agent.types.delete_knowledge_base_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.disassociate_agent_knowledge_base_request
    import capo_bedrock_agent.types.disassociate_agent_knowledge_base_response
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.get_agent_knowledge_base_request
    import capo_bedrock_agent.types.get_agent_knowledge_base_response
    import capo_bedrock_agent.types.get_knowledge_base_request
    import capo_bedrock_agent.types.get_knowledge_base_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_role_arn
    import capo_bedrock_agent.types.knowledge_base_state
    import capo_bedrock_agent.types.knowledge_base_summary
    import capo_bedrock_agent.types.list_agent_knowledge_bases_request
    import capo_bedrock_agent.types.list_agent_knowledge_bases_response
    import capo_bedrock_agent.types.list_knowledge_bases_request
    import capo_bedrock_agent.types.list_knowledge_bases_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.storage_configuration
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_agent_knowledge_base_request
    import capo_bedrock_agent.types.update_agent_knowledge_base_response
    import capo_bedrock_agent.types.update_knowledge_base_request
    import capo_bedrock_agent.types.update_knowledge_base_response
    import capo_bedrock_agent.types.version
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class KnowledgeBaseResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def associate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        description: "capo_bedrock_agent.types.description.Description",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse":
        """<p>Associates a knowledge base with an agent. If a knowledge base is associated and its <code>indexState</code> is set to <code>Enabled</code>, the agent queries the knowledge base for information to augment its response to the user.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which you want to associate the knowledge base.</p>
            agent_version: <p>The version of the agent with which you want to associate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to associate with the agent.</p>
            description: <p>A description of what the agent should use the knowledge base for.</p>
            knowledge_base_state: <p>Specifies whether to use the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base.associate_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
            "description": description,
        }
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_knowledge_base(
        self,
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse":
        """<p>Creates a knowledge base. A knowledge base contains your data sources so that Large Language Models (LLMs) can use your data. To create a knowledge base, you must first set up your data sources and configure a supported vector store. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowlege-base-prereq.html">Set up a knowledge base</a>.</p> <note> <p>To create a managed knowledge base, provide a <code>managedKnowledgeBaseConfiguration</code> during creation. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html">Build a managed knowledge base</a>.</p> </note> <ul> <li> <p>Provide the <code>name</code> and an optional <code>description</code>.</p> </li> <li> <p>Provide the Amazon Resource Name (ARN) with permissions to create a knowledge base in the <code>roleArn</code> field.</p> </li> <li> <p>For managed knowledge bases, set <code>embeddingModelType</code> to <code>MANAGED</code> to use the service-managed embedding model, or <code>CUSTOM</code> with an <code>embeddingModelArn</code> to use your own. To use your own KMS key for encryption, provide the ARN in <code>serverSideEncryptionConfiguration</code>. No vector store configuration is required for managed knowledge bases.</p> </li> <li> <p>For self-managed knowledge bases, provide the embedding model to use in the <code>embeddingModelArn</code> field in the <code>knowledgeBaseConfiguration</code> object.</p> </li> <li> <p>For self-managed knowledge bases, provide the configuration for your vector store in the <code>storageConfiguration</code> object.</p> <ul> <li> <p>For an Amazon OpenSearch Service database, use the <code>opensearchServerlessConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html">Create a vector store in Amazon OpenSearch Service</a>.</p> </li> <li> <p>For an Amazon Aurora database, use the <code>RdsConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html">Create a vector store in Amazon Aurora</a>.</p> </li> <li> <p>For a Pinecone database, use the <code>pineconeConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html">Create a vector store in Pinecone</a>.</p> </li> <li> <p>For a Redis Enterprise Cloud database, use the <code>redisEnterpriseCloudConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-redis.html">Create a vector store in Redis Enterprise Cloud</a>.</p> </li> </ul> </li> </ul>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>A name for the knowledge base.</p>
            description: <p>A description of the knowledge base.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Contains details about the embeddings model used for the knowledge base.</p>
            storage_configuration: <p>Contains details about the configuration of the vector database used for the knowledge base.</p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to your knowledge base in this object.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base.create_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse":
        """<p>Deletes a knowledge base. Before deleting a knowledge base, you should disassociate the knowledge base from any agents that it is associated with by making a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentKnowledgeBase.html">DisassociateAgentKnowledgeBase</a> request.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base.delete_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse":
        """<p>Disassociates a knowledge base from an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent from which to disassociate the knowledge base.</p>
            agent_version: <p>The version of the agent from which to disassociate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to disassociate.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base.disassociate_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse":
        """<p>Gets information about a knowledge base associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which the knowledge base is associated.</p>
            agent_version: <p>The version of the agent with which the knowledge base is associated.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base associated with the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base.get_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
    ):
        """<p>Gets information about a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base.get_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_knowledge_bases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse":
        """<p>Lists knowledge bases associated with an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to return information about knowledge bases associated with it.</p>
            agent_version: <p>The version of the agent for which to return information about knowledge bases associated with it.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases.list_agent_knowledge_bases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    def list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases in an account. The list also includesinformation about each knowledge base.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases.list_knowledge_bases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    def update_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse":
        """<p>Updates the configuration for a knowledge base that has been associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent associated with the knowledge base that you want to update.</p>
            agent_version: <p>The version of the agent associated with the knowledge base that you want to update.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base that has been associated with an agent.</p>
            description: <p>Specifies a new description for the knowledge base associated with an agent.</p>
            knowledge_base_state: <p>Specifies whether the agent uses the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base.update_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }
        if description is not None:
            input_["description"] = description
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse":
        """<p>Updates the configuration of a knowledge base with the fields that you specify. Because all fields will be overwritten, you must include the same values for fields that you want to keep the same.</p> <p>You can change the following fields:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>description</code> </p> </li> <li> <p> <code>roleArn</code> </p> </li> </ul> <p>You can't change the <code>knowledgeBaseConfiguration</code> or <code>storageConfiguration</code> fields, so you must specify the same configurations as when you created the knowledge base. You can send a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html">GetKnowledgeBase</a> request and copy the same configurations.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to update.</p>
            name: <p>Specifies a new name for the knowledge base.</p>
            description: <p>Specifies a new description for the knowledge base.</p>
            role_arn: <p>Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>
            storage_configuration: <p>Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base.update_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncKnowledgeBaseResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def associate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        description: "capo_bedrock_agent.types.description.Description",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse":
        """<p>Associates a knowledge base with an agent. If a knowledge base is associated and its <code>indexState</code> is set to <code>Enabled</code>, the agent queries the knowledge base for information to augment its response to the user.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which you want to associate the knowledge base.</p>
            agent_version: <p>The version of the agent with which you want to associate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to associate with the agent.</p>
            description: <p>A description of what the agent should use the knowledge base for.</p>
            knowledge_base_state: <p>Specifies whether to use the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base.async_associate_agent_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
            "description": description,
        }
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_knowledge_base(
        self,
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse":
        """<p>Creates a knowledge base. A knowledge base contains your data sources so that Large Language Models (LLMs) can use your data. To create a knowledge base, you must first set up your data sources and configure a supported vector store. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowlege-base-prereq.html">Set up a knowledge base</a>.</p> <note> <p>To create a managed knowledge base, provide a <code>managedKnowledgeBaseConfiguration</code> during creation. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html">Build a managed knowledge base</a>.</p> </note> <ul> <li> <p>Provide the <code>name</code> and an optional <code>description</code>.</p> </li> <li> <p>Provide the Amazon Resource Name (ARN) with permissions to create a knowledge base in the <code>roleArn</code> field.</p> </li> <li> <p>For managed knowledge bases, set <code>embeddingModelType</code> to <code>MANAGED</code> to use the service-managed embedding model, or <code>CUSTOM</code> with an <code>embeddingModelArn</code> to use your own. To use your own KMS key for encryption, provide the ARN in <code>serverSideEncryptionConfiguration</code>. No vector store configuration is required for managed knowledge bases.</p> </li> <li> <p>For self-managed knowledge bases, provide the embedding model to use in the <code>embeddingModelArn</code> field in the <code>knowledgeBaseConfiguration</code> object.</p> </li> <li> <p>For self-managed knowledge bases, provide the configuration for your vector store in the <code>storageConfiguration</code> object.</p> <ul> <li> <p>For an Amazon OpenSearch Service database, use the <code>opensearchServerlessConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html">Create a vector store in Amazon OpenSearch Service</a>.</p> </li> <li> <p>For an Amazon Aurora database, use the <code>RdsConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html">Create a vector store in Amazon Aurora</a>.</p> </li> <li> <p>For a Pinecone database, use the <code>pineconeConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html">Create a vector store in Pinecone</a>.</p> </li> <li> <p>For a Redis Enterprise Cloud database, use the <code>redisEnterpriseCloudConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-redis.html">Create a vector store in Redis Enterprise Cloud</a>.</p> </li> </ul> </li> </ul>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>A name for the knowledge base.</p>
            description: <p>A description of the knowledge base.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Contains details about the embeddings model used for the knowledge base.</p>
            storage_configuration: <p>Contains details about the configuration of the vector database used for the knowledge base.</p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to your knowledge base in this object.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base.async_create_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse":
        """<p>Deletes a knowledge base. Before deleting a knowledge base, you should disassociate the knowledge base from any agents that it is associated with by making a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentKnowledgeBase.html">DisassociateAgentKnowledgeBase</a> request.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base.async_delete_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse":
        """<p>Disassociates a knowledge base from an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent from which to disassociate the knowledge base.</p>
            agent_version: <p>The version of the agent from which to disassociate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to disassociate.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base.async_disassociate_agent_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse":
        """<p>Gets information about a knowledge base associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which the knowledge base is associated.</p>
            agent_version: <p>The version of the agent with which the knowledge base is associated.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base associated with the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base.async_get_agent_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
    ):
        """<p>Gets information about a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base.async_get_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_knowledge_bases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse":
        """<p>Lists knowledge bases associated with an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to return information about knowledge bases associated with it.</p>
            agent_version: <p>The version of the agent for which to return information about knowledge bases associated with it.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases.async_list_agent_knowledge_bases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    async def list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases in an account. The list also includesinformation about each knowledge base.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases.async_list_knowledge_bases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    async def update_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse":
        """<p>Updates the configuration for a knowledge base that has been associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent associated with the knowledge base that you want to update.</p>
            agent_version: <p>The version of the agent associated with the knowledge base that you want to update.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base that has been associated with an agent.</p>
            description: <p>Specifies a new description for the knowledge base associated with an agent.</p>
            knowledge_base_state: <p>Specifies whether the agent uses the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base.async_update_agent_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }
        if description is not None:
            input_["description"] = description
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse":
        """<p>Updates the configuration of a knowledge base with the fields that you specify. Because all fields will be overwritten, you must include the same values for fields that you want to keep the same.</p> <p>You can change the following fields:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>description</code> </p> </li> <li> <p> <code>roleArn</code> </p> </li> </ul> <p>You can't change the <code>knowledgeBaseConfiguration</code> or <code>storageConfiguration</code> fields, so you must specify the same configurations as when you created the knowledge base. You can send a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html">GetKnowledgeBase</a> request and copy the same configurations.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to update.</p>
            name: <p>Specifies a new name for the knowledge base.</p>
            description: <p>Specifies a new description for the knowledge base.</p>
            role_arn: <p>Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>
            storage_configuration: <p>Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base.async_update_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
