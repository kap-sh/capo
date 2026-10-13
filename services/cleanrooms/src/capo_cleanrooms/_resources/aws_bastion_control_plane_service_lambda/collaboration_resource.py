from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.allowed_result_regions
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.analysis_template_arn_list
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.auto_approved_change_type_list
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_input
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_output
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_input
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_output
    import capo_cleanrooms.types.batch_get_schema_input
    import capo_cleanrooms.types.batch_get_schema_output
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.change_input_list
    import capo_cleanrooms.types.change_request_action
    import capo_cleanrooms.types.change_request_status
    import capo_cleanrooms.types.collaboration_change_request_identifier
    import capo_cleanrooms.types.collaboration_change_request_summary
    import capo_cleanrooms.types.collaboration_configured_audience_model_association_summary
    import capo_cleanrooms.types.collaboration_description
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.collaboration_job_log_status
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.collaboration_privacy_budget_summary
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary
    import capo_cleanrooms.types.collaboration_query_log_status
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.create_collaboration_change_request_input
    import capo_cleanrooms.types.create_collaboration_change_request_output
    import capo_cleanrooms.types.create_collaboration_input
    import capo_cleanrooms.types.create_collaboration_output
    import capo_cleanrooms.types.data_encryption_metadata
    import capo_cleanrooms.types.delete_collaboration_input
    import capo_cleanrooms.types.delete_collaboration_output
    import capo_cleanrooms.types.delete_member_input
    import capo_cleanrooms.types.delete_member_output
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.filterable_member_status
    import capo_cleanrooms.types.get_collaboration_analysis_template_input
    import capo_cleanrooms.types.get_collaboration_analysis_template_output
    import capo_cleanrooms.types.get_collaboration_change_request_input
    import capo_cleanrooms.types.get_collaboration_change_request_output
    import capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input
    import capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output
    import capo_cleanrooms.types.get_collaboration_id_namespace_association_input
    import capo_cleanrooms.types.get_collaboration_id_namespace_association_output
    import capo_cleanrooms.types.get_collaboration_input
    import capo_cleanrooms.types.get_collaboration_output
    import capo_cleanrooms.types.get_collaboration_privacy_budget_template_input
    import capo_cleanrooms.types.get_collaboration_privacy_budget_template_output
    import capo_cleanrooms.types.get_schema_analysis_rule_input
    import capo_cleanrooms.types.get_schema_analysis_rule_output
    import capo_cleanrooms.types.get_schema_input
    import capo_cleanrooms.types.get_schema_output
    import capo_cleanrooms.types.id_namespace_association_identifier
    import capo_cleanrooms.types.list_collaboration_analysis_templates_input
    import capo_cleanrooms.types.list_collaboration_analysis_templates_output
    import capo_cleanrooms.types.list_collaboration_change_requests_input
    import capo_cleanrooms.types.list_collaboration_change_requests_output
    import capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input
    import capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output
    import capo_cleanrooms.types.list_collaboration_id_namespace_associations_input
    import capo_cleanrooms.types.list_collaboration_id_namespace_associations_output
    import capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input
    import capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output
    import capo_cleanrooms.types.list_collaboration_privacy_budgets_input
    import capo_cleanrooms.types.list_collaboration_privacy_budgets_output
    import capo_cleanrooms.types.list_collaborations_input
    import capo_cleanrooms.types.list_collaborations_output
    import capo_cleanrooms.types.list_members_input
    import capo_cleanrooms.types.list_members_output
    import capo_cleanrooms.types.list_schemas_input
    import capo_cleanrooms.types.list_schemas_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.member_list
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.payment_configuration
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.schema_analysis_rule_request_list
    import capo_cleanrooms.types.schema_type
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_alias_list
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_collaboration_change_request_input
    import capo_cleanrooms.types.update_collaboration_change_request_output
    import capo_cleanrooms.types.update_collaboration_input
    import capo_cleanrooms.types.update_collaboration_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class CollaborationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        members: "capo_cleanrooms.types.member_list.MemberList",
        name: "capo_cleanrooms.types.collaboration_name.CollaborationName",
        creator_member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities",
        creator_display_name: "capo_cleanrooms.types.display_name.DisplayName",
        query_log_status: "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        creator_ml_member_abilities: Optional[
            "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
        ] = None,
        data_encryption_metadata: Optional[
            "capo_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        creator_payment_configuration: Optional[
            "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
        auto_approved_change_request_types: Optional[
            "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
        ] = None,
        allowed_result_regions: Optional[
            "capo_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput":
        """<p>Creates a new collaboration.</p>

        Args:
            members: <p>A list of initial members, not including the creator. This list is immutable.</p>
            name: <p>The display name for a collaboration.</p>
            description: <p>A description of the collaboration provided by the collaboration owner.</p>
            creator_member_abilities: <p>The abilities granted to the collaboration creator.</p>
            creator_ml_member_abilities: <p>The ML abilities granted to the collaboration creator.</p>
            creator_display_name: <p>The display name of the collaboration creator.</p>
            data_encryption_metadata: <p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            creator_payment_configuration: <p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>
            analytics_engine: <p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>
            auto_approved_change_request_types: <p>The types of change requests that are automatically approved for this collaboration.</p>
            allowed_result_regions: <p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>
            is_metrics_enabled: <p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration.create_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCollaboration")
        )
        input_: capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput = {
            "members": members,
            "name": name,
            "creator_member_abilities": creator_member_abilities,
            "creator_display_name": creator_display_name,
            "query_log_status": query_log_status,
        }
        if description is not None:
            input_["description"] = description
        if creator_ml_member_abilities is not None:
            input_["creator_ml_member_abilities"] = creator_ml_member_abilities
        if data_encryption_metadata is not None:
            input_["data_encryption_metadata"] = data_encryption_metadata
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if creator_payment_configuration is not None:
            input_["creator_payment_configuration"] = creator_payment_configuration
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine
        if auto_approved_change_request_types is not None:
            input_["auto_approved_change_request_types"] = (
                auto_approved_change_request_types
            )
        if allowed_result_regions is not None:
            input_["allowed_result_regions"] = allowed_result_regions
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
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput":
        """<p>Returns metadata about a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration.get_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaboration")
        )
        input_: capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
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
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.collaboration_name.CollaborationName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput":
        """<p>Updates collaboration metadata and can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>
            name: <p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>
            description: <p>A description of the collaboration.</p>
            analytics_engine: <p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration.update_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCollaboration")
        )
        input_: capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput":
        """<p>Deletes a collaboration. It can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration.delete_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCollaboration")
        )
        input_: capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
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
        member_status: Optional[
            "capo_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput":
        """<p>Lists collaborations the caller owns, is active in, or has been invited to.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            member_status: <p>The caller's status in a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations.list_collaborations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborations")
        )
        input_: capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if member_status is not None:
            input_["member_status"] = member_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arns: "capo_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arns: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template.batch_get_collaboration_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.batch_get_collaboration_analysis_template_output

            return capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "BatchGetCollaborationAnalysisTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arns": analysis_template_arns,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        names: "capo_cleanrooms.types.table_alias_list.TableAliasList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput":
        """<p>Retrieves multiple schemas by their identifiers.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>
            names: <p>The names for the schema objects to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema.batch_get_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSchema")
        )
        input_: capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "names": names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        schema_analysis_rule_requests: "capo_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput":
        """<p>Retrieves multiple analysis rule schemas.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the schema analysis rule.</p>
            schema_analysis_rule_requests: <p>The information that's necessary to retrieve a schema analysis rule.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule.batch_get_schema_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSchemaAnalysisRule")
        )
        input_: capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "schema_analysis_rule_requests": schema_analysis_rule_requests,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        changes: "capo_cleanrooms.types.change_input_list.ChangeInputList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput":
        """<p>Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            changes: <p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request.create_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "changes": changes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_member(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        account_id: "capo_cleanrooms.types.account_id.AccountId",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput":
        """<p>Removes the specified member from a collaboration. The removed member is placed in the Removed status and can't interact with the collaboration. The removed member's data is inaccessible to active members of the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier for the associated collaboration.</p>
            account_id: <p>The account ID of the member to remove.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.delete_member_input.DeleteMemberInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member.delete_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMember")
        )
        input_: capo_cleanrooms.types.delete_member_input.DeleteMemberInput = {
            "collaboration_identifier": collaboration_identifier,
            "account_id": account_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves an analysis template within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arn: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template.get_collaboration_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_collaboration_analysis_template_output

            return capo_cleanrooms.types.get_collaboration_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCollaborationAnalysisTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arn": analysis_template_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput":
        """<p>Retrieves detailed information about a specific collaboration change request.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            change_request_identifier: <p>A unique identifier for the change request to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request.get_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collaboration_configured_audience_model_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput":
        """<p>Retrieves a configured audience model association within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association.get_collaboration_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCollaborationConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collaboration_id_namespace_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association from a specific collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association.get_collaboration_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "id_namespace_association_identifier": id_namespace_association_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collaboration_privacy_budget_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput":
        """<p>Returns details about a specified privacy budget template.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_template_identifier: <p>A unique identifier for one of your privacy budget templates.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template.get_collaboration_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationPrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_output.GetSchemaOutput":
        """<p>Retrieves the schema for a relation within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the relation to retrieve the schema for.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_schema_input.GetSchemaInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_schema_output.GetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema.get_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchema")
        )
        input_: capo_cleanrooms.types.get_schema_input.GetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput":
        """<p>Retrieves a schema analysis rule.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the schema to retrieve the analysis rule for.</p>
            type: <p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule.get_schema_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchemaAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
            "type": type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_collaboration_analysis_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput":
        """<p>Lists analysis templates within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates.list_collaboration_analysis_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationAnalysisTemplates")
        )
        input_: capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_collaboration_change_requests(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput":
        """<p>Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            status: <p>A filter to only return change requests with the specified status.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests.list_collaboration_change_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationChangeRequests")
        )
        input_: capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        """<p>Lists configured audience model associations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations.list_collaboration_configured_audience_model_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationConfiguredAudienceModelAssociations"),
        )
        input_: capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput":
        """<p>Returns a list of the ID namespace associations in a collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations.list_collaboration_id_namespace_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationIdNamespaceAssociations"),
        )
        input_: capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput":
        """<p>Returns an array that summarizes each privacy budget in a specified collaboration. The summary includes the collaboration ARN, creation time, creating account, and privacy budget details.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets.list_collaboration_privacy_budgets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationPrivacyBudgets")
        )
        input_: capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput":
        """<p>Returns an array that summarizes each privacy budget template in a specified collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates.list_collaboration_privacy_budget_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationPrivacyBudgetTemplates"),
        )
        input_: capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_members(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_members_output.ListMembersOutput":
        """<p>Lists all members within a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration in which the members are listed.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_members_input.ListMembersInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_members_output.ListMembersOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMembers")
        )
        input_: capo_cleanrooms.types.list_members_input.ListMembersInput = {
            "collaboration_identifier": collaboration_identifier
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

    def list_schemas(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        schema_type: Optional["capo_cleanrooms.types.schema_type.SchemaType"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput":
        """<p>Lists the schemas for relations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            schema_type: <p>If present, filter schemas by schema type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_schemas_input.ListSchemasInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas.list_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSchemas")
        )
        input_: capo_cleanrooms.types.list_schemas_input.ListSchemasInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if schema_type is not None:
            input_["schema_type"] = schema_type
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

    def update_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        action: "capo_cleanrooms.types.change_request_action.ChangeRequestAction",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput":
        """<p>Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the change request to be updated.</p>
            change_request_identifier: <p>The unique identifier of the specific change request to be updated within the collaboration.</p>
            action: <p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request.update_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
            "action": action,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCollaborationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        members: "capo_cleanrooms.types.member_list.MemberList",
        name: "capo_cleanrooms.types.collaboration_name.CollaborationName",
        creator_member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities",
        creator_display_name: "capo_cleanrooms.types.display_name.DisplayName",
        query_log_status: "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        creator_ml_member_abilities: Optional[
            "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
        ] = None,
        data_encryption_metadata: Optional[
            "capo_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        creator_payment_configuration: Optional[
            "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
        auto_approved_change_request_types: Optional[
            "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
        ] = None,
        allowed_result_regions: Optional[
            "capo_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput":
        """<p>Creates a new collaboration.</p>

        Args:
            members: <p>A list of initial members, not including the creator. This list is immutable.</p>
            name: <p>The display name for a collaboration.</p>
            description: <p>A description of the collaboration provided by the collaboration owner.</p>
            creator_member_abilities: <p>The abilities granted to the collaboration creator.</p>
            creator_ml_member_abilities: <p>The ML abilities granted to the collaboration creator.</p>
            creator_display_name: <p>The display name of the collaboration creator.</p>
            data_encryption_metadata: <p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            creator_payment_configuration: <p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>
            analytics_engine: <p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>
            auto_approved_change_request_types: <p>The types of change requests that are automatically approved for this collaboration.</p>
            allowed_result_regions: <p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>
            is_metrics_enabled: <p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration.async_create_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCollaboration")
        )
        input_: capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput = {
            "members": members,
            "name": name,
            "creator_member_abilities": creator_member_abilities,
            "creator_display_name": creator_display_name,
            "query_log_status": query_log_status,
        }
        if description is not None:
            input_["description"] = description
        if creator_ml_member_abilities is not None:
            input_["creator_ml_member_abilities"] = creator_ml_member_abilities
        if data_encryption_metadata is not None:
            input_["data_encryption_metadata"] = data_encryption_metadata
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if creator_payment_configuration is not None:
            input_["creator_payment_configuration"] = creator_payment_configuration
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine
        if auto_approved_change_request_types is not None:
            input_["auto_approved_change_request_types"] = (
                auto_approved_change_request_types
            )
        if allowed_result_regions is not None:
            input_["allowed_result_regions"] = allowed_result_regions
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
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput":
        """<p>Returns metadata about a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration.async_get_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaboration")
        )
        input_: capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
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
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.collaboration_name.CollaborationName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput":
        """<p>Updates collaboration metadata and can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>
            name: <p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>
            description: <p>A description of the collaboration.</p>
            analytics_engine: <p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration.async_update_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCollaboration")
        )
        input_: capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput":
        """<p>Deletes a collaboration. It can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration.async_delete_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCollaboration")
        )
        input_: capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
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
        member_status: Optional[
            "capo_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput":
        """<p>Lists collaborations the caller owns, is active in, or has been invited to.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            member_status: <p>The caller's status in a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations.async_list_collaborations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborations")
        )
        input_: capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if member_status is not None:
            input_["member_status"] = member_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arns: "capo_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arns: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template.async_batch_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.batch_get_collaboration_analysis_template_output

            return capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "BatchGetCollaborationAnalysisTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arns": analysis_template_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        names: "capo_cleanrooms.types.table_alias_list.TableAliasList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput":
        """<p>Retrieves multiple schemas by their identifiers.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>
            names: <p>The names for the schema objects to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema.async_batch_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSchema")
        )
        input_: capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "names": names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        schema_analysis_rule_requests: "capo_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput":
        """<p>Retrieves multiple analysis rule schemas.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the schema analysis rule.</p>
            schema_analysis_rule_requests: <p>The information that's necessary to retrieve a schema analysis rule.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule.async_batch_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSchemaAnalysisRule")
        )
        input_: capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "schema_analysis_rule_requests": schema_analysis_rule_requests,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        changes: "capo_cleanrooms.types.change_input_list.ChangeInputList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput":
        """<p>Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            changes: <p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request.async_create_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "changes": changes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_member(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        account_id: "capo_cleanrooms.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput":
        """<p>Removes the specified member from a collaboration. The removed member is placed in the Removed status and can't interact with the collaboration. The removed member's data is inaccessible to active members of the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier for the associated collaboration.</p>
            account_id: <p>The account ID of the member to remove.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_member_input.DeleteMemberInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member.async_delete_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMember")
        )
        input_: capo_cleanrooms.types.delete_member_input.DeleteMemberInput = {
            "collaboration_identifier": collaboration_identifier,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves an analysis template within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arn: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template.async_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_collaboration_analysis_template_output

            return capo_cleanrooms.types.get_collaboration_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetCollaborationAnalysisTemplate", redact_output=_redact_output
            ),
        )
        input_: capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arn": analysis_template_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput":
        """<p>Retrieves detailed information about a specific collaboration change request.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            change_request_identifier: <p>A unique identifier for the change request to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request.async_get_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_configured_audience_model_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput":
        """<p>Retrieves a configured audience model association within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association.async_get_collaboration_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCollaborationConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_id_namespace_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association from a specific collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association.async_get_collaboration_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "id_namespace_association_identifier": id_namespace_association_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_privacy_budget_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput":
        """<p>Returns details about a specified privacy budget template.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_template_identifier: <p>A unique identifier for one of your privacy budget templates.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template.async_get_collaboration_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationPrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_output.GetSchemaOutput":
        """<p>Retrieves the schema for a relation within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the relation to retrieve the schema for.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_schema_input.GetSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_schema_output.GetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema.async_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchema")
        )
        input_: capo_cleanrooms.types.get_schema_input.GetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput":
        """<p>Retrieves a schema analysis rule.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the schema to retrieve the analysis rule for.</p>
            type: <p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule.async_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchemaAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_collaboration_analysis_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput":
        """<p>Lists analysis templates within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates.async_list_collaboration_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationAnalysisTemplates")
        )
        input_: capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_collaboration_change_requests(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput":
        """<p>Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            status: <p>A filter to only return change requests with the specified status.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests.async_list_collaboration_change_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationChangeRequests")
        )
        input_: capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        """<p>Lists configured audience model associations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations.async_list_collaboration_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationConfiguredAudienceModelAssociations"),
        )
        input_: capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput":
        """<p>Returns a list of the ID namespace associations in a collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations.async_list_collaboration_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationIdNamespaceAssociations"),
        )
        input_: capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput":
        """<p>Returns an array that summarizes each privacy budget in a specified collaboration. The summary includes the collaboration ARN, creation time, creating account, and privacy budget details.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets.async_list_collaboration_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollaborationPrivacyBudgets")
        )
        input_: capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput":
        """<p>Returns an array that summarizes each privacy budget template in a specified collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates.async_list_collaboration_privacy_budget_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCollaborationPrivacyBudgetTemplates"),
        )
        input_: capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_members(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_members_output.ListMembersOutput":
        """<p>Lists all members within a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration in which the members are listed.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_members_input.ListMembersInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_members_output.ListMembersOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMembers")
        )
        input_: capo_cleanrooms.types.list_members_input.ListMembersInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_schemas(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        schema_type: Optional["capo_cleanrooms.types.schema_type.SchemaType"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput":
        """<p>Lists the schemas for relations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            schema_type: <p>If present, filter schemas by schema type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_schemas_input.ListSchemasInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSchemas")
        )
        input_: capo_cleanrooms.types.list_schemas_input.ListSchemasInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if schema_type is not None:
            input_["schema_type"] = schema_type
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

    async def update_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        action: "capo_cleanrooms.types.change_request_action.ChangeRequestAction",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput":
        """<p>Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the change request to be updated.</p>
            change_request_identifier: <p>The unique identifier of the specific change request to be updated within the collaboration.</p>
            action: <p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request.async_update_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCollaborationChangeRequest")
        )
        input_: capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
            "action": action,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
