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
    import capo_bedrock_agent.types.create_data_source_request
    import capo_bedrock_agent.types.create_data_source_response
    import capo_bedrock_agent.types.data_deletion_policy
    import capo_bedrock_agent.types.data_source_configuration
    import capo_bedrock_agent.types.data_source_summary
    import capo_bedrock_agent.types.delete_data_source_request
    import capo_bedrock_agent.types.delete_data_source_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.get_data_source_request
    import capo_bedrock_agent.types.get_data_source_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.list_data_sources_request
    import capo_bedrock_agent.types.list_data_sources_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.update_data_source_request
    import capo_bedrock_agent.types.update_data_source_response
    import capo_bedrock_agent.types.vector_ingestion_configuration
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class DataSourceResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
    ):
        """<p>Connects a knowledge base to a data source. You specify the configuration for the specific data source service in the <code>dataSourceConfiguration</code> field.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to which to add the data source.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>The name of the data source.</p>
            description: <p>A description of the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source.</p>
            data_deletion_policy: <p>The data deletion policy for the data source.</p> <p>You can set the data deletion policy to:</p> <ul> <li> <p>DELETE: Deletes all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b>, only the data. This flag is ignored if an Amazon Web Services account is deleted.</p> </li> <li> <p>RETAIN: Retains all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b> if you delete a knowledge base or data source resource.</p> </li> </ul> <note> <p>For managed knowledge bases, the only supported option is <code>DELETE</code>, which is also the default.</p> </note>
            server_side_encryption_configuration: <p>Contains details about the server-side encryption for the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
    ):
        """<p>Deletes a data source from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base from which to delete the data source.</p>
            data_source_id: <p>The unique identifier of the data source to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse":
        """<p>Gets information about a data source.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source.get_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_sources(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the data sources in a knowledge base and information about each one.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for which to return a list of information.</p>
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
            req: "OperationRequest[capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    def update_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
    ):
        """<p>Updates the configurations for a data source connector.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector. Specify the existing <code>chunkingConfiguration</code>.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>
            name: <p>Specifies a new name for the data source.</p>
            description: <p>Specifies a new description for the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source that you want to update.</p>
            data_deletion_policy: <p>The data deletion policy for the data source that you want to update.</p>
            server_side_encryption_configuration: <p>Contains details about server-side encryption of the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataSourceResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
    ):
        """<p>Connects a knowledge base to a data source. You specify the configuration for the specific data source service in the <code>dataSourceConfiguration</code> field.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to which to add the data source.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>The name of the data source.</p>
            description: <p>A description of the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source.</p>
            data_deletion_policy: <p>The data deletion policy for the data source.</p> <p>You can set the data deletion policy to:</p> <ul> <li> <p>DELETE: Deletes all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b>, only the data. This flag is ignored if an Amazon Web Services account is deleted.</p> </li> <li> <p>RETAIN: Retains all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b> if you delete a knowledge base or data source resource.</p> </li> </ul> <note> <p>For managed knowledge bases, the only supported option is <code>DELETE</code>, which is also the default.</p> </note>
            server_side_encryption_configuration: <p>Contains details about the server-side encryption for the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source.async_create_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
    ):
        """<p>Deletes a data source from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base from which to delete the data source.</p>
            data_source_id: <p>The unique identifier of the data source to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse":
        """<p>Gets information about a data source.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_sources(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the data sources in a knowledge base and information about each one.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for which to return a list of information.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources.async_list_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def update_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
    ):
        """<p>Updates the configurations for a data source connector.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector. Specify the existing <code>chunkingConfiguration</code>.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>
            name: <p>Specifies a new name for the data source.</p>
            description: <p>Specifies a new description for the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source that you want to update.</p>
            data_deletion_policy: <p>The data deletion policy for the data source that you want to update.</p>
            server_side_encryption_configuration: <p>Contains details about server-side encryption of the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
