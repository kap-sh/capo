from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_connectcases._auth._signers
import capo_connectcases._auth._sigv4
from capo_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_identifier_list
    import capo_connectcases.types.batch_create_related_item_request
    import capo_connectcases.types.batch_create_related_item_response
    import capo_connectcases.types.batch_update_case_identifier_list
    import capo_connectcases.types.batch_update_case_request
    import capo_connectcases.types.batch_update_case_response
    import capo_connectcases.types.case_filter
    import capo_connectcases.types.case_id
    import capo_connectcases.types.case_id_list
    import capo_connectcases.types.case_status
    import capo_connectcases.types.case_title
    import capo_connectcases.types.contact_arn
    import capo_connectcases.types.create_case_request
    import capo_connectcases.types.create_case_response
    import capo_connectcases.types.customer_profile_arn
    import capo_connectcases.types.delete_case_request
    import capo_connectcases.types.delete_case_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_identifier_list
    import capo_connectcases.types.field_value_input_list
    import capo_connectcases.types.field_value_list
    import capo_connectcases.types.fields_configuration_list
    import capo_connectcases.types.get_case_audit_events_request
    import capo_connectcases.types.get_case_audit_events_response
    import capo_connectcases.types.get_case_request
    import capo_connectcases.types.get_case_response
    import capo_connectcases.types.get_merge_cases_status_request
    import capo_connectcases.types.get_merge_cases_status_response
    import capo_connectcases.types.list_cases_for_contact_request
    import capo_connectcases.types.list_cases_for_contact_response
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.next_token
    import capo_connectcases.types.related_item_input_content
    import capo_connectcases.types.related_items_configuration
    import capo_connectcases.types.search_cases_request
    import capo_connectcases.types.search_cases_response
    import capo_connectcases.types.search_cases_response_item
    import capo_connectcases.types.sort_list
    import capo_connectcases.types.start_merge_cases_request
    import capo_connectcases.types.start_merge_cases_response
    import capo_connectcases.types.template_id
    import capo_connectcases.types.update_case_request
    import capo_connectcases.types.update_case_response
    import capo_connectcases.types.user_union
    from capo_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from capo_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Case:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        client_token: Optional[str] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        tags: Optional["capo_connectcases.types.mutable_tags.MutableTags"] = None,
    ) -> "capo_connectcases.types.create_case_response.CreateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following field is always required when creating a case:</p> <ul> <li> <p> <code>title</code> </p> </li> </ul> <p>The following field may be required depending on the template configuration:</p> <ul> <li> <p> <code>customer_id</code> - Required only if the template's <code>requiredFields</code> list includes <code>customer_id</code>. When required, provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account_ID:domains/your_profiles_domain_name/profiles/profile_ID</code>. When not required, the field is optional and can be omitted, added, changed, or removed after case creation.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.create_case_request.CreateCaseRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.create_case.create_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.create_case_request.CreateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.create_case_request

            return capo_connectcases.types.create_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCase", redact_input=_redact_input)
        )
        input_: capo_connectcases.types.create_case_request.CreateCaseRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
            "fields": fields,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if performed_by is not None:
            input_["performed_by"] = performed_by
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
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_response.GetCaseResponse":
        """<p>Returns information about a specific case if it exists. </p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_case_request.GetCaseRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_case_response.GetCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_case.get_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCase")
        )
        input_: capo_connectcases.types.get_case_request.GetCaseRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
            "fields": fields,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> "capo_connectcases.types.update_case_response.UpdateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input.</p> <p>If the case is the secondary case of a merge that is running, the request fails with a <code>ConflictException</code>. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.update_case_request.UpdateCaseRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.update_case.update_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.update_case_request.UpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.update_case_request

            return capo_connectcases.types.update_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCase", redact_input=_redact_input)
        )
        input_: capo_connectcases.types.update_case_request.UpdateCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "fields": fields,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_response.DeleteCaseResponse":
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <p>You can't delete a case while it's part of a merge that is running, as either the primary or the secondary case. The request fails with a <code>ConflictException</code>. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>.</p> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.delete_case_request.DeleteCaseRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.delete_case_response.DeleteCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.delete_case.delete_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCase")
        )
        input_: capo_connectcases.types.delete_case_request.DeleteCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_case_audit_events(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse":
        """<p>Returns the audit history about a specific case if it exists.</p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain.</p>
            max_results: <p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_audit_events

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_case_audit_events.get_case_audit_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse",
        ) -> dict[str, Any]:
            import capo_connectcases.types.get_case_audit_events_response

            return (
                capo_connectcases.types.get_case_audit_events_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCaseAuditEvents", redact_output=_redact_output),
        )
        input_: capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
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

    def get_merge_cases_status(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_merge_cases_status_response.GetMergeCasesStatusResponse":
        """<p>Returns the merge status of a case. Use this operation to track a merge that you started with <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>, or to check whether a case is part of a merge before you modify it.</p> <p>The operation returns the following, depending on the case:</p> <ul> <li> <p>For the primary case or the secondary case of a merge that is running, it returns <code>IN_PROGRESS</code>.</p> </li> <li> <p>For a case that was merged into another case as the secondary case, it returns <code>COMPLETED</code>.</p> </li> <li> <p>For any other case, it returns a <code>ResourceNotFoundException</code>. This includes the primary case after its merge finishes.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>The unique identifier of the case. This can be the primary case or the secondary case of a merge.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_merge_cases_status_request.GetMergeCasesStatusRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_merge_cases_status_response.GetMergeCasesStatusResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_merge_cases_status

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_merge_cases_status.get_merge_cases_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMergeCasesStatus")
        )
        input_: capo_connectcases.types.get_merge_cases_status_request.GetMergeCasesStatusRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_merge_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        secondary_case_ids: "capo_connectcases.types.case_id_list.CaseIdList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        fields_configuration: Optional[
            "capo_connectcases.types.fields_configuration_list.FieldsConfigurationList"
        ] = None,
        related_items_configuration: Optional[
            "capo_connectcases.types.related_items_configuration.RelatedItemsConfiguration"
        ] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> "capo_connectcases.types.start_merge_cases_response.StartMergeCasesResponse":
        """<p>Merges a secondary case into a primary case. The primary case, which you specify in the request URI, remains active. Both cases must belong to the same domain.</p> <p>The merge runs asynchronously. To track its progress, call <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetMergeCasesStatus.html">GetMergeCasesStatus</a>. When the merge finishes, the selected field values and related items from the secondary case are on the primary case, the two cases are linked, and the secondary case is closed. Both cases record the merge in their audit history. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseAuditEvents.html">GetCaseAuditEvents</a>.</p> <p> <b>Important things to know</b> </p> <ul> <li> <p>Both cases must have the same customer, or at least one of them must have no customer.</p> </li> <li> <p>While the merge runs, you can't modify the secondary case or its related items, and you can't delete the primary case. These requests return a <code>ConflictException</code>.</p> </li> <li> <p>After the merge, the secondary case can be reopened, updated, and deleted, but it can't be merged again.</p> </li> </ul> <p>The request fails with a <code>ValidationException</code>, and no merge starts, if:</p> <ul> <li> <p>The primary case and the secondary case are the same case.</p> </li> <li> <p>Either case is closed.</p> </li> <li> <p>Both cases have a customer, and the customers are different.</p> </li> <li> <p> <code>fieldsConfiguration</code> selects a field that can't be merged, or a field that the secondary case doesn't have.</p> </li> <li> <p>After the merge, the primary case would have more than 500 field values, or would exceed the maximum case size.</p> </li> </ul> <p>The request fails with a <code>ServiceQuotaExceededException</code> if, after the merge, either case would exceed the quota for related items per case. For the primary case, the count is its existing related items, plus the related items moved from the secondary case, plus the new case link. See <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas">Connect Customer Cases quotas</a>.</p> <p>The request fails with a <code>ConflictException</code> if either case is already part of a merge that is running, or was previously merged into another case as the secondary case.</p> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>The unique identifier of the primary case. The primary case remains active and receives the merged field values and related items. The cases can use different templates, and the primary case keeps its template.</p>
            secondary_case_ids: <p>The unique identifier of the secondary case to merge into the primary case. The secondary case is closed when the merge finishes. Specify exactly one case ID.</p>
            fields_configuration: <p>The fields whose values to take from the secondary case. You can only merge custom fields and the following system fields: <code>assigned_queue</code>, <code>assigned_user</code>, <code>summary</code>, and <code>case_reason</code>. If you select any other system field, the request fails with a <code>ValidationException</code>.</p> <p>For each field that can be merged, the merge works as follows:</p> <ul> <li> <p>If you select the field, the primary case gets the secondary case's value. If the secondary case's value is empty, the primary case's value is cleared.</p> </li> <li> <p>If you don't select the field and the primary case has a value for it, the primary case keeps its value.</p> </li> <li> <p>If you don't select the field and the primary case doesn't have the field, or its value is empty, the primary case gets the secondary case's value. This applies even when the field isn't on the primary case's template.</p> </li> </ul> <p>Field values are read from both cases when the merge runs, so changes that you make to the primary case after you start the merge are taken into account.</p> <p>Specify at most one entry, and set its <code>sourceCaseId</code> to the secondary case ID.</p>
            related_items_configuration: <p>The types of related items to move from the secondary case to the primary case. Related items of a type that you don't select, or set to <code>false</code>, stay on the closed secondary case. If you omit this parameter, no related items are moved.</p> <p>File, SLA, and work plan related items are never moved. They stay on the secondary case.</p>
            performed_by: <p>The user who performed the merge. If you provide <code>userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of that user.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Connect Customer Service Quotas</a> in the <i>Connect Customer Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.start_merge_cases_response.StartMergeCasesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.start_merge_cases

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.start_merge_cases.start_merge_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.start_merge_cases_request

            return capo_connectcases.types.start_merge_cases_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartMergeCases", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "secondary_case_ids": secondary_case_ids,
        }
        if fields_configuration is not None:
            input_["fields_configuration"] = fields_configuration
        if related_items_configuration is not None:
            input_["related_items_configuration"] = related_items_configuration
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_create_related_item(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        content: "capo_connectcases.types.related_item_input_content.RelatedItemInputContent",
        cases: "capo_connectcases.types.batch_create_related_item_identifier_list.BatchCreateRelatedItemIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_connectcases.types.batch_create_related_item_response.BatchCreateRelatedItemResponse":
        """<p>Creates a comment and associates it with multiple cases in a single request. All cases must belong to the same domain. This operation supports only the Comment related item type.</p> <p>Each case is processed independently. If some cases fail, the remaining cases still receive the related item. To determine whether individual items failed, inspect the <code>failedItems</code> array in the response.</p> <p>The entire request fails, and no related items are created, in the following cases:</p> <ul> <li> <p>The specified domain doesn't exist.</p> </li> <li> <p>A reference ID doesn't match any case in the domain.</p> </li> <li> <p>The request contains duplicate case IDs.</p> </li> <li> <p>The content isn't comment content.</p> </li> </ul> <note> <p>This operation uses the same IAM action as <a href="https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateRelatedItem.html">CreateRelatedItem</a> (<code>cases:CreateRelatedItem</code>). You can use the <code>cases:IsBatchAction</code> condition key in IAM policies to allow or deny batch operations independently from single-case operations.</p> </note> <note> <p>If you provide a value for <code>performedBy.userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </note> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            content: <p>The content of the related item to be created. The same content is applied to every case in the request. Only comment content is supported for batch creation.</p>
            cases: <p>The list of cases to associate the related item with. All cases must belong to the same domain.</p>
            performed_by: <p>The entity that created the related item.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Connect Customer Service Quotas</a> in the <i>Connect Customer Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.batch_create_related_item_response.BatchCreateRelatedItemResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_create_related_item

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.batch_create_related_item.batch_create_related_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.batch_create_related_item_request

            return capo_connectcases.types.batch_create_related_item_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchCreateRelatedItem", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest = {
            "domain_id": domain_id,
            "content": content,
            "cases": cases,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by
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

    def batch_update_case(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        cases: "capo_connectcases.types.batch_update_case_identifier_list.BatchUpdateCaseIdentifierList",
        fields: "capo_connectcases.types.field_value_input_list.FieldValueInputList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        title: Optional["capo_connectcases.types.case_title.CaseTitle"] = None,
        status: Optional["capo_connectcases.types.case_status.CaseStatus"] = None,
        customer_id: Optional[
            "capo_connectcases.types.customer_profile_arn.CustomerProfileArn"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_connectcases.types.batch_update_case_response.BatchUpdateCaseResponse":
        """<p>Updates fields on multiple cases in a single request. All cases must belong to the same domain. Set the title, status, and customer ID through the top-level <code>title</code>, <code>status</code>, and <code>customerId</code> parameters, and set other fields through the <code>fields</code> array.</p> <p>Each case is processed independently. If some cases fail, the remaining cases are still updated. To determine whether individual cases failed, inspect the <code>failedCases</code> array in the response.</p> <p>The entire request fails, and no cases are updated, in the following cases:</p> <ul> <li> <p>The specified domain doesn't exist.</p> </li> <li> <p>A reference ID doesn't match any case in the domain.</p> </li> <li> <p>The request contains duplicate case IDs.</p> </li> <li> <p>The request doesn't specify any update. Provide at least one entry in <code>fields</code>, or a <code>title</code>, <code>status</code>, or <code>customerId</code>.</p> </li> <li> <p>A field identifier in <code>fields</code> doesn't resolve to a field in the domain, for example, an unknown field name.</p> </li> <li> <p>A field name contains a pipe (<code>|</code>) or comma (<code>,</code>) character.</p> </li> <li> <p> <code>fields</code> includes <code>title</code>, <code>status</code>, or <code>customerId</code>.</p> </li> </ul> <note> <p>This operation uses the same IAM action as <a href="https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCase.html">UpdateCase</a> (<code>cases:UpdateCase</code>). You can use the <code>cases:IsBatchAction</code> condition key in IAM policies to allow or deny batch operations independently from single-case operations.</p> </note> <note> <p>If you provide a value for <code>performedBy.userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </note> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            cases: <p>The list of cases to update. All cases must belong to the same domain.</p>
            fields: <p>An array of objects, each with a <code>fieldIdentifier</code> and a <code>value</code>. You can identify each field by its ID or by its name; identifying a field by name is supported only in <code>BatchUpdateCase</code>. The same field values are applied to every case in the request. This field must be present, but can be an empty list when you provide the top-level <code>title</code>, <code>status</code>, or <code>customerId</code> parameters. Do not include <code>title</code>, <code>status</code>, or <code>customerId</code> in this list; set those values only through their top-level parameters. Duplicating them in <code>fields</code> results in a validation error.</p>
            performed_by: <p>The entity that performed the action.</p>
            title: <p>The title to apply to all cases in the request.</p>
            status: <p>The status to apply to all cases in the request.</p>
            customer_id: <p>The ARN of the customer profile to associate with all cases in the request.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.batch_update_case_response.BatchUpdateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_update_case

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.batch_update_case.batch_update_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.batch_update_case_request

            return capo_connectcases.types.batch_update_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchUpdateCase", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest = {
            "domain_id": domain_id,
            "cases": cases,
            "fields": fields,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by
        if title is not None:
            input_["title"] = title
        if status is not None:
            input_["status"] = status
        if customer_id is not None:
            input_["customer_id"] = customer_id
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

    def list_cases_for_contact(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        contact_arn: "capo_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse":
        """<p>Lists cases for a given contact.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            contact_arn: <p>A unique identifier of a contact in Connect Customer.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact.list_cases_for_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCasesForContact")
        )
        input_: capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest = {
            "domain_id": domain_id,
            "contact_arn": contact_arn,
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

    def search_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["capo_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["capo_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "capo_connectcases.types.search_cases_response.SearchCasesResponse":
        """<p>Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.</p> <note> <p>For <code>customer_id</code> you must provide the full customer profile ARN in this format: <code> arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID</code>. </p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            search_term: <p>A word or phrase used to perform a quick search.</p>
            filter: <p>A list of filter objects.</p>
            sorts: <p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>
            fields: <p>The list of field identifiers to be returned as part of the response.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.search_cases_request.SearchCasesRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.search_cases_response.SearchCasesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_cases

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.search_cases.search_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchCases")
        )
        input_: capo_connectcases.types.search_cases_request.SearchCasesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if search_term is not None:
            input_["search_term"] = search_term
        if filter is not None:
            input_["filter"] = filter
        if sorts is not None:
            input_["sorts"] = sorts
        if fields is not None:
            input_["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCase:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        client_token: Optional[str] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        tags: Optional["capo_connectcases.types.mutable_tags.MutableTags"] = None,
    ) -> "capo_connectcases.types.create_case_response.CreateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following field is always required when creating a case:</p> <ul> <li> <p> <code>title</code> </p> </li> </ul> <p>The following field may be required depending on the template configuration:</p> <ul> <li> <p> <code>customer_id</code> - Required only if the template's <code>requiredFields</code> list includes <code>customer_id</code>. When required, provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account_ID:domains/your_profiles_domain_name/profiles/profile_ID</code>. When not required, the field is optional and can be omitted, added, changed, or removed after case creation.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.create_case_request.CreateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.create_case_request

            return capo_connectcases.types.create_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCase", redact_input=_redact_input)
        )
        input_: capo_connectcases.types.create_case_request.CreateCaseRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
            "fields": fields,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if performed_by is not None:
            input_["performed_by"] = performed_by
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
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_response.GetCaseResponse":
        """<p>Returns information about a specific case if it exists. </p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_request.GetCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_response.GetCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case.async_get_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCase")
        )
        input_: capo_connectcases.types.get_case_request.GetCaseRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
            "fields": fields,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> "capo_connectcases.types.update_case_response.UpdateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input.</p> <p>If the case is the secondary case of a merge that is running, the request fails with a <code>ConflictException</code>. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_case_request.UpdateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_case.async_update_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.update_case_request.UpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.update_case_request

            return capo_connectcases.types.update_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCase", redact_input=_redact_input)
        )
        input_: capo_connectcases.types.update_case_request.UpdateCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "fields": fields,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_response.DeleteCaseResponse":
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <p>You can't delete a case while it's part of a merge that is running, as either the primary or the secondary case. The request fails with a <code>ConflictException</code>. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>.</p> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_case_request.DeleteCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_case_response.DeleteCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_case.async_delete_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCase")
        )
        input_: capo_connectcases.types.delete_case_request.DeleteCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_case_audit_events(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse":
        """<p>Returns the audit history about a specific case if it exists.</p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain.</p>
            max_results: <p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_audit_events

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case_audit_events.async_get_case_audit_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse",
        ) -> dict[str, Any]:
            import capo_connectcases.types.get_case_audit_events_response

            return (
                capo_connectcases.types.get_case_audit_events_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCaseAuditEvents", redact_output=_redact_output),
        )
        input_: capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
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

    async def get_merge_cases_status(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_merge_cases_status_response.GetMergeCasesStatusResponse":
        """<p>Returns the merge status of a case. Use this operation to track a merge that you started with <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html">StartMergeCases</a>, or to check whether a case is part of a merge before you modify it.</p> <p>The operation returns the following, depending on the case:</p> <ul> <li> <p>For the primary case or the secondary case of a merge that is running, it returns <code>IN_PROGRESS</code>.</p> </li> <li> <p>For a case that was merged into another case as the secondary case, it returns <code>COMPLETED</code>.</p> </li> <li> <p>For any other case, it returns a <code>ResourceNotFoundException</code>. This includes the primary case after its merge finishes.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>The unique identifier of the case. This can be the primary case or the secondary case of a merge.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_merge_cases_status_request.GetMergeCasesStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_merge_cases_status_response.GetMergeCasesStatusResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_merge_cases_status

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_merge_cases_status.async_get_merge_cases_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMergeCasesStatus")
        )
        input_: capo_connectcases.types.get_merge_cases_status_request.GetMergeCasesStatusRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_merge_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        secondary_case_ids: "capo_connectcases.types.case_id_list.CaseIdList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        fields_configuration: Optional[
            "capo_connectcases.types.fields_configuration_list.FieldsConfigurationList"
        ] = None,
        related_items_configuration: Optional[
            "capo_connectcases.types.related_items_configuration.RelatedItemsConfiguration"
        ] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> "capo_connectcases.types.start_merge_cases_response.StartMergeCasesResponse":
        """<p>Merges a secondary case into a primary case. The primary case, which you specify in the request URI, remains active. Both cases must belong to the same domain.</p> <p>The merge runs asynchronously. To track its progress, call <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetMergeCasesStatus.html">GetMergeCasesStatus</a>. When the merge finishes, the selected field values and related items from the secondary case are on the primary case, the two cases are linked, and the secondary case is closed. Both cases record the merge in their audit history. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseAuditEvents.html">GetCaseAuditEvents</a>.</p> <p> <b>Important things to know</b> </p> <ul> <li> <p>Both cases must have the same customer, or at least one of them must have no customer.</p> </li> <li> <p>While the merge runs, you can't modify the secondary case or its related items, and you can't delete the primary case. These requests return a <code>ConflictException</code>.</p> </li> <li> <p>After the merge, the secondary case can be reopened, updated, and deleted, but it can't be merged again.</p> </li> </ul> <p>The request fails with a <code>ValidationException</code>, and no merge starts, if:</p> <ul> <li> <p>The primary case and the secondary case are the same case.</p> </li> <li> <p>Either case is closed.</p> </li> <li> <p>Both cases have a customer, and the customers are different.</p> </li> <li> <p> <code>fieldsConfiguration</code> selects a field that can't be merged, or a field that the secondary case doesn't have.</p> </li> <li> <p>After the merge, the primary case would have more than 500 field values, or would exceed the maximum case size.</p> </li> </ul> <p>The request fails with a <code>ServiceQuotaExceededException</code> if, after the merge, either case would exceed the quota for related items per case. For the primary case, the count is its existing related items, plus the related items moved from the secondary case, plus the new case link. See <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas">Connect Customer Cases quotas</a>.</p> <p>The request fails with a <code>ConflictException</code> if either case is already part of a merge that is running, or was previously merged into another case as the secondary case.</p> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>The unique identifier of the primary case. The primary case remains active and receives the merged field values and related items. The cases can use different templates, and the primary case keeps its template.</p>
            secondary_case_ids: <p>The unique identifier of the secondary case to merge into the primary case. The secondary case is closed when the merge finishes. Specify exactly one case ID.</p>
            fields_configuration: <p>The fields whose values to take from the secondary case. You can only merge custom fields and the following system fields: <code>assigned_queue</code>, <code>assigned_user</code>, <code>summary</code>, and <code>case_reason</code>. If you select any other system field, the request fails with a <code>ValidationException</code>.</p> <p>For each field that can be merged, the merge works as follows:</p> <ul> <li> <p>If you select the field, the primary case gets the secondary case's value. If the secondary case's value is empty, the primary case's value is cleared.</p> </li> <li> <p>If you don't select the field and the primary case has a value for it, the primary case keeps its value.</p> </li> <li> <p>If you don't select the field and the primary case doesn't have the field, or its value is empty, the primary case gets the secondary case's value. This applies even when the field isn't on the primary case's template.</p> </li> </ul> <p>Field values are read from both cases when the merge runs, so changes that you make to the primary case after you start the merge are taken into account.</p> <p>Specify at most one entry, and set its <code>sourceCaseId</code> to the secondary case ID.</p>
            related_items_configuration: <p>The types of related items to move from the secondary case to the primary case. Related items of a type that you don't select, or set to <code>false</code>, stay on the closed secondary case. If you omit this parameter, no related items are moved.</p> <p>File, SLA, and work plan related items are never moved. They stay on the secondary case.</p>
            performed_by: <p>The user who performed the merge. If you provide <code>userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of that user.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Connect Customer Service Quotas</a> in the <i>Connect Customer Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.start_merge_cases_response.StartMergeCasesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.start_merge_cases

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.start_merge_cases.async_start_merge_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.start_merge_cases_request

            return capo_connectcases.types.start_merge_cases_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartMergeCases", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.start_merge_cases_request.StartMergeCasesRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "secondary_case_ids": secondary_case_ids,
        }
        if fields_configuration is not None:
            input_["fields_configuration"] = fields_configuration
        if related_items_configuration is not None:
            input_["related_items_configuration"] = related_items_configuration
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_create_related_item(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        content: "capo_connectcases.types.related_item_input_content.RelatedItemInputContent",
        cases: "capo_connectcases.types.batch_create_related_item_identifier_list.BatchCreateRelatedItemIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_connectcases.types.batch_create_related_item_response.BatchCreateRelatedItemResponse":
        """<p>Creates a comment and associates it with multiple cases in a single request. All cases must belong to the same domain. This operation supports only the Comment related item type.</p> <p>Each case is processed independently. If some cases fail, the remaining cases still receive the related item. To determine whether individual items failed, inspect the <code>failedItems</code> array in the response.</p> <p>The entire request fails, and no related items are created, in the following cases:</p> <ul> <li> <p>The specified domain doesn't exist.</p> </li> <li> <p>A reference ID doesn't match any case in the domain.</p> </li> <li> <p>The request contains duplicate case IDs.</p> </li> <li> <p>The content isn't comment content.</p> </li> </ul> <note> <p>This operation uses the same IAM action as <a href="https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateRelatedItem.html">CreateRelatedItem</a> (<code>cases:CreateRelatedItem</code>). You can use the <code>cases:IsBatchAction</code> condition key in IAM policies to allow or deny batch operations independently from single-case operations.</p> </note> <note> <p>If you provide a value for <code>performedBy.userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </note> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            content: <p>The content of the related item to be created. The same content is applied to every case in the request. Only comment content is supported for batch creation.</p>
            cases: <p>The list of cases to associate the related item with. All cases must belong to the same domain.</p>
            performed_by: <p>The entity that created the related item.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Connect Customer Service Quotas</a> in the <i>Connect Customer Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_create_related_item_response.BatchCreateRelatedItemResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_create_related_item

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_create_related_item.async_batch_create_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.batch_create_related_item_request

            return capo_connectcases.types.batch_create_related_item_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchCreateRelatedItem", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.batch_create_related_item_request.BatchCreateRelatedItemRequest = {
            "domain_id": domain_id,
            "content": content,
            "cases": cases,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by
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

    async def batch_update_case(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        cases: "capo_connectcases.types.batch_update_case_identifier_list.BatchUpdateCaseIdentifierList",
        fields: "capo_connectcases.types.field_value_input_list.FieldValueInputList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        title: Optional["capo_connectcases.types.case_title.CaseTitle"] = None,
        status: Optional["capo_connectcases.types.case_status.CaseStatus"] = None,
        customer_id: Optional[
            "capo_connectcases.types.customer_profile_arn.CustomerProfileArn"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_connectcases.types.batch_update_case_response.BatchUpdateCaseResponse":
        """<p>Updates fields on multiple cases in a single request. All cases must belong to the same domain. Set the title, status, and customer ID through the top-level <code>title</code>, <code>status</code>, and <code>customerId</code> parameters, and set other fields through the <code>fields</code> array.</p> <p>Each case is processed independently. If some cases fail, the remaining cases are still updated. To determine whether individual cases failed, inspect the <code>failedCases</code> array in the response.</p> <p>The entire request fails, and no cases are updated, in the following cases:</p> <ul> <li> <p>The specified domain doesn't exist.</p> </li> <li> <p>A reference ID doesn't match any case in the domain.</p> </li> <li> <p>The request contains duplicate case IDs.</p> </li> <li> <p>The request doesn't specify any update. Provide at least one entry in <code>fields</code>, or a <code>title</code>, <code>status</code>, or <code>customerId</code>.</p> </li> <li> <p>A field identifier in <code>fields</code> doesn't resolve to a field in the domain, for example, an unknown field name.</p> </li> <li> <p>A field name contains a pipe (<code>|</code>) or comma (<code>,</code>) character.</p> </li> <li> <p> <code>fields</code> includes <code>title</code>, <code>status</code>, or <code>customerId</code>.</p> </li> </ul> <note> <p>This operation uses the same IAM action as <a href="https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCase.html">UpdateCase</a> (<code>cases:UpdateCase</code>). You can use the <code>cases:IsBatchAction</code> condition key in IAM policies to allow or deny batch operations independently from single-case operations.</p> </note> <note> <p>If you provide a value for <code>performedBy.userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </note> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Connect Customer endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            cases: <p>The list of cases to update. All cases must belong to the same domain.</p>
            fields: <p>An array of objects, each with a <code>fieldIdentifier</code> and a <code>value</code>. You can identify each field by its ID or by its name; identifying a field by name is supported only in <code>BatchUpdateCase</code>. The same field values are applied to every case in the request. This field must be present, but can be an empty list when you provide the top-level <code>title</code>, <code>status</code>, or <code>customerId</code> parameters. Do not include <code>title</code>, <code>status</code>, or <code>customerId</code> in this list; set those values only through their top-level parameters. Duplicating them in <code>fields</code> results in a validation error.</p>
            performed_by: <p>The entity that performed the action.</p>
            title: <p>The title to apply to all cases in the request.</p>
            status: <p>The status to apply to all cases in the request.</p>
            customer_id: <p>The ARN of the customer profile to associate with all cases in the request.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_update_case_response.BatchUpdateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_update_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_update_case.async_batch_update_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_connectcases.types.batch_update_case_request

            return capo_connectcases.types.batch_update_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchUpdateCase", redact_input=_redact_input),
        )
        input_: capo_connectcases.types.batch_update_case_request.BatchUpdateCaseRequest = {
            "domain_id": domain_id,
            "cases": cases,
            "fields": fields,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by
        if title is not None:
            input_["title"] = title
        if status is not None:
            input_["status"] = status
        if customer_id is not None:
            input_["customer_id"] = customer_id
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

    async def list_cases_for_contact(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        contact_arn: "capo_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse":
        """<p>Lists cases for a given contact.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            contact_arn: <p>A unique identifier of a contact in Connect Customer.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact.async_list_cases_for_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCasesForContact")
        )
        input_: capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest = {
            "domain_id": domain_id,
            "contact_arn": contact_arn,
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

    async def search_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["capo_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["capo_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "capo_connectcases.types.search_cases_response.SearchCasesResponse":
        """<p>Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.</p> <note> <p>For <code>customer_id</code> you must provide the full customer profile ARN in this format: <code> arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID</code>. </p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            search_term: <p>A word or phrase used to perform a quick search.</p>
            filter: <p>A list of filter objects.</p>
            sorts: <p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>
            fields: <p>The list of field identifiers to be returned as part of the response.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.search_cases_request.SearchCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.search_cases_response.SearchCasesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_cases

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.search_cases.async_search_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchCases")
        )
        input_: capo_connectcases.types.search_cases_request.SearchCasesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if search_term is not None:
            input_["search_term"] = search_term
        if filter is not None:
            input_["filter"] = filter
        if sorts is not None:
            input_["sorts"] = sorts
        if fields is not None:
            input_["fields"] = fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
