from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_security_ir._auth._signers
import capo_security_ir._auth._sigv4
from capo_security_ir._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_security_ir.types.attachment_id
    import capo_security_ir.types.case_description
    import capo_security_ir.types.case_edit_item
    import capo_security_ir.types.case_id
    import capo_security_ir.types.case_metadata
    import capo_security_ir.types.case_title
    import capo_security_ir.types.close_case_request
    import capo_security_ir.types.close_case_response
    import capo_security_ir.types.comment_body
    import capo_security_ir.types.comment_id
    import capo_security_ir.types.content_length
    import capo_security_ir.types.create_case_comment_request
    import capo_security_ir.types.create_case_comment_response
    import capo_security_ir.types.create_case_request
    import capo_security_ir.types.create_case_response
    import capo_security_ir.types.engagement_type
    import capo_security_ir.types.feedback_comment
    import capo_security_ir.types.file_name
    import capo_security_ir.types.get_case_attachment_download_url_request
    import capo_security_ir.types.get_case_attachment_download_url_response
    import capo_security_ir.types.get_case_attachment_upload_url_request
    import capo_security_ir.types.get_case_attachment_upload_url_response
    import capo_security_ir.types.get_case_request
    import capo_security_ir.types.get_case_response
    import capo_security_ir.types.impacted_accounts
    import capo_security_ir.types.impacted_aws_region_list
    import capo_security_ir.types.impacted_services_list
    import capo_security_ir.types.investigation_action
    import capo_security_ir.types.list_case_edits_request
    import capo_security_ir.types.list_case_edits_response
    import capo_security_ir.types.list_cases_item
    import capo_security_ir.types.list_cases_request
    import capo_security_ir.types.list_cases_response
    import capo_security_ir.types.list_comments_item
    import capo_security_ir.types.list_comments_request
    import capo_security_ir.types.list_comments_response
    import capo_security_ir.types.list_investigations_request
    import capo_security_ir.types.list_investigations_response
    import capo_security_ir.types.resolver_type
    import capo_security_ir.types.result_id
    import capo_security_ir.types.self_managed_case_status
    import capo_security_ir.types.send_feedback_request
    import capo_security_ir.types.send_feedback_response
    import capo_security_ir.types.tag_map
    import capo_security_ir.types.threat_actor_ip_list
    import capo_security_ir.types.update_case_comment_request
    import capo_security_ir.types.update_case_comment_response
    import capo_security_ir.types.update_case_request
    import capo_security_ir.types.update_case_response
    import capo_security_ir.types.update_case_status_request
    import capo_security_ir.types.update_case_status_response
    import capo_security_ir.types.update_resolver_type_request
    import capo_security_ir.types.update_resolver_type_response
    import capo_security_ir.types.usefulness_rating
    import capo_security_ir.types.watchers
    from capo_security_ir._services.async_security_ir import (
        AsyncSecurityIRClient,
        AsyncSecurityIRClientConfig,
    )
    from capo_security_ir._services.security_ir import (
        SecurityIRClient,
        SecurityIRClientConfig,
    )


class Case:
    def __init__(self, service: SecurityIRClient) -> None:
        self._service = service

    def create(
        self,
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        title: "capo_security_ir.types.case_title.CaseTitle",
        description: "capo_security_ir.types.case_description.CaseDescription",
        engagement_type: "capo_security_ir.types.engagement_type.EngagementType",
        reported_incident_start_date: datetime.datetime,
        impacted_accounts: "capo_security_ir.types.impacted_accounts.ImpactedAccounts",
        watchers: "capo_security_ir.types.watchers.Watchers",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        threat_actor_ip_addresses: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
    ) -> "capo_security_ir.types.create_case_response.CreateCaseResponse":
        """<p>Creates a new case.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            resolver_type: <p>Required element used in combination with CreateCase to identify the resolver type.</p>
            title: <p>Required element used in combination with CreateCase to provide a title for the new case.</p>
            description: <p>Required element used in combination with CreateCase</p> <p>to provide a description for the new case.</p>
            engagement_type: <p>Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident | Investigation </p>
            reported_incident_start_date: <p>Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity. </p>
            impacted_accounts: <p>Required element used in combination with CreateCase to provide a list of impacted accounts.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            watchers: <p>Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates. </p>
            threat_actor_ip_addresses: <p>An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity. </p>
            impacted_services: <p>An optional element used in combination with CreateCase to provide a list of services impacted.</p>
            impacted_aws_regions: <p>An optional element used in combination with CreateCase to provide a list of impacted regions.</p>
            tags: <p>An optional element used in combination with CreateCase to add customer specified tags to a case.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCase

            >>> client.create(resolver_type='Self', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', engagement_type='Investigation', watchers=[{'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}, {'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], impacted_accounts=['000000000000', '111111111111'], impacted_services=['Amazon EC2', 'Amazon EKS'], impacted_aws_regions=[{'region': 'ap-southeast-1'}], threat_actor_ip_addresses=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_case_request.CreateCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_case.create_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.create_case_request.CreateCaseRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.create_case_request

            return capo_security_ir.types.create_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCase", redact_input=_redact_input)
        )
        input_: capo_security_ir.types.create_case_request.CreateCaseRequest = {
            "resolver_type": resolver_type,
            "title": title,
            "description": description,
            "engagement_type": engagement_type,
            "reported_incident_start_date": reported_incident_start_date,
            "impacted_accounts": impacted_accounts,
            "watchers": watchers,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if threat_actor_ip_addresses is not None:
            input_["threat_actor_ip_addresses"] = threat_actor_ip_addresses
        if impacted_services is not None:
            input_["impacted_services"] = impacted_services
        if impacted_aws_regions is not None:
            input_["impacted_aws_regions"] = impacted_aws_regions
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
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_response.GetCaseResponse":
        """<p>Returns the attributes of a case.</p>

        Args:
            case_id: <p>Required element for GetCase to identify the requested case ID.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCase

            >>> client.read(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_request.GetCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_response.GetCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case.get_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.get_case_response.GetCaseResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_response

            return capo_security_ir.types.get_case_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCase", redact_output=_redact_output)
        )
        input_: capo_security_ir.types.get_case_request.GetCaseRequest = {
            "case_id": case_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        title: Optional["capo_security_ir.types.case_title.CaseTitle"] = None,
        description: Optional[
            "capo_security_ir.types.case_description.CaseDescription"
        ] = None,
        reported_incident_start_date: Optional[datetime.datetime] = None,
        actual_incident_start_date: Optional[datetime.datetime] = None,
        engagement_type: Optional[
            "capo_security_ir.types.engagement_type.EngagementType"
        ] = None,
        watchers_to_add: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        watchers_to_delete: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        threat_actor_ip_addresses_to_add: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        threat_actor_ip_addresses_to_delete: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services_to_add: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_services_to_delete: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions_to_add: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_aws_regions_to_delete: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_accounts_to_add: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        impacted_accounts_to_delete: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        case_metadata: Optional[
            "capo_security_ir.types.case_metadata.CaseMetadata"
        ] = None,
    ) -> "capo_security_ir.types.update_case_response.UpdateCaseResponse":
        """<p>Updates an existing case.</p>

        Args:
            case_id: <p>Required element for UpdateCase to identify the case ID for updates.</p>
            title: <p>Optional element for UpdateCase to provide content for the title field.</p>
            description: <p>Optional element for UpdateCase to provide content for the description field.</p>
            reported_incident_start_date: <p>Optional element for UpdateCase to provide content for the customer reported incident start date field. </p>
            actual_incident_start_date: <p>Optional element for UpdateCase to provide content for the incident start date field.</p>
            engagement_type: <p>Optional element for UpdateCase to provide content for the engagement type field. <code>Available engagement types include Security Incident | Investigation</code>. </p>
            watchers_to_add: <p>Optional element for UpdateCase to provide content to add additional watchers to a case.</p>
            watchers_to_delete: <p>Optional element for UpdateCase to provide content to remove existing watchers from a case.</p>
            threat_actor_ip_addresses_to_add: <p>Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case. </p>
            threat_actor_ip_addresses_to_delete: <p>Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.</p>
            impacted_services_to_add: <p>Optional element for UpdateCase to provide content to add services impacted.</p>
            impacted_services_to_delete: <p>Optional element for UpdateCase to provide content to remove services impacted.</p>
            impacted_aws_regions_to_add: <p>Optional element for UpdateCase to provide content to add regions impacted.</p>
            impacted_aws_regions_to_delete: <p>Optional element for UpdateCase to provide content to remove regions impacted.</p>
            impacted_accounts_to_add: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            impacted_accounts_to_delete: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            case_metadata: <p>Update the case request with case metadata</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCase

            >>> client.update(case_id='8403556009', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', actual_incident_start_date='2023-03-25T15:32:01.789Z', engagement_type='Investigation', watchers_to_add=[{'email': 'Sam@example.com', 'name': 'Same', 'jobTitle': 'CEO'}], watchers_to_delete=[{'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], threat_actor_ip_addresses_to_add=[{'ipAddress': '190.160.190.160', 'userAgent': 'Browser'}], threat_actor_ip_addresses_to_delete=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}], impacted_services_to_add=['Amazon EC2'], impacted_services_to_delete=['Amazon EKS'], impacted_aws_regions_to_add=[{'region': 'ap-southeast-1'}], impacted_aws_regions_to_delete=[{'region': 'us-east-1'}], impacted_accounts_to_add=['000000000000'], impacted_accounts_to_delete=['111111111111'])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_request.UpdateCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case.update_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.update_case_request.UpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_request

            return capo_security_ir.types.update_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCase", redact_input=_redact_input)
        )
        input_: capo_security_ir.types.update_case_request.UpdateCaseRequest = {
            "case_id": case_id
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if reported_incident_start_date is not None:
            input_["reported_incident_start_date"] = reported_incident_start_date
        if actual_incident_start_date is not None:
            input_["actual_incident_start_date"] = actual_incident_start_date
        if engagement_type is not None:
            input_["engagement_type"] = engagement_type
        if watchers_to_add is not None:
            input_["watchers_to_add"] = watchers_to_add
        if watchers_to_delete is not None:
            input_["watchers_to_delete"] = watchers_to_delete
        if threat_actor_ip_addresses_to_add is not None:
            input_["threat_actor_ip_addresses_to_add"] = (
                threat_actor_ip_addresses_to_add
            )
        if threat_actor_ip_addresses_to_delete is not None:
            input_["threat_actor_ip_addresses_to_delete"] = (
                threat_actor_ip_addresses_to_delete
            )
        if impacted_services_to_add is not None:
            input_["impacted_services_to_add"] = impacted_services_to_add
        if impacted_services_to_delete is not None:
            input_["impacted_services_to_delete"] = impacted_services_to_delete
        if impacted_aws_regions_to_add is not None:
            input_["impacted_aws_regions_to_add"] = impacted_aws_regions_to_add
        if impacted_aws_regions_to_delete is not None:
            input_["impacted_aws_regions_to_delete"] = impacted_aws_regions_to_delete
        if impacted_accounts_to_add is not None:
            input_["impacted_accounts_to_add"] = impacted_accounts_to_add
        if impacted_accounts_to_delete is not None:
            input_["impacted_accounts_to_delete"] = impacted_accounts_to_delete
        if case_metadata is not None:
            input_["case_metadata"] = case_metadata

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
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_cases_response.ListCasesResponse":
        """<p>Lists all cases the requester has access to.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCases. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListCases to limit the number of responses.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCases

            >>> client.list(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_cases_request.ListCasesRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_cases_response.ListCasesResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_cases

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_cases.list_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.list_cases_response.ListCasesResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.list_cases_response

            return capo_security_ir.types.list_cases_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCases", redact_output=_redact_output),
        )
        input_: capo_security_ir.types.list_cases_request.ListCasesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def close_case(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.close_case_response.CloseCaseResponse":
        """<p>Closes an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CloseCase to identify the case ID to close.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CloseCase

            >>> client.close_case(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.close_case_request.CloseCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.close_case_response.CloseCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.close_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.close_case.close_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CloseCase")
        )
        input_: capo_security_ir.types.close_case_request.CloseCaseRequest = {
            "case_id": case_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
    ):
        """<p>Adds a comment to an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CreateCaseComment to specify a case ID.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            body: <p>Required element used in combination with CreateCaseComment to add content for the new comment.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCaseComment

            >>> client.create_case_comment(case_id='8403556009', body='Case comment body.')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case_comment

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_case_comment.create_case_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.create_case_comment_request

            return capo_security_ir.types.create_case_comment_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCaseComment", redact_input=_redact_input),
        )
        input_: capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest = {
            "case_id": case_id,
            "body": body,
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

    def get_case_attachment_download_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        attachment_id: "capo_security_ir.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse":
        """<p>Returns a Pre-Signed URL for uploading attachments into a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the case ID for downloading an attachment from. </p>
            attachment_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the attachment ID for downloading an attachment. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentDownloadUrl

            >>> client.get_case_attachment_download_url(case_id='8403556009', attachment_id='3C5A6B89-1DEF-4C2D-A5B6-123456789ABC')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_download_url

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case_attachment_download_url.get_case_attachment_download_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_download_url_response

            return capo_security_ir.types.get_case_attachment_download_url_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCaseAttachmentDownloadUrl", redact_output=_redact_output
            ),
        )
        input_: capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest = {
            "case_id": case_id,
            "attachment_id": attachment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_case_attachment_upload_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        file_name: "capo_security_ir.types.file_name.FileName",
        content_length: "capo_security_ir.types.content_length.ContentLength",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse":
        """<p>Uploads an attachment to a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment. </p>
            file_name: <p>Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload. </p>
            content_length: <p>Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentUploadUrl

            >>> client.get_case_attachment_upload_url(case_id='8403556009', file_name='TestFileName', content_length=1500)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url.get_case_attachment_upload_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_upload_url_request

            return capo_security_ir.types.get_case_attachment_upload_url_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_upload_url_response

            return capo_security_ir.types.get_case_attachment_upload_url_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCaseAttachmentUploadUrl",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest = {
            "case_id": case_id,
            "file_name": file_name,
            "content_length": content_length,
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

    def list_case_edits(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse":
        """<p>Views the case history for edits made to a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCaseEdits. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element to identify how many results to obtain. There is a maximum value of 25.</p>
            case_id: <p>Required element used with ListCaseEdits to identify the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCaseEdits

            >>> client.list_case_edits(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_case_edits

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_case_edits.list_case_edits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCaseEdits")
        )
        input_: capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_comments(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_comments_response.ListCommentsResponse":
        """<p>Returns comments for a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListComments. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListComments to limit the number of responses.</p>
            case_id: <p>Required element for ListComments to designate the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComments

            >>> client.list_comments(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_comments_request.ListCommentsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_comments_response.ListCommentsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_comments

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_comments.list_comments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.list_comments_response.ListCommentsResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.list_comments_response

            return capo_security_ir.types.list_comments_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListComments", redact_output=_redact_output),
        )
        input_: capo_security_ir.types.list_comments_request.ListCommentsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_investigations(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
    ):
        """<p>Investigation performed by an agent for a security incident...</p>

        Args:
            next_token: <p>Investigation performed by an agent for a security incident request</p>
            max_results: <p>Investigation performed by an agent for a security incident request, returning max results</p>
            case_id: <p>Investigation performed by an agent for a security incident per caseID</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListInvestigations with feedback examples

            >>> client.list_investigations(case_id='8403556009', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_investigations

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_investigations.list_investigations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListInvestigations")
        )
        input_: capo_security_ir.types.list_investigations_request.ListInvestigationsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_feedback(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        result_id: "capo_security_ir.types.result_id.ResultId",
        usefulness: "capo_security_ir.types.usefulness_rating.UsefulnessRating",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        comment: Optional[
            "capo_security_ir.types.feedback_comment.FeedbackComment"
        ] = None,
    ) -> "capo_security_ir.types.send_feedback_response.SendFeedbackResponse":
        """<p>Send feedback based on response investigation action</p>

        Args:
            case_id: <p>Send feedback based on request caseID</p>
            result_id: <p>Send feedback based on request result ID</p>
            usefulness: <p>Required enum value indicating user assessment of result q.....</p>
            comment: <p>Send feedback based on request comments</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Send positive feedback for investigation result

            >>> client.send_feedback(case_id='8403556009', result_id='inv-polkjhyuty', usefulness='USEFUL', comment='The CloudTrail analysis was very helpful in identifying the root cause of the security incident.')
            Send negative feedback with detailed comment

            >>> client.send_feedback(case_id='8403556009', result_id='inv-irutjfhgjk', usefulness='NOT_USEFUL', comment="The investigation results were too generic and didn't provide actionable insights for our specific incident.")
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.send_feedback_request.SendFeedbackRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.send_feedback_response.SendFeedbackResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.send_feedback

            output, http_response = (
                capo_security_ir._operations.security_incident_response.send_feedback.send_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SendFeedback")
        )
        input_: capo_security_ir.types.send_feedback_request.SendFeedbackRequest = {
            "case_id": case_id,
            "result_id": result_id,
            "usefulness": usefulness,
        }
        if comment is not None:
            input_["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        comment_id: "capo_security_ir.types.comment_id.CommentId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
    ):
        """<p>Updates an existing case comment.</p>

        Args:
            case_id: <p>Required element for UpdateCaseComment to identify the case ID containing the comment to be updated. </p>
            comment_id: <p>Required element for UpdateCaseComment to identify the case ID to be updated.</p>
            body: <p>Required element for UpdateCaseComment to identify the content for the comment to be updated.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseComment

            >>> client.update_case_comment(case_id='8403556009', comment_id='000000', body='Updated case comment.')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_comment

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case_comment.update_case_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_comment_request

            return capo_security_ir.types.update_case_comment_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_comment_response

            return capo_security_ir.types.update_case_comment_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateCaseComment",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest = {
            "case_id": case_id,
            "comment_id": comment_id,
            "body": body,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_case_status(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        case_status: "capo_security_ir.types.self_managed_case_status.SelfManagedCaseStatus",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse":
        """<p>Updates the state transitions for a designated cases.</p> <p> <b>Self-managed</b>: the following states are available for self-managed cases. </p> <ul> <li> <p>Submitted → Detection and Analysis</p> </li> <li> <p>Detection and Analysis → Containment, Eradication, and Recovery</p> </li> <li> <p>Detection and Analysis → Post-incident Activities</p> </li> <li> <p>Containment, Eradication, and Recovery → Detection and Analysis</p> </li> <li> <p>Containment, Eradication, and Recovery → Post-incident Activities</p> </li> <li> <p>Post-incident Activities → Containment, Eradication, and Recovery</p> </li> <li> <p>Post-incident Activities → Detection and Analysis</p> </li> <li> <p>Any → Closed</p> </li> </ul> <p> <b>AWS supported</b>: You must use the <code>CloseCase</code> API to close. </p>

        Args:
            case_id: <p>Required element for UpdateCaseStatus to identify the case to update.</p>
            case_status: <p>Required element for UpdateCaseStatus to identify the status for a case. Options include <code>Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities</code>. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseStatus

            >>> client.update_case_status(case_id='8403556009', case_status='Post-incident Activities')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_status

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case_status.update_case_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCaseStatus")
        )
        input_: capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest = {
            "case_id": case_id,
            "case_status": case_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resolver_type(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse":
        """<p>Updates the resolver type for a case.</p> <important> <p>This is a one-way action and cannot be reversed.</p> </important>

        Args:
            case_id: <p>Required element for UpdateResolverType to identify the case to update.</p>
            resolver_type: <p>Required element for UpdateResolverType to identify the new resolver.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateResolverType

            >>> client.update_resolver_type(case_id='8403556009', resolver_type='AWS')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_resolver_type

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_resolver_type.update_resolver_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateResolverType")
        )
        input_: capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest = {
            "case_id": case_id,
            "resolver_type": resolver_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCase:
    def __init__(self, service: AsyncSecurityIRClient) -> None:
        self._service = service

    async def create(
        self,
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        title: "capo_security_ir.types.case_title.CaseTitle",
        description: "capo_security_ir.types.case_description.CaseDescription",
        engagement_type: "capo_security_ir.types.engagement_type.EngagementType",
        reported_incident_start_date: datetime.datetime,
        impacted_accounts: "capo_security_ir.types.impacted_accounts.ImpactedAccounts",
        watchers: "capo_security_ir.types.watchers.Watchers",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        threat_actor_ip_addresses: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
    ) -> "capo_security_ir.types.create_case_response.CreateCaseResponse":
        """<p>Creates a new case.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            resolver_type: <p>Required element used in combination with CreateCase to identify the resolver type.</p>
            title: <p>Required element used in combination with CreateCase to provide a title for the new case.</p>
            description: <p>Required element used in combination with CreateCase</p> <p>to provide a description for the new case.</p>
            engagement_type: <p>Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident | Investigation </p>
            reported_incident_start_date: <p>Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity. </p>
            impacted_accounts: <p>Required element used in combination with CreateCase to provide a list of impacted accounts.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            watchers: <p>Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates. </p>
            threat_actor_ip_addresses: <p>An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity. </p>
            impacted_services: <p>An optional element used in combination with CreateCase to provide a list of services impacted.</p>
            impacted_aws_regions: <p>An optional element used in combination with CreateCase to provide a list of impacted regions.</p>
            tags: <p>An optional element used in combination with CreateCase to add customer specified tags to a case.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCase

            >>> await client.create(resolver_type='Self', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', engagement_type='Investigation', watchers=[{'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}, {'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], impacted_accounts=['000000000000', '111111111111'], impacted_services=['Amazon EC2', 'Amazon EKS'], impacted_aws_regions=[{'region': 'ap-southeast-1'}], threat_actor_ip_addresses=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.create_case_request.CreateCaseRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.create_case_request

            return capo_security_ir.types.create_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCase", redact_input=_redact_input)
        )
        input_: capo_security_ir.types.create_case_request.CreateCaseRequest = {
            "resolver_type": resolver_type,
            "title": title,
            "description": description,
            "engagement_type": engagement_type,
            "reported_incident_start_date": reported_incident_start_date,
            "impacted_accounts": impacted_accounts,
            "watchers": watchers,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if threat_actor_ip_addresses is not None:
            input_["threat_actor_ip_addresses"] = threat_actor_ip_addresses
        if impacted_services is not None:
            input_["impacted_services"] = impacted_services
        if impacted_aws_regions is not None:
            input_["impacted_aws_regions"] = impacted_aws_regions
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
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_response.GetCaseResponse":
        """<p>Returns the attributes of a case.</p>

        Args:
            case_id: <p>Required element for GetCase to identify the requested case ID.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCase

            >>> await client.read(case_id='8403556009')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.get_case_request.GetCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.get_case_response.GetCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.get_case.async_get_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.get_case_response.GetCaseResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_response

            return capo_security_ir.types.get_case_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCase", redact_output=_redact_output)
        )
        input_: capo_security_ir.types.get_case_request.GetCaseRequest = {
            "case_id": case_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        title: Optional["capo_security_ir.types.case_title.CaseTitle"] = None,
        description: Optional[
            "capo_security_ir.types.case_description.CaseDescription"
        ] = None,
        reported_incident_start_date: Optional[datetime.datetime] = None,
        actual_incident_start_date: Optional[datetime.datetime] = None,
        engagement_type: Optional[
            "capo_security_ir.types.engagement_type.EngagementType"
        ] = None,
        watchers_to_add: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        watchers_to_delete: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        threat_actor_ip_addresses_to_add: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        threat_actor_ip_addresses_to_delete: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services_to_add: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_services_to_delete: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions_to_add: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_aws_regions_to_delete: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_accounts_to_add: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        impacted_accounts_to_delete: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        case_metadata: Optional[
            "capo_security_ir.types.case_metadata.CaseMetadata"
        ] = None,
    ) -> "capo_security_ir.types.update_case_response.UpdateCaseResponse":
        """<p>Updates an existing case.</p>

        Args:
            case_id: <p>Required element for UpdateCase to identify the case ID for updates.</p>
            title: <p>Optional element for UpdateCase to provide content for the title field.</p>
            description: <p>Optional element for UpdateCase to provide content for the description field.</p>
            reported_incident_start_date: <p>Optional element for UpdateCase to provide content for the customer reported incident start date field. </p>
            actual_incident_start_date: <p>Optional element for UpdateCase to provide content for the incident start date field.</p>
            engagement_type: <p>Optional element for UpdateCase to provide content for the engagement type field. <code>Available engagement types include Security Incident | Investigation</code>. </p>
            watchers_to_add: <p>Optional element for UpdateCase to provide content to add additional watchers to a case.</p>
            watchers_to_delete: <p>Optional element for UpdateCase to provide content to remove existing watchers from a case.</p>
            threat_actor_ip_addresses_to_add: <p>Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case. </p>
            threat_actor_ip_addresses_to_delete: <p>Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.</p>
            impacted_services_to_add: <p>Optional element for UpdateCase to provide content to add services impacted.</p>
            impacted_services_to_delete: <p>Optional element for UpdateCase to provide content to remove services impacted.</p>
            impacted_aws_regions_to_add: <p>Optional element for UpdateCase to provide content to add regions impacted.</p>
            impacted_aws_regions_to_delete: <p>Optional element for UpdateCase to provide content to remove regions impacted.</p>
            impacted_accounts_to_add: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            impacted_accounts_to_delete: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            case_metadata: <p>Update the case request with case metadata</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCase

            >>> await client.update(case_id='8403556009', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', actual_incident_start_date='2023-03-25T15:32:01.789Z', engagement_type='Investigation', watchers_to_add=[{'email': 'Sam@example.com', 'name': 'Same', 'jobTitle': 'CEO'}], watchers_to_delete=[{'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], threat_actor_ip_addresses_to_add=[{'ipAddress': '190.160.190.160', 'userAgent': 'Browser'}], threat_actor_ip_addresses_to_delete=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}], impacted_services_to_add=['Amazon EC2'], impacted_services_to_delete=['Amazon EKS'], impacted_aws_regions_to_add=[{'region': 'ap-southeast-1'}], impacted_aws_regions_to_delete=[{'region': 'us-east-1'}], impacted_accounts_to_add=['000000000000'], impacted_accounts_to_delete=['111111111111'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.update_case_request.UpdateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.update_case.async_update_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.update_case_request.UpdateCaseRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_request

            return capo_security_ir.types.update_case_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCase", redact_input=_redact_input)
        )
        input_: capo_security_ir.types.update_case_request.UpdateCaseRequest = {
            "case_id": case_id
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if reported_incident_start_date is not None:
            input_["reported_incident_start_date"] = reported_incident_start_date
        if actual_incident_start_date is not None:
            input_["actual_incident_start_date"] = actual_incident_start_date
        if engagement_type is not None:
            input_["engagement_type"] = engagement_type
        if watchers_to_add is not None:
            input_["watchers_to_add"] = watchers_to_add
        if watchers_to_delete is not None:
            input_["watchers_to_delete"] = watchers_to_delete
        if threat_actor_ip_addresses_to_add is not None:
            input_["threat_actor_ip_addresses_to_add"] = (
                threat_actor_ip_addresses_to_add
            )
        if threat_actor_ip_addresses_to_delete is not None:
            input_["threat_actor_ip_addresses_to_delete"] = (
                threat_actor_ip_addresses_to_delete
            )
        if impacted_services_to_add is not None:
            input_["impacted_services_to_add"] = impacted_services_to_add
        if impacted_services_to_delete is not None:
            input_["impacted_services_to_delete"] = impacted_services_to_delete
        if impacted_aws_regions_to_add is not None:
            input_["impacted_aws_regions_to_add"] = impacted_aws_regions_to_add
        if impacted_aws_regions_to_delete is not None:
            input_["impacted_aws_regions_to_delete"] = impacted_aws_regions_to_delete
        if impacted_accounts_to_add is not None:
            input_["impacted_accounts_to_add"] = impacted_accounts_to_add
        if impacted_accounts_to_delete is not None:
            input_["impacted_accounts_to_delete"] = impacted_accounts_to_delete
        if case_metadata is not None:
            input_["case_metadata"] = case_metadata

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
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_cases_response.ListCasesResponse":
        """<p>Lists all cases the requester has access to.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCases. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListCases to limit the number of responses.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCases

            >>> await client.list(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.list_cases_request.ListCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.list_cases_response.ListCasesResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_cases

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.list_cases.async_list_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.list_cases_response.ListCasesResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.list_cases_response

            return capo_security_ir.types.list_cases_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCases", redact_output=_redact_output),
        )
        input_: capo_security_ir.types.list_cases_request.ListCasesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def close_case(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.close_case_response.CloseCaseResponse":
        """<p>Closes an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CloseCase to identify the case ID to close.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CloseCase

            >>> await client.close_case(case_id='8403556009')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.close_case_request.CloseCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.close_case_response.CloseCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.close_case

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.close_case.async_close_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CloseCase")
        )
        input_: capo_security_ir.types.close_case_request.CloseCaseRequest = {
            "case_id": case_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
    ):
        """<p>Adds a comment to an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CreateCaseComment to specify a case ID.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            body: <p>Required element used in combination with CreateCaseComment to add content for the new comment.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCaseComment

            >>> await client.create_case_comment(case_id='8403556009', body='Case comment body.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case_comment

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.create_case_comment.async_create_case_comment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.create_case_comment_request

            return capo_security_ir.types.create_case_comment_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCaseComment", redact_input=_redact_input),
        )
        input_: capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest = {
            "case_id": case_id,
            "body": body,
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

    async def get_case_attachment_download_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        attachment_id: "capo_security_ir.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse":
        """<p>Returns a Pre-Signed URL for uploading attachments into a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the case ID for downloading an attachment from. </p>
            attachment_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the attachment ID for downloading an attachment. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentDownloadUrl

            >>> await client.get_case_attachment_download_url(case_id='8403556009', attachment_id='3C5A6B89-1DEF-4C2D-A5B6-123456789ABC')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_download_url

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.get_case_attachment_download_url.async_get_case_attachment_download_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_download_url_response

            return capo_security_ir.types.get_case_attachment_download_url_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCaseAttachmentDownloadUrl", redact_output=_redact_output
            ),
        )
        input_: capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest = {
            "case_id": case_id,
            "attachment_id": attachment_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_case_attachment_upload_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        file_name: "capo_security_ir.types.file_name.FileName",
        content_length: "capo_security_ir.types.content_length.ContentLength",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse":
        """<p>Uploads an attachment to a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment. </p>
            file_name: <p>Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload. </p>
            content_length: <p>Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentUploadUrl

            >>> await client.get_case_attachment_upload_url(case_id='8403556009', file_name='TestFileName', content_length=1500)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url.async_get_case_attachment_upload_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_upload_url_request

            return capo_security_ir.types.get_case_attachment_upload_url_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.get_case_attachment_upload_url_response

            return capo_security_ir.types.get_case_attachment_upload_url_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCaseAttachmentUploadUrl",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest = {
            "case_id": case_id,
            "file_name": file_name,
            "content_length": content_length,
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

    async def list_case_edits(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse":
        """<p>Views the case history for edits made to a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCaseEdits. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element to identify how many results to obtain. There is a maximum value of 25.</p>
            case_id: <p>Required element used with ListCaseEdits to identify the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCaseEdits

            >>> await client.list_case_edits(case_id='8403556009')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_case_edits

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.list_case_edits.async_list_case_edits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCaseEdits")
        )
        input_: capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_comments(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_comments_response.ListCommentsResponse":
        """<p>Returns comments for a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListComments. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListComments to limit the number of responses.</p>
            case_id: <p>Required element for ListComments to designate the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComments

            >>> await client.list_comments(case_id='8403556009')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.list_comments_request.ListCommentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.list_comments_response.ListCommentsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_comments

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.list_comments.async_list_comments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_security_ir.types.list_comments_response.ListCommentsResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.list_comments_response

            return capo_security_ir.types.list_comments_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListComments", redact_output=_redact_output),
        )
        input_: capo_security_ir.types.list_comments_request.ListCommentsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_investigations(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
    ):
        """<p>Investigation performed by an agent for a security incident...</p>

        Args:
            next_token: <p>Investigation performed by an agent for a security incident request</p>
            max_results: <p>Investigation performed by an agent for a security incident request, returning max results</p>
            case_id: <p>Investigation performed by an agent for a security incident per caseID</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListInvestigations with feedback examples

            >>> await client.list_investigations(case_id='8403556009', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_investigations

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.list_investigations.async_list_investigations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListInvestigations")
        )
        input_: capo_security_ir.types.list_investigations_request.ListInvestigationsRequest = {
            "case_id": case_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_feedback(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        result_id: "capo_security_ir.types.result_id.ResultId",
        usefulness: "capo_security_ir.types.usefulness_rating.UsefulnessRating",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        comment: Optional[
            "capo_security_ir.types.feedback_comment.FeedbackComment"
        ] = None,
    ) -> "capo_security_ir.types.send_feedback_response.SendFeedbackResponse":
        """<p>Send feedback based on response investigation action</p>

        Args:
            case_id: <p>Send feedback based on request caseID</p>
            result_id: <p>Send feedback based on request result ID</p>
            usefulness: <p>Required enum value indicating user assessment of result q.....</p>
            comment: <p>Send feedback based on request comments</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Send positive feedback for investigation result

            >>> await client.send_feedback(case_id='8403556009', result_id='inv-polkjhyuty', usefulness='USEFUL', comment='The CloudTrail analysis was very helpful in identifying the root cause of the security incident.')
            Send negative feedback with detailed comment

            >>> await client.send_feedback(case_id='8403556009', result_id='inv-irutjfhgjk', usefulness='NOT_USEFUL', comment="The investigation results were too generic and didn't provide actionable insights for our specific incident.")
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.send_feedback_request.SendFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.send_feedback_response.SendFeedbackResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.send_feedback

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.send_feedback.async_send_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SendFeedback")
        )
        input_: capo_security_ir.types.send_feedback_request.SendFeedbackRequest = {
            "case_id": case_id,
            "result_id": result_id,
            "usefulness": usefulness,
        }
        if comment is not None:
            input_["comment"] = comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        comment_id: "capo_security_ir.types.comment_id.CommentId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
    ):
        """<p>Updates an existing case comment.</p>

        Args:
            case_id: <p>Required element for UpdateCaseComment to identify the case ID containing the comment to be updated. </p>
            comment_id: <p>Required element for UpdateCaseComment to identify the case ID to be updated.</p>
            body: <p>Required element for UpdateCaseComment to identify the content for the comment to be updated.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseComment

            >>> await client.update_case_comment(case_id='8403556009', comment_id='000000', body='Updated case comment.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_comment

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.update_case_comment.async_update_case_comment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_comment_request

            return capo_security_ir.types.update_case_comment_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse",
        ) -> dict[str, Any]:
            import capo_security_ir.types.update_case_comment_response

            return capo_security_ir.types.update_case_comment_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateCaseComment",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest = {
            "case_id": case_id,
            "comment_id": comment_id,
            "body": body,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_case_status(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        case_status: "capo_security_ir.types.self_managed_case_status.SelfManagedCaseStatus",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse":
        """<p>Updates the state transitions for a designated cases.</p> <p> <b>Self-managed</b>: the following states are available for self-managed cases. </p> <ul> <li> <p>Submitted → Detection and Analysis</p> </li> <li> <p>Detection and Analysis → Containment, Eradication, and Recovery</p> </li> <li> <p>Detection and Analysis → Post-incident Activities</p> </li> <li> <p>Containment, Eradication, and Recovery → Detection and Analysis</p> </li> <li> <p>Containment, Eradication, and Recovery → Post-incident Activities</p> </li> <li> <p>Post-incident Activities → Containment, Eradication, and Recovery</p> </li> <li> <p>Post-incident Activities → Detection and Analysis</p> </li> <li> <p>Any → Closed</p> </li> </ul> <p> <b>AWS supported</b>: You must use the <code>CloseCase</code> API to close. </p>

        Args:
            case_id: <p>Required element for UpdateCaseStatus to identify the case to update.</p>
            case_status: <p>Required element for UpdateCaseStatus to identify the status for a case. Options include <code>Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities</code>. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseStatus

            >>> await client.update_case_status(case_id='8403556009', case_status='Post-incident Activities')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_status

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.update_case_status.async_update_case_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCaseStatus")
        )
        input_: capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest = {
            "case_id": case_id,
            "case_status": case_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resolver_type(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse":
        """<p>Updates the resolver type for a case.</p> <important> <p>This is a one-way action and cannot be reversed.</p> </important>

        Args:
            case_id: <p>Required element for UpdateResolverType to identify the case to update.</p>
            resolver_type: <p>Required element for UpdateResolverType to identify the new resolver.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateResolverType

            >>> await client.update_resolver_type(case_id='8403556009', resolver_type='AWS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_resolver_type

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.update_resolver_type.async_update_resolver_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateResolverType")
        )
        input_: capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest = {
            "case_id": case_id,
            "resolver_type": resolver_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
