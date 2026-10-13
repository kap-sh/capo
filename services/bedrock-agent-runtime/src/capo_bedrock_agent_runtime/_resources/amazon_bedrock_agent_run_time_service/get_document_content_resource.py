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
    import capo_bedrock_agent_runtime.types.document_output_format
    import capo_bedrock_agent_runtime.types.get_document_content_request
    import capo_bedrock_agent_runtime.types.get_document_content_response
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.user_context
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class GetDocumentContentResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def get_document_content(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        output_format: Optional[
            "capo_bedrock_agent_runtime.types.document_output_format.DocumentOutputFormat"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse":
        """<p>Retrieves the content of an ingested document from a knowledge base. Returns a pre-signed URL for secure document access.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve content for.</p>
            output_format: <p>The output format for the document content. <code>RAW</code> returns the original file. <code>EXTRACTED</code> returns parsed text as JSON. Defaults to <code>RAW</code>.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content.get_document_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_document_content_request

            return capo_bedrock_agent_runtime.types.get_document_content_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_document_content_response

            return capo_bedrock_agent_runtime.types.get_document_content_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetDocumentContent",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }
        if output_format is not None:
            input_["output_format"] = output_format
        if user_context is not None:
            input_["user_context"] = user_context

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGetDocumentContentResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def get_document_content(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        output_format: Optional[
            "capo_bedrock_agent_runtime.types.document_output_format.DocumentOutputFormat"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse":
        """<p>Retrieves the content of an ingested document from a knowledge base. Returns a pre-signed URL for secure document access.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve content for.</p>
            output_format: <p>The output format for the document content. <code>RAW</code> returns the original file. <code>EXTRACTED</code> returns parsed text as JSON. Defaults to <code>RAW</code>.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content.async_get_document_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_document_content_request

            return capo_bedrock_agent_runtime.types.get_document_content_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.get_document_content_response

            return capo_bedrock_agent_runtime.types.get_document_content_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetDocumentContent",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }
        if output_format is not None:
            input_["output_format"] = output_format
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
