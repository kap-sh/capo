from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_mpa._auth._signers
import capo_mpa._auth._sigv4
from capo_mpa._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.approval_team_name
    import capo_mpa.types.approval_team_request_approvers
    import capo_mpa.types.create_approval_team_request
    import capo_mpa.types.create_approval_team_response
    import capo_mpa.types.delete_inactive_approval_team_version_request
    import capo_mpa.types.delete_inactive_approval_team_version_response
    import capo_mpa.types.description
    import capo_mpa.types.get_approval_team_request
    import capo_mpa.types.get_approval_team_response
    import capo_mpa.types.list_approval_teams_request
    import capo_mpa.types.list_approval_teams_response
    import capo_mpa.types.list_approval_teams_response_approval_team
    import capo_mpa.types.max_results
    import capo_mpa.types.policies_references
    import capo_mpa.types.start_active_approval_team_deletion_request
    import capo_mpa.types.start_active_approval_team_deletion_response
    import capo_mpa.types.start_approval_team_baseline_approver_ids
    import capo_mpa.types.start_approval_team_baseline_request
    import capo_mpa.types.start_approval_team_baseline_response
    import capo_mpa.types.string
    import capo_mpa.types.tags
    import capo_mpa.types.token
    import capo_mpa.types.update_actions
    import capo_mpa.types.update_approval_team_request
    import capo_mpa.types.update_approval_team_response
    from capo_mpa._services.async_mpa import AsyncMPAClient, AsyncMPAClientConfig
    from capo_mpa._services.mpa import MPAClient, MPAClientConfig


class ApprovalTeam:
    def __init__(self, service: MPAClient) -> None:
        self._service = service

    def create(
        self,
        approval_strategy: "capo_mpa.types.approval_strategy.ApprovalStrategy",
        approvers: "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers",
        description: "capo_mpa.types.description.Description",
        policies: "capo_mpa.types.policies_references.PoliciesReferences",
        name: "capo_mpa.types.approval_team_name.ApprovalTeamName",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        client_token: Optional["capo_mpa.types.token.Token"] = None,
        tags: Optional["capo_mpa.types.tags.Tags"] = None,
    ) -> "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse":
        """<p>Creates a new approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Approval team</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequesterApprovers</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            policies: <p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>
            name: <p>Name of the team.</p>
            tags: <p>Tags you want to attach to the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.create_approval_team

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.create_approval_team.create_approval_team(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest = {
            "approval_strategy": approval_strategy,
            "approvers": approvers,
            "description": description,
            "policies": policies,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse":
        """<p>Returns details for an approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_approval_team

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.get_approval_team.get_approval_team(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest = {
            "arn": arn
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
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        approval_strategy: Optional[
            "capo_mpa.types.approval_strategy.ApprovalStrategy"
        ] = None,
        approvers: Optional[
            "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers"
        ] = None,
        description: Optional["capo_mpa.types.description.Description"] = None,
        update_actions: Optional["capo_mpa.types.update_actions.UpdateActions"] = None,
    ) -> "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse":
        """<p>Updates an approval team. You can request to update the team description, approval threshold, and approvers in the team.</p> <note> <p> <b>Updates require team approval</b> </p> <p>Updates to an active team must be approved by the team.</p> </note>

        Args:
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequestApprover</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>
            update_actions: <p>A list of <code>UpdateAction</code> to perform when updating the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.update_approval_team

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.update_approval_team.update_approval_team(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest = {
            "arn": arn
        }
        if approval_strategy is not None:
            input_["approval_strategy"] = approval_strategy
        if approvers is not None:
            input_["approvers"] = approvers
        if description is not None:
            input_["description"] = description
        if update_actions is not None:
            input_["update_actions"] = update_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        version_id: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse":
        """<p>Deletes an inactive approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p> <p>You can also use this operation to delete a team draft. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/update-team.html#update-team-draft-status">Interacting with drafts</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            arn: <p>Amaazon Resource Name (ARN) for the team.</p>
            version_id: <p>Version ID for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version.delete_inactive_approval_team_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest = {
            "arn": arn,
            "version_id": version_id,
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
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse":
        """<p>Returns a list of approval teams.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_approval_teams

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_approval_teams.list_approval_teams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest = {}
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

    def start_active_approval_team_deletion(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        pending_window_days: Optional[int] = None,
    ) -> "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse":
        """<p>Starts the deletion process for an active approval team.</p> <note> <p> <b>Deletions require team approval</b> </p> <p>Requests to delete an active team must be approved by the team.</p> </note>

        Args:
            pending_window_days: <p>Number of days between when the team approves the delete request and when the team is deleted.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion.start_active_approval_team_deletion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest = {
            "arn": arn
        }
        if pending_window_days is not None:
            input_["pending_window_days"] = pending_window_days

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_approval_team_baseline(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        approver_ids: Optional[
            "capo_mpa.types.start_approval_team_baseline_approver_ids.StartApprovalTeamBaselineApproverIds"
        ] = None,
    ) -> "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse":
        """<p>Starts a baseline session for specified approvers on an <code>ACTIVE</code> approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            approver_ids: <p>Array of approver IDs.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline.start_approval_team_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest = {
            "arn": arn
        }
        if approver_ids is not None:
            input_["approver_ids"] = approver_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApprovalTeam:
    def __init__(self, service: AsyncMPAClient) -> None:
        self._service = service

    async def create(
        self,
        approval_strategy: "capo_mpa.types.approval_strategy.ApprovalStrategy",
        approvers: "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers",
        description: "capo_mpa.types.description.Description",
        policies: "capo_mpa.types.policies_references.PoliciesReferences",
        name: "capo_mpa.types.approval_team_name.ApprovalTeamName",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        client_token: Optional["capo_mpa.types.token.Token"] = None,
        tags: Optional["capo_mpa.types.tags.Tags"] = None,
    ) -> "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse":
        """<p>Creates a new approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Approval team</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequesterApprovers</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            policies: <p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>
            name: <p>Name of the team.</p>
            tags: <p>Tags you want to attach to the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.create_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.create_approval_team.async_create_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest = {
            "approval_strategy": approval_strategy,
            "approvers": approvers,
            "description": description,
            "policies": policies,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse":
        """<p>Returns details for an approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_approval_team.async_get_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest = {
            "arn": arn
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
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        approval_strategy: Optional[
            "capo_mpa.types.approval_strategy.ApprovalStrategy"
        ] = None,
        approvers: Optional[
            "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers"
        ] = None,
        description: Optional["capo_mpa.types.description.Description"] = None,
        update_actions: Optional["capo_mpa.types.update_actions.UpdateActions"] = None,
    ) -> "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse":
        """<p>Updates an approval team. You can request to update the team description, approval threshold, and approvers in the team.</p> <note> <p> <b>Updates require team approval</b> </p> <p>Updates to an active team must be approved by the team.</p> </note>

        Args:
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequestApprover</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>
            update_actions: <p>A list of <code>UpdateAction</code> to perform when updating the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.update_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.update_approval_team.async_update_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest = {
            "arn": arn
        }
        if approval_strategy is not None:
            input_["approval_strategy"] = approval_strategy
        if approvers is not None:
            input_["approvers"] = approvers
        if description is not None:
            input_["description"] = description
        if update_actions is not None:
            input_["update_actions"] = update_actions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        version_id: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse":
        """<p>Deletes an inactive approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p> <p>You can also use this operation to delete a team draft. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/update-team.html#update-team-draft-status">Interacting with drafts</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            arn: <p>Amaazon Resource Name (ARN) for the team.</p>
            version_id: <p>Version ID for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version.async_delete_inactive_approval_team_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest = {
            "arn": arn,
            "version_id": version_id,
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
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse":
        """<p>Returns a list of approval teams.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_approval_teams

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_approval_teams.async_list_approval_teams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest = {}
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

    async def start_active_approval_team_deletion(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        pending_window_days: Optional[int] = None,
    ) -> "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse":
        """<p>Starts the deletion process for an active approval team.</p> <note> <p> <b>Deletions require team approval</b> </p> <p>Requests to delete an active team must be approved by the team.</p> </note>

        Args:
            pending_window_days: <p>Number of days between when the team approves the delete request and when the team is deleted.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion.async_start_active_approval_team_deletion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest = {
            "arn": arn
        }
        if pending_window_days is not None:
            input_["pending_window_days"] = pending_window_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_approval_team_baseline(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        approver_ids: Optional[
            "capo_mpa.types.start_approval_team_baseline_approver_ids.StartApprovalTeamBaselineApproverIds"
        ] = None,
    ) -> "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse":
        """<p>Starts a baseline session for specified approvers on an <code>ACTIVE</code> approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            approver_ids: <p>Array of approver IDs.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline.async_start_approval_team_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest = {
            "arn": arn
        }
        if approver_ids is not None:
            input_["approver_ids"] = approver_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
