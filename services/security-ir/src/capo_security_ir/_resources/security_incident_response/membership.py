from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Optional

import capo_security_ir._auth._signers
import capo_security_ir._auth._sigv4
from capo_security_ir._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_security_ir.types.aws_account_ids
    import capo_security_ir.types.batch_get_member_account_details_request
    import capo_security_ir.types.batch_get_member_account_details_response
    import capo_security_ir.types.cancel_membership_request
    import capo_security_ir.types.cancel_membership_response
    import capo_security_ir.types.create_membership_request
    import capo_security_ir.types.create_membership_response
    import capo_security_ir.types.get_finding_metrics_request
    import capo_security_ir.types.get_finding_metrics_response
    import capo_security_ir.types.get_membership_request
    import capo_security_ir.types.get_membership_response
    import capo_security_ir.types.incident_response_team
    import capo_security_ir.types.list_membership_item
    import capo_security_ir.types.list_memberships_request
    import capo_security_ir.types.list_memberships_response
    import capo_security_ir.types.membership_accounts_configurations_update
    import capo_security_ir.types.membership_id
    import capo_security_ir.types.membership_name
    import capo_security_ir.types.opt_in_features
    import capo_security_ir.types.tag_map
    import capo_security_ir.types.update_membership_request
    import capo_security_ir.types.update_membership_response
    from capo_security_ir._services.async_security_ir import (
        AsyncSecurityIRClient,
        AsyncSecurityIRClientConfig,
    )
    from capo_security_ir._services.security_ir import (
        SecurityIRClient,
        SecurityIRClientConfig,
    )


class Membership:
    def __init__(self, service: SecurityIRClient) -> None:
        self._service = service

    def create(
        self,
        membership_name: "capo_security_ir.types.membership_name.MembershipName",
        incident_response_team: "capo_security_ir.types.incident_response_team.IncidentResponseTeam",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
        cover_entire_organization: Optional[bool] = None,
    ) -> "capo_security_ir.types.create_membership_response.CreateMembershipResponse":
        """<p>Creates a new membership.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            membership_name: <p>Required element used in combination with CreateMembership to create a name for the membership.</p>
            incident_response_team: <p>Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership. </p>
            opt_in_features: <p>Optional element to enable the monitoring and investigation opt-in features for the service.</p>
            tags: <p>Optional element for customer configured tags.</p>
            cover_entire_organization: <p>The <code>coverEntireOrganization</code> parameter is a boolean flag that determines whether the membership should be applied to the entire Amazon Web Services Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts. </p> <p>This parameter is optional. If not specified, the default value is false.</p> <ul> <li> <p>If set to <i>true</i>: The membership will automatically include all existing and future accounts in the Amazon Web Services Organization. </p> </li> <li> <p>If set to <i>false</i>: The membership will only apply to explicitly specified accounts. </p> </li> </ul>

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
            Invoke CreateMembership

            >>> client.create(membership_name='Example Membership Name.', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_membership_request.CreateMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_membership_response.CreateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_membership.create_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.create_membership_request.CreateMembershipRequest = {
            "membership_name": membership_name,
            "incident_response_team": incident_response_team,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if tags is not None:
            input_["tags"] = tags
        if cover_entire_organization is not None:
            input_["cover_entire_organization"] = cover_entire_organization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_membership_response.GetMembershipResponse":
        """<p>Returns the attributes of a membership.</p>

        Args:
            membership_id: <p>Required element for GetMembership to identify the membership ID to query.</p>

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
            Invoke GetMembership

            >>> client.read(membership_id='m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_membership_request.GetMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_membership_response.GetMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_membership.get_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.get_membership_request.GetMembershipRequest = {
            "membership_id": membership_id
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
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        membership_name: Optional[
            "capo_security_ir.types.membership_name.MembershipName"
        ] = None,
        incident_response_team: Optional[
            "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
        ] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        membership_accounts_configurations_update: Optional[
            "capo_security_ir.types.membership_accounts_configurations_update.MembershipAccountsConfigurationsUpdate"
        ] = None,
        undo_membership_cancellation: Optional[bool] = None,
    ) -> "capo_security_ir.types.update_membership_response.UpdateMembershipResponse":
        """<p>Updates membership configuration.</p>

        Args:
            membership_id: <p>Required element for UpdateMembership to identify the membership to update.</p>
            membership_name: <p>Optional element for UpdateMembership to update the membership name.</p>
            incident_response_team: <p>Optional element for UpdateMembership to update the membership name.</p>
            opt_in_features: <p>Optional element for UpdateMembership to enable or disable opt-in features for the service.</p>
            membership_accounts_configurations_update: <p>The <code>membershipAccountsConfigurationsUpdate</code> field in the <code>UpdateMembershipRequest</code> structure allows you to update the configuration settings for accounts within a membership. </p> <p>This field is optional and contains a structure of type <code>MembershipAccountsConfigurationsUpdate </code> that specifies the updated account configurations for the membership. </p>
            undo_membership_cancellation: <p>The <code>undoMembershipCancellation</code> parameter is a boolean flag that indicates whether to reverse a previously requested membership cancellation. When set to true, this will revoke the cancellation request and maintain the membership status. </p> <p>This parameter is optional and can be used in scenarios where you need to restore a membership that was marked for cancellation but hasn't been fully terminated yet. </p> <ul> <li> <p>If set to <code>true</code>, the cancellation request will be revoked </p> </li> <li> <p>If set to <code>false</code> the service will throw a ValidationException. </p> </li> </ul>

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
            Invoke UpdateMembership

            >>> client.update(membership_id='m-abcd1234efgh', membership_name='New membership name', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_membership_request.UpdateMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_membership_response.UpdateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_membership.update_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.update_membership_request.UpdateMembershipRequest = {
            "membership_id": membership_id
        }
        if membership_name is not None:
            input_["membership_name"] = membership_name
        if incident_response_team is not None:
            input_["incident_response_team"] = incident_response_team
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if membership_accounts_configurations_update is not None:
            input_["membership_accounts_configurations_update"] = (
                membership_accounts_configurations_update
            )
        if undo_membership_cancellation is not None:
            input_["undo_membership_cancellation"] = undo_membership_cancellation

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
    ) -> "capo_security_ir.types.list_memberships_response.ListMembershipsResponse":
        """<p>Returns the memberships that the calling principal can access.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListMemberships. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Request element for ListMemberships to limit the number of responses.</p>

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
            Invoke ListMemberships

            >>> client.list(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_memberships_request.ListMembershipsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_memberships_response.ListMembershipsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_memberships

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_memberships.list_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.list_memberships_request.ListMembershipsRequest = {}
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

    def batch_get_member_account_details(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        account_ids: "capo_security_ir.types.aws_account_ids.AWSAccountIds",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse":
        """<p>Provides information on whether the supplied account IDs are associated with a membership.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

        Args:
            membership_id: <p>Required element used in combination with BatchGetMemberAccountDetails to identify the membership ID to query. </p>
            account_ids: <p>Optional element to query the membership relationship status to a provided list of account IDs.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

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
            Invoke BatchGetMemberAccountDetails

            >>> client.batch_get_member_account_details(membership_id='m-abcd1234efgh', account_ids=['123412341234'])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.batch_get_member_account_details

            output, http_response = (
                capo_security_ir._operations.security_incident_response.batch_get_member_account_details.batch_get_member_account_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest = {
            "membership_id": membership_id,
            "account_ids": account_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_membership(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse":
        """<p>Cancels an existing membership.</p>

        Args:
            membership_id: <p>Required element used in combination with CancelMembershipRequest to identify the membership ID to cancel. </p>

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
            Invoke CancelMembership

            >>> client.cancel_membership(membership_id='m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.cancel_membership_request.CancelMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.cancel_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.cancel_membership.cancel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.cancel_membership_request.CancelMembershipRequest = {
            "membership_id": membership_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_finding_metrics(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
    ):
        """Returns finding-lifecycle metrics for a membership over a date range.

        Args:
            membership_id: The membership ID to retrieve metrics for.
            start_date: The start of the day-aligned UTC window, inclusive.
            end_date: The end of the day-aligned UTC window, inclusive.

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
            Retrieve finding-lifecycle metrics for a membership

            >>> client.get_finding_metrics(membership_id='m-a1b2c3d4e5f', start_date='2026-08-01T00:00:00Z', end_date='2026-08-18T00:00:00Z')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_finding_metrics

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_finding_metrics.get_finding_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest = {
            "membership_id": membership_id,
            "start_date": start_date,
            "end_date": end_date,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMembership:
    def __init__(self, service: AsyncSecurityIRClient) -> None:
        self._service = service

    async def create(
        self,
        membership_name: "capo_security_ir.types.membership_name.MembershipName",
        incident_response_team: "capo_security_ir.types.incident_response_team.IncidentResponseTeam",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
        cover_entire_organization: Optional[bool] = None,
    ) -> "capo_security_ir.types.create_membership_response.CreateMembershipResponse":
        """<p>Creates a new membership.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            membership_name: <p>Required element used in combination with CreateMembership to create a name for the membership.</p>
            incident_response_team: <p>Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership. </p>
            opt_in_features: <p>Optional element to enable the monitoring and investigation opt-in features for the service.</p>
            tags: <p>Optional element for customer configured tags.</p>
            cover_entire_organization: <p>The <code>coverEntireOrganization</code> parameter is a boolean flag that determines whether the membership should be applied to the entire Amazon Web Services Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts. </p> <p>This parameter is optional. If not specified, the default value is false.</p> <ul> <li> <p>If set to <i>true</i>: The membership will automatically include all existing and future accounts in the Amazon Web Services Organization. </p> </li> <li> <p>If set to <i>false</i>: The membership will only apply to explicitly specified accounts. </p> </li> </ul>

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
            Invoke CreateMembership

            >>> await client.create(membership_name='Example Membership Name.', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.create_membership_request.CreateMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.create_membership_response.CreateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_membership

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.create_membership_request.CreateMembershipRequest = {
            "membership_name": membership_name,
            "incident_response_team": incident_response_team,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if tags is not None:
            input_["tags"] = tags
        if cover_entire_organization is not None:
            input_["cover_entire_organization"] = cover_entire_organization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_membership_response.GetMembershipResponse":
        """<p>Returns the attributes of a membership.</p>

        Args:
            membership_id: <p>Required element for GetMembership to identify the membership ID to query.</p>

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
            Invoke GetMembership

            >>> await client.read(membership_id='m-abcd1234efgh')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.get_membership_request.GetMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.get_membership_response.GetMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_membership

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.get_membership.async_get_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.get_membership_request.GetMembershipRequest = {
            "membership_id": membership_id
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
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
        membership_name: Optional[
            "capo_security_ir.types.membership_name.MembershipName"
        ] = None,
        incident_response_team: Optional[
            "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
        ] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        membership_accounts_configurations_update: Optional[
            "capo_security_ir.types.membership_accounts_configurations_update.MembershipAccountsConfigurationsUpdate"
        ] = None,
        undo_membership_cancellation: Optional[bool] = None,
    ) -> "capo_security_ir.types.update_membership_response.UpdateMembershipResponse":
        """<p>Updates membership configuration.</p>

        Args:
            membership_id: <p>Required element for UpdateMembership to identify the membership to update.</p>
            membership_name: <p>Optional element for UpdateMembership to update the membership name.</p>
            incident_response_team: <p>Optional element for UpdateMembership to update the membership name.</p>
            opt_in_features: <p>Optional element for UpdateMembership to enable or disable opt-in features for the service.</p>
            membership_accounts_configurations_update: <p>The <code>membershipAccountsConfigurationsUpdate</code> field in the <code>UpdateMembershipRequest</code> structure allows you to update the configuration settings for accounts within a membership. </p> <p>This field is optional and contains a structure of type <code>MembershipAccountsConfigurationsUpdate </code> that specifies the updated account configurations for the membership. </p>
            undo_membership_cancellation: <p>The <code>undoMembershipCancellation</code> parameter is a boolean flag that indicates whether to reverse a previously requested membership cancellation. When set to true, this will revoke the cancellation request and maintain the membership status. </p> <p>This parameter is optional and can be used in scenarios where you need to restore a membership that was marked for cancellation but hasn't been fully terminated yet. </p> <ul> <li> <p>If set to <code>true</code>, the cancellation request will be revoked </p> </li> <li> <p>If set to <code>false</code> the service will throw a ValidationException. </p> </li> </ul>

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
            Invoke UpdateMembership

            >>> await client.update(membership_id='m-abcd1234efgh', membership_name='New membership name', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.update_membership_request.UpdateMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.update_membership_response.UpdateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_membership

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.update_membership.async_update_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.update_membership_request.UpdateMembershipRequest = {
            "membership_id": membership_id
        }
        if membership_name is not None:
            input_["membership_name"] = membership_name
        if incident_response_team is not None:
            input_["incident_response_team"] = incident_response_team
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if membership_accounts_configurations_update is not None:
            input_["membership_accounts_configurations_update"] = (
                membership_accounts_configurations_update
            )
        if undo_membership_cancellation is not None:
            input_["undo_membership_cancellation"] = undo_membership_cancellation

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
    ) -> "capo_security_ir.types.list_memberships_response.ListMembershipsResponse":
        """<p>Returns the memberships that the calling principal can access.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListMemberships. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Request element for ListMemberships to limit the number of responses.</p>

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
            Invoke ListMemberships

            >>> await client.list(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.list_memberships_request.ListMembershipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.list_memberships_response.ListMembershipsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_memberships

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.list_memberships_request.ListMembershipsRequest = {}
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

    async def batch_get_member_account_details(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        account_ids: "capo_security_ir.types.aws_account_ids.AWSAccountIds",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse":
        """<p>Provides information on whether the supplied account IDs are associated with a membership.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

        Args:
            membership_id: <p>Required element used in combination with BatchGetMemberAccountDetails to identify the membership ID to query. </p>
            account_ids: <p>Optional element to query the membership relationship status to a provided list of account IDs.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

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
            Invoke BatchGetMemberAccountDetails

            >>> await client.batch_get_member_account_details(membership_id='m-abcd1234efgh', account_ids=['123412341234'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.batch_get_member_account_details

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.batch_get_member_account_details.async_batch_get_member_account_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest = {
            "membership_id": membership_id,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_membership(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse":
        """<p>Cancels an existing membership.</p>

        Args:
            membership_id: <p>Required element used in combination with CancelMembershipRequest to identify the membership ID to cancel. </p>

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
            Invoke CancelMembership

            >>> await client.cancel_membership(membership_id='m-abcd1234efgh')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.cancel_membership_request.CancelMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.cancel_membership

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.cancel_membership.async_cancel_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.cancel_membership_request.CancelMembershipRequest = {
            "membership_id": membership_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_finding_metrics(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
    ):
        """Returns finding-lifecycle metrics for a membership over a date range.

        Args:
            membership_id: The membership ID to retrieve metrics for.
            start_date: The start of the day-aligned UTC window, inclusive.
            end_date: The end of the day-aligned UTC window, inclusive.

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
            Retrieve finding-lifecycle metrics for a membership

            >>> await client.get_finding_metrics(membership_id='m-a1b2c3d4e5f', start_date='2026-08-01T00:00:00Z', end_date='2026-08-18T00:00:00Z')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_finding_metrics

            (
                output,
                http_response,
            ) = await capo_security_ir._operations.security_incident_response.get_finding_metrics.async_get_finding_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest = {
            "membership_id": membership_id,
            "start_date": start_date,
            "end_date": end_date,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
