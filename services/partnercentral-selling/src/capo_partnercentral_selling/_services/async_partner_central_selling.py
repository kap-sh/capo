"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AWSPartnerCentralSelling``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_partnercentral_selling._auth._signers
import capo_partnercentral_selling._auth._sigv4
from capo_partnercentral_selling._auth._identity import Credentials
from capo_partnercentral_selling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_selling._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_selling._pagination import resolve_path as _resolve_path
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement import (
    AsyncEngagement,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_by_accepting_invitation_task import (
    AsyncEngagementByAcceptingInvitationTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_from_opportunity_task import (
    AsyncEngagementFromOpportunityTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_invitation import (
    AsyncEngagementInvitation,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.opportunity import (
    AsyncOpportunity,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.opportunity_from_engagement_task import (
    AsyncOpportunityFromEngagementTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.prospecting_from_engagement_task import (
    AsyncProspectingFromEngagementTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.resource_snapshot import (
    AsyncResourceSnapshot,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.resource_snapshot_job import (
    AsyncResourceSnapshotJob,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.solution import (
    AsyncSolution,
)
from capo_partnercentral_selling._services._aws_config import aaws_config
from capo_partnercentral_selling._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.accept_engagement_invitation_request
    import capo_partnercentral_selling.types.assign_opportunity_request
    import capo_partnercentral_selling.types.assignee_contact
    import capo_partnercentral_selling.types.associate_opportunity_request
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.aws_account_id_or_alias_list
    import capo_partnercentral_selling.types.aws_account_list
    import capo_partnercentral_selling.types.aws_marketplace_solution_arn_list
    import capo_partnercentral_selling.types.aws_submission
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.context_identifier
    import capo_partnercentral_selling.types.context_identifiers
    import capo_partnercentral_selling.types.create_engagement_context_request
    import capo_partnercentral_selling.types.create_engagement_context_response
    import capo_partnercentral_selling.types.create_engagement_invitation_request
    import capo_partnercentral_selling.types.create_engagement_invitation_response
    import capo_partnercentral_selling.types.create_engagement_request
    import capo_partnercentral_selling.types.create_engagement_response
    import capo_partnercentral_selling.types.create_opportunity_request
    import capo_partnercentral_selling.types.create_opportunity_response
    import capo_partnercentral_selling.types.create_resource_snapshot_job_request
    import capo_partnercentral_selling.types.create_resource_snapshot_job_response
    import capo_partnercentral_selling.types.create_resource_snapshot_request
    import capo_partnercentral_selling.types.create_resource_snapshot_response
    import capo_partnercentral_selling.types.created_date_filter
    import capo_partnercentral_selling.types.customer
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.delete_resource_snapshot_job_request
    import capo_partnercentral_selling.types.disassociate_opportunity_request
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_context_payload
    import capo_partnercentral_selling.types.engagement_context_type
    import capo_partnercentral_selling.types.engagement_context_type_list
    import capo_partnercentral_selling.types.engagement_contexts
    import capo_partnercentral_selling.types.engagement_description
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.engagement_identifier_list
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_invitation_identifiers
    import capo_partnercentral_selling.types.engagement_invitation_summary
    import capo_partnercentral_selling.types.engagement_invitations_payload_type
    import capo_partnercentral_selling.types.engagement_member
    import capo_partnercentral_selling.types.engagement_page_size
    import capo_partnercentral_selling.types.engagement_resource_association_summary
    import capo_partnercentral_selling.types.engagement_sort
    import capo_partnercentral_selling.types.engagement_summary
    import capo_partnercentral_selling.types.engagement_title
    import capo_partnercentral_selling.types.filter_identifier
    import capo_partnercentral_selling.types.filter_life_cycle_review_status
    import capo_partnercentral_selling.types.filter_life_cycle_stage
    import capo_partnercentral_selling.types.filter_status
    import capo_partnercentral_selling.types.get_aws_opportunity_summary_request
    import capo_partnercentral_selling.types.get_aws_opportunity_summary_response
    import capo_partnercentral_selling.types.get_engagement_invitation_request
    import capo_partnercentral_selling.types.get_engagement_invitation_response
    import capo_partnercentral_selling.types.get_engagement_request
    import capo_partnercentral_selling.types.get_engagement_response
    import capo_partnercentral_selling.types.get_opportunity_request
    import capo_partnercentral_selling.types.get_opportunity_response
    import capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request
    import capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response
    import capo_partnercentral_selling.types.get_resource_snapshot_job_request
    import capo_partnercentral_selling.types.get_resource_snapshot_job_response
    import capo_partnercentral_selling.types.get_resource_snapshot_request
    import capo_partnercentral_selling.types.get_resource_snapshot_response
    import capo_partnercentral_selling.types.get_selling_system_settings_request
    import capo_partnercentral_selling.types.get_selling_system_settings_response
    import capo_partnercentral_selling.types.invitation
    import capo_partnercentral_selling.types.invitation_status_list
    import capo_partnercentral_selling.types.last_modified_date
    import capo_partnercentral_selling.types.life_cycle
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_task_summary
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request
    import capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response
    import capo_partnercentral_selling.types.list_engagement_invitations_request
    import capo_partnercentral_selling.types.list_engagement_invitations_response
    import capo_partnercentral_selling.types.list_engagement_members_request
    import capo_partnercentral_selling.types.list_engagement_members_response
    import capo_partnercentral_selling.types.list_engagement_resource_associations_request
    import capo_partnercentral_selling.types.list_engagement_resource_associations_response
    import capo_partnercentral_selling.types.list_engagements_request
    import capo_partnercentral_selling.types.list_engagements_response
    import capo_partnercentral_selling.types.list_opportunities_request
    import capo_partnercentral_selling.types.list_opportunities_response
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response
    import capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request
    import capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response
    import capo_partnercentral_selling.types.list_resource_snapshot_jobs_request
    import capo_partnercentral_selling.types.list_resource_snapshot_jobs_response
    import capo_partnercentral_selling.types.list_resource_snapshots_request
    import capo_partnercentral_selling.types.list_resource_snapshots_response
    import capo_partnercentral_selling.types.list_solutions_request
    import capo_partnercentral_selling.types.list_solutions_response
    import capo_partnercentral_selling.types.list_tags_for_resource_request
    import capo_partnercentral_selling.types.list_tags_for_resource_response
    import capo_partnercentral_selling.types.list_tasks_sort_base
    import capo_partnercentral_selling.types.marketing
    import capo_partnercentral_selling.types.member_page_size
    import capo_partnercentral_selling.types.national_security
    import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_identifiers
    import capo_partnercentral_selling.types.opportunity_origin
    import capo_partnercentral_selling.types.opportunity_sort
    import capo_partnercentral_selling.types.opportunity_summary
    import capo_partnercentral_selling.types.opportunity_type
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.participant_type
    import capo_partnercentral_selling.types.partner_opportunity_team_members_list
    import capo_partnercentral_selling.types.primary_needs_from_aws
    import capo_partnercentral_selling.types.project
    import capo_partnercentral_selling.types.prospecting_from_engagement_task_sort
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.prospecting_task_summary
    import capo_partnercentral_selling.types.put_selling_system_settings_request
    import capo_partnercentral_selling.types.put_selling_system_settings_response
    import capo_partnercentral_selling.types.reject_engagement_invitation_request
    import capo_partnercentral_selling.types.rejection_reason_string
    import capo_partnercentral_selling.types.related_entity_type
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_role_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_status
    import capo_partnercentral_selling.types.resource_snapshot_job_summary
    import capo_partnercentral_selling.types.resource_snapshot_revision
    import capo_partnercentral_selling.types.resource_snapshot_summary
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.software_revenue
    import capo_partnercentral_selling.types.solution_base
    import capo_partnercentral_selling.types.solution_identifiers
    import capo_partnercentral_selling.types.solution_sort
    import capo_partnercentral_selling.types.sort_object
    import capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request
    import capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response
    import capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request
    import capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response
    import capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request
    import capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response
    import capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request
    import capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response
    import capo_partnercentral_selling.types.start_resource_snapshot_job_request
    import capo_partnercentral_selling.types.stop_resource_snapshot_job_request
    import capo_partnercentral_selling.types.string_list
    import capo_partnercentral_selling.types.submit_opportunity_request
    import capo_partnercentral_selling.types.tag_key_list
    import capo_partnercentral_selling.types.tag_list
    import capo_partnercentral_selling.types.tag_resource_request
    import capo_partnercentral_selling.types.tag_resource_response
    import capo_partnercentral_selling.types.taggable_resource_arn
    import capo_partnercentral_selling.types.target_close_date_filter
    import capo_partnercentral_selling.types.task_identifier_list
    import capo_partnercentral_selling.types.task_identifiers
    import capo_partnercentral_selling.types.task_name
    import capo_partnercentral_selling.types.task_name_list
    import capo_partnercentral_selling.types.task_statuses
    import capo_partnercentral_selling.types.untag_resource_request
    import capo_partnercentral_selling.types.untag_resource_response
    import capo_partnercentral_selling.types.update_engagement_context_payload
    import capo_partnercentral_selling.types.update_engagement_context_request
    import capo_partnercentral_selling.types.update_engagement_context_response
    import capo_partnercentral_selling.types.update_opportunity_request
    import capo_partnercentral_selling.types.update_opportunity_response
    import capo_partnercentral_selling.types.visibility


class AsyncPartnerCentralSellingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPartnerCentralSellingClient:
    """A client for the ``PartnerCentralSelling`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncPartnerCentralSellingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.engagement = AsyncEngagement(self)
        self.engagement_by_accepting_invitation_task = (
            AsyncEngagementByAcceptingInvitationTask(self)
        )
        self.engagement_from_opportunity_task = AsyncEngagementFromOpportunityTask(self)
        self.engagement_invitation = AsyncEngagementInvitation(self)
        self.opportunity = AsyncOpportunity(self)
        self.opportunity_from_engagement_task = AsyncOpportunityFromEngagementTask(self)
        self.prospecting_from_engagement_task = AsyncProspectingFromEngagementTask(self)
        self.resource_snapshot = AsyncResourceSnapshot(self)
        self.resource_snapshot_job = AsyncResourceSnapshotJob(self)
        self.solution = AsyncSolution(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralSellingClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_engagement_context(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "capo_partnercentral_selling.types.engagement_context_payload.EngagementContextPayload",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse":
        """<p>Creates a new context within an existing engagement. This action allows you to add contextual information such as customer projects or documents to an engagement, providing additional details that help facilitate collaboration between engagement members.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is created in. Use <code>AWS</code> to create contexts in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> for which the context is being created. This parameter ensures the context is associated with the correct engagement and provides the necessary linkage between the engagement and its contextual information.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure that the request is handled exactly once. This token helps prevent duplicate context creations and must not exceed sixty-four alphanumeric characters. Use a UUID or other unique string to ensure idempotency.</p>
            type: <p>Specifies the type of context being created for the engagement. This field determines the structure and content of the context payload. Valid values include <code>CustomerProject</code> for customer project-related contexts. The type field ensures that the context is properly categorized and processed according to its intended purpose.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context.async_create_engagement_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest = {
            "catalog": catalog,
            "engagement_identifier": engagement_identifier,
            "client_token": client_token,
            "type": type,
            "payload": payload,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_selling_system_settings(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse":
        """<p>Retrieves the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings are defined. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings.async_get_selling_system_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest = {
            "catalog": catalog
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_selling_system_settings(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        resource_snapshot_job_role_identifier: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_role_identifier.ResourceSnapshotJobRoleIdentifier"
        ] = None,
    ) -> "capo_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse":
        """<p>Updates the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings will be updated. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            resource_snapshot_job_role_identifier: <p>Specifies the ARN of the IAM Role used for resource snapshot job executions.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings.async_put_selling_system_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest = {
            "catalog": catalog
        }
        if resource_snapshot_job_role_identifier is not None:
            input_["resource_snapshot_job_role_identifier"] = (
                resource_snapshot_job_role_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_partnercentral_selling.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.tag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_partnercentral_selling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.untag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_engagement_context(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier",
        engagement_last_modified_at: "capo_partnercentral_selling.types.date_time.DateTime",
        type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "capo_partnercentral_selling.types.update_engagement_context_payload.UpdateEngagementContextPayload",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse":
        """<p>Updates the context information for an existing engagement with new or modified data.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is updated in.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.</p>
            engagement_last_modified_at: <p>The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.</p>
            type: <p>Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.</p>
            payload: <p>Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context.async_update_engagement_context(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest = {
            "catalog": catalog,
            "engagement_identifier": engagement_identifier,
            "context_identifier": context_identifier,
            "engagement_last_modified_at": engagement_last_modified_at,
            "type": type,
            "payload": payload,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_engagement(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        title: Optional[
            "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
        ] = None,
        description: Optional[
            "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
        ] = None,
        contexts: Optional[
            "capo_partnercentral_selling.types.engagement_contexts.EngagementContexts"
        ] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse":
        """<p>The <code>CreateEngagement</code> action allows you to create an <code>Engagement</code>, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created <code>Engagement</code>.</p>

        Args:
            catalog: <p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>
            client_token: <p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>
            title: <p>Specifies the title of the <code>Engagement</code>.</p>
            description: <p>Provides a description of the <code>Engagement</code>.</p>
            contexts: <p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement.async_create_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if contexts is not None:
            input_["contexts"] = contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_engagement(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse":
        """<p>Use this action to retrieve the engagement record for a given <code>EngagementIdentifier</code>.</p>

        Args:
            catalog: <p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>
            identifier: <p>Specifies the identifier of the Engagement record to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement.async_get_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_engagements(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse":
        """<p>This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            created_by: <p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>
            exclude_created_by: <p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>
            context_types: <p>Filters engagements to include only those containing the specified context types, such as "CustomerProject" or "Lead". Use this to find engagements that have specific types of contextual information associated with them.</p>
            exclude_context_types: <p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. This value is returned from a previous call.</p>
            engagement_identifier: <p>An array of strings representing engagement identifiers to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements.async_list_engagements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest = {
            "catalog": catalog
        }
        if created_by is not None:
            input_["created_by"] = created_by
        if exclude_created_by is not None:
            input_["exclude_created_by"] = exclude_created_by
        if context_types is not None:
            input_["context_types"] = context_types
        if exclude_context_types is not None:
            input_["exclude_context_types"] = exclude_context_types
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_engagements(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.engagement_summary.EngagementSummary]":
        _token = next_token
        while True:
            _response = await self.list_engagements(
                catalog,
                config_overrides=config_overrides,
                created_by=created_by,
                exclude_created_by=exclude_created_by,
                context_types=context_types,
                exclude_context_types=exclude_context_types,
                sort=sort,
                max_results=max_results,
                next_token=_token,
                engagement_identifier=engagement_identifier,
            )
            _page = _resolve_path(_response, ("engagement_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_engagement_members(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse":
        """<p>Retrieves the details of member partners in an Engagement. This operation can only be invoked by members of the Engagement. The <code>ListEngagementMembers</code> operation allows you to fetch information about the members of a specific Engagement. This action is restricted to members of the Engagement being queried. </p>

        Args:
            catalog: <p>The catalog related to the request.</p>
            identifier: <p>Identifier of the Engagement record to retrieve members from.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members.async_list_engagement_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest = {
            "catalog": catalog,
            "identifier": identifier,
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

    async def iter_list_engagement_members(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.engagement_member.EngagementMember]":
        _token = next_token
        while True:
            _response = await self.list_engagement_members(
                catalog,
                identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("engagement_member_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_engagement_by_accepting_invitation_task(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse":
        """<p>This action starts the engagement by accepting an <code>EngagementInvitation</code>. The task is asynchronous and involves the following steps: accepting the invitation, creating an opportunity in the partner’s account from the AWS opportunity, and copying details for tracking. When completed, an <code>Opportunity Created</code> event is generated, indicating that the opportunity has been successfully created in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog related to the task. Use <code>AWS</code> for production engagements and <code>Sandbox</code> for testing scenarios.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client that helps to ensure the idempotency of the request. This can be a random or meaningful string but must be unique for each request.</p>
            identifier: <p>Specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier helps ensure that the correct engagement is processed.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task.async_start_engagement_by_accepting_invitation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
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

    async def list_engagement_by_accepting_invitation_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_invitation_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_invitation_identifiers.EngagementInvitationIdentifiers"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse":
        """<p> Lists all in-progress, completed, or failed StartEngagementByAcceptingInvitationTask tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> Use this parameter for pagination when the result set spans multiple pages. This value is obtained from the NextToken field in the response of a previous call to this API. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            opportunity_identifier: <p> Filters tasks by the identifiers of the opportunities they created or are associated with. </p>
            engagement_invitation_identifier: <p> Filters tasks by the identifiers of the engagement invitations they are processing. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks.async_list_engagement_by_accepting_invitation_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if task_status is not None:
            input_["task_status"] = task_status
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_invitation_identifier is not None:
            input_["engagement_invitation_identifier"] = (
                engagement_invitation_identifier
            )
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_engagement_by_accepting_invitation_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_invitation_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_invitation_identifiers.EngagementInvitationIdentifiers"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary.ListEngagementByAcceptingInvitationTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_engagement_by_accepting_invitation_tasks(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                task_status=task_status,
                opportunity_identifier=opportunity_identifier,
                engagement_invitation_identifier=engagement_invitation_identifier,
                task_identifier=task_identifier,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_engagement_from_opportunity_task(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        aws_submission: "capo_partnercentral_selling.types.aws_submission.AwsSubmission",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse":
        """<p>Similar to <code>StartEngagementByAcceptingInvitationTask</code>, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including <code>GetOpportunity</code>, <code>CreateEngagement</code> (if it doesn't exist), <code>CreateResourceSnapshot</code>, <code>CreateResourceSnapshotJob</code>, <code>CreateEngagementInvitation</code> (if not already invited/accepted), and <code>SubmitOpportunity</code>. </p>

        Args:
            catalog: <p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task.async_start_engagement_from_opportunity_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "aws_submission": aws_submission,
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

    async def list_engagement_from_opportunity_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse":
        """<p> Lists all in-progress, completed, or failed <code>EngagementFromOpportunity</code> tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
            opportunity_identifier: <p> The identifier of the original opportunity associated with this task. </p>
            engagement_identifier: <p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks.async_list_engagement_from_opportunity_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if task_status is not None:
            input_["task_status"] = task_status
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_engagement_from_opportunity_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.list_engagement_from_opportunity_task_summary.ListEngagementFromOpportunityTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_engagement_from_opportunity_tasks(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                task_status=task_status,
                task_identifier=task_identifier,
                opportunity_identifier=opportunity_identifier,
                engagement_identifier=engagement_identifier,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        invitation: "capo_partnercentral_selling.types.invitation.Invitation",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse":
        """<p> This action creates an invitation from a sender to a single receiver to join an engagement. </p>

        Args:
            catalog: <p> Specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate invitation creations. </p>
            engagement_identifier: <p> The unique identifier of the <code>Engagement</code> associated with the invitation. This parameter ensures the invitation is created within the correct <code>Engagement</code> context. </p>
            invitation: <p> The <code>Invitation</code> object all information necessary to initiate an engagement invitation to a partner. It contains a personalized message from the sender, the invitation's receiver, and a payload. The <code>Payload</code> can be the <code>OpportunityInvitation</code>, which includes detailed structures for sender contacts, partner responsibilities, customer information, and project details, or <code>LeadInvitation</code>, which includes structures for customer information and interaction details. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation.async_create_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "invitation": invitation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse":
        """<p>Retrieves the details of an engagement invitation shared by AWS with a partner. The information includes aspects such as customer, project details, and lifecycle information. To connect an engagement invitation with an opportunity, match the invitation’s <code>Payload.Project.Title</code> with opportunity <code>Project.Title</code>.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. The field accepts values from the predefined set: <code>AWS</code> for live operations or <code>Sandbox</code> for testing environments.</p>
            identifier: <p>Specifies the unique identifier for the retrieved engagement invitation.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation.async_get_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_engagement_invitations(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        participant_type: "capo_partnercentral_selling.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.OpportunityEngagementInvitationSort"
        ] = None,
        payload_type: Optional[
            "capo_partnercentral_selling.types.engagement_invitations_payload_type.EngagementInvitationsPayloadType"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.invitation_status_list.InvitationStatusList"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        sender_aws_account_id: Optional[
            "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse":
        """<p>Retrieves a list of engagement invitations sent to the partner. This allows partners to view all pending or past engagement invitations, helping them track opportunities shared by AWS.</p>

        Args:
            catalog: <p>Specifies the catalog from which to list the engagement invitations. Use <code>AWS</code> for production invitations or <code>Sandbox</code> for testing environments.</p>
            max_results: <p>Specifies the maximum number of engagement invitations to return in the response. If more results are available, a pagination token will be provided.</p>
            next_token: <p>A pagination token used to retrieve additional pages of results when the response to a previous request was truncated. Pass this token to continue listing invitations from where the previous call left off.</p>
            sort: <p>Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as <code>InvitationDate</code> or <code>Status</code> to help partners view results in their preferred order.</p>
            payload_type: <p>Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.</p>
            participant_type: <p>Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.</p>
            status: <p> Status values to filter the invitations. </p>
            engagement_identifier: <p> Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days. </p>
            sender_aws_account_id: <p> List of sender AWS account IDs to filter the invitations. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations.async_list_engagement_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest = {
            "catalog": catalog,
            "participant_type": participant_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if payload_type is not None:
            input_["payload_type"] = payload_type
        if status is not None:
            input_["status"] = status
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if sender_aws_account_id is not None:
            input_["sender_aws_account_id"] = sender_aws_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_engagement_invitations(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        participant_type: "capo_partnercentral_selling.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.OpportunityEngagementInvitationSort"
        ] = None,
        payload_type: Optional[
            "capo_partnercentral_selling.types.engagement_invitations_payload_type.EngagementInvitationsPayloadType"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.invitation_status_list.InvitationStatusList"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        sender_aws_account_id: Optional[
            "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.engagement_invitation_summary.EngagementInvitationSummary]":
        _token = next_token
        while True:
            _response = await self.list_engagement_invitations(
                catalog,
                participant_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                payload_type=payload_type,
                status=status,
                engagement_identifier=engagement_identifier,
                sender_aws_account_id=sender_aws_account_id,
            )
            _page = _resolve_path(_response, ("engagement_invitation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def accept_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Use the <code>AcceptEngagementInvitation</code> action to accept an engagement invitation shared by AWS. Accepting the invitation indicates your willingness to participate in the engagement, granting you access to all engagement-related data.</p>

        Args:
            catalog: <p>The <code>CatalogType</code> parameter specifies the catalog associated with the engagement invitation. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement invitation is managed.</p>
            identifier: <p> The <code>Identifier</code> parameter in the <code>AcceptEngagementInvitationRequest</code> specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier ensures that the intended invitation is accepted. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation.async_accept_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        rejection_reason: Optional[
            "capo_partnercentral_selling.types.rejection_reason_string.RejectionReasonString"
        ] = None,
    ) -> None:
        """<p>This action rejects an <code>EngagementInvitation</code> that AWS shared. Rejecting an invitation indicates that the partner doesn't want to pursue the opportunity, and all related data will become inaccessible thereafter.</p>

        Args:
            catalog: <p>This is the catalog that's associated with the engagement invitation. Acceptable values are <code>AWS</code> or <code>Sandbox</code>, and these values determine the environment in which the opportunity is managed.</p>
            identifier: <p>This is the unique identifier of the rejected <code>EngagementInvitation</code>. Providing the correct identifier helps to ensure that the intended invitation is rejected.</p>
            rejection_reason: <p>This describes the reason for rejecting the engagement invitation, which helps AWS track usage patterns. Acceptable values include the following:</p> <ul> <li> <p> <i>Customer problem unclear:</i> The customer's problem isn't understood.</p> </li> <li> <p> <i>Next steps unclear:</i> The next steps required to proceed aren't understood.</p> </li> <li> <p> <i>Unable to support:</i> The partner is unable to provide support due to resource or capability constraints.</p> </li> <li> <p> <i>Duplicate of partner referral:</i> The opportunity is a duplicate of an existing referral.</p> </li> <li> <p> <i>Other:</i> Any reason not covered by other values.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation.async_reject_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if rejection_reason is not None:
            input_["rejection_reason"] = rejection_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
        origin: Optional[
            "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
        ] = None,
        opportunity_team: Optional[
            "capo_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
        ] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse":
        """<p>Creates an <code>Opportunity</code> record in Partner Central. Use this operation to create a potential business opportunity for submission to Amazon Web Services. Creating an opportunity sets <code>Lifecycle.ReviewStatus</code> to <code>Pending Submission</code>.</p> <p>To submit an opportunity, follow these steps:</p> <ol> <li> <p>To create the opportunity, use <code>CreateOpportunity</code>.</p> </li> <li> <p>To associate a solution with the opportunity, use <code>AssociateOpportunity</code>.</p> </li> <li> <p>To start the engagement with AWS, use <code>StartEngagementFromOpportunity</code>.</p> </li> </ol> <p>After submission, you can't edit the opportunity until the review is complete. But opportunities in the <code>Pending Submission</code> state must have complete details. You can update the opportunity while it's in the <code>Pending Submission</code> state.</p> <p>There's a set of mandatory fields to create opportunities, but consider providing optional fields to enrich the opportunity record.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is created in. Use <code>AWS</code> to create opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.</p> </li> </ul>
            national_security: <p>Indicates whether the <code>Opportunity</code> pertains to a national security project. This field must be set to <code>true</code> only when the customer's industry is <i>Government</i>. Additional privacy and security measures apply during the review and management process for opportunities marked as <code>NationalSecurity</code>.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload to the partner.</p> <p>This field allows partners to link an opportunity to their CRM, which helps to ensure seamless integration and accurate synchronization between the Partner Central API and the partner's internal systems.</p>
            customer: <p>Specifies customer details associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>This object contains marketing details and is optional for an opportunity.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. This is required only for partners in eligible programs.</p>
            client_token: <p>Required to be unique, and should be unchanging, it can be randomly generated or a meaningful string.</p> <p>Default: None</p> <p>Best practice: To help ensure uniqueness and avoid conflicts, use a Universally Unique Identifier (UUID) as the <code>ClientToken</code>. You can use standard libraries from most programming languages to generate this. If you use the same client token, the API returns the following error: "Conflicting client token submitted for a new request body."</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>
            origin: <p>Specifies the origin of the opportunity, indicating if it was sourced from Amazon Web Services or the partner. For all opportunities created with <code>Catalog: AWS</code>, this field must only be <code>Partner Referral</code>. However, when using <code>Catalog: Sandbox</code>, you can set this field to <code>AWS Referral</code> to simulate Amazon Web Services referral creation. This allows Amazon Web Services-originated flows testing in the sandbox catalog.</p>
            opportunity_team: <p>Represents the internal team handling the opportunity. Specify collaborating members of this opportunity who are within the partner's organization.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity.async_create_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle
        if origin is not None:
            input_["origin"] = origin
        if opportunity_team is not None:
            input_["opportunity_team"] = opportunity_team
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse":
        """<p>Fetches the <code>Opportunity</code> record from Partner Central by a given <code>Identifier</code>.</p> <p>Use the <code>ListOpportunities</code> action or the event notification (from Amazon EventBridge) to obtain this identifier.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is fetched from. Use <code>AWS</code> to retrieve opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> to retrieve opportunities in a secure, isolated testing environment.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity.async_get_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        last_modified_date: "capo_partnercentral_selling.types.date_time.DateTime",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
    ) -> "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse":
        """<p>Updates the <code>Opportunity</code> record identified by a given <code>Identifier</code>. This operation allows you to modify the details of an existing opportunity to reflect the latest information and progress. Use this action to keep the opportunity record up-to-date and accurate.</p> <p>When you perform updates, include the entire payload with each request. If any field is omitted, the API assumes that the field is set to <code>null</code>. The best practice is to always perform a <code>GetOpportunity</code> to retrieve the latest values, then send the complete payload with the updated values to be changed.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is updated in. Use <code>AWS</code> to update real opportunities in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments. When you use the <code>Sandbox</code> catalog, it allows you to simulate and validate your interactions with Amazon Web Services services without affecting live data or operations.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an AWS seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connection with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs RFx support from Amazon Web Services.</p> </li> </ul>
            national_security: <p>Specifies if the opportunity is associated with national security concerns. This flag is only applicable when the industry is <code>Government</code>. For national-security-related opportunities, validation and compliance rules may apply, impacting the opportunity's visibility and processing.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.</p>
            customer: <p>Specifies details of the customer associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details summary for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>An object that contains marketing details for the <code>Opportunity</code>.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. Required only for partners in eligible programs.</p>
            last_modified_date: <p> <code>DateTime</code> when the opportunity was last modified.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity.async_update_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest = {
            "catalog": catalog,
            "last_modified_date": last_modified_date,
            "identifier": identifier,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_opportunities(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_sort.OpportunitySort"
        ] = None,
        last_modified_date: Optional[
            "capo_partnercentral_selling.types.last_modified_date.LastModifiedDate"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.filter_identifier.FilterIdentifier"
        ] = None,
        life_cycle_stage: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
        ] = None,
        life_cycle_review_status: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
        ] = None,
        customer_company_name: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        created_date: Optional[
            "capo_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
        ] = None,
        target_close_date: Optional[
            "capo_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse":
        """<p>This request accepts a list of filters that retrieve opportunity subsets as well as sort options. This feature is available to partners from <a href="https://partnercentral.awspartner.com/">Partner Central</a> using the <code>ListOpportunities</code> API action.</p> <p>To synchronize your system with Amazon Web Services, list only the opportunities that were newly created or updated. We recommend you rely on events emitted by the service into your Amazon Web Services account’s Amazon EventBridge default event bus. You can also use the <code>ListOpportunities</code> action.</p> <p>We recommend the following approach:</p> <ol> <li> <p>Find the latest <code>LastModifiedDate</code> that you stored, and only use the values that came from Amazon Web Services. Don’t use values generated by your system.</p> </li> <li> <p>When you send a <code>ListOpportunities</code> request, submit the date in ISO 8601 format in the <code>AfterLastModifiedDate</code> filter.</p> </li> <li> <p>Amazon Web Services only returns opportunities created or updated on or after that date and time. Use <code>NextToken</code> to iterate over all pages.</p> </li> </ol>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunities are listed in. Use <code>AWS</code> for listing real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            max_results: <p>Specifies the maximum number of results to return in a single call. This limits the number of opportunities returned in the response to avoid providing too many results at once.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>An object that specifies how the response is sorted. The default <code>Sort.SortBy</code> value is <code>LastModifiedDate</code>.</p>
            last_modified_date: <p>Filters the opportunities based on their last modified date. This filter helps retrieve opportunities that were updated after the specified date, allowing partners to track recent changes or updates.</p>
            identifier: <p>Filters the opportunities based on the opportunity identifier. This allows partners to retrieve specific opportunities by providing their unique identifiers, ensuring precise results.</p>
            life_cycle_stage: <p>Filters the opportunities based on their lifecycle stage. This filter allows partners to retrieve opportunities at various stages in the sales cycle, such as <code>Qualified</code>, <code>Technical Validation</code>, <code>Business Validation</code>, or <code>Closed Won</code>.</p>
            life_cycle_review_status: <p>Filters the opportunities based on their current lifecycle approval status. Use this filter to retrieve opportunities with statuses such as <code>Pending Submission</code>, <code>In Review</code>, <code>Action Required</code>, or <code>Approved</code>.</p>
            customer_company_name: <p>Filters the opportunities based on the customer's company name. This allows partners to search for opportunities associated with a specific customer by matching the provided company name string.</p>
            created_date: <p>Filter opportunities by creation date criteria.</p>
            target_close_date: <p>Filters opportunities based on their target close date. This filter helps retrieve opportunities with an expected close date before or after a specified date.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities.async_list_opportunities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if last_modified_date is not None:
            input_["last_modified_date"] = last_modified_date
        if identifier is not None:
            input_["identifier"] = identifier
        if life_cycle_stage is not None:
            input_["life_cycle_stage"] = life_cycle_stage
        if life_cycle_review_status is not None:
            input_["life_cycle_review_status"] = life_cycle_review_status
        if customer_company_name is not None:
            input_["customer_company_name"] = customer_company_name
        if created_date is not None:
            input_["created_date"] = created_date
        if target_close_date is not None:
            input_["target_close_date"] = target_close_date

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_opportunities(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_sort.OpportunitySort"
        ] = None,
        last_modified_date: Optional[
            "capo_partnercentral_selling.types.last_modified_date.LastModifiedDate"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.filter_identifier.FilterIdentifier"
        ] = None,
        life_cycle_stage: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
        ] = None,
        life_cycle_review_status: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
        ] = None,
        customer_company_name: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        created_date: Optional[
            "capo_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
        ] = None,
        target_close_date: Optional[
            "capo_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.opportunity_summary.OpportunitySummary]":
        _token = next_token
        while True:
            _response = await self.list_opportunities(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                last_modified_date=last_modified_date,
                identifier=identifier,
                life_cycle_stage=life_cycle_stage,
                life_cycle_review_status=life_cycle_review_status,
                customer_company_name=customer_company_name,
                created_date=created_date,
                target_close_date=target_close_date,
            )
            _page = _resolve_path(_response, ("opportunity_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def assign_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        assignee: "capo_partnercentral_selling.types.assignee_contact.AssigneeContact",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to reassign an existing <code>Opportunity</code> to another user within your Partner Central account. The specified user receives the opportunity, and it appears on their Partner Central dashboard, allowing them to take necessary actions or proceed with the opportunity.</p> <p>This is useful for distributing opportunities to the appropriate team members or departments within your organization, ensuring that each opportunity is handled by the right person. By default, the opportunity owner is the one who creates it. Currently, there's no API to enumerate the list of available users.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is assigned in. Use <code>AWS</code> to assign real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to assign it to another user. Provide the correct identifier so the intended opportunity is reassigned.</p>
            assignee: <p>Specifies the user or team member responsible for managing the assigned opportunity. This field identifies the <i>Assignee</i> based on the partner's internal team structure. Ensure that the email address is associated with a registered user in your Partner Central account.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity.async_assign_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "assignee": assignee,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to create a formal association between an <code>Opportunity</code> and various related entities, enriching the context and details of the opportunity for better collaboration and decision making. You can associate an opportunity with the following entity types:</p> <ul> <li> <p>Partner Solution: A software product or consulting practice created and delivered by Partners. Partner Solutions help customers address business challenges using Amazon Web Services services.</p> </li> <li> <p>Amazon Web Services Products: Amazon Web Services offers many products and services that provide scalable, reliable, and cost-effective infrastructure solutions. For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Allows Amazon Web Services Marketplace sellers to extend custom pricing and terms to individual Amazon Web Services customers. Sellers can negotiate custom prices, payment schedules, and end user license terms through private offers, enabling Amazon Web Services customers to acquire software solutions tailored to their specific needs. For more information, see <a href="https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html">Private offers in Amazon Web Services Marketplace</a>.</p> </li> </ul> <p>To obtain identifiers for these entities, use the following methods:</p> <ul> <li> <p>Solution: Use the <code>ListSolutions</code> operation.</p> </li> <li> <p>AWS Products: For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Use the <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html">Using the Amazon Web Services Marketplace Catalog API</a> to list entities. Specifically, use the <code>ListEntities</code> operation to retrieve a list of private offers. The request returns the details of available private offers. For more information, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html">ListEntities</a>.</p> </li> </ul>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity association is made in. Use <code>AWS</code> to associate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to associate it with a related entity. Provide the correct identifier so the intended opportunity is updated with the association.</p>
            related_entity_type: <p>Specifies the entity type that you're associating with the <code> Opportunity</code>. This helps to categorize and properly process the association.</p>
            related_entity_identifier: <p>Requires the related entity's unique identifier when you want to associate it with the <code> Opportunity</code>. For Amazon Web Services Marketplace entities, provide the Amazon Resource Name (ARN). Use the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services Marketplace API</a> to obtain the ARN.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity.async_associate_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Allows you to remove an existing association between an <code>Opportunity</code> and related entities, such as a Partner Solution, Amazon Web Services product, or an Amazon Web Services Marketplace offer. This operation is the counterpart to <code>AssociateOpportunity</code>, and it provides flexibility to manage associations as business needs change.</p> <p>Use this operation to update the associations of an <code>Opportunity</code> due to changes in the related entities, or if an association was made in error. Ensuring accurate associations helps maintain clarity and accuracy to track and manage business opportunities. When you replace an entity, first attach the new entity and then disassociate the one to be removed, especially if it's the last remaining entity that's required.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity disassociation is made in. Use <code>AWS</code> to disassociate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>The opportunity's unique identifier for when you want to disassociate it from related entities. This identifier helps to ensure that the correct opportunity is updated.</p> <p>Validation: Ensure that the provided identifier corresponds to an existing opportunity in the Amazon Web Services system because incorrect identifiers result in an error and no changes are made.</p>
            related_entity_type: <p>The type of the entity that you're disassociating from the opportunity. When you specify the entity type, it helps the system correctly process the disassociation request to ensure that the right connections are removed.</p> <p>Examples of entity types include Partner Solution, Amazon Web Services product, and Amazon Web Services Marketplaceoffer. Ensure that the value matches one of the expected entity types.</p> <p>Validation: Provide a valid entity type to help ensure successful disassociation. An invalid or incorrect entity type results in an error.</p>
            related_entity_identifier: <p>The related entity's identifier that you want to disassociate from the opportunity. Depending on the type of entity, this could be a simple identifier or an Amazon Resource Name (ARN) for entities managed through Amazon Web Services Marketplace.</p> <p>For Amazon Web Services Marketplace entities, use the Amazon Web Services Marketplace API to obtain the necessary ARNs. For guidance on retrieving these ARNs, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services MarketplaceUsing the Amazon Web Services Marketplace Catalog API</a>.</p> <p>Validation: Ensure the identifier or ARN is valid and corresponds to an existing entity. An incorrect or invalid identifier results in an error.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity.async_disassociate_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_aws_opportunity_summary(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        related_opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse":
        """<p>Retrieves a summary of an AWS Opportunity. This summary includes high-level details about the opportunity sourced from AWS, such as lifecycle information, customer details, and involvement type. It is useful for tracking updates on the AWS opportunity corresponding to an opportunity in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the AWS Opportunity is located. Accepted values include <code>AWS</code> for production opportunities or <code>Sandbox</code> for testing purposes. The catalog determines which environment the opportunity data is pulled from.</p>
            related_opportunity_identifier: <p>The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary.async_get_aws_opportunity_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest = {
            "catalog": catalog,
            "related_opportunity_identifier": related_opportunity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        involvement_type: "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        visibility: Optional[
            "capo_partnercentral_selling.types.visibility.Visibility"
        ] = None,
    ) -> None:
        """<p>Use this action to submit an Opportunity that was previously created by partner for AWS review. After you perform this action, the Opportunity becomes non-editable until it is reviewed by AWS and has <code> LifeCycle.ReviewStatus </code> as either <code>Approved</code> or <code>Action Required</code>. </p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Submits the opportunity request from the production AWS environment.</p> </li> <li> <p>Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            identifier: <p>The identifier of the Opportunity previously created by partner and needs to be submitted.</p>
            involvement_type: <p>Specifies the level of AWS sellers' involvement on the opportunity. Valid values:</p> <ul> <li> <p> <code>Co-sell</code>: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.</p> </li> <li> <p> <code>For Visibility Only</code>: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.</p> </li> </ul>
            visibility: <p>Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:</p> <ul> <li> <p> <code>Full</code>: The opportunity is fully visible to AWS sales.</p> </li> <li> <p> <code>Limited</code>: The opportunity has restricted visibility to AWS sales.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity.async_submit_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "involvement_type": involvement_type,
        }
        if visibility is not None:
            input_["visibility"] = visibility

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_opportunity_from_engagement_task(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "capo_partnercentral_selling.types.context_identifier.ContextIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse":
        """<p>This action creates an opportunity from an existing engagement context. The task is asynchronous and orchestrates the process of converting engagement contextual information into a structured opportunity record within the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the opportunity creation task is executed. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the engagement from which the opportunity creation task is to be initiated. This helps ensure that the task is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the engagement context from which to create the opportunity. This specifies the specific contextual information within the engagement that will be used for opportunity creation.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_opportunity_from_engagement_task_response.StartOpportunityFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_opportunity_from_engagement_task.async_start_opportunity_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_opportunity_from_engagement_task_request.StartOpportunityFromEngagementTaskRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "identifier": identifier,
            "context_identifier": context_identifier,
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

    async def list_opportunity_from_engagement_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        context_identifier: Optional[
            "capo_partnercentral_selling.types.context_identifiers.ContextIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse":
        """<p>Lists all in-progress, completed, or failed opportunity creation tasks from engagements that were initiated by the caller's account.</p>

        Args:
            max_results: <p>Specifies the maximum number of results to return in a single page of the response. Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.</p>
            next_token: <p>The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.</p>
            catalog: <p>Specifies the catalog related to the request. Valid values are <code>AWS</code> for production environments and <code>Sandbox</code> for testing or development purposes. The catalog determines which environment the task data is retrieved from.</p>
            task_status: <p>Filters the tasks based on their current status. This allows you to focus on tasks in specific states. Valid values are <code>COMPLETE</code> for tasks that have finished successfully, <code>INPROGRESS</code> for tasks that are currently running, and <code>FAILED</code> for tasks that have encountered an error and failed to complete.</p>
            task_identifier: <p>Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. Provide the task ID to get details about a particular opportunity creation task.</p>
            opportunity_identifier: <p>Filters tasks by the identifiers of the opportunities they created or are associated with. Use this to find tasks related to specific opportunity creation processes.</p>
            engagement_identifier: <p>Filters tasks by the identifiers of the engagements from which opportunities are being created. Use this to find all opportunity creation tasks associated with a specific engagement.</p>
            context_identifier: <p>Filters tasks by the identifiers of the engagement contexts associated with the opportunity creation. Use this to find tasks related to specific contextual information within engagements that are being converted to opportunities.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_response.ListOpportunityFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunity_from_engagement_tasks.async_list_opportunity_from_engagement_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunity_from_engagement_tasks_request.ListOpportunityFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if task_status is not None:
            input_["task_status"] = task_status
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if context_identifier is not None:
            input_["context_identifier"] = context_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_opportunity_from_engagement_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        context_identifier: Optional[
            "capo_partnercentral_selling.types.context_identifiers.ContextIdentifiers"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary.ListOpportunityFromEngagementTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_opportunity_from_engagement_tasks(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                task_status=task_status,
                task_identifier=task_identifier,
                opportunity_identifier=opportunity_identifier,
                engagement_identifier=engagement_identifier,
                context_identifier=context_identifier,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_prospecting_from_engagement_task(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifiers: "capo_partnercentral_selling.types.engagement_identifier_list.EngagementIdentifierList",
        task_name: "capo_partnercentral_selling.types.task_name.TaskName",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse":
        """<p>Starts a task to convert one or more engagement contexts into new prospecting leads. The task runs asynchronously. To poll for status, use <code>GetProspectingFromEngagementTask</code>, or use <code>ListProspectingFromEngagementTasks</code> to monitor multiple tasks.</p>

        Args:
            catalog: <p>Specifies the catalog in which the task is initiated. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            identifiers: <p>The list of engagement identifiers to include in this prospecting task. Each identifier must correspond to an existing engagement in the specified catalog. Maximum of 100 identifiers per task.</p>
            task_name: <p>A descriptive name for the task. This name helps identify the task in list and get operations. The name must contain 1 to 128 characters.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure idempotency. Making the same request with the same <code>ClientToken</code> returns the same response without creating a duplicate task.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.start_prospecting_from_engagement_task_response.StartProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_prospecting_from_engagement_task.async_start_prospecting_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_prospecting_from_engagement_task_request.StartProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "identifiers": identifiers,
            "task_name": task_name,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_prospecting_from_engagement_task(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        task_identifier: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse":
        """<p>Retrieves the details and current status of a prospecting task previously started with <code>StartProspectingFromEngagementTask</code> to enable polling for completion and access to per-engagement processing results.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the task. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes. The value must match the catalog used when the task was created.</p>
            task_identifier: <p>The unique identifier of the prospecting task to retrieve. This value is returned in the <code>TaskId</code> field of the <code>StartProspectingFromEngagementTask</code> response.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_prospecting_from_engagement_task_response.GetProspectingFromEngagementTaskResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_prospecting_from_engagement_task.async_get_prospecting_from_engagement_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_prospecting_from_engagement_task_request.GetProspectingFromEngagementTaskRequest = {
            "catalog": catalog,
            "task_identifier": task_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_prospecting_from_engagement_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifier_list.TaskIdentifierList"
        ] = None,
        task_name: Optional[
            "capo_partnercentral_selling.types.task_name_list.TaskNameList"
        ] = None,
        start_after: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        start_before: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.ProspectingFromEngagementTaskSort"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse":
        """<p>Lists all prospecting tasks initiated by the caller's account. Supports optional filters by task identifier, task name, or start time range. Results can be sorted using configurable options. The response is paginated. Use the <code>NextToken</code> value from each response to retrieve subsequent pages.</p>

        Args:
            catalog: <p>Specifies the catalog to list tasks from. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>
            max_results: <p>The maximum number of results to return in a single page. If additional results exist, the response includes a <code>NextToken</code> value for retrieving the next page. If omitted, the API uses a service-defined default page size.</p>
            next_token: <p>The pagination token from a previous call to this API. Include this value to retrieve the next page of results. If omitted, the first page is returned.</p>
            task_identifier: <p>Filters the results to include only the tasks with the specified identifiers. Provide up to 10 task IDs to narrow the list to specific tasks. If omitted, tasks are not filtered by identifier.</p>
            task_name: <p>Filters the results to include only tasks with the specified names. Provide up to 10 task names to narrow the list. If omitted, tasks are not filtered by name.</p>
            start_after: <p>Filters tasks to include only those that started after the specified timestamp. Use this with <code>StartBefore</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            start_before: <p>Filters tasks to include only those that started before the specified timestamp. Use this with <code>StartAfter</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>
            sort: <p>Specifies the field and order used to sort the returned tasks. If omitted, tasks are returned in the default sort order.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_response.ListProspectingFromEngagementTasksResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_prospecting_from_engagement_tasks.async_list_prospecting_from_engagement_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_prospecting_from_engagement_tasks_request.ListProspectingFromEngagementTasksRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier
        if task_name is not None:
            input_["task_name"] = task_name
        if start_after is not None:
            input_["start_after"] = start_after
        if start_before is not None:
            input_["start_before"] = start_before
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_prospecting_from_engagement_tasks(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        task_identifier: Optional[
            "capo_partnercentral_selling.types.task_identifier_list.TaskIdentifierList"
        ] = None,
        task_name: Optional[
            "capo_partnercentral_selling.types.task_name_list.TaskNameList"
        ] = None,
        start_after: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        start_before: Optional[
            "capo_partnercentral_selling.types.date_time.DateTime"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.ProspectingFromEngagementTaskSort"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.prospecting_task_summary.ProspectingTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_prospecting_from_engagement_tasks(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                task_identifier=task_identifier,
                task_name=task_name,
                start_after=start_after,
                start_before=start_before,
                sort=sort,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_resource_snapshot(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse":
        """<p> This action allows you to create an immutable snapshot of a specific resource, such as an opportunity, within the context of an engagement. The snapshot captures a subset of the resource's data based on the schema defined by the provided template.</p>

        Args:
            catalog: <p> Specifies the catalog where the snapshot is created. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context. </p>
            resource_type: <p> Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: <code>Opportunity</code>. </p>
            resource_identifier: <p> The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the <code>ResourceType</code> specified. For example: For <code>Opportunity</code> type, it will be an opportunity ID. </p>
            resource_snapshot_template_identifier: <p> The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified <code>ResourceType</code>. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot.async_create_resource_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest = {
            "catalog": catalog,
            "engagement_identifier": engagement_identifier,
            "resource_type": resource_type,
            "resource_identifier": resource_identifier,
            "resource_snapshot_template_identifier": resource_snapshot_template_identifier,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_snapshot(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
        ] = None,
    ) -> "capo_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse":
        """<p>Use this action to retrieve a specific snapshot record.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Retrieves the snapshot from the production AWS environment.</p> </li> <li> <p>Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            engagement_identifier: <p>The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.</p>
            resource_type: <p>Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:<code>Opportunity</code>: For opportunity-related data. </p>
            resource_identifier: <p>The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For <code>Opportunity</code> type, it will be an <code>opportunity ID</code> </p>
            resource_snapshot_template_identifier: <p>he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified <code>ResourceType</code>.</p>
            revision: <p>Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot.async_get_resource_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest = {
            "catalog": catalog,
            "engagement_identifier": engagement_identifier,
            "resource_type": resource_type,
            "resource_identifier": resource_identifier,
            "resource_snapshot_template_identifier": resource_snapshot_template_identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_engagement_resource_associations(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        resource_type: Optional[
            "capo_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse":
        """<p>Lists the associations between resources and engagements where the caller is a member and has at least one snapshot in the engagement.</p>

        Args:
            catalog: <p>Specifies the catalog in which to search for engagement-resource associations. Valid Values: "AWS" or "Sandbox"</p> <ul> <li> <p> <code>AWS</code> for production environments.</p> </li> <li> <p> <code>Sandbox</code> for testing and development purposes.</p> </li> </ul>
            max_results: <p>Limits the number of results returned in a single call. Use this to control the number of results returned, especially useful for pagination.</p>
            next_token: <p>A token used for pagination of results. Include this token in subsequent requests to retrieve the next set of results.</p>
            engagement_identifier: <p>Filters the results to include only associations related to the specified engagement. Use this when you want to find all resources associated with a specific engagement.</p>
            resource_type: <p> Filters the results to include only associations with resources of the specified type. </p>
            resource_identifier: <p>Filters the results to include only associations with the specified resource. Varies depending on the resource type. Use this when you want to find all engagements associated with a specific resource.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account ID. Use this when you want to find associations related to resources owned by a particular account. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations.async_list_engagement_resource_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if created_by is not None:
            input_["created_by"] = created_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_engagement_resource_associations(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        resource_type: Optional[
            "capo_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.engagement_resource_association_summary.EngagementResourceAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_engagement_resource_associations(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                engagement_identifier=engagement_identifier,
                resource_type=resource_type,
                resource_identifier=resource_identifier,
                created_by=created_by,
            )
            _page = _resolve_path(
                _response, ("engagement_resource_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_snapshots(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        resource_type: Optional[
            "capo_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_snapshot_template_identifier: Optional[
            "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
        ] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse":
        """<p>Retrieves a list of resource view snapshots based on specified criteria. This operation supports various use cases, including: </p> <ul> <li> <p>Fetching all snapshots associated with an engagement.</p> </li> <li> <p>Retrieving snapshots of a specific resource type within an engagement.</p> </li> <li> <p>Obtaining snapshots for a particular resource using a specified template.</p> </li> <li> <p>Accessing the latest snapshot of a resource within an engagement.</p> </li> <li> <p>Filtering snapshots by resource owner.</p> </li> </ul>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with the snapshots. </p>
            resource_type: <p> Filters the response to include only snapshots of the specified resource type. </p>
            resource_identifier: <p> Filters the response to include only snapshots of the specified resource. </p>
            resource_snapshot_template_identifier: <p>Filters the response to include only snapshots created using the specified template.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots.async_list_resource_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest = {
            "catalog": catalog,
            "engagement_identifier": engagement_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if resource_snapshot_template_identifier is not None:
            input_["resource_snapshot_template_identifier"] = (
                resource_snapshot_template_identifier
            )
        if created_by is not None:
            input_["created_by"] = created_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resource_snapshots(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        resource_type: Optional[
            "capo_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_snapshot_template_identifier: Optional[
            "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
        ] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.resource_snapshot_summary.ResourceSnapshotSummary]":
        _token = next_token
        while True:
            _response = await self.list_resource_snapshots(
                catalog,
                engagement_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_type=resource_type,
                resource_identifier=resource_identifier,
                resource_snapshot_template_identifier=resource_snapshot_template_identifier,
                created_by=created_by,
            )
            _page = _resolve_path(_response, ("resource_snapshot_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse":
        """<p>Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.</p>

        Args:
            catalog: <p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>
            client_token: <p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>
            engagement_identifier: <p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>
            resource_type: <p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>
            resource_identifier: <p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>
            resource_snapshot_template_identifier: <p>Specifies the name of the template that defines the schema for the snapshot.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job.async_create_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "resource_type": resource_type,
            "resource_identifier": resource_identifier,
            "resource_snapshot_template_identifier": resource_snapshot_template_identifier,
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

    async def get_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse":
        """<p>Use this action to retrieves information about a specific resource snapshot job.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p> AWS: Retrieves the snapshot job from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            resource_snapshot_job_identifier: <p>The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job.async_get_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p> Use this action to deletes a previously created resource snapshot job. The job must be in a stopped state before it can be deleted. </p>

        Args:
            catalog: <p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            resource_snapshot_job_identifier: <p> The unique identifier of the resource snapshot job to be deleted. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job.async_delete_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_resource_snapshot_jobs(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse":
        """<p> Lists resource snapshot jobs owned by the customer. This operation supports various filtering scenarios, including listing all jobs owned by the caller, jobs for a specific engagement, jobs with a specific status, or any combination of these filters. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The identifier of the engagement to filter the response. </p>
            status: <p> The status of the jobs to filter the response. </p>
            sort: <p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs.async_list_resource_snapshot_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resource_snapshot_jobs(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.resource_snapshot_job_summary.ResourceSnapshotJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_resource_snapshot_jobs(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                engagement_identifier=engagement_identifier,
                status=status,
                sort=sort,
            )
            _page = _resolve_path(_response, ("resource_snapshot_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Starts a resource snapshot job that has been previously created.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the resource snapshot job to start.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job.async_start_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_resource_snapshot_job(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Stops a resource snapshot job. The job must be started prior to being stopped.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the job to stop.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job.async_stop_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest = {
            "catalog": catalog,
            "resource_snapshot_job_identifier": resource_snapshot_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_solutions(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        aws_marketplace_solution_arn: Optional[
            "capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.AwsMarketplaceSolutionArnList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse":
        """<p>Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>
            status: <p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>
            identifier: <p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>
            category: <p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>
            aws_marketplace_solution_arn: <p>Filters results by AWS Marketplace solution ARN. You can provide up to 10 ARNs.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions.async_list_solutions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if status is not None:
            input_["status"] = status
        if identifier is not None:
            input_["identifier"] = identifier
        if category is not None:
            input_["category"] = category
        if aws_marketplace_solution_arn is not None:
            input_["aws_marketplace_solution_arn"] = aws_marketplace_solution_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_solutions(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        aws_marketplace_solution_arn: Optional[
            "capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.AwsMarketplaceSolutionArnList"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_selling.types.solution_base.SolutionBase]":
        _token = next_token
        while True:
            _response = await self.list_solutions(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort=sort,
                status=status,
                identifier=identifier,
                category=category,
                aws_marketplace_solution_arn=aws_marketplace_solution_arn,
            )
            _page = _resolve_path(_response, ("solution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
