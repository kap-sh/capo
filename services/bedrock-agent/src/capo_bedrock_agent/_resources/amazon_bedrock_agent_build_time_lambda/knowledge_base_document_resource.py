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
    import capo_bedrock_agent.types.delete_knowledge_base_documents_request
    import capo_bedrock_agent.types.delete_knowledge_base_documents_response
    import capo_bedrock_agent.types.document_identifiers
    import capo_bedrock_agent.types.get_knowledge_base_documents_request
    import capo_bedrock_agent.types.get_knowledge_base_documents_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.ingest_knowledge_base_documents_request
    import capo_bedrock_agent.types.ingest_knowledge_base_documents_response
    import capo_bedrock_agent.types.knowledge_base_document_detail
    import capo_bedrock_agent.types.knowledge_base_documents
    import capo_bedrock_agent.types.list_knowledge_base_documents_request
    import capo_bedrock_agent.types.list_knowledge_base_documents_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class KnowledgeBaseDocumentResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def delete_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse":
        """<p>Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents.delete_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
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

    def get_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse":
        """<p>Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents.get_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def ingest_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        documents: "capo_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse":
        """<p>Ingests documents directly into the knowledge base that is connected to the data source. The <code>dataSourceType</code> specified in the content for each document must match the type of the data source that you specify in the header. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to ingest the documents into.</p>
            data_source_id: <p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            documents: <p>A list of objects, each of which contains information about the documents to add.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents.ingest_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "documents": documents,
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

    def list_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse":
        """<p>Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents.list_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
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


class AsyncKnowledgeBaseDocumentResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def delete_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse":
        """<p>Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents.async_delete_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
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

    async def get_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse":
        """<p>Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents.async_get_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def ingest_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        documents: "capo_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse":
        """<p>Ingests documents directly into the knowledge base that is connected to the data source. The <code>dataSourceType</code> specified in the content for each document must match the type of the data source that you specify in the header. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to ingest the documents into.</p>
            data_source_id: <p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            documents: <p>A list of objects, each of which contains information about the documents to add.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents.async_ingest_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "documents": documents,
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

    async def list_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse":
        """<p>Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents.async_list_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
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
