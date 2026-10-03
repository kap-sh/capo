from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.analysis_log_export_identifier
    import capo_cleanrooms.types.analysis_log_export_result_configuration
    import capo_cleanrooms.types.analysis_log_export_status
    import capo_cleanrooms.types.analysis_log_export_summary
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.compute_configuration
    import capo_cleanrooms.types.create_membership_input
    import capo_cleanrooms.types.create_membership_output
    import capo_cleanrooms.types.delete_membership_input
    import capo_cleanrooms.types.delete_membership_output
    import capo_cleanrooms.types.disallow_intermediate_table_input
    import capo_cleanrooms.types.disallow_intermediate_table_output
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.get_analysis_log_export_input
    import capo_cleanrooms.types.get_analysis_log_export_output
    import capo_cleanrooms.types.get_membership_input
    import capo_cleanrooms.types.get_membership_output
    import capo_cleanrooms.types.get_protected_job_input
    import capo_cleanrooms.types.get_protected_job_output
    import capo_cleanrooms.types.get_protected_query_input
    import capo_cleanrooms.types.get_protected_query_output
    import capo_cleanrooms.types.list_analysis_log_exports_input
    import capo_cleanrooms.types.list_analysis_log_exports_output
    import capo_cleanrooms.types.list_memberships_input
    import capo_cleanrooms.types.list_memberships_output
    import capo_cleanrooms.types.list_privacy_budgets_input
    import capo_cleanrooms.types.list_privacy_budgets_output
    import capo_cleanrooms.types.list_protected_jobs_input
    import capo_cleanrooms.types.list_protected_jobs_output
    import capo_cleanrooms.types.list_protected_queries_input
    import capo_cleanrooms.types.list_protected_queries_output
    import capo_cleanrooms.types.log_export_analysis_type
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.membership_job_log_status
    import capo_cleanrooms.types.membership_payment_configuration
    import capo_cleanrooms.types.membership_protected_job_result_configuration
    import capo_cleanrooms.types.membership_protected_query_result_configuration
    import capo_cleanrooms.types.membership_query_log_status
    import capo_cleanrooms.types.membership_status
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.preview_privacy_impact_input
    import capo_cleanrooms.types.preview_privacy_impact_output
    import capo_cleanrooms.types.preview_privacy_impact_parameters_input
    import capo_cleanrooms.types.privacy_budget_summary
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.protected_job_compute_configuration
    import capo_cleanrooms.types.protected_job_identifier
    import capo_cleanrooms.types.protected_job_parameters
    import capo_cleanrooms.types.protected_job_result_configuration_input
    import capo_cleanrooms.types.protected_job_status
    import capo_cleanrooms.types.protected_job_summary
    import capo_cleanrooms.types.protected_job_type
    import capo_cleanrooms.types.protected_query_identifier
    import capo_cleanrooms.types.protected_query_result_configuration
    import capo_cleanrooms.types.protected_query_sql_parameters
    import capo_cleanrooms.types.protected_query_status
    import capo_cleanrooms.types.protected_query_summary
    import capo_cleanrooms.types.protected_query_type
    import capo_cleanrooms.types.start_analysis_log_export_input
    import capo_cleanrooms.types.start_analysis_log_export_output
    import capo_cleanrooms.types.start_protected_job_input
    import capo_cleanrooms.types.start_protected_job_output
    import capo_cleanrooms.types.start_protected_query_input
    import capo_cleanrooms.types.start_protected_query_output
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.target_protected_job_status
    import capo_cleanrooms.types.target_protected_query_status
    import capo_cleanrooms.types.update_membership_input
    import capo_cleanrooms.types.update_membership_output
    import capo_cleanrooms.types.update_membership_payment_configuration
    import capo_cleanrooms.types.update_protected_job_input
    import capo_cleanrooms.types.update_protected_job_output
    import capo_cleanrooms.types.update_protected_query_input
    import capo_cleanrooms.types.update_protected_query_output
    import capo_cleanrooms.types.uuid
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class MembershipResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        query_log_status: "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        payment_configuration: Optional[
            "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput":
        """<p>Creates a membership for a specific collaboration identifier and joins the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique ID for the associated collaboration.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>
            payment_configuration: <p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>
            is_metrics_enabled: <p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.create_membership_input.CreateMembershipInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership.create_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_membership_input.CreateMembershipInput = {
            "collaboration_identifier": collaboration_identifier,
            "query_log_status": query_log_status,
        }
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if payment_configuration is not None:
            input_["payment_configuration"] = payment_configuration
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_membership_output.GetMembershipOutput":
        """<p>Retrieves a specified membership for an identifier.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_membership_input.GetMembershipInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_membership_output.GetMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership.get_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_membership_input.GetMembershipInput = {
            "membership_identifier": membership_identifier
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        query_log_status: Optional[
            "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        membership_payment_configuration: Optional[
            "capo_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
        ] = None,
    ) -> "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput":
        """<p>Updates a membership.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p> The default job result configuration.</p>
            membership_payment_configuration: <p>The payment configuration to update for the membership.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_membership_input.UpdateMembershipInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership.update_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_membership_input.UpdateMembershipInput = {
            "membership_identifier": membership_identifier
        }
        if query_log_status is not None:
            input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if membership_payment_configuration is not None:
            input_["membership_payment_configuration"] = (
                membership_payment_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput":
        """<p>Deletes a specified membership. All resources under a membership must be deleted.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership.delete_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput = {
            "membership_identifier": membership_identifier
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
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        status: Optional[
            "capo_cleanrooms.types.membership_status.MembershipStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput":
        """<p>Lists all memberships resources within the caller's account.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            status: <p>A filter which will return only memberships in the specified status.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_memberships_input.ListMembershipsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships.list_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_memberships_input.ListMembershipsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disallow_intermediate_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_name: "capo_cleanrooms.types.display_name.DisplayName",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        include_descendants: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput":
        """<p>Marks an intermediate table as invalid when it references the caller's base table. The data provider (base table owner) calls this operation, not the intermediate table owner. By default, the operation also marks all descendant intermediate tables as invalid.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table to disallow.</p>
            intermediate_table_name: <p>The name of the intermediate table to disallow.</p>
            include_descendants: <p>Specifies whether to cascade the disallow action to descendant intermediate tables. Default is <code>true</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table.disallow_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_name": intermediate_table_name,
        }
        if include_descendants is not None:
            input_["include_descendants"] = include_descendants

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_log_export_identifier: "capo_cleanrooms.types.analysis_log_export_identifier.AnalysisLogExportIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput":
        """<p>Returns information about an analysis log export, including its current status and, if the export failed, the reason for the failure.</p> <p>Poll this operation until the <code>status</code> is <code>SUCCESS</code> or <code>FAILED</code>. An export can't be canceled after it starts.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership that the analysis log export belongs to. Currently accepts the membership ID.</p>
            analysis_log_export_identifier: <p>The unique identifier of the analysis log export to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export.get_analysis_log_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_log_export_identifier": analysis_log_export_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput":
        """<p>Returns job processing metadata.</p>

        Args:
            membership_identifier: <p> The identifier for a membership in a protected job instance.</p>
            protected_job_identifier: <p> The identifier for the protected job instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job.get_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput":
        """<p>Returns query processing metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership in a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query.get_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_analysis_log_exports(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        analysis_identifier: Optional["capo_cleanrooms.types.uuid.UUID"] = None,
        status: Optional[
            "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput":
        """<p>Lists analysis log exports, sorted by the most recent export. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list analysis log exports for. Currently accepts the membership ID.</p>
            analysis_identifier: <p>A filter on the unique identifier of the protected query that the analysis logs were exported for.</p>
            status: <p>A filter on the status of the analysis log export.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports.list_analysis_log_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput = {
            "membership_identifier": membership_identifier
        }
        if analysis_identifier is not None:
            input_["analysis_identifier"] = analysis_identifier
        if status is not None:
            input_["status"] = status
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

    def list_privacy_budgets(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput":
        """<p>Returns detailed information about the privacy budgets in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_type: <p>The privacy budget type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets.list_privacy_budgets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_protected_jobs(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput":
        """<p>Lists protected jobs, sorted by most recent job.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected job.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs.list_protected_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    def list_protected_queries(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
    ):
        """<p>Lists protected queries, sorted by the most recent query.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected query.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries.list_protected_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    def preview_privacy_impact(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        parameters: "capo_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
    ):
        """<p>An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>
            parameters: <p>Specifies the desired epsilon and noise parameters to preview.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact.preview_privacy_impact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput = {
            "membership_identifier": membership_identifier,
            "parameters": parameters,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_id: "capo_cleanrooms.types.uuid.UUID",
        analysis_type: "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType",
        result_configuration: "capo_cleanrooms.types.analysis_log_export_result_configuration.AnalysisLogExportResultConfiguration",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput":
        """<p>Starts an export of the Apache Spark logs for a protected query to an Amazon S3 bucket that you own. Use the exported logs to diagnose a query that failed or that ran more slowly than you expected.</p> <p>Clean Rooms exports a redacted copy of the Spark logs instead of the raw logs. Analyze the exported logs with the tooling of your choice, such as Spark History Server. For details about what the exported logs contain, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html</a>.</p> <p>The export runs asynchronously and returns with a <code>status</code> of <code>IN_PROGRESS</code>. Call <code>GetAnalysisLogExport</code> to poll for the final status.</p> <important> <p>To use this operation, you must have the <code>CAN_EXPORT_QUERY_ANALYSIS_LOG</code> ability for your membership. You must also be the query runner or the query payer. Having the ability alone is not sufficient.</p> <p>The query must have reached a terminal state, and it must have reached the execution stage. A query that failed validation or that was canceled before it started produces no Spark logs.</p> <p>Log export isn't supported for queries that use differential privacy, and isn't supported for PySpark jobs.</p> <p>The destination bucket must be in the same Amazon Web Services Region as the collaboration. Cross-Region export isn't supported.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html</a>.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to export the analysis logs for. Currently accepts a membership ID.</p>
            analysis_id: <p>The unique identifier of the protected query that you want to export the analysis logs for.</p>
            analysis_type: <p>The type of analysis that the logs are exported for. Currently, only <code>PROTECTED_QUERY</code> is supported.</p>
            result_configuration: <p>The details needed to write the exported analysis logs.</p> <p>You don't need to create an IAM role for log export. Clean Rooms writes the exported logs using your own identity, so Clean Rooms writes the exported logs only where your existing permissions allow.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export.start_analysis_log_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_id": analysis_id,
            "analysis_type": analysis_type,
            "result_configuration": result_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_protected_job(
        self,
        type: "capo_cleanrooms.types.protected_job_type.ProtectedJobType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        job_parameters: "capo_cleanrooms.types.protected_job_parameters.ProtectedJobParameters",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
        ] = None,
        job_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput":
        """<p>Creates a protected job that is started by Clean Rooms.</p>

        Args:
            type: <p> The type of protected job to start.</p>
            membership_identifier: <p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>
            job_parameters: <p> The job parameters.</p>
            result_configuration: <p>The details needed to write the job results.</p>
            compute_configuration: <p>The compute configuration for the protected job.</p>
            job_compute_payer_account_id: <p>The account ID of the member that pays for the job compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job.start_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "job_parameters": job_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if job_compute_payer_account_id is not None:
            input_["job_compute_payer_account_id"] = job_compute_payer_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_protected_query(
        self,
        type: "capo_cleanrooms.types.protected_query_type.ProtectedQueryType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        sql_parameters: "capo_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.compute_configuration.ComputeConfiguration"
        ] = None,
        query_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput":
        """<p>Creates a protected query that is started by Clean Rooms.</p>

        Args:
            type: <p>The type of the protected query to be started.</p>
            membership_identifier: <p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>
            sql_parameters: <p>The protected SQL query parameters.</p>
            result_configuration: <p>The details needed to write the query results.</p>
            compute_configuration: <p> The compute configuration for the protected query.</p>
            query_compute_payer_account_id: <p>The account ID of the member that pays for the query compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query.start_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "sql_parameters": sql_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if query_compute_payer_account_id is not None:
            input_["query_compute_payer_account_id"] = query_compute_payer_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput":
        """<p>Updates the processing of a currently running job.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected job instance.</p>
            protected_job_identifier: <p> The identifier of the protected job to update.</p>
            target_status: <p>The target status of a protected job. Used to update the execution status of a currently running job.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job.update_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
            "target_status": target_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
    ):
        """<p>Updates the processing of a currently running query.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
            target_status: <p>The target status of a query. Used to update the execution status of a currently running query.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query.update_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
            "target_status": target_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMembershipResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        query_log_status: "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        payment_configuration: Optional[
            "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput":
        """<p>Creates a membership for a specific collaboration identifier and joins the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique ID for the associated collaboration.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>
            payment_configuration: <p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>
            is_metrics_enabled: <p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_membership_input.CreateMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_membership_input.CreateMembershipInput = {
            "collaboration_identifier": collaboration_identifier,
            "query_log_status": query_log_status,
        }
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if payment_configuration is not None:
            input_["payment_configuration"] = payment_configuration
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_membership_output.GetMembershipOutput":
        """<p>Retrieves a specified membership for an identifier.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_membership_input.GetMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_membership_output.GetMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership.async_get_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_membership_input.GetMembershipInput = {
            "membership_identifier": membership_identifier
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        query_log_status: Optional[
            "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        membership_payment_configuration: Optional[
            "capo_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
        ] = None,
    ) -> "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput":
        """<p>Updates a membership.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p> The default job result configuration.</p>
            membership_payment_configuration: <p>The payment configuration to update for the membership.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_membership_input.UpdateMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership.async_update_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_membership_input.UpdateMembershipInput = {
            "membership_identifier": membership_identifier
        }
        if query_log_status is not None:
            input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if membership_payment_configuration is not None:
            input_["membership_payment_configuration"] = (
                membership_payment_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput":
        """<p>Deletes a specified membership. All resources under a membership must be deleted.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership.async_delete_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput = {
            "membership_identifier": membership_identifier
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
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        status: Optional[
            "capo_cleanrooms.types.membership_status.MembershipStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput":
        """<p>Lists all memberships resources within the caller's account.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            status: <p>A filter which will return only memberships in the specified status.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_memberships_input.ListMembershipsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_memberships_input.ListMembershipsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disallow_intermediate_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_name: "capo_cleanrooms.types.display_name.DisplayName",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        include_descendants: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput":
        """<p>Marks an intermediate table as invalid when it references the caller's base table. The data provider (base table owner) calls this operation, not the intermediate table owner. By default, the operation also marks all descendant intermediate tables as invalid.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table to disallow.</p>
            intermediate_table_name: <p>The name of the intermediate table to disallow.</p>
            include_descendants: <p>Specifies whether to cascade the disallow action to descendant intermediate tables. Default is <code>true</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table.async_disallow_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_name": intermediate_table_name,
        }
        if include_descendants is not None:
            input_["include_descendants"] = include_descendants

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_log_export_identifier: "capo_cleanrooms.types.analysis_log_export_identifier.AnalysisLogExportIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput":
        """<p>Returns information about an analysis log export, including its current status and, if the export failed, the reason for the failure.</p> <p>Poll this operation until the <code>status</code> is <code>SUCCESS</code> or <code>FAILED</code>. An export can't be canceled after it starts.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership that the analysis log export belongs to. Currently accepts the membership ID.</p>
            analysis_log_export_identifier: <p>The unique identifier of the analysis log export to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export.async_get_analysis_log_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_log_export_identifier": analysis_log_export_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput":
        """<p>Returns job processing metadata.</p>

        Args:
            membership_identifier: <p> The identifier for a membership in a protected job instance.</p>
            protected_job_identifier: <p> The identifier for the protected job instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job.async_get_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput":
        """<p>Returns query processing metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership in a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query.async_get_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_analysis_log_exports(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        analysis_identifier: Optional["capo_cleanrooms.types.uuid.UUID"] = None,
        status: Optional[
            "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput":
        """<p>Lists analysis log exports, sorted by the most recent export. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list analysis log exports for. Currently accepts the membership ID.</p>
            analysis_identifier: <p>A filter on the unique identifier of the protected query that the analysis logs were exported for.</p>
            status: <p>A filter on the status of the analysis log export.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports.async_list_analysis_log_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput = {
            "membership_identifier": membership_identifier
        }
        if analysis_identifier is not None:
            input_["analysis_identifier"] = analysis_identifier
        if status is not None:
            input_["status"] = status
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

    async def list_privacy_budgets(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput":
        """<p>Returns detailed information about the privacy budgets in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_type: <p>The privacy budget type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets.async_list_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_protected_jobs(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput":
        """<p>Lists protected jobs, sorted by most recent job.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected job.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs.async_list_protected_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    async def list_protected_queries(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
    ):
        """<p>Lists protected queries, sorted by the most recent query.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected query.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries.async_list_protected_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    async def preview_privacy_impact(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        parameters: "capo_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
    ):
        """<p>An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>
            parameters: <p>Specifies the desired epsilon and noise parameters to preview.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact.async_preview_privacy_impact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput = {
            "membership_identifier": membership_identifier,
            "parameters": parameters,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_id: "capo_cleanrooms.types.uuid.UUID",
        analysis_type: "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType",
        result_configuration: "capo_cleanrooms.types.analysis_log_export_result_configuration.AnalysisLogExportResultConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput":
        """<p>Starts an export of the Apache Spark logs for a protected query to an Amazon S3 bucket that you own. Use the exported logs to diagnose a query that failed or that ran more slowly than you expected.</p> <p>Clean Rooms exports a redacted copy of the Spark logs instead of the raw logs. Analyze the exported logs with the tooling of your choice, such as Spark History Server. For details about what the exported logs contain, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html</a>.</p> <p>The export runs asynchronously and returns with a <code>status</code> of <code>IN_PROGRESS</code>. Call <code>GetAnalysisLogExport</code> to poll for the final status.</p> <important> <p>To use this operation, you must have the <code>CAN_EXPORT_QUERY_ANALYSIS_LOG</code> ability for your membership. You must also be the query runner or the query payer. Having the ability alone is not sufficient.</p> <p>The query must have reached a terminal state, and it must have reached the execution stage. A query that failed validation or that was canceled before it started produces no Spark logs.</p> <p>Log export isn't supported for queries that use differential privacy, and isn't supported for PySpark jobs.</p> <p>The destination bucket must be in the same Amazon Web Services Region as the collaboration. Cross-Region export isn't supported.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html</a>.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to export the analysis logs for. Currently accepts a membership ID.</p>
            analysis_id: <p>The unique identifier of the protected query that you want to export the analysis logs for.</p>
            analysis_type: <p>The type of analysis that the logs are exported for. Currently, only <code>PROTECTED_QUERY</code> is supported.</p>
            result_configuration: <p>The details needed to write the exported analysis logs.</p> <p>You don't need to create an IAM role for log export. Clean Rooms writes the exported logs using your own identity, so Clean Rooms writes the exported logs only where your existing permissions allow.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export.async_start_analysis_log_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_id": analysis_id,
            "analysis_type": analysis_type,
            "result_configuration": result_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_protected_job(
        self,
        type: "capo_cleanrooms.types.protected_job_type.ProtectedJobType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        job_parameters: "capo_cleanrooms.types.protected_job_parameters.ProtectedJobParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
        ] = None,
        job_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput":
        """<p>Creates a protected job that is started by Clean Rooms.</p>

        Args:
            type: <p> The type of protected job to start.</p>
            membership_identifier: <p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>
            job_parameters: <p> The job parameters.</p>
            result_configuration: <p>The details needed to write the job results.</p>
            compute_configuration: <p>The compute configuration for the protected job.</p>
            job_compute_payer_account_id: <p>The account ID of the member that pays for the job compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job.async_start_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "job_parameters": job_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if job_compute_payer_account_id is not None:
            input_["job_compute_payer_account_id"] = job_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_protected_query(
        self,
        type: "capo_cleanrooms.types.protected_query_type.ProtectedQueryType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        sql_parameters: "capo_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.compute_configuration.ComputeConfiguration"
        ] = None,
        query_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput":
        """<p>Creates a protected query that is started by Clean Rooms.</p>

        Args:
            type: <p>The type of the protected query to be started.</p>
            membership_identifier: <p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>
            sql_parameters: <p>The protected SQL query parameters.</p>
            result_configuration: <p>The details needed to write the query results.</p>
            compute_configuration: <p> The compute configuration for the protected query.</p>
            query_compute_payer_account_id: <p>The account ID of the member that pays for the query compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query.async_start_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "sql_parameters": sql_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if query_compute_payer_account_id is not None:
            input_["query_compute_payer_account_id"] = query_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput":
        """<p>Updates the processing of a currently running job.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected job instance.</p>
            protected_job_identifier: <p> The identifier of the protected job to update.</p>
            target_status: <p>The target status of a protected job. Used to update the execution status of a currently running job.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job.async_update_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
            "target_status": target_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
    ):
        """<p>Updates the processing of a currently running query.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
            target_status: <p>The target status of a query. Used to update the execution status of a currently running query.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query.async_update_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
            "target_status": target_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
