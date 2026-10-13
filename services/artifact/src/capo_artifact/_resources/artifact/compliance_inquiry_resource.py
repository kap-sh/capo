from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_artifact._auth._signers
import capo_artifact._auth._sigv4
from capo_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_artifact.types.create_compliance_inquiry_request
    import capo_artifact.types.create_compliance_inquiry_response
    import capo_artifact.types.export_compliance_inquiry_request
    import capo_artifact.types.export_compliance_inquiry_response
    import capo_artifact.types.feedback_comment_attribute
    import capo_artifact.types.feedback_rating
    import capo_artifact.types.feedback_reason_code_list
    import capo_artifact.types.get_compliance_inquiry_metadata_request
    import capo_artifact.types.get_compliance_inquiry_metadata_response
    import capo_artifact.types.idempotent_client_token
    import capo_artifact.types.inquiry_content
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.inquiry_name
    import capo_artifact.types.inquiry_summary
    import capo_artifact.types.inquiry_support_mode
    import capo_artifact.types.list_compliance_inquiries_request
    import capo_artifact.types.list_compliance_inquiries_response
    import capo_artifact.types.list_compliance_inquiry_queries_request
    import capo_artifact.types.list_compliance_inquiry_queries_response
    import capo_artifact.types.max_results_attribute
    import capo_artifact.types.next_token_attribute
    import capo_artifact.types.put_compliance_inquiry_feedback_request
    import capo_artifact.types.put_compliance_inquiry_feedback_response
    import capo_artifact.types.query_identifiers_list
    import capo_artifact.types.query_summary
    import capo_artifact.types.tags_map
    from capo_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from capo_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class ComplianceInquiryResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def create_compliance_inquiry(
        self,
        name: "capo_artifact.types.inquiry_name.InquiryName",
        inquiry_content: "capo_artifact.types.inquiry_content.InquiryContent",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
        support_mode: Optional[
            "capo_artifact.types.inquiry_support_mode.InquirySupportMode"
        ] = None,
        tags: Optional["capo_artifact.types.tags_map.TagsMap"] = None,
    ) -> "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse":
        """<p>Create a new compliance inquiry.</p>

        Args:
            name: <p>Title of the inquiry.</p>
            inquiry_content: <p>Content for creating a compliance inquiry - either a single query or file content.</p>
            client_token: <p>Idempotency token for the request.</p>
            support_mode: <p>Support mode for inquiry processing. Only supported for file upload mode. Defaults to AI_ONLY if not specified.</p>
            tags: <p>Tags to associate with the compliance inquiry resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateComplianceInquiry operation
            Creates a compliance inquiry with a single text query.

            >>> client.create_compliance_inquiry(name='My Compliance Inquiry', inquiry_content={'query': 'Is my workload compliant with SOC 2?'}, client_token='unique-client-token-1234', support_mode='AI_ONLY')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.create_compliance_inquiry

            output, http_response = (
                capo_artifact._operations.artifact.create_compliance_inquiry.create_compliance_inquiry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest",
        ) -> dict[str, Any]:
            import capo_artifact.types.create_compliance_inquiry_request

            return (
                capo_artifact.types.create_compliance_inquiry_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateComplianceInquiry", redact_input=_redact_input),
        )
        input_: capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest = {
            "name": name,
            "inquiry_content": inquiry_content,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if support_mode is not None:
            input_["support_mode"] = support_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_compliance_inquiry(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        query_identifiers: Optional[
            "capo_artifact.types.query_identifiers_list.QueryIdentifiersList"
        ] = None,
        include_citations: Optional[bool] = None,
    ) -> "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse":
        """<p>Export a compliance inquiry report.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            query_identifiers: <p>List of query identifiers to include in the export.</p>
            include_citations: <p>When true, include citations in the exported document.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ExportComplianceInquiry operation
            Exports a compliance inquiry report.

            >>> client.export_compliance_inquiry(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', query_identifiers=[1, 2], include_citations=True)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.export_compliance_inquiry

            output, http_response = (
                capo_artifact._operations.artifact.export_compliance_inquiry.export_compliance_inquiry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse",
        ) -> dict[str, Any]:
            import capo_artifact.types.export_compliance_inquiry_response

            return (
                capo_artifact.types.export_compliance_inquiry_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ExportComplianceInquiry", redact_output=_redact_output),
        )
        input_: capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }
        if query_identifiers is not None:
            input_["query_identifiers"] = query_identifiers
        if include_citations is not None:
            input_["include_citations"] = include_citations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compliance_inquiry_metadata(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
    ) -> "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse":
        """<p>Get the metadata for a single compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetComplianceInquiryMetadata operation
            Gets metadata for a compliance inquiry.

            >>> client.get_compliance_inquiry_metadata(compliance_inquiry_id='compliance-inquiry-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_compliance_inquiry_metadata

            output, http_response = (
                capo_artifact._operations.artifact.get_compliance_inquiry_metadata.get_compliance_inquiry_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetComplianceInquiryMetadata")
        )
        input_: capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_compliance_inquiries(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse":
        """<p>List available compliance inquiries.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiries operation
            Lists all compliance inquiries.

            >>> client.list_compliance_inquiries(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiries

            output, http_response = (
                capo_artifact._operations.artifact.list_compliance_inquiries.list_compliance_inquiries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComplianceInquiries")
        )
        input_: capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest = {}
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

    def list_compliance_inquiry_queries(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse":
        """<p>List queries within a compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiryQueries operation
            Lists queries within a compliance inquiry.

            >>> client.list_compliance_inquiry_queries(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiry_queries

            output, http_response = (
                capo_artifact._operations.artifact.list_compliance_inquiry_queries.list_compliance_inquiry_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComplianceInquiryQueries")
        )
        input_: capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
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

    def put_compliance_inquiry_feedback(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        rating: "capo_artifact.types.feedback_rating.FeedbackRating",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        query_identifier: Optional[int] = None,
        response_revision_id: Optional[int] = None,
        reason_codes: Optional[
            "capo_artifact.types.feedback_reason_code_list.FeedbackReasonCodeList"
        ] = None,
        comment: Optional[
            "capo_artifact.types.feedback_comment_attribute.FeedbackCommentAttribute"
        ] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
    ) -> "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse":
        """<p>Submits feedback on a compliance inquiry response.</p>

        Args:
            compliance_inquiry_id: <p>The unique identifier for the compliance inquiry.</p>
            query_identifier: <p>The sequential identifier of the query to provide feedback on.</p>
            rating: <p>The rating for the feedback. Valid values are THUMBS_UP and THUMBS_DOWN.</p>
            response_revision_id: <p>The response revision ID. Use this value to prevent submitting feedback on a stale response.</p>
            reason_codes: <p>The reason codes that describe why you rated the response. Valid values are OTHER, PARTIAL_RESPONSE, and IRRELEVANT_RESPONSE.</p>
            comment: <p>An optional comment for the feedback.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse"
        ]:
            import capo_artifact._operations.artifact.put_compliance_inquiry_feedback

            output, http_response = (
                capo_artifact._operations.artifact.put_compliance_inquiry_feedback.put_compliance_inquiry_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest",
        ) -> dict[str, Any]:
            import capo_artifact.types.put_compliance_inquiry_feedback_request

            return capo_artifact.types.put_compliance_inquiry_feedback_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "PutComplianceInquiryFeedback", redact_input=_redact_input
            ),
        )
        input_: capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest = {
            "compliance_inquiry_id": compliance_inquiry_id,
            "rating": rating,
        }
        if query_identifier is not None:
            input_["query_identifier"] = query_identifier
        if response_revision_id is not None:
            input_["response_revision_id"] = response_revision_id
        if reason_codes is not None:
            input_["reason_codes"] = reason_codes
        if comment is not None:
            input_["comment"] = comment
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


class AsyncComplianceInquiryResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def create_compliance_inquiry(
        self,
        name: "capo_artifact.types.inquiry_name.InquiryName",
        inquiry_content: "capo_artifact.types.inquiry_content.InquiryContent",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
        support_mode: Optional[
            "capo_artifact.types.inquiry_support_mode.InquirySupportMode"
        ] = None,
        tags: Optional["capo_artifact.types.tags_map.TagsMap"] = None,
    ) -> "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse":
        """<p>Create a new compliance inquiry.</p>

        Args:
            name: <p>Title of the inquiry.</p>
            inquiry_content: <p>Content for creating a compliance inquiry - either a single query or file content.</p>
            client_token: <p>Idempotency token for the request.</p>
            support_mode: <p>Support mode for inquiry processing. Only supported for file upload mode. Defaults to AI_ONLY if not specified.</p>
            tags: <p>Tags to associate with the compliance inquiry resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateComplianceInquiry operation
            Creates a compliance inquiry with a single text query.

            >>> await client.create_compliance_inquiry(name='My Compliance Inquiry', inquiry_content={'query': 'Is my workload compliant with SOC 2?'}, client_token='unique-client-token-1234', support_mode='AI_ONLY')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.create_compliance_inquiry

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.create_compliance_inquiry.async_create_compliance_inquiry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest",
        ) -> dict[str, Any]:
            import capo_artifact.types.create_compliance_inquiry_request

            return (
                capo_artifact.types.create_compliance_inquiry_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateComplianceInquiry", redact_input=_redact_input),
        )
        input_: capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest = {
            "name": name,
            "inquiry_content": inquiry_content,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if support_mode is not None:
            input_["support_mode"] = support_mode
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_compliance_inquiry(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        query_identifiers: Optional[
            "capo_artifact.types.query_identifiers_list.QueryIdentifiersList"
        ] = None,
        include_citations: Optional[bool] = None,
    ) -> "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse":
        """<p>Export a compliance inquiry report.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            query_identifiers: <p>List of query identifiers to include in the export.</p>
            include_citations: <p>When true, include citations in the exported document.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ExportComplianceInquiry operation
            Exports a compliance inquiry report.

            >>> await client.export_compliance_inquiry(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', query_identifiers=[1, 2], include_citations=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.export_compliance_inquiry

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.export_compliance_inquiry.async_export_compliance_inquiry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse",
        ) -> dict[str, Any]:
            import capo_artifact.types.export_compliance_inquiry_response

            return (
                capo_artifact.types.export_compliance_inquiry_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ExportComplianceInquiry", redact_output=_redact_output),
        )
        input_: capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }
        if query_identifiers is not None:
            input_["query_identifiers"] = query_identifiers
        if include_citations is not None:
            input_["include_citations"] = include_citations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_compliance_inquiry_metadata(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
    ) -> "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse":
        """<p>Get the metadata for a single compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetComplianceInquiryMetadata operation
            Gets metadata for a compliance inquiry.

            >>> await client.get_compliance_inquiry_metadata(compliance_inquiry_id='compliance-inquiry-abcdef0123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_compliance_inquiry_metadata

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.get_compliance_inquiry_metadata.async_get_compliance_inquiry_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetComplianceInquiryMetadata")
        )
        input_: capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_compliance_inquiries(
        self,
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse":
        """<p>List available compliance inquiries.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiries operation
            Lists all compliance inquiries.

            >>> await client.list_compliance_inquiries(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiries

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.list_compliance_inquiries.async_list_compliance_inquiries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComplianceInquiries")
        )
        input_: capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest = {}
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

    async def list_compliance_inquiry_queries(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse":
        """<p>List queries within a compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiryQueries operation
            Lists queries within a compliance inquiry.

            >>> await client.list_compliance_inquiry_queries(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiry_queries

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.list_compliance_inquiry_queries.async_list_compliance_inquiry_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComplianceInquiryQueries")
        )
        input_: capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
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

    async def put_compliance_inquiry_feedback(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        rating: "capo_artifact.types.feedback_rating.FeedbackRating",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        query_identifier: Optional[int] = None,
        response_revision_id: Optional[int] = None,
        reason_codes: Optional[
            "capo_artifact.types.feedback_reason_code_list.FeedbackReasonCodeList"
        ] = None,
        comment: Optional[
            "capo_artifact.types.feedback_comment_attribute.FeedbackCommentAttribute"
        ] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
    ) -> "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse":
        """<p>Submits feedback on a compliance inquiry response.</p>

        Args:
            compliance_inquiry_id: <p>The unique identifier for the compliance inquiry.</p>
            query_identifier: <p>The sequential identifier of the query to provide feedback on.</p>
            rating: <p>The rating for the feedback. Valid values are THUMBS_UP and THUMBS_DOWN.</p>
            response_revision_id: <p>The response revision ID. Use this value to prevent submitting feedback on a stale response.</p>
            reason_codes: <p>The reason codes that describe why you rated the response. Valid values are OTHER, PARTIAL_RESPONSE, and IRRELEVANT_RESPONSE.</p>
            comment: <p>An optional comment for the feedback.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse"
        ]:
            import capo_artifact._operations.artifact.put_compliance_inquiry_feedback

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.put_compliance_inquiry_feedback.async_put_compliance_inquiry_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest",
        ) -> dict[str, Any]:
            import capo_artifact.types.put_compliance_inquiry_feedback_request

            return capo_artifact.types.put_compliance_inquiry_feedback_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "PutComplianceInquiryFeedback", redact_input=_redact_input
            ),
        )
        input_: capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest = {
            "compliance_inquiry_id": compliance_inquiry_id,
            "rating": rating,
        }
        if query_identifier is not None:
            input_["query_identifier"] = query_identifier
        if response_revision_id is not None:
            input_["response_revision_id"] = response_revision_id
        if reason_codes is not None:
            input_["reason_codes"] = reason_codes
        if comment is not None:
            input_["comment"] = comment
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
