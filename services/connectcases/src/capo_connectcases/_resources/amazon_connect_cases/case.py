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
    import capo_connectcases.types.get_case_audit_events_request
    import capo_connectcases.types.get_case_audit_events_response
    import capo_connectcases.types.get_case_request
    import capo_connectcases.types.get_case_response
    import capo_connectcases.types.list_cases_for_contact_request
    import capo_connectcases.types.list_cases_for_contact_response
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.next_token
    import capo_connectcases.types.related_item_input_content
    import capo_connectcases.types.search_cases_request
    import capo_connectcases.types.search_cases_response
    import capo_connectcases.types.search_cases_response_item
    import capo_connectcases.types.sort_list
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
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
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code>, you must also have the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the user ARN that you provide.</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
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
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
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
