from __future__ import annotations

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
    import capo_connectcases.types.create_domain_request
    import capo_connectcases.types.create_domain_response
    import capo_connectcases.types.delete_domain_request
    import capo_connectcases.types.delete_domain_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.domain_name
    import capo_connectcases.types.event_bridge_configuration
    import capo_connectcases.types.get_case_event_configuration_request
    import capo_connectcases.types.get_case_event_configuration_response
    import capo_connectcases.types.get_domain_request
    import capo_connectcases.types.get_domain_response
    import capo_connectcases.types.list_domains_request
    import capo_connectcases.types.list_domains_response
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token
    import capo_connectcases.types.put_case_event_configuration_request
    import capo_connectcases.types.put_case_event_configuration_response
    import capo_connectcases.types.related_item_filter_list
    import capo_connectcases.types.search_all_related_items_request
    import capo_connectcases.types.search_all_related_items_response
    import capo_connectcases.types.search_all_related_items_response_item
    import capo_connectcases.types.search_all_related_items_sort_list
    from capo_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from capo_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Domain:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_connectcases.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Amazon Connect instance can be associated with only one Cases domain.</p> <important> <p>This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html">CreateIntegrationAssociation</a> API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam">Onboard to Cases</a>.</p> </important>

        Args:
            name: <p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_domain

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_domain_request.CreateDomainRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain if it exists. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_domain_request.GetDomainRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_domain_response.GetDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_domain

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_domain.get_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_domain_request.GetDomainRequest = {
            "domain_id": domain_id
        }

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
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a Cases domain.</p> <note> <p>After deleting your domain you must disassociate the deleted domain from your Amazon Connect instance with another API call before being able to use Cases again with this Amazon Connect instance. See <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html">DeleteIntegrationAssociation</a>.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

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
            req: "OperationRequest[capo_connectcases.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_domain

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
        }

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
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all cases domains in the Amazon Web Services account. Each list item is a condensed summary object of the domain.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_domains

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_domains_request.ListDomainsRequest = {}
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

    def get_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse":
        """<p>Returns the case event publishing configuration.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration.get_case_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest = {
            "domain_id": domain_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        event_bridge: "capo_connectcases.types.event_bridge_configuration.EventBridgeConfiguration",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse":
        """<p>Adds case event publishing configuration. For a complete list of fields you can add to the event message, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html">Create case fields</a> in the <i>Amazon Connect Administrator Guide</i> </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            event_bridge: <p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>

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
            req: "OperationRequest[capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration.put_case_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest = {
            "domain_id": domain_id,
            "event_bridge": event_bridge,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_all_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "capo_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse":
        """<p>Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html">SearchRelatedItems</a> API.</p> <p> <b>Use cases</b> </p> <p>Following are common uses cases for this API:</p> <ul> <li> <p>Find cases with similar issues across the domain. For example, search for all cases containing comments about "product defect" to identify patterns and existing solutions.</p> </li> <li> <p>Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey. </p> </li> <li> <p>Monitor SLA compliance across cases. For example, search for all cases with "Active" SLA status to prioritize remediation efforts.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html">GetCase</a> API for each returned case ID. </p> </li> <li> <p>This API searches across related items content, not case fields. Use the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html">SearchCases</a> API to search within case field values.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>
            sorts: <p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_all_related_items

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.search_all_related_items.search_all_related_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sorts is not None:
            input_["sorts"] = sorts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDomain:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_connectcases.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Amazon Connect instance can be associated with only one Cases domain.</p> <important> <p>This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html">CreateIntegrationAssociation</a> API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam">Onboard to Cases</a>.</p> </important>

        Args:
            name: <p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_domain_request.CreateDomainRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain if it exists. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_domain_request.GetDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_domain_response.GetDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_domain_request.GetDomainRequest = {
            "domain_id": domain_id
        }

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
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a Cases domain.</p> <note> <p>After deleting your domain you must disassociate the deleted domain from your Amazon Connect instance with another API call before being able to use Cases again with this Amazon Connect instance. See <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html">DeleteIntegrationAssociation</a>.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

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
            req: "AsyncOperationRequest[capo_connectcases.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
        }

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
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all cases domains in the Amazon Web Services account. Each list item is a condensed summary object of the domain.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_domains

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_domains_request.ListDomainsRequest = {}
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

    async def get_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse":
        """<p>Returns the case event publishing configuration.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration.async_get_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        event_bridge: "capo_connectcases.types.event_bridge_configuration.EventBridgeConfiguration",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse":
        """<p>Adds case event publishing configuration. For a complete list of fields you can add to the event message, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html">Create case fields</a> in the <i>Amazon Connect Administrator Guide</i> </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            event_bridge: <p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>

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
            req: "AsyncOperationRequest[capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration.async_put_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest = {
            "domain_id": domain_id,
            "event_bridge": event_bridge,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_all_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "capo_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse":
        """<p>Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html">SearchRelatedItems</a> API.</p> <p> <b>Use cases</b> </p> <p>Following are common uses cases for this API:</p> <ul> <li> <p>Find cases with similar issues across the domain. For example, search for all cases containing comments about "product defect" to identify patterns and existing solutions.</p> </li> <li> <p>Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey. </p> </li> <li> <p>Monitor SLA compliance across cases. For example, search for all cases with "Active" SLA status to prioritize remediation efforts.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html">GetCase</a> API for each returned case ID. </p> </li> <li> <p>This API searches across related items content, not case fields. Use the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html">SearchCases</a> API to search within case field values.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>
            sorts: <p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_all_related_items

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.search_all_related_items.async_search_all_related_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sorts is not None:
            input_["sorts"] = sorts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
