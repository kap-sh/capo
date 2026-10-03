from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_connectcases._auth._signers
import capo_connectcases._auth._sigv4
from capo_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_connectcases.types.case_filter
    import capo_connectcases.types.case_id
    import capo_connectcases.types.contact_arn
    import capo_connectcases.types.create_case_request
    import capo_connectcases.types.create_case_response
    import capo_connectcases.types.delete_case_request
    import capo_connectcases.types.delete_case_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_identifier_list
    import capo_connectcases.types.field_value_list
    import capo_connectcases.types.get_case_audit_events_request
    import capo_connectcases.types.get_case_audit_events_response
    import capo_connectcases.types.get_case_request
    import capo_connectcases.types.get_case_response
    import capo_connectcases.types.list_cases_for_contact_request
    import capo_connectcases.types.list_cases_for_contact_response
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.next_token
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following fields are required when creating a case:</p> <ul> <li> <p> <code>customer_id</code> - You must provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID</code> </p> </li> <li> <p> <code>title</code> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input .</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
            contact_arn: <p>A unique identifier of a contact in Amazon Connect.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following fields are required when creating a case:</p> <ul> <li> <p> <code>customer_id</code> - You must provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID</code> </p> </li> <li> <p> <code>title</code> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input .</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
            contact_arn: <p>A unique identifier of a contact in Amazon Connect.</p>
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
