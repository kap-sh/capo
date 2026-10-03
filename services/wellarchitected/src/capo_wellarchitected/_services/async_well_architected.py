"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WellArchitectedApiServiceLambda``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_wellarchitected._auth._signers
import capo_wellarchitected._auth._sigv4
from capo_wellarchitected._auth._identity import Credentials
from capo_wellarchitected._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_wellarchitected._auth._zapros_handler import AuthMiddleware
from capo_wellarchitected._pagination import resolve_path as _resolve_path
from capo_wellarchitected._services._aws_config import aaws_config
from capo_wellarchitected._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_jira_configuration_input
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.agent_profile_summary
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.agent_recommendation_generation_summary
    import capo_wellarchitected.types.agent_recommendation_item_summary
    import capo_wellarchitected.types.agent_recommendation_summary
    import capo_wellarchitected.types.aggregation_configurations
    import capo_wellarchitected.types.answer_reason
    import capo_wellarchitected.types.associate_lenses_input
    import capo_wellarchitected.types.associate_profiles_input
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.choice_updates
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.context_content
    import capo_wellarchitected.types.context_summary
    import capo_wellarchitected.types.context_type
    import capo_wellarchitected.types.create_agent_context_request
    import capo_wellarchitected.types.create_agent_context_response
    import capo_wellarchitected.types.create_agent_goal_request
    import capo_wellarchitected.types.create_agent_goal_response
    import capo_wellarchitected.types.create_agent_profile_request
    import capo_wellarchitected.types.create_agent_profile_response
    import capo_wellarchitected.types.create_lens_share_input
    import capo_wellarchitected.types.create_lens_share_output
    import capo_wellarchitected.types.create_lens_version_input
    import capo_wellarchitected.types.create_lens_version_output
    import capo_wellarchitected.types.create_milestone_input
    import capo_wellarchitected.types.create_milestone_output
    import capo_wellarchitected.types.create_profile_input
    import capo_wellarchitected.types.create_profile_output
    import capo_wellarchitected.types.create_profile_share_input
    import capo_wellarchitected.types.create_profile_share_output
    import capo_wellarchitected.types.create_review_template_input
    import capo_wellarchitected.types.create_review_template_output
    import capo_wellarchitected.types.create_template_share_input
    import capo_wellarchitected.types.create_template_share_output
    import capo_wellarchitected.types.create_workload_input
    import capo_wellarchitected.types.create_workload_output
    import capo_wellarchitected.types.create_workload_share_input
    import capo_wellarchitected.types.create_workload_share_output
    import capo_wellarchitected.types.delete_agent_context_request
    import capo_wellarchitected.types.delete_agent_context_response
    import capo_wellarchitected.types.delete_agent_goal_request
    import capo_wellarchitected.types.delete_agent_goal_response
    import capo_wellarchitected.types.delete_agent_profile_request
    import capo_wellarchitected.types.delete_agent_profile_response
    import capo_wellarchitected.types.delete_lens_input
    import capo_wellarchitected.types.delete_lens_share_input
    import capo_wellarchitected.types.delete_profile_input
    import capo_wellarchitected.types.delete_profile_share_input
    import capo_wellarchitected.types.delete_review_template_input
    import capo_wellarchitected.types.delete_template_share_input
    import capo_wellarchitected.types.delete_workload_input
    import capo_wellarchitected.types.delete_workload_share_input
    import capo_wellarchitected.types.disassociate_lenses_input
    import capo_wellarchitected.types.disassociate_profiles_input
    import capo_wellarchitected.types.discovery_integration_status
    import capo_wellarchitected.types.export_lens_input
    import capo_wellarchitected.types.export_lens_output
    import capo_wellarchitected.types.feedback_category
    import capo_wellarchitected.types.get_agent_context_request
    import capo_wellarchitected.types.get_agent_context_response
    import capo_wellarchitected.types.get_agent_goal_request
    import capo_wellarchitected.types.get_agent_goal_response
    import capo_wellarchitected.types.get_agent_profile_request
    import capo_wellarchitected.types.get_agent_profile_response
    import capo_wellarchitected.types.get_agent_recommendation_generation_request
    import capo_wellarchitected.types.get_agent_recommendation_generation_response
    import capo_wellarchitected.types.get_agent_recommendation_request
    import capo_wellarchitected.types.get_agent_recommendation_response
    import capo_wellarchitected.types.get_answer_input
    import capo_wellarchitected.types.get_answer_output
    import capo_wellarchitected.types.get_consolidated_report_input
    import capo_wellarchitected.types.get_consolidated_report_output
    import capo_wellarchitected.types.get_global_settings_output
    import capo_wellarchitected.types.get_lens_input
    import capo_wellarchitected.types.get_lens_output
    import capo_wellarchitected.types.get_lens_review_input
    import capo_wellarchitected.types.get_lens_review_output
    import capo_wellarchitected.types.get_lens_review_report_input
    import capo_wellarchitected.types.get_lens_review_report_output
    import capo_wellarchitected.types.get_lens_version_difference_input
    import capo_wellarchitected.types.get_lens_version_difference_output
    import capo_wellarchitected.types.get_milestone_input
    import capo_wellarchitected.types.get_milestone_output
    import capo_wellarchitected.types.get_profile_input
    import capo_wellarchitected.types.get_profile_output
    import capo_wellarchitected.types.get_profile_template_input
    import capo_wellarchitected.types.get_profile_template_output
    import capo_wellarchitected.types.get_review_template_answer_input
    import capo_wellarchitected.types.get_review_template_answer_output
    import capo_wellarchitected.types.get_review_template_input
    import capo_wellarchitected.types.get_review_template_lens_review_input
    import capo_wellarchitected.types.get_review_template_lens_review_output
    import capo_wellarchitected.types.get_review_template_output
    import capo_wellarchitected.types.get_workload_input
    import capo_wellarchitected.types.get_workload_output
    import capo_wellarchitected.types.goal_summary
    import capo_wellarchitected.types.import_lens_input
    import capo_wellarchitected.types.import_lens_output
    import capo_wellarchitected.types.include_shared_resources
    import capo_wellarchitected.types.integrating_service
    import capo_wellarchitected.types.is_applicable
    import capo_wellarchitected.types.is_major_version
    import capo_wellarchitected.types.is_review_owner_update_acknowledged
    import capo_wellarchitected.types.jira_selected_question_configuration
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_aliases
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_json
    import capo_wellarchitected.types.lens_name
    import capo_wellarchitected.types.lens_name_prefix
    import capo_wellarchitected.types.lens_status_type
    import capo_wellarchitected.types.lens_type
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.list_agent_contexts_request
    import capo_wellarchitected.types.list_agent_contexts_response
    import capo_wellarchitected.types.list_agent_goals_request
    import capo_wellarchitected.types.list_agent_goals_response
    import capo_wellarchitected.types.list_agent_profiles_request
    import capo_wellarchitected.types.list_agent_profiles_response
    import capo_wellarchitected.types.list_agent_recommendation_generations_request
    import capo_wellarchitected.types.list_agent_recommendation_generations_response
    import capo_wellarchitected.types.list_agent_recommendation_items_request
    import capo_wellarchitected.types.list_agent_recommendation_items_response
    import capo_wellarchitected.types.list_agent_recommendations_request
    import capo_wellarchitected.types.list_agent_recommendations_response
    import capo_wellarchitected.types.list_answers_input
    import capo_wellarchitected.types.list_answers_output
    import capo_wellarchitected.types.list_check_details_input
    import capo_wellarchitected.types.list_check_details_output
    import capo_wellarchitected.types.list_check_summaries_input
    import capo_wellarchitected.types.list_check_summaries_output
    import capo_wellarchitected.types.list_lens_review_improvements_input
    import capo_wellarchitected.types.list_lens_review_improvements_output
    import capo_wellarchitected.types.list_lens_reviews_input
    import capo_wellarchitected.types.list_lens_reviews_output
    import capo_wellarchitected.types.list_lens_shares_input
    import capo_wellarchitected.types.list_lens_shares_output
    import capo_wellarchitected.types.list_lenses_input
    import capo_wellarchitected.types.list_lenses_output
    import capo_wellarchitected.types.list_milestones_input
    import capo_wellarchitected.types.list_milestones_output
    import capo_wellarchitected.types.list_notifications_input
    import capo_wellarchitected.types.list_notifications_output
    import capo_wellarchitected.types.list_profile_notifications_input
    import capo_wellarchitected.types.list_profile_notifications_output
    import capo_wellarchitected.types.list_profile_shares_input
    import capo_wellarchitected.types.list_profile_shares_output
    import capo_wellarchitected.types.list_profiles_input
    import capo_wellarchitected.types.list_profiles_output
    import capo_wellarchitected.types.list_review_template_answers_input
    import capo_wellarchitected.types.list_review_template_answers_output
    import capo_wellarchitected.types.list_review_templates_input
    import capo_wellarchitected.types.list_review_templates_output
    import capo_wellarchitected.types.list_share_invitations_input
    import capo_wellarchitected.types.list_share_invitations_output
    import capo_wellarchitected.types.list_tags_for_resource_input
    import capo_wellarchitected.types.list_tags_for_resource_output
    import capo_wellarchitected.types.list_template_shares_input
    import capo_wellarchitected.types.list_template_shares_output
    import capo_wellarchitected.types.list_workload_shares_input
    import capo_wellarchitected.types.list_workload_shares_output
    import capo_wellarchitected.types.list_workloads_input
    import capo_wellarchitected.types.list_workloads_output
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.milestone_name
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.organization_sharing_status
    import capo_wellarchitected.types.permission_type
    import capo_wellarchitected.types.pillar
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.pillar_notes
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_arns
    import capo_wellarchitected.types.profile_description
    import capo_wellarchitected.types.profile_name
    import capo_wellarchitected.types.profile_name_prefix
    import capo_wellarchitected.types.profile_owner_type
    import capo_wellarchitected.types.profile_question_updates
    import capo_wellarchitected.types.profile_version
    import capo_wellarchitected.types.put_agent_recommendation_feedback_request
    import capo_wellarchitected.types.put_agent_recommendation_feedback_response
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_priority
    import capo_wellarchitected.types.recommendation_feedback_type
    import capo_wellarchitected.types.recommendation_item_type
    import capo_wellarchitected.types.recommendation_state
    import capo_wellarchitected.types.recommendation_status
    import capo_wellarchitected.types.recommendation_type
    import capo_wellarchitected.types.recommendation_types
    import capo_wellarchitected.types.remediation_type
    import capo_wellarchitected.types.report_format
    import capo_wellarchitected.types.resource_arn
    import capo_wellarchitected.types.review_template_arns
    import capo_wellarchitected.types.review_template_lens_aliases
    import capo_wellarchitected.types.review_template_lenses
    import capo_wellarchitected.types.role_arn
    import capo_wellarchitected.types.scope
    import capo_wellarchitected.types.selected_choices
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.share_invitation_action
    import capo_wellarchitected.types.share_invitation_id
    import capo_wellarchitected.types.share_resource_type
    import capo_wellarchitected.types.share_status
    import capo_wellarchitected.types.shared_with
    import capo_wellarchitected.types.shared_with_prefix
    import capo_wellarchitected.types.start_agent_recommendation_generation_request
    import capo_wellarchitected.types.start_agent_recommendation_generation_response
    import capo_wellarchitected.types.tag_key_list
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.tag_resource_input
    import capo_wellarchitected.types.tag_resource_output
    import capo_wellarchitected.types.tags
    import capo_wellarchitected.types.template_arn
    import capo_wellarchitected.types.template_description
    import capo_wellarchitected.types.template_name
    import capo_wellarchitected.types.template_name_prefix
    import capo_wellarchitected.types.untag_resource_input
    import capo_wellarchitected.types.untag_resource_output
    import capo_wellarchitected.types.update_agent_context_request
    import capo_wellarchitected.types.update_agent_context_response
    import capo_wellarchitected.types.update_agent_goal_request
    import capo_wellarchitected.types.update_agent_goal_response
    import capo_wellarchitected.types.update_agent_profile_request
    import capo_wellarchitected.types.update_agent_profile_response
    import capo_wellarchitected.types.update_agent_recommendation_status_request
    import capo_wellarchitected.types.update_agent_recommendation_status_response
    import capo_wellarchitected.types.update_answer_input
    import capo_wellarchitected.types.update_answer_output
    import capo_wellarchitected.types.update_global_settings_input
    import capo_wellarchitected.types.update_integration_input
    import capo_wellarchitected.types.update_lens_review_input
    import capo_wellarchitected.types.update_lens_review_output
    import capo_wellarchitected.types.update_profile_input
    import capo_wellarchitected.types.update_profile_output
    import capo_wellarchitected.types.update_review_template_answer_input
    import capo_wellarchitected.types.update_review_template_answer_output
    import capo_wellarchitected.types.update_review_template_input
    import capo_wellarchitected.types.update_review_template_lens_review_input
    import capo_wellarchitected.types.update_review_template_lens_review_output
    import capo_wellarchitected.types.update_review_template_output
    import capo_wellarchitected.types.update_share_invitation_input
    import capo_wellarchitected.types.update_share_invitation_output
    import capo_wellarchitected.types.update_workload_input
    import capo_wellarchitected.types.update_workload_output
    import capo_wellarchitected.types.update_workload_share_input
    import capo_wellarchitected.types.update_workload_share_output
    import capo_wellarchitected.types.upgrade_lens_review_input
    import capo_wellarchitected.types.upgrade_profile_version_input
    import capo_wellarchitected.types.upgrade_review_template_lens_review_input
    import capo_wellarchitected.types.uuid
    import capo_wellarchitected.types.workload_account_ids
    import capo_wellarchitected.types.workload_applications
    import capo_wellarchitected.types.workload_architectural_design
    import capo_wellarchitected.types.workload_arn
    import capo_wellarchitected.types.workload_aws_regions
    import capo_wellarchitected.types.workload_description
    import capo_wellarchitected.types.workload_discovery_config
    import capo_wellarchitected.types.workload_environment
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_improvement_status
    import capo_wellarchitected.types.workload_industry
    import capo_wellarchitected.types.workload_industry_type
    import capo_wellarchitected.types.workload_jira_configuration_input
    import capo_wellarchitected.types.workload_lenses
    import capo_wellarchitected.types.workload_name
    import capo_wellarchitected.types.workload_name_prefix
    import capo_wellarchitected.types.workload_non_aws_regions
    import capo_wellarchitected.types.workload_pillar_priorities
    import capo_wellarchitected.types.workload_profile_arns
    import capo_wellarchitected.types.workload_review_owner


class AsyncWellArchitectedClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncWellArchitectedClient:
    """A client for the ``WellArchitected`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncWellArchitectedClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWellArchitectedClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_lenses(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_aliases: Optional[
            "capo_wellarchitected.types.lens_aliases.LensAliases"
        ] = None,
    ) -> None:
        """<p>Associate a lens to a workload.</p> <p>Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.</p> <note> <p> <b>Disclaimer</b> </p> <p>By accessing and/or applying custom lenses created by another Amazon Web Services user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the Amazon Web Services Customer Agreement. </p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.associate_lenses_input.AssociateLensesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses.async_associate_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.associate_lenses_input.AssociateLensesInput = {
            "workload_id": workload_id
        }
        if lens_aliases is not None:
            input_["lens_aliases"] = lens_aliases

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_profiles(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_arns: Optional[
            "capo_wellarchitected.types.profile_arns.ProfileArns"
        ] = None,
    ) -> None:
        """<p>Associate a profile with a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to associate with the workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.associate_profiles_input.AssociateProfilesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles.async_associate_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.associate_profiles_input.AssociateProfilesInput = {
            "workload_id": workload_id
        }
        if profile_arns is not None:
            input_["profile_arns"] = profile_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_agent_context(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        title: "capo_wellarchitected.types.sensitive_string.SensitiveString",
        context_type: "capo_wellarchitected.types.context_type.ContextType",
        content: "capo_wellarchitected.types.context_content.ContextContent",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_wellarchitected.types.create_agent_context_response.CreateAgentContextResponse":
        """<p>Creates a context associated with an optimization profile. Contexts provide application and environment information used during recommendation generation.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile to associate the context with.</p>
            title: <p>The title of the context.</p>
            context_type: <p>The type of the context.</p>
            content: <p>The typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_agent_context_request.CreateAgentContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_agent_context_response.CreateAgentContextResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_context

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_context.async_create_agent_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_agent_context_request.CreateAgentContextRequest = {
            "profile_arn": profile_arn,
            "title": title,
            "context_type": context_type,
            "content": content,
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

    async def create_agent_goal(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        pillars: "capo_wellarchitected.types.pillars.Pillars",
        title: "capo_wellarchitected.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_token: Optional[str] = None,
        description: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> (
        "capo_wellarchitected.types.create_agent_goal_response.CreateAgentGoalResponse"
    ):
        """<p>Creates an optimization goal associated with a profile. Goals define specific targets and objectives for the optimization process.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile to associate the goal with.</p>
            pillars: <p>The Well-Architected Tool Framework pillars to associate with this goal.</p>
            title: <p>The title of the goal.</p>
            description: <p>A description of the goal.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_agent_goal_request.CreateAgentGoalRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_agent_goal_response.CreateAgentGoalResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_goal

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_goal.async_create_agent_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_agent_goal_request.CreateAgentGoalRequest = {
            "profile_arn": profile_arn,
            "pillars": pillars,
            "title": title,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_agent_profile(
        self,
        name: str,
        pillars: "capo_wellarchitected.types.pillars.Pillars",
        execution_role_arn: "capo_wellarchitected.types.role_arn.RoleArn",
        aggregation_configuration: "capo_wellarchitected.types.aggregation_configurations.AggregationConfigurations",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        display_name: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        business_overview: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        deletion_protection: Optional[bool] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_wellarchitected.types.tags.Tags"] = None,
    ) -> "capo_wellarchitected.types.create_agent_profile_response.CreateAgentProfileResponse":
        """<p>Creates an optimization profile that defines the scope and configuration for generating recommendations. A profile specifies the execution role, target pillars, and aggregation settings for analyzing your Amazon Web Services resources.</p>

        Args:
            name: <p>The system name of the profile.</p>
            display_name: <p>The display name of the profile shown to users.</p>
            description: <p>A description of the profile.</p>
            business_overview: <p>The business overview for this profile.</p>
            pillars: <p>The Well-Architected Tool Framework pillars to associate with this profile.</p>
            deletion_protection: <p>Indicates whether deletion protection is enabled for the profile.</p>
            execution_role_arn: <p>The ARN of the IAM execution role used for recommendation actions.</p>
            aggregation_configuration: <p>The aggregation configuration that defines which Amazon Web Services accounts and Regions to analyze.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>The tags to associate with the profile.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_agent_profile_request.CreateAgentProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_agent_profile_response.CreateAgentProfileResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_agent_profile.async_create_agent_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_agent_profile_request.CreateAgentProfileRequest = {
            "name": name,
            "pillars": pillars,
            "execution_role_arn": execution_role_arn,
            "aggregation_configuration": aggregation_configuration,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if business_overview is not None:
            input_["business_overview"] = business_overview
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    async def create_lens_share(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with: Optional[
            "capo_wellarchitected.types.shared_with.SharedWith"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_lens_share_output.CreateLensShareOutput":
        """<p>Create a lens share.</p> <p>The owner of a lens can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be shared.</p> <p> Shared access to a lens is not removed until the lens invitation is deleted.</p> <p>If you share a lens with an organization or OU, all accounts in the organization or OU are granted access to the lens.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html">Sharing a custom lens</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_lens_share_input.CreateLensShareInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_lens_share_output.CreateLensShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share.async_create_lens_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_lens_share_input.CreateLensShareInput = {
            "lens_alias": lens_alias
        }
        if shared_with is not None:
            input_["shared_with"] = shared_with
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_lens_version(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
        is_major_version: Optional[
            "capo_wellarchitected.types.is_major_version.IsMajorVersion"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> (
        "capo_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput"
    ):
        """<p>Create a new lens version.</p> <p>A lens can have up to 100 versions.</p> <p>Use this operation to publish a new lens version after you have imported a lens. The <code>LensAlias</code> is used to identify the lens to be published. The owner of a lens can share the lens with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Only the owner of a lens can delete it. </p>

        Args:
            lens_version: <p>The version of the lens being created.</p>
            is_major_version: <p>Set to true if this new major lens version.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_lens_version_input.CreateLensVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version.async_create_lens_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_lens_version_input.CreateLensVersionInput = {
            "lens_alias": lens_alias
        }
        if lens_version is not None:
            input_["lens_version"] = lens_version
        if is_major_version is not None:
            input_["is_major_version"] = is_major_version
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_milestone(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_name: Optional[
            "capo_wellarchitected.types.milestone_name.MilestoneName"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_milestone_output.CreateMilestoneOutput":
        """<p>Create a milestone for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_milestone_input.CreateMilestoneInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_milestone_output.CreateMilestoneOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_milestone

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_milestone.async_create_milestone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_milestone_input.CreateMilestoneInput = {
            "workload_id": workload_id
        }
        if milestone_name is not None:
            input_["milestone_name"] = milestone_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_profile(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_name: Optional[
            "capo_wellarchitected.types.profile_name.ProfileName"
        ] = None,
        profile_description: Optional[
            "capo_wellarchitected.types.profile_description.ProfileDescription"
        ] = None,
        profile_questions: Optional[
            "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.create_profile_output.CreateProfileOutput":
        """<p>Create a profile.</p>

        Args:
            profile_name: <p>Name of the profile.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>The profile questions.</p>
            tags: <p>The tags assigned to the profile.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_profile_input.CreateProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_profile_output.CreateProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_profile_input.CreateProfileInput = {}
        if profile_name is not None:
            input_["profile_name"] = profile_name
        if profile_description is not None:
            input_["profile_description"] = profile_description
        if profile_questions is not None:
            input_["profile_questions"] = profile_questions
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_profile_share(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with: Optional[
            "capo_wellarchitected.types.shared_with.SharedWith"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput":
        """<p>Create a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_profile_share_input.CreateProfileShareInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share.async_create_profile_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_profile_share_input.CreateProfileShareInput = {
            "profile_arn": profile_arn
        }
        if shared_with is not None:
            input_["shared_with"] = shared_with
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_review_template(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        template_name: Optional[
            "capo_wellarchitected.types.template_name.TemplateName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.template_description.TemplateDescription"
        ] = None,
        lenses: Optional[
            "capo_wellarchitected.types.review_template_lenses.ReviewTemplateLenses"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput":
        """<p>Create a review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your review templates. If your review template or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            template_name: <p>Name of the review template.</p>
            description: <p>The review template description.</p>
            lenses: <p>Lenses applied to the review template.</p>
            tags: <p>The tags assigned to the review template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_review_template

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_review_template.async_create_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput = {}
        if template_name is not None:
            input_["template_name"] = template_name
        if description is not None:
            input_["description"] = description
        if lenses is not None:
            input_["lenses"] = lenses
        if notes is not None:
            input_["notes"] = notes
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_template_share(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with: Optional[
            "capo_wellarchitected.types.shared_with.SharedWith"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput":
        """<p>Create a review template share.</p> <p>The owner of a review template can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. </p> <p> Shared access to a review template is not removed until the review template share invitation is deleted.</p> <p>If you share a review template with an organization or OU, all accounts in the organization or OU are granted access to the review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your review template with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your review template available to those other accounts.</p> </note>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_template_share_input.CreateTemplateShareInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_template_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_template_share.async_create_template_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_template_share_input.CreateTemplateShareInput = {
            "template_arn": template_arn
        }
        if shared_with is not None:
            input_["shared_with"] = shared_with
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workload(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name: Optional[
            "capo_wellarchitected.types.workload_name.WorkloadName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.workload_description.WorkloadDescription"
        ] = None,
        environment: Optional[
            "capo_wellarchitected.types.workload_environment.WorkloadEnvironment"
        ] = None,
        account_ids: Optional[
            "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        industry_type: Optional[
            "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        lenses: Optional[
            "capo_wellarchitected.types.workload_lenses.WorkloadLenses"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
        discovery_config: Optional[
            "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "capo_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        profile_arns: Optional[
            "capo_wellarchitected.types.workload_profile_arns.WorkloadProfileArns"
        ] = None,
        review_template_arns: Optional[
            "capo_wellarchitected.types.review_template_arns.ReviewTemplateArns"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "capo_wellarchitected.types.create_workload_output.CreateWorkloadOutput":
        """<p>Create a new workload.</p> <p>The owner of a workload can share the workload with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Only the owner of a workload can delete it.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html">Defining a Workload</a> in the <i>Well-Architected Tool User Guide</i>.</p> <important> <p>Either <code>AwsRegions</code>, <code>NonAwsRegions</code>, or both must be specified when creating a workload.</p> <p>You also must specify <code>ReviewOwner</code>, even though the parameter is listed as not being required in the following section. </p> </important> <p>When creating a workload using a review template, you must have the following IAM permissions:</p> <ul> <li> <p> <code>wellarchitected:GetReviewTemplate</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateAnswer</code> </p> </li> <li> <p> <code>wellarchitected:ListReviewTemplateAnswers</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateLensReview</code> </p> </li> </ul>

        Args:
            tags: <p>The tags to be associated with the workload.</p>
            discovery_config: <p>Well-Architected discovery configuration settings associated to the workload.</p>
            applications: <p>List of AppRegistry application ARNs associated to the workload.</p>
            profile_arns: <p>The list of profile ARNs associated with the workload.</p>
            review_template_arns: <p>The list of review template ARNs to associate with the workload.</p>
            jira_configuration: <p>Jira configuration settings when creating a workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_workload_input.CreateWorkloadInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_workload_output.CreateWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload.async_create_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_workload_input.CreateWorkloadInput = {}
        if workload_name is not None:
            input_["workload_name"] = workload_name
        if description is not None:
            input_["description"] = description
        if environment is not None:
            input_["environment"] = environment
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if aws_regions is not None:
            input_["aws_regions"] = aws_regions
        if non_aws_regions is not None:
            input_["non_aws_regions"] = non_aws_regions
        if pillar_priorities is not None:
            input_["pillar_priorities"] = pillar_priorities
        if architectural_design is not None:
            input_["architectural_design"] = architectural_design
        if review_owner is not None:
            input_["review_owner"] = review_owner
        if industry_type is not None:
            input_["industry_type"] = industry_type
        if industry is not None:
            input_["industry"] = industry
        if lenses is not None:
            input_["lenses"] = lenses
        if notes is not None:
            input_["notes"] = notes
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if discovery_config is not None:
            input_["discovery_config"] = discovery_config
        if applications is not None:
            input_["applications"] = applications
        if profile_arns is not None:
            input_["profile_arns"] = profile_arns
        if review_template_arns is not None:
            input_["review_template_arns"] = review_template_arns
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workload_share(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with: Optional[
            "capo_wellarchitected.types.shared_with.SharedWith"
        ] = None,
        permission_type: Optional[
            "capo_wellarchitected.types.permission_type.PermissionType"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput":
        """<p>Create a workload share.</p> <p>The owner of a workload can share it with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Shared access to a workload is not removed until the workload invitation is deleted.</p> <p>If you share a workload with an organization or OU, all accounts in the organization or OU are granted access to the workload.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html">Sharing a workload</a> in the <i>Well-Architected Tool User Guide</i>.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share.async_create_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput = {
            "workload_id": workload_id
        }
        if shared_with is not None:
            input_["shared_with"] = shared_with
        if permission_type is not None:
            input_["permission_type"] = permission_type
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_context(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.delete_agent_context_response.DeleteAgentContextResponse":
        """<p>Deletes a context associated with a profile.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the context.</p>
            id: <p>The unique identifier of the context to delete.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_agent_context_request.DeleteAgentContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.delete_agent_context_response.DeleteAgentContextResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_context

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_context.async_delete_agent_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_agent_context_request.DeleteAgentContextRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_goal(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> (
        "capo_wellarchitected.types.delete_agent_goal_response.DeleteAgentGoalResponse"
    ):
        """<p>Deletes an optimization goal from a profile.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the goal.</p>
            id: <p>The unique identifier of the goal to delete.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_agent_goal_request.DeleteAgentGoalRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.delete_agent_goal_response.DeleteAgentGoalResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_goal

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_goal.async_delete_agent_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_agent_goal_request.DeleteAgentGoalRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_profile(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.delete_agent_profile_response.DeleteAgentProfileResponse":
        """<p>Deletes an optimization profile and its associated configuration. This action cannot be undone.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile to delete.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_agent_profile_request.DeleteAgentProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.delete_agent_profile_response.DeleteAgentProfileResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_agent_profile.async_delete_agent_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_agent_profile_request.DeleteAgentProfileRequest = {
            "profile_arn": profile_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
        lens_status: Optional[
            "capo_wellarchitected.types.lens_status_type.LensStatusType"
        ] = None,
    ) -> None:
        """<p>Delete an existing lens.</p> <p>Only the owner of a lens can delete it. After the lens is deleted, Amazon Web Services accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads. </p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            lens_status: <p>The status of the lens to be deleted.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_lens_input.DeleteLensInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens.async_delete_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_lens_input.DeleteLensInput = {
            "lens_alias": lens_alias
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if lens_status is not None:
            input_["lens_status"] = lens_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lens_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a lens share.</p> <p>After the lens share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share.async_delete_lens_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput = {
            "share_id": share_id,
            "lens_alias": lens_alias,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a profile.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your profile with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your profile available to those other accounts. Those other accounts may continue to access and use your shared profile even if you delete the profile from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_profile_input.DeleteProfileInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_profile_input.DeleteProfileInput = {
            "profile_arn": profile_arn
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profile_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share.async_delete_profile_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput = {
            "share_id": share_id,
            "profile_arn": profile_arn,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a review template.</p> <p>Only the owner of a review template can delete it.</p> <p>After the review template is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template.async_delete_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput = {
            "template_arn": template_arn
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a review template share.</p> <p>After the review template share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share.async_delete_template_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput = {
            "share_id": share_id,
            "template_arn": template_arn,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_workload_input.DeleteWorkloadInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload.async_delete_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_workload_input.DeleteWorkloadInput = {
            "workload_id": workload_id
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workload_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Delete a workload share.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share.async_delete_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput = {
            "share_id": share_id,
            "workload_id": workload_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_lenses(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_aliases: Optional[
            "capo_wellarchitected.types.lens_aliases.LensAliases"
        ] = None,
    ) -> None:
        """<p>Disassociate a lens from a workload.</p> <p>Up to 10 lenses can be disassociated from a workload in a single API operation.</p> <note> <p>The Amazon Web Services Well-Architected Framework lens (<code>wellarchitected</code>) cannot be removed from a workload.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses.async_disassociate_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput = {
            "workload_id": workload_id
        }
        if lens_aliases is not None:
            input_["lens_aliases"] = lens_aliases

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_profiles(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_arns: Optional[
            "capo_wellarchitected.types.profile_arns.ProfileArns"
        ] = None,
    ) -> None:
        """<p>Disassociate a profile from a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to disassociate from the workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles.async_disassociate_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput = {
            "workload_id": workload_id
        }
        if profile_arns is not None:
            input_["profile_arns"] = profile_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.export_lens_output.ExportLensOutput":
        """<p>Export an existing lens.</p> <p>Only the owner of a lens can export it. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be exported.</p> <p>Lenses are defined in JSON. For more information, see <a href="https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            lens_version: <p>The lens version to be exported.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.export_lens_input.ExportLensInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.export_lens_output.ExportLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.export_lens

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.export_lens.async_export_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.export_lens_input.ExportLensInput = {
            "lens_alias": lens_alias
        }
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_context(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> (
        "capo_wellarchitected.types.get_agent_context_response.GetAgentContextResponse"
    ):
        """<p>Retrieves detailed information about a specific context associated with a profile.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the context.</p>
            id: <p>The unique identifier of the context to retrieve.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_agent_context_request.GetAgentContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_agent_context_response.GetAgentContextResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_context

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_context.async_get_agent_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_agent_context_request.GetAgentContextRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_goal(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_agent_goal_response.GetAgentGoalResponse":
        """<p>Retrieves detailed information about a specific optimization goal.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the goal.</p>
            id: <p>The unique identifier of the goal to retrieve.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_agent_goal_request.GetAgentGoalRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_agent_goal_response.GetAgentGoalResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_goal

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_goal.async_get_agent_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_agent_goal_request.GetAgentGoalRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_profile(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> (
        "capo_wellarchitected.types.get_agent_profile_response.GetAgentProfileResponse"
    ):
        """<p>Retrieves detailed information about an optimization profile, including its configuration and metadata.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the optimization profile to retrieve.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_agent_profile_request.GetAgentProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_agent_profile_response.GetAgentProfileResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_profile.async_get_agent_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_agent_profile_request.GetAgentProfileRequest = {
            "profile_arn": profile_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_recommendation(
        self,
        recommendation_arn: "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        remediation_type: Optional[
            "capo_wellarchitected.types.remediation_type.RemediationType"
        ] = None,
    ) -> "capo_wellarchitected.types.get_agent_recommendation_response.GetAgentRecommendationResponse":
        """<p>Retrieves detailed information about a specific optimization recommendation, including its impact analysis, content, and implementation guidance.</p>

        Args:
            recommendation_arn: <p>The Amazon Resource Name (ARN) of the recommendation to retrieve.</p>
            remediation_type: <p>Optional filter on remediation type.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_agent_recommendation_request.GetAgentRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_agent_recommendation_response.GetAgentRecommendationResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_recommendation

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_recommendation.async_get_agent_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_agent_recommendation_request.GetAgentRecommendationRequest = {
            "recommendation_arn": recommendation_arn
        }
        if remediation_type is not None:
            input_["remediation_type"] = remediation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_recommendation_generation(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        generation_id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_agent_recommendation_generation_response.GetAgentRecommendationGenerationResponse":
        """<p>Retrieves information about a recommendation generation process, including its status, progress, and results. Recommendation generation is asynchronous: poll this operation until status reaches a terminal value of COMPLETED (results are ready) or ERROR (see errorDetails). Intermediate values are QUEUED and IN_PROGRESS.</p>

        Args:
            profile_arn: <p>The ARN of the optimization profile associated with this generation.</p>
            generation_id: <p>The unique identifier of the recommendation generation to retrieve.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_agent_recommendation_generation_request.GetAgentRecommendationGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_agent_recommendation_generation_response.GetAgentRecommendationGenerationResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_recommendation_generation

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_agent_recommendation_generation.async_get_agent_recommendation_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_agent_recommendation_generation_request.GetAgentRecommendationGenerationRequest = {
            "profile_arn": profile_arn,
            "generation_id": generation_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_answer(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_answer_output.GetAnswerOutput":
        """<p>Get the answer to a specific question in a workload review.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_answer_input.GetAnswerInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_answer_output.GetAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_answer

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_answer.async_get_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_answer_input.GetAnswerInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
            "question_id": question_id,
        }
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_consolidated_report(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        format: Optional[
            "capo_wellarchitected.types.report_format.ReportFormat"
        ] = None,
        include_shared_resources: Optional[
            "capo_wellarchitected.types.include_shared_resources.IncludeSharedResources"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput":
        """<p>Get a consolidated report of your workloads.</p> <p>You can optionally choose to include workloads that have been shared with you.</p>

        Args:
            format: <p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>
            include_shared_resources: <p>Set to <code>true</code> to have shared resources included in the report.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report.async_get_consolidated_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput = {}
        if format is not None:
            input_["format"] = format
        if include_shared_resources is not None:
            input_["include_shared_resources"] = include_shared_resources
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

    async def iter_get_consolidated_report(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        format: Optional[
            "capo_wellarchitected.types.report_format.ReportFormat"
        ] = None,
        include_shared_resources: Optional[
            "capo_wellarchitected.types.include_shared_resources.IncludeSharedResources"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput]":
        _token = next_token
        while True:
            _response = await self.get_consolidated_report(
                config_overrides=config_overrides,
                format=format,
                include_shared_resources=include_shared_resources,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_global_settings(
        self, *, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> (
        "capo_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput"
    ):
        """<p>Global settings for all workloads.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings.async_get_global_settings(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_output.GetLensOutput":
        """<p>Get an existing lens.</p>

        Args:
            lens_version: <p>The lens version to be retrieved.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_lens_input.GetLensInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_lens_output.GetLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens.async_get_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_input.GetLensInput = {
            "lens_alias": lens_alias
        }
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_review_output.GetLensReviewOutput":
        """<p>Get lens review.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_lens_review_input.GetLensReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_lens_review_output.GetLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review.async_get_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_review_input.GetLensReviewInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lens_review_report(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput":
        """<p>Get lens review report.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report.async_get_lens_review_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lens_version_difference(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        base_lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
        target_lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput":
        """<p>Get lens version differences.</p>

        Args:
            base_lens_version: <p>The base version of the lens.</p>
            target_lens_version: <p>The lens version to target a difference for.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference.async_get_lens_version_difference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput = {
            "lens_alias": lens_alias
        }
        if base_lens_version is not None:
            input_["base_lens_version"] = base_lens_version
        if target_lens_version is not None:
            input_["target_lens_version"] = target_lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_milestone(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        milestone_number: "capo_wellarchitected.types.milestone_number.MilestoneNumber",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_milestone_output.GetMilestoneOutput":
        """<p>Get a milestone for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_milestone_input.GetMilestoneInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_milestone_output.GetMilestoneOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_milestone

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_milestone.async_get_milestone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_milestone_input.GetMilestoneInput = {
            "workload_id": workload_id,
            "milestone_number": milestone_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_version: Optional[
            "capo_wellarchitected.types.profile_version.ProfileVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_profile_output.GetProfileOutput":
        """<p>Get profile information.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_version: <p>The profile version.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_profile_input.GetProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_profile_output.GetProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_profile_input.GetProfileInput = {
            "profile_arn": profile_arn
        }
        if profile_version is not None:
            input_["profile_version"] = profile_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile_template(
        self, *, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> "capo_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput":
        """<p>Get profile template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template.async_get_profile_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> (
        "capo_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput"
    ):
        """<p>Get review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_review_template_input.GetReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template.async_get_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_input.GetReviewTemplateInput = {
            "template_arn": template_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_review_template_answer(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput":
        """<p>Get review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer.async_get_review_template_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
            "question_id": question_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput":
        """<p>Get a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review.async_get_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_workload_output.GetWorkloadOutput":
        """<p>Get an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.get_workload_input.GetWorkloadInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.get_workload_output.GetWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_workload

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.get_workload.async_get_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_workload_input.GetWorkloadInput = {
            "workload_id": workload_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_lens(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_alias: Optional["capo_wellarchitected.types.lens_alias.LensAlias"] = None,
        json_string: Optional["capo_wellarchitected.types.lens_json.LensJSON"] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.import_lens_output.ImportLensOutput":
        """<p>Import a new custom lens or update an existing custom lens.</p> <p>To update an existing custom lens, specify its ARN as the <code>LensAlias</code>. If no ARN is specified, a new custom lens is created.</p> <p>The new or updated lens will have a status of <code>DRAFT</code>. The lens cannot be applied to workloads or shared with other Amazon Web Services accounts until it's published with <a>CreateLensVersion</a>.</p> <p>Lenses are defined in JSON. For more information, see <a href="https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <p>A custom lens cannot exceed 500 KB in size.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            json_string: <p>The JSON representation of a lens.</p>
            tags: <p>Tags to associate to a lens.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.import_lens_input.ImportLensInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.import_lens_output.ImportLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.import_lens

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.import_lens.async_import_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.import_lens_input.ImportLensInput = {}
        if lens_alias is not None:
            input_["lens_alias"] = lens_alias
        if json_string is not None:
            input_["json_string"] = json_string
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_contexts(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "capo_wellarchitected.types.list_agent_contexts_response.ListAgentContextsResponse":
        """<p>Lists contexts associated with a profile.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile to list contexts for.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_contexts_request.ListAgentContextsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_contexts_response.ListAgentContextsResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_contexts

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_contexts.async_list_agent_contexts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_contexts_request.ListAgentContextsRequest = {
            "profile_arn": profile_arn
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

    async def iter_list_agent_contexts(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.context_summary.ContextSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_contexts(
                profile_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agent_goals(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "capo_wellarchitected.types.list_agent_goals_response.ListAgentGoalsResponse":
        """<p>Lists optimization goals associated with a specified profile. Goals define specific targets and objectives for the optimization process.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the optimization profile to list goals for.</p>
            max_results: <p>The maximum number of goals to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue retrieving results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_goals_request.ListAgentGoalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_goals_response.ListAgentGoalsResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_goals

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_goals.async_list_agent_goals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_goals_request.ListAgentGoalsRequest = {
            "profile_arn": profile_arn
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

    async def iter_list_agent_goals(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.goal_summary.GoalSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_goals(
                profile_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agent_profiles(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "capo_wellarchitected.types.list_agent_profiles_response.ListAgentProfilesResponse":
        """<p>Lists optimization profiles in your account. Profiles define the scope and configuration for generating optimization recommendations.</p>

        Args:
            max_results: <p>The maximum number of profiles to return in a single call. Default is 100.</p>
            next_token: <p>A pagination token returned from a previous call to continue retrieving results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_profiles_request.ListAgentProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_profiles_response.ListAgentProfilesResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_profiles

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_profiles.async_list_agent_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_profiles_request.ListAgentProfilesRequest = {}
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

    async def iter_list_agent_profiles(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.agent_profile_summary.AgentProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agent_recommendation_generations(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        recommendation_type: Optional[
            "capo_wellarchitected.types.recommendation_type.RecommendationType"
        ] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "capo_wellarchitected.types.list_agent_recommendation_generations_response.ListAgentRecommendationGenerationsResponse":
        """<p>Lists recommendation generation processes for a specified profile.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the optimization profile to list generation processes for.</p>
            recommendation_type: <p>Optional filter by recommendation type.</p>
            max_results: <p>The maximum number of generation processes to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue retrieving results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_recommendation_generations_request.ListAgentRecommendationGenerationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_recommendation_generations_response.ListAgentRecommendationGenerationsResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendation_generations

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendation_generations.async_list_agent_recommendation_generations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_recommendation_generations_request.ListAgentRecommendationGenerationsRequest = {
            "profile_arn": profile_arn
        }
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type
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

    async def iter_list_agent_recommendation_generations(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        recommendation_type: Optional[
            "capo_wellarchitected.types.recommendation_type.RecommendationType"
        ] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.agent_recommendation_generation_summary.AgentRecommendationGenerationSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_recommendation_generations(
                profile_arn,
                config_overrides=config_overrides,
                recommendation_type=recommendation_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agent_recommendation_items(
        self,
        recommendation_arn: "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        type: Optional[
            "capo_wellarchitected.types.recommendation_item_type.RecommendationItemType"
        ] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "capo_wellarchitected.types.list_agent_recommendation_items_response.ListAgentRecommendationItemsResponse":
        """<p>Lists recommendation items for a specific recommendation. Recommendation items provide detailed information about individual optimization opportunities.</p>

        Args:
            recommendation_arn: <p>The Amazon Resource Name (ARN) of the recommendation to list items for.</p>
            type: <p>Optional filter to return only recommendation items of the specified type.</p>
            max_results: <p>The maximum number of recommendation items to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue retrieving results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_recommendation_items_request.ListAgentRecommendationItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_recommendation_items_response.ListAgentRecommendationItemsResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendation_items

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendation_items.async_list_agent_recommendation_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_recommendation_items_request.ListAgentRecommendationItemsRequest = {
            "recommendation_arn": recommendation_arn
        }
        if type is not None:
            input_["type"] = type
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

    async def iter_list_agent_recommendation_items(
        self,
        recommendation_arn: "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        type: Optional[
            "capo_wellarchitected.types.recommendation_item_type.RecommendationItemType"
        ] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.agent_recommendation_item_summary.AgentRecommendationItemSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_recommendation_items(
                recommendation_arn,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agent_recommendations(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_wellarchitected.types.recommendation_state.RecommendationState"
        ] = None,
        pillar: Optional["capo_wellarchitected.types.pillar.Pillar"] = None,
    ) -> "capo_wellarchitected.types.list_agent_recommendations_response.ListAgentRecommendationsResponse":
        """<p>Lists active optimization recommendations for a specified profile with optional filtering by state.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the optimization profile to list recommendations for.</p>
            max_results: <p>The maximum number of recommendations to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue retrieving results.</p>
            state: <p>Optional filter to return only recommendations with the specified state (OPEN or CLOSED).</p>
            pillar: <p>Optional filter to return only recommendations for the specified pillar.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_agent_recommendations_request.ListAgentRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_agent_recommendations_response.ListAgentRecommendationsResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendations

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_agent_recommendations.async_list_agent_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_agent_recommendations_request.ListAgentRecommendationsRequest = {
            "profile_arn": profile_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state
        if pillar is not None:
            input_["pillar"] = pillar

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_agent_recommendations(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_wellarchitected.types.recommendation_state.RecommendationState"
        ] = None,
        pillar: Optional["capo_wellarchitected.types.pillar.Pillar"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.agent_recommendation_summary.AgentRecommendationSummary]":
        _token = next_token
        while True:
            _response = await self.list_agent_recommendations(
                profile_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state=state,
                pillar=pillar,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_answers(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "capo_wellarchitected.types.list_answers_output.ListAnswersOutput":
        """<p>List of answers for a particular workload and lens.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_answers_input.ListAnswersInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_answers_output.ListAnswersOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_answers

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_answers.async_list_answers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_answers_input.ListAnswersInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if question_priority is not None:
            input_["question_priority"] = question_priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_answers(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_answers_output.ListAnswersOutput]":
        _token = next_token
        while True:
            _response = await self.list_answers(
                workload_id,
                lens_alias,
                config_overrides=config_overrides,
                pillar_id=pillar_id,
                milestone_number=milestone_number,
                next_token=_token,
                max_results=max_results,
                question_priority=question_priority,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_check_details(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_arn: Optional["capo_wellarchitected.types.lens_arn.LensArn"] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        question_id: Optional[
            "capo_wellarchitected.types.question_id.QuestionId"
        ] = None,
        choice_id: Optional["capo_wellarchitected.types.choice_id.ChoiceId"] = None,
    ) -> "capo_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput":
        """<p>List of Trusted Advisor check details by account related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_check_details_input.ListCheckDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_details

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_details.async_list_check_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_check_details_input.ListCheckDetailsInput = {
            "workload_id": workload_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if lens_arn is not None:
            input_["lens_arn"] = lens_arn
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if question_id is not None:
            input_["question_id"] = question_id
        if choice_id is not None:
            input_["choice_id"] = choice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_check_details(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_arn: Optional["capo_wellarchitected.types.lens_arn.LensArn"] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        question_id: Optional[
            "capo_wellarchitected.types.question_id.QuestionId"
        ] = None,
        choice_id: Optional["capo_wellarchitected.types.choice_id.ChoiceId"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput]":
        _token = next_token
        while True:
            _response = await self.list_check_details(
                workload_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                lens_arn=lens_arn,
                pillar_id=pillar_id,
                question_id=question_id,
                choice_id=choice_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_check_summaries(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_arn: Optional["capo_wellarchitected.types.lens_arn.LensArn"] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        question_id: Optional[
            "capo_wellarchitected.types.question_id.QuestionId"
        ] = None,
        choice_id: Optional["capo_wellarchitected.types.choice_id.ChoiceId"] = None,
    ) -> "capo_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput":
        """<p>List of Trusted Advisor checks summarized for all accounts related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries.async_list_check_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput = {
            "workload_id": workload_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if lens_arn is not None:
            input_["lens_arn"] = lens_arn
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if question_id is not None:
            input_["question_id"] = question_id
        if choice_id is not None:
            input_["choice_id"] = choice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_check_summaries(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_arn: Optional["capo_wellarchitected.types.lens_arn.LensArn"] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        question_id: Optional[
            "capo_wellarchitected.types.question_id.QuestionId"
        ] = None,
        choice_id: Optional["capo_wellarchitected.types.choice_id.ChoiceId"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput]":
        _token = next_token
        while True:
            _response = await self.list_check_summaries(
                workload_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                lens_arn=lens_arn,
                pillar_id=pillar_id,
                question_id=question_id,
                choice_id=choice_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lenses(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_type: Optional["capo_wellarchitected.types.lens_type.LensType"] = None,
        lens_status: Optional[
            "capo_wellarchitected.types.lens_status_type.LensStatusType"
        ] = None,
        lens_name: Optional["capo_wellarchitected.types.lens_name.LensName"] = None,
    ) -> "capo_wellarchitected.types.list_lenses_output.ListLensesOutput":
        """<p>List the available lenses.</p>

        Args:
            lens_type: <p>The type of lenses to be returned.</p>
            lens_status: <p>The status of lenses to be returned.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_lenses_input.ListLensesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_lenses_output.ListLensesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lenses

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_lenses.async_list_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lenses_input.ListLensesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if lens_type is not None:
            input_["lens_type"] = lens_type
        if lens_status is not None:
            input_["lens_status"] = lens_status
        if lens_name is not None:
            input_["lens_name"] = lens_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_lenses(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_type: Optional["capo_wellarchitected.types.lens_type.LensType"] = None,
        lens_status: Optional[
            "capo_wellarchitected.types.lens_status_type.LensStatusType"
        ] = None,
        lens_name: Optional["capo_wellarchitected.types.lens_name.LensName"] = None,
    ) -> (
        "AsyncIterator[capo_wellarchitected.types.list_lenses_output.ListLensesOutput]"
    ):
        _token = next_token
        while True:
            _response = await self.list_lenses(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                lens_type=lens_type,
                lens_status=lens_status,
                lens_name=lens_name,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lens_review_improvements(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "capo_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput":
        """<p>List the improvements of a particular lens review.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements.async_list_lens_review_improvements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if question_priority is not None:
            input_["question_priority"] = question_priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_lens_review_improvements(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput]":
        _token = next_token
        while True:
            _response = await self.list_lens_review_improvements(
                workload_id,
                lens_alias,
                config_overrides=config_overrides,
                pillar_id=pillar_id,
                milestone_number=milestone_number,
                next_token=_token,
                max_results=max_results,
                question_priority=question_priority,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lens_reviews(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput":
        """<p>List lens reviews for a particular workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews.async_list_lens_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput = {
            "workload_id": workload_id
        }
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
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

    async def iter_list_lens_reviews(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput]":
        _token = next_token
        while True:
            _response = await self.list_lens_reviews(
                workload_id,
                config_overrides=config_overrides,
                milestone_number=milestone_number,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lens_shares(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput":
        """<p>List the lens shares associated with the lens.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the lens is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_lens_shares_input.ListLensSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares.async_list_lens_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_shares_input.ListLensSharesInput = {
            "lens_alias": lens_alias
        }
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
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

    async def iter_list_lens_shares(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput]":
        _token = next_token
        while True:
            _response = await self.list_lens_shares(
                lens_alias,
                config_overrides=config_overrides,
                shared_with_prefix=shared_with_prefix,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_milestones(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_milestones_output.ListMilestonesOutput":
        """<p>List all milestones for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_milestones_input.ListMilestonesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_milestones_output.ListMilestonesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_milestones

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_milestones.async_list_milestones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_milestones_input.ListMilestonesInput = {
            "workload_id": workload_id
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

    async def iter_list_milestones(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_milestones_output.ListMilestonesOutput]":
        _token = next_token
        while True:
            _response = await self.list_milestones(
                workload_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        resource_arn: Optional[
            "capo_wellarchitected.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_wellarchitected.types.list_notifications_output.ListNotificationsOutput":
        """<p>List lens notifications.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            resource_arn: <p>The ARN for the related resource for the notification.</p> <note> <p>Only one of <code>WorkloadID</code> or <code>ResourceARN</code> should be specified.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_notifications_input.ListNotificationsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_notifications_output.ListNotificationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_notifications

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_notifications.async_list_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_notifications_input.ListNotificationsInput = {}
        if workload_id is not None:
            input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        resource_arn: Optional[
            "capo_wellarchitected.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_notifications_output.ListNotificationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_notifications(
                config_overrides=config_overrides,
                workload_id=workload_id,
                next_token=_token,
                max_results=max_results,
                resource_arn=resource_arn,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_profile_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput":
        """<p>List profile notifications.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications.async_list_profile_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput = {}
        if workload_id is not None:
            input_["workload_id"] = workload_id
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

    async def iter_list_profile_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_profile_notifications(
                config_overrides=config_overrides,
                workload_id=workload_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        profile_owner_type: Optional[
            "capo_wellarchitected.types.profile_owner_type.ProfileOwnerType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_profiles_output.ListProfilesOutput":
        """<p>List profiles.</p>

        Args:
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            profile_owner_type: <p>Profile owner type.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_profiles_input.ListProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_profiles_output.ListProfilesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profiles

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profiles_input.ListProfilesInput = {}
        if profile_name_prefix is not None:
            input_["profile_name_prefix"] = profile_name_prefix
        if profile_owner_type is not None:
            input_["profile_owner_type"] = profile_owner_type
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

    async def iter_list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        profile_owner_type: Optional[
            "capo_wellarchitected.types.profile_owner_type.ProfileOwnerType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_profiles_output.ListProfilesOutput]":
        _token = next_token
        while True:
            _response = await self.list_profiles(
                config_overrides=config_overrides,
                profile_name_prefix=profile_name_prefix,
                profile_owner_type=profile_owner_type,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_profile_shares(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> (
        "capo_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput"
    ):
        """<p>List profile shares.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares.async_list_profile_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput = {
            "profile_arn": profile_arn
        }
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
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

    async def iter_list_profile_shares(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput]":
        _token = next_token
        while True:
            _response = await self.list_profile_shares(
                profile_arn,
                config_overrides=config_overrides,
                shared_with_prefix=shared_with_prefix,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_review_template_answers(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput":
        """<p>List the answers of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers.async_list_review_template_answers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
        }
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
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

    async def iter_list_review_template_answers(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput]":
        _token = next_token
        while True:
            _response = await self.list_review_template_answers(
                template_arn,
                lens_alias,
                config_overrides=config_overrides,
                pillar_id=pillar_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_review_templates(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput":
        """<p>List review templates.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates.async_list_review_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput = {}
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

    async def iter_list_review_templates(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput]":
        _token = next_token
        while True:
            _response = await self.list_review_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_share_invitations(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        lens_name_prefix: Optional[
            "capo_wellarchitected.types.lens_name_prefix.LensNamePrefix"
        ] = None,
        share_resource_type: Optional[
            "capo_wellarchitected.types.share_resource_type.ShareResourceType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        template_name_prefix: Optional[
            "capo_wellarchitected.types.template_name_prefix.TemplateNamePrefix"
        ] = None,
    ) -> "capo_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput":
        """<p>List the share invitations.</p> <p> <code>WorkloadNamePrefix</code>, <code>LensNamePrefix</code>, <code>ProfileNamePrefix</code>, and <code>TemplateNamePrefix</code> are mutually exclusive. Use the parameter that matches your <code>ShareResourceType</code>.</p>

        Args:
            lens_name_prefix: <p>An optional string added to the beginning of each lens name returned in the results.</p>
            share_resource_type: <p>The type of share invitations to be returned.</p>
            max_results: <p>The maximum number of results to return for this request.</p>
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            template_name_prefix: <p>An optional string added to the beginning of each review template name returned in the results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations.async_list_share_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput = {}
        if workload_name_prefix is not None:
            input_["workload_name_prefix"] = workload_name_prefix
        if lens_name_prefix is not None:
            input_["lens_name_prefix"] = lens_name_prefix
        if share_resource_type is not None:
            input_["share_resource_type"] = share_resource_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if profile_name_prefix is not None:
            input_["profile_name_prefix"] = profile_name_prefix
        if template_name_prefix is not None:
            input_["template_name_prefix"] = template_name_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_share_invitations(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        lens_name_prefix: Optional[
            "capo_wellarchitected.types.lens_name_prefix.LensNamePrefix"
        ] = None,
        share_resource_type: Optional[
            "capo_wellarchitected.types.share_resource_type.ShareResourceType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        template_name_prefix: Optional[
            "capo_wellarchitected.types.template_name_prefix.TemplateNamePrefix"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_share_invitations(
                config_overrides=config_overrides,
                workload_name_prefix=workload_name_prefix,
                lens_name_prefix=lens_name_prefix,
                share_resource_type=share_resource_type,
                next_token=_token,
                max_results=max_results,
                profile_name_prefix=profile_name_prefix,
                template_name_prefix=template_name_prefix,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List the tags for a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "workload_arn": workload_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_template_shares(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput":
        """<p>List review template shares.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares.async_list_template_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput = {
            "template_arn": template_arn
        }
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
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

    async def iter_list_template_shares(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput]":
        _token = next_token
        while True:
            _response = await self.list_template_shares(
                template_arn,
                config_overrides=config_overrides,
                shared_with_prefix=shared_with_prefix,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workloads(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Paginated list of workloads.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_workloads_input.ListWorkloadsInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_workloads

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_workloads_input.ListWorkloadsInput = {}
        if workload_name_prefix is not None:
            input_["workload_name_prefix"] = workload_name_prefix
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

    async def iter_list_workloads(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_workloads_output.ListWorkloadsOutput]":
        _token = next_token
        while True:
            _response = await self.list_workloads(
                config_overrides=config_overrides,
                workload_name_prefix=workload_name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workload_shares(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput":
        """<p>List the workload shares associated with the workload.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the workload is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares.async_list_workload_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput = {
            "workload_id": workload_id
        }
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
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

    async def iter_list_workload_shares(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "AsyncIterator[capo_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput]":
        _token = next_token
        while True:
            _response = await self.list_workload_shares(
                workload_id,
                config_overrides=config_overrides,
                shared_with_prefix=shared_with_prefix,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_agent_recommendation_feedback(
        self,
        recommendation_arn: "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn",
        type: "capo_wellarchitected.types.recommendation_feedback_type.RecommendationFeedbackType",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        feedback_category: Optional[
            "capo_wellarchitected.types.feedback_category.FeedbackCategory"
        ] = None,
        comments: Optional[str] = None,
    ) -> "capo_wellarchitected.types.put_agent_recommendation_feedback_response.PutAgentRecommendationFeedbackResponse":
        """<p>Submits user feedback on a recommendation to help improve future optimization suggestions and track implementation outcomes.</p>

        Args:
            recommendation_arn: <p>The Amazon Resource Name (ARN) of the recommendation to provide feedback for.</p>
            type: <p>The type of feedback being provided.</p>
            feedback_category: <p>Optional category classifying the nature of the feedback.</p>
            comments: <p>Optional comments providing additional context about the feedback.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.put_agent_recommendation_feedback_request.PutAgentRecommendationFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.put_agent_recommendation_feedback_response.PutAgentRecommendationFeedbackResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.put_agent_recommendation_feedback

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.put_agent_recommendation_feedback.async_put_agent_recommendation_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.put_agent_recommendation_feedback_request.PutAgentRecommendationFeedbackRequest = {
            "recommendation_arn": recommendation_arn,
            "type": type,
        }
        if feedback_category is not None:
            input_["feedback_category"] = feedback_category
        if comments is not None:
            input_["comments"] = comments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_agent_recommendation_generation(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        types: "capo_wellarchitected.types.recommendation_types.RecommendationTypes",
        scope: "capo_wellarchitected.types.scope.Scope",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        name: Optional[str] = None,
        additional_context: Optional[object] = None,
    ) -> "capo_wellarchitected.types.start_agent_recommendation_generation_response.StartAgentRecommendationGenerationResponse":
        """<p>Initiates a new recommendation generation process for the specified optimization profile. This asynchronous operation analyzes your Amazon Web Services resources and generates optimization recommendations based on the configured pillars and scope. Use GetAgentRecommendationGeneration to check status.</p>

        Args:
            profile_arn: <p>The Amazon Resource Name (ARN) of the optimization profile to use for generating recommendations.</p>
            types: <p>The types of recommendations to generate.</p>
            name: <p>An optional name for this generation process to help identify it in lists and logs.</p>
            additional_context: <p>Optional additional context to guide the recommendation generation, such as specific business requirements or constraints.</p>
            scope: <p>Scope configuration to focus the generation on specific pillars or goals.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.start_agent_recommendation_generation_request.StartAgentRecommendationGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.start_agent_recommendation_generation_response.StartAgentRecommendationGenerationResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.start_agent_recommendation_generation

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.start_agent_recommendation_generation.async_start_agent_recommendation_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.start_agent_recommendation_generation_request.StartAgentRecommendationGenerationRequest = {
            "profile_arn": profile_arn,
            "types": types,
            "scope": scope,
        }
        if name is not None:
            input_["name"] = name
        if additional_context is not None:
            input_["additional_context"] = additional_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tags to the specified resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Args:
            tags: <p>The tags for the resource.</p>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.tag_resource

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.tag_resource_input.TagResourceInput = {
            "workload_arn": workload_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        tag_keys: Optional["capo_wellarchitected.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_wellarchitected.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note> <p>To specify multiple tags, use separate <b>tagKeys</b> parameters, for example:</p> <p> <code>DELETE /tags/WorkloadArn?tagKeys=key1&amp;tagKeys=key2</code> </p>

        Args:
            tag_keys: <p>A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.</p>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.untag_resource

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.untag_resource_input.UntagResourceInput = {
            "workload_arn": workload_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_context(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_token: Optional[str] = None,
        title: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        content: Optional[
            "capo_wellarchitected.types.context_content.ContextContent"
        ] = None,
    ) -> "capo_wellarchitected.types.update_agent_context_response.UpdateAgentContextResponse":
        """<p>Updates an existing context associated with a profile.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the context.</p>
            id: <p>The unique identifier of the context to update.</p>
            title: <p>The updated title of the context.</p>
            content: <p>The updated typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_agent_context_request.UpdateAgentContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_agent_context_response.UpdateAgentContextResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_context

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_context.async_update_agent_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_agent_context_request.UpdateAgentContextRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if title is not None:
            input_["title"] = title
        if content is not None:
            input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_goal(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        id: "capo_wellarchitected.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_token: Optional[str] = None,
        pillars: Optional["capo_wellarchitected.types.pillars.Pillars"] = None,
        title: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> (
        "capo_wellarchitected.types.update_agent_goal_response.UpdateAgentGoalResponse"
    ):
        """<p>Updates the pillars and title of an existing goal associated with a profile.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile containing the goal to update.</p>
            id: <p>The unique identifier of the goal to update.</p>
            pillars: <p>The updated pillars for the goal. Pillars define the optimization focus areas such as cost, performance, resilience, and operational excellence.</p>
            title: <p>The updated title for the goal. Maximum length of 1000 characters.</p>
            description: <p>A description of the goal.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_agent_goal_request.UpdateAgentGoalRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_agent_goal_response.UpdateAgentGoalResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_goal

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_goal.async_update_agent_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_agent_goal_request.UpdateAgentGoalRequest = {
            "profile_arn": profile_arn,
            "id": id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if pillars is not None:
            input_["pillars"] = pillars
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_profile(
        self,
        profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_token: Optional[str] = None,
        display_name: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        execution_role_arn: Optional[
            "capo_wellarchitected.types.role_arn.RoleArn"
        ] = None,
        aggregation_configuration: Optional[
            "capo_wellarchitected.types.aggregation_configurations.AggregationConfigurations"
        ] = None,
        business_overview: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
        pillars: Optional["capo_wellarchitected.types.pillars.Pillars"] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_wellarchitected.types.update_agent_profile_response.UpdateAgentProfileResponse":
        """<p>Updates an existing optimization profile's configuration, including its pillars, execution role, and aggregation settings.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            profile_arn: <p>The Amazon Resource Name (ARN) of the profile to update.</p>
            display_name: <p>The updated display name of the profile.</p>
            description: <p>The updated description of the profile.</p>
            execution_role_arn: <p>The updated ARN of the IAM execution role.</p>
            aggregation_configuration: <p>The updated aggregation configuration.</p>
            business_overview: <p>The updated business overview for the profile.</p>
            pillars: <p>The updated Well-Architected Tool Framework pillars for the profile.</p>
            deletion_protection: <p>Indicates whether deletion protection is enabled for the profile.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_agent_profile_request.UpdateAgentProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_agent_profile_response.UpdateAgentProfileResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_profile.async_update_agent_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_agent_profile_request.UpdateAgentProfileRequest = {
            "profile_arn": profile_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if aggregation_configuration is not None:
            input_["aggregation_configuration"] = aggregation_configuration
        if business_overview is not None:
            input_["business_overview"] = business_overview
        if pillars is not None:
            input_["pillars"] = pillars
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_recommendation_status(
        self,
        recommendation_arn: "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn",
        status: "capo_wellarchitected.types.recommendation_status.RecommendationStatus",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        update_reason: Optional[
            "capo_wellarchitected.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "capo_wellarchitected.types.update_agent_recommendation_status_response.UpdateAgentRecommendationStatusResponse":
        """<p>Updates the status of a recommendation to track its progress through the implementation lifecycle.</p>

        Args:
            recommendation_arn: <p>The Amazon Resource Name (ARN) of the recommendation to update.</p>
            status: <p>The new status to assign to the recommendation.</p>
            update_reason: <p>A free-text reason explaining this status update.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_agent_recommendation_status_request.UpdateAgentRecommendationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_agent_recommendation_status_response.UpdateAgentRecommendationStatusResponse"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_recommendation_status

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_agent_recommendation_status.async_update_agent_recommendation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_agent_recommendation_status_request.UpdateAgentRecommendationStatusRequest = {
            "recommendation_arn": recommendation_arn,
            "status": status,
        }
        if update_reason is not None:
            input_["update_reason"] = update_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_answer(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "capo_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "capo_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "capo_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "capo_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "capo_wellarchitected.types.update_answer_output.UpdateAnswerOutput":
        """<p>Update the answer to a specific question in a workload review.</p>

        Args:
            choice_updates: <p>A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated.</p>
            reason: <p>The reason why a question is not applicable to your workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_answer_input.UpdateAnswerInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_answer_output.UpdateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_answer

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_answer.async_update_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_answer_input.UpdateAnswerInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
            "question_id": question_id,
        }
        if selected_choices is not None:
            input_["selected_choices"] = selected_choices
        if choice_updates is not None:
            input_["choice_updates"] = choice_updates
        if notes is not None:
            input_["notes"] = notes
        if is_applicable is not None:
            input_["is_applicable"] = is_applicable
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_global_settings(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        organization_sharing_status: Optional[
            "capo_wellarchitected.types.organization_sharing_status.OrganizationSharingStatus"
        ] = None,
        discovery_integration_status: Optional[
            "capo_wellarchitected.types.discovery_integration_status.DiscoveryIntegrationStatus"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.account_jira_configuration_input.AccountJiraConfigurationInput"
        ] = None,
    ) -> None:
        """<p>Update whether the Amazon Web Services account is opted into organization sharing and discovery integration features.</p>

        Args:
            organization_sharing_status: <p>The status of organization sharing settings.</p>
            discovery_integration_status: <p>The status of discovery support settings.</p>
            jira_configuration: <p>The status of Jira integration settings.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings.async_update_global_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput = {}
        if organization_sharing_status is not None:
            input_["organization_sharing_status"] = organization_sharing_status
        if discovery_integration_status is not None:
            input_["discovery_integration_status"] = discovery_integration_status
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_integration(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
        integrating_service: Optional[
            "capo_wellarchitected.types.integrating_service.IntegratingService"
        ] = None,
    ) -> None:
        """<p>Update integration features.</p>

        Args:
            integrating_service: <p>Which integrated service to update.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_integration

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_integration_input.UpdateIntegrationInput = {
            "workload_id": workload_id
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if integrating_service is not None:
            input_["integrating_service"] = integrating_service

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "capo_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
        ] = None,
    ) -> "capo_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput":
        """<p>Update lens review for a particular workload.</p>

        Args:
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review.async_update_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_description: Optional[
            "capo_wellarchitected.types.profile_description.ProfileDescription"
        ] = None,
        profile_questions: Optional[
            "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
        ] = None,
    ) -> "capo_wellarchitected.types.update_profile_output.UpdateProfileOutput":
        """<p>Update a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>Profile questions.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_profile_input.UpdateProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_profile_output.UpdateProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_profile

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_profile_input.UpdateProfileInput = {
            "profile_arn": profile_arn
        }
        if profile_description is not None:
            input_["profile_description"] = profile_description
        if profile_questions is not None:
            input_["profile_questions"] = profile_questions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        template_name: Optional[
            "capo_wellarchitected.types.template_name.TemplateName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.template_description.TemplateDescription"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        lenses_to_associate: Optional[
            "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
        lenses_to_disassociate: Optional[
            "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput":
        """<p>Update a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            template_name: <p>The review template name.</p>
            description: <p>The review template description.</p>
            lenses_to_associate: <p>A list of lens aliases or ARNs to apply to the review template.</p>
            lenses_to_disassociate: <p>A list of lens aliases or ARNs to unapply to the review template. The <code>wellarchitected</code> lens cannot be unapplied.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template.async_update_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput = {
            "template_arn": template_arn
        }
        if template_name is not None:
            input_["template_name"] = template_name
        if description is not None:
            input_["description"] = description
        if notes is not None:
            input_["notes"] = notes
        if lenses_to_associate is not None:
            input_["lenses_to_associate"] = lenses_to_associate
        if lenses_to_disassociate is not None:
            input_["lenses_to_disassociate"] = lenses_to_disassociate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_review_template_answer(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "capo_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "capo_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "capo_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "capo_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput":
        """<p>Update a review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            choice_updates: <p>A list of choices to be updated.</p>
            reason: <p>The update reason.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer.async_update_review_template_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
            "question_id": question_id,
        }
        if selected_choices is not None:
            input_["selected_choices"] = selected_choices
        if choice_updates is not None:
            input_["choice_updates"] = choice_updates
        if notes is not None:
            input_["notes"] = notes
        if is_applicable is not None:
            input_["is_applicable"] = is_applicable
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "capo_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput":
        """<p>Update a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review.async_update_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
        }
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_share_invitation(
        self,
        share_invitation_id: "capo_wellarchitected.types.share_invitation_id.ShareInvitationId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        share_invitation_action: Optional[
            "capo_wellarchitected.types.share_invitation_action.ShareInvitationAction"
        ] = None,
    ) -> "capo_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput":
        """<p>Update a workload or custom lens share invitation.</p> <note> <p>This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.</p> </note>

        Args:
            share_invitation_id: <p>The ID assigned to the share invitation.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation.async_update_share_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput = {
            "share_invitation_id": share_invitation_id
        }
        if share_invitation_action is not None:
            input_["share_invitation_action"] = share_invitation_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name: Optional[
            "capo_wellarchitected.types.workload_name.WorkloadName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.workload_description.WorkloadDescription"
        ] = None,
        environment: Optional[
            "capo_wellarchitected.types.workload_environment.WorkloadEnvironment"
        ] = None,
        account_ids: Optional[
            "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        is_review_owner_update_acknowledged: Optional[
            "capo_wellarchitected.types.is_review_owner_update_acknowledged.IsReviewOwnerUpdateAcknowledged"
        ] = None,
        industry_type: Optional[
            "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        improvement_status: Optional[
            "capo_wellarchitected.types.workload_improvement_status.WorkloadImprovementStatus"
        ] = None,
        discovery_config: Optional[
            "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "capo_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "capo_wellarchitected.types.update_workload_output.UpdateWorkloadOutput":
        """<p>Update an existing workload.</p>

        Args:
            is_review_owner_update_acknowledged: <p>Flag indicating whether the workload owner has acknowledged that the <i>Review owner</i> field is required.</p> <p>If a <b>Review owner</b> is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.</p>
            discovery_config: <p>Well-Architected discovery configuration settings to associate to the workload.</p>
            applications: <p>List of AppRegistry application ARNs to associate to the workload.</p>
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_workload_input.UpdateWorkloadInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_workload_output.UpdateWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload.async_update_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_workload_input.UpdateWorkloadInput = {
            "workload_id": workload_id
        }
        if workload_name is not None:
            input_["workload_name"] = workload_name
        if description is not None:
            input_["description"] = description
        if environment is not None:
            input_["environment"] = environment
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if aws_regions is not None:
            input_["aws_regions"] = aws_regions
        if non_aws_regions is not None:
            input_["non_aws_regions"] = non_aws_regions
        if pillar_priorities is not None:
            input_["pillar_priorities"] = pillar_priorities
        if architectural_design is not None:
            input_["architectural_design"] = architectural_design
        if review_owner is not None:
            input_["review_owner"] = review_owner
        if is_review_owner_update_acknowledged is not None:
            input_["is_review_owner_update_acknowledged"] = (
                is_review_owner_update_acknowledged
            )
        if industry_type is not None:
            input_["industry_type"] = industry_type
        if industry is not None:
            input_["industry"] = industry
        if notes is not None:
            input_["notes"] = notes
        if improvement_status is not None:
            input_["improvement_status"] = improvement_status
        if discovery_config is not None:
            input_["discovery_config"] = discovery_config
        if applications is not None:
            input_["applications"] = applications
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workload_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        permission_type: Optional[
            "capo_wellarchitected.types.permission_type.PermissionType"
        ] = None,
    ) -> "capo_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput":
        """<p>Update a workload share.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput]",
        ) -> AsyncOperationResponse[
            "capo_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share.async_update_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput = {
            "share_id": share_id,
            "workload_id": workload_id,
        }
        if permission_type is not None:
            input_["permission_type"] = permission_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upgrade_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_name: Optional[
            "capo_wellarchitected.types.milestone_name.MilestoneName"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade lens review for a particular workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review.async_upgrade_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput = {
            "workload_id": workload_id,
            "lens_alias": lens_alias,
        }
        if milestone_name is not None:
            input_["milestone_name"] = milestone_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upgrade_profile_version(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_name: Optional[
            "capo_wellarchitected.types.milestone_name.MilestoneName"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version.async_upgrade_profile_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput = {
            "workload_id": workload_id,
            "profile_arn": profile_arn,
        }
        if milestone_name is not None:
            input_["milestone_name"] = milestone_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upgrade_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade the lens review of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review

            (
                output,
                http_response,
            ) = await capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review.async_upgrade_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput = {
            "template_arn": template_arn,
            "lens_alias": lens_alias,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
