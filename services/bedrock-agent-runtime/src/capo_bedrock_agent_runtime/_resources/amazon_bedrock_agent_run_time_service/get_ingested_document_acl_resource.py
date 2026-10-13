from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.get_ingested_document_acl_request
    import capo_bedrock_agent_runtime.types.get_ingested_document_acl_response
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class GetIngestedDocumentAclResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def get_ingested_document_acl(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse":
        """<p>Retrieves the ingested access control list (ACL) for a specific document in a knowledge base. Use this operation to inspect the allow and deny lists that were ingested for a document to troubleshoot access control issues. To use this operation, you must have the <code>bedrock:GetIngestedDocumentAcl</code> permission.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve the ingested access control list (ACL) for.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl.get_ingested_document_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_ingested_document_acl_response

            return capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetIngestedDocumentAcl", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGetIngestedDocumentAclResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def get_ingested_document_acl(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse":
        """<p>Retrieves the ingested access control list (ACL) for a specific document in a knowledge base. Use this operation to inspect the allow and deny lists that were ingested for a document to troubleshoot access control issues. To use this operation, you must have the <code>bedrock:GetIngestedDocumentAcl</code> permission.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve the ingested access control list (ACL) for.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl.async_get_ingested_document_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_ingested_document_acl_response

            return capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetIngestedDocumentAcl", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
