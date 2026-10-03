"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CloudWatchOmniFrontend``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cloudwatchomni._auth._signers
import capo_cloudwatchomni._auth._sigv4
from capo_cloudwatchomni._auth._identity import Credentials
from capo_cloudwatchomni._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudwatchomni._auth._zapros_handler import AuthMiddleware
from capo_cloudwatchomni._pagination import resolve_path as _resolve_path
from capo_cloudwatchomni._resources.cloud_watch_omni_frontend.space_resource import (
    AsyncSpaceResource,
)
from capo_cloudwatchomni._services._aws_config import aaws_config
from capo_cloudwatchomni._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant_permission
    import capo_cloudwatchomni.types.access_grant_principal
    import capo_cloudwatchomni.types.access_grant_principal_type
    import capo_cloudwatchomni.types.access_grant_summary
    import capo_cloudwatchomni.types.access_profile_name
    import capo_cloudwatchomni.types.access_profile_summary
    import capo_cloudwatchomni.types.alert_filter_criteria
    import capo_cloudwatchomni.types.alert_id
    import capo_cloudwatchomni.types.alert_sort_field
    import capo_cloudwatchomni.types.alert_sort_order
    import capo_cloudwatchomni.types.alert_summary
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.create_access_grant_input
    import capo_cloudwatchomni.types.create_access_grant_output
    import capo_cloudwatchomni.types.create_access_profile_input
    import capo_cloudwatchomni.types.create_access_profile_output
    import capo_cloudwatchomni.types.create_alert_input
    import capo_cloudwatchomni.types.create_alert_output
    import capo_cloudwatchomni.types.create_domain_access_grant_for_organization_input
    import capo_cloudwatchomni.types.create_domain_access_grant_for_organization_output
    import capo_cloudwatchomni.types.create_domain_for_organization_input
    import capo_cloudwatchomni.types.create_domain_for_organization_output
    import capo_cloudwatchomni.types.create_domain_input
    import capo_cloudwatchomni.types.create_domain_output
    import capo_cloudwatchomni.types.create_integration_input
    import capo_cloudwatchomni.types.create_integration_output
    import capo_cloudwatchomni.types.create_omni_dashboard_input
    import capo_cloudwatchomni.types.create_omni_dashboard_output
    import capo_cloudwatchomni.types.create_one_time_deep_link_code_input
    import capo_cloudwatchomni.types.create_one_time_deep_link_code_output
    import capo_cloudwatchomni.types.create_space_input
    import capo_cloudwatchomni.types.create_space_output
    import capo_cloudwatchomni.types.create_view_request
    import capo_cloudwatchomni.types.create_view_response
    import capo_cloudwatchomni.types.dashboard_id
    import capo_cloudwatchomni.types.delete_access_grant_input
    import capo_cloudwatchomni.types.delete_access_grant_output
    import capo_cloudwatchomni.types.delete_access_profile_input
    import capo_cloudwatchomni.types.delete_access_profile_output
    import capo_cloudwatchomni.types.delete_alert_input
    import capo_cloudwatchomni.types.delete_alert_output
    import capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_input
    import capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_output
    import capo_cloudwatchomni.types.delete_domain_for_organization_input
    import capo_cloudwatchomni.types.delete_domain_for_organization_output
    import capo_cloudwatchomni.types.delete_domain_input
    import capo_cloudwatchomni.types.delete_domain_output
    import capo_cloudwatchomni.types.delete_integration_input
    import capo_cloudwatchomni.types.delete_integration_output
    import capo_cloudwatchomni.types.delete_omni_dashboard_input
    import capo_cloudwatchomni.types.delete_omni_dashboard_output
    import capo_cloudwatchomni.types.delete_space_input
    import capo_cloudwatchomni.types.delete_space_output
    import capo_cloudwatchomni.types.delete_view_request
    import capo_cloudwatchomni.types.delete_view_response
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.domain_summary
    import capo_cloudwatchomni.types.edge_filters
    import capo_cloudwatchomni.types.encryption_configuration
    import capo_cloudwatchomni.types.field
    import capo_cloudwatchomni.types.get_access_grant_input
    import capo_cloudwatchomni.types.get_access_grant_output
    import capo_cloudwatchomni.types.get_access_profile_input
    import capo_cloudwatchomni.types.get_access_profile_output
    import capo_cloudwatchomni.types.get_alert_input
    import capo_cloudwatchomni.types.get_alert_output
    import capo_cloudwatchomni.types.get_context_graph_input
    import capo_cloudwatchomni.types.get_context_graph_output
    import capo_cloudwatchomni.types.get_domain_access_grant_for_organization_input
    import capo_cloudwatchomni.types.get_domain_access_grant_for_organization_output
    import capo_cloudwatchomni.types.get_domain_for_organization_input
    import capo_cloudwatchomni.types.get_domain_for_organization_output
    import capo_cloudwatchomni.types.get_domain_input
    import capo_cloudwatchomni.types.get_domain_output
    import capo_cloudwatchomni.types.get_integration_input
    import capo_cloudwatchomni.types.get_integration_output
    import capo_cloudwatchomni.types.get_intelligence_configuration_input
    import capo_cloudwatchomni.types.get_intelligence_configuration_output
    import capo_cloudwatchomni.types.get_omni_dashboard_input
    import capo_cloudwatchomni.types.get_omni_dashboard_output
    import capo_cloudwatchomni.types.get_space_credentials_for_organization_input
    import capo_cloudwatchomni.types.get_space_credentials_for_organization_output
    import capo_cloudwatchomni.types.get_space_input
    import capo_cloudwatchomni.types.get_space_output
    import capo_cloudwatchomni.types.get_telemetry_query_results_request
    import capo_cloudwatchomni.types.get_telemetry_query_results_response
    import capo_cloudwatchomni.types.get_view_request
    import capo_cloudwatchomni.types.get_view_response
    import capo_cloudwatchomni.types.grant_id
    import capo_cloudwatchomni.types.iam_role_arn
    import capo_cloudwatchomni.types.identity_provider_configuration
    import capo_cloudwatchomni.types.identity_provider_list
    import capo_cloudwatchomni.types.integration
    import capo_cloudwatchomni.types.integration_credential
    import capo_cloudwatchomni.types.integration_identifier
    import capo_cloudwatchomni.types.integration_status
    import capo_cloudwatchomni.types.integration_type
    import capo_cloudwatchomni.types.intelligence_kms_key_arn
    import capo_cloudwatchomni.types.list_access_grants_input
    import capo_cloudwatchomni.types.list_access_grants_output
    import capo_cloudwatchomni.types.list_access_profiles_input
    import capo_cloudwatchomni.types.list_access_profiles_output
    import capo_cloudwatchomni.types.list_alerts_input
    import capo_cloudwatchomni.types.list_alerts_output
    import capo_cloudwatchomni.types.list_domain_access_grants_for_organization_input
    import capo_cloudwatchomni.types.list_domain_access_grants_for_organization_output
    import capo_cloudwatchomni.types.list_domains_input
    import capo_cloudwatchomni.types.list_domains_output
    import capo_cloudwatchomni.types.list_integrations_input
    import capo_cloudwatchomni.types.list_integrations_output
    import capo_cloudwatchomni.types.list_omni_dashboards_input
    import capo_cloudwatchomni.types.list_omni_dashboards_output
    import capo_cloudwatchomni.types.list_spaces_for_organization_input
    import capo_cloudwatchomni.types.list_spaces_for_organization_output
    import capo_cloudwatchomni.types.list_spaces_input
    import capo_cloudwatchomni.types.list_spaces_output
    import capo_cloudwatchomni.types.list_telemetry_fields_request
    import capo_cloudwatchomni.types.list_telemetry_fields_response
    import capo_cloudwatchomni.types.list_telemetry_query_sessions_request
    import capo_cloudwatchomni.types.list_telemetry_query_sessions_response
    import capo_cloudwatchomni.types.list_views_request
    import capo_cloudwatchomni.types.list_views_response
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.node
    import capo_cloudwatchomni.types.node_filters
    import capo_cloudwatchomni.types.notification_rule_list
    import capo_cloudwatchomni.types.omni_dashboard_summary
    import capo_cloudwatchomni.types.organization_access_grant_principal
    import capo_cloudwatchomni.types.organization_access_grant_summary
    import capo_cloudwatchomni.types.organization_credential_type
    import capo_cloudwatchomni.types.organization_grant_permission
    import capo_cloudwatchomni.types.organization_grant_principal_type
    import capo_cloudwatchomni.types.pagination_token
    import capo_cloudwatchomni.types.principal_id
    import capo_cloudwatchomni.types.principal_search_result
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.put_intelligence_configuration_input
    import capo_cloudwatchomni.types.put_intelligence_configuration_output
    import capo_cloudwatchomni.types.row
    import capo_cloudwatchomni.types.rule
    import capo_cloudwatchomni.types.scoped_actions_list
    import capo_cloudwatchomni.types.search_principals_input
    import capo_cloudwatchomni.types.search_principals_next_token
    import capo_cloudwatchomni.types.search_principals_output
    import capo_cloudwatchomni.types.session_summary
    import capo_cloudwatchomni.types.space_credential_request_context
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.space_summary
    import capo_cloudwatchomni.types.start_telemetry_query_request
    import capo_cloudwatchomni.types.start_telemetry_query_response
    import capo_cloudwatchomni.types.start_telemetry_query_session_request
    import capo_cloudwatchomni.types.start_telemetry_query_session_response
    import capo_cloudwatchomni.types.stop_telemetry_query_request
    import capo_cloudwatchomni.types.stop_telemetry_query_response
    import capo_cloudwatchomni.types.stop_telemetry_query_session_request
    import capo_cloudwatchomni.types.stop_telemetry_query_session_response
    import capo_cloudwatchomni.types.string_map
    import capo_cloudwatchomni.types.tag_map
    import capo_cloudwatchomni.types.telemetry_type
    import capo_cloudwatchomni.types.update_access_profile_input
    import capo_cloudwatchomni.types.update_access_profile_output
    import capo_cloudwatchomni.types.update_alert_input
    import capo_cloudwatchomni.types.update_alert_output
    import capo_cloudwatchomni.types.update_domain_for_organization_input
    import capo_cloudwatchomni.types.update_domain_for_organization_output
    import capo_cloudwatchomni.types.update_domain_input
    import capo_cloudwatchomni.types.update_domain_output
    import capo_cloudwatchomni.types.update_integration_input
    import capo_cloudwatchomni.types.update_integration_output
    import capo_cloudwatchomni.types.update_omni_dashboard_input
    import capo_cloudwatchomni.types.update_omni_dashboard_output
    import capo_cloudwatchomni.types.update_space_input
    import capo_cloudwatchomni.types.update_space_output
    import capo_cloudwatchomni.types.update_view_request
    import capo_cloudwatchomni.types.update_view_response
    import capo_cloudwatchomni.types.view_definition
    import capo_cloudwatchomni.types.view_description
    import capo_cloudwatchomni.types.view_name
    import capo_cloudwatchomni.types.view_summary
    import capo_cloudwatchomni.types.view_type


class AsyncCloudWatchOmniClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncCloudWatchOmniClient:
    """A client for the ``CloudWatchOmni`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self._config = AsyncCloudWatchOmniClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.space_resource = AsyncSpaceResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudWatchOmniClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_access_grant(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        name: str,
        principal: "capo_cloudwatchomni.types.access_grant_principal.AccessGrantPrincipal",
        permission: "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        scoped_actions: Optional[
            "capo_cloudwatchomni.types.scoped_actions_list.ScopedActionsList"
        ] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_access_grant_output.CreateAccessGrantOutput":
        """Creates an AccessGrant that authorizes a principal to perform a set of actions on resources in a space. Optionally narrow the grant with scoped actions that limit it to specific resources and fields. Use ListAccessGrants and GetAccessGrant to retrieve grants, and DeleteAccessGrant to remove them.

        Args:
            domain_id: The ID of the domain that contains the space.
            space_id: The ID of the space to scope the grant to.
            name: A name that identifies the access grant.
            principal: The principal receiving the grant.
            permission: The permission to grant. Exactly one permission is granted per request.
            scoped_actions: Groups of actions to allow, each with the resource scopes and conditions that limit those actions.
            tags: The tags to associate with the access grant.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an access grant
            The following example creates a custom access grant that authorizes an Identity Center user to read and update a specific dashboard in a space. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_access_grant(domain_id='d-1a2b3c4d5e', space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', name='analyst-read-access', principal={'principalType': 'IDC_USER', 'principalId': '94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f'}, permission='CUSTOM', scoped_actions=[{'actions': ['cloudwatch:GetOmniDashboard', 'cloudwatch:UpdateOmniDashboard'], 'resources': [{'resourceType': 'OmniDashboard', 'resourceArns': ['arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f']}]}], tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_access_grant_input.CreateAccessGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_access_grant_output.CreateAccessGrantOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_access_grant

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_access_grant.async_create_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_access_grant_input.CreateAccessGrantInput = {
            "domain_id": domain_id,
            "space_id": space_id,
            "name": name,
            "principal": principal,
            "permission": permission,
        }
        if scoped_actions is not None:
            input_["scoped_actions"] = scoped_actions
        if tags is not None:
            input_["tags"] = tags
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

    async def create_access_profile(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        name: "capo_cloudwatchomni.types.access_profile_name.AccessProfileName",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_access_profile_output.CreateAccessProfileOutput":
        """Creates an access profile in a space. Use GetAccessProfile and ListAccessProfiles to retrieve profiles, and UpdateAccessProfile to modify one.

        Args:
            space_id: The unique ID of the space to create the profile in.
            name: A name that identifies the access profile.
            description: An optional description of the access profile.
            tags: The tags to associate with the access profile.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an access profile
            The following example creates a customer-managed access profile in a space. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_access_profile(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', name='Analyst read-only profile', description='Read-only access for analysts.', tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_access_profile_input.CreateAccessProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_access_profile_output.CreateAccessProfileOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_access_profile

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_access_profile.async_create_access_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_access_profile_input.CreateAccessProfileInput = {
            "space_id": space_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    async def create_alert(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId",
        name: str,
        rule: "capo_cloudwatchomni.types.rule.Rule",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        description: Optional[str] = None,
        notifications_enabled: Optional[bool] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        notification_rules: Optional[
            "capo_cloudwatchomni.types.notification_rule_list.NotificationRuleList"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.create_alert_output.CreateAlertOutput":
        r"""Creates a new alert within a space. Use GetAlert and ListAlerts to retrieve alerts, UpdateAlert to modify one, and DeleteAlert to remove it.

        Args:
            space_id: The unique ID of the space to create the alert in.
            profile_id: The ID of the access profile the alert uses to evaluate its query and execute notifications. The caller supplies it: there is no managed alert profile, and the service does not pick one on the caller's behalf.
            name: Alert name, for display. Max 256 (the AlarmName budget). Not the alert's identity: the backend mints a separate uuid as the {@link AlertId}, so the name need not be unique within a space and addressing an alert never depends on it. UpdateAlert accepts a new name to rename the alert.
            description: An optional description of the alert.
            rule: The rule that defines how the alert is evaluated.
            notifications_enabled: Whether actions (notifications) are enabled for this alert. Defaults to true when omitted.
            tags: The tags to associate with the alert.
            notification_rules: The notification rules that determine when and where notifications are sent.
            client_token: Idempotency token for safe retries. Retrying with the same token within the idempotency window returns the original alert instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an alert on a field value
            The following example creates an alert whose threshold is compared against a named field of each result row, so every service the query groups by is tracked as its own contributor. FIELD_VALUE requires thresholdField. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly', name='service-error-count-elevated', description='Alerts when a service logs more errors than its accepted rate.', rule={'telemetryRule': {'query': {'language': 'SQL', 'expression': 'SELECT resource[\'attributes\'][\'service.name\'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE severityText = \'ERROR\' GROUP BY service'}, 'condition': {'thresholdMode': 'FIELD_VALUE', 'thresholdField': 'error_count', 'comparator': 'GT', 'warningThreshold': 50.0, 'criticalThreshold': 200.0}, 'evaluation': {'intervalSeconds': 300, 'pendingDurationSeconds': 600, 'recoveryDurationSeconds': 300}, 'noData': {'treatAs': 'NODATA'}}}, notifications_enabled=True, notification_rules=[{'trigger': {'stateValues': ['CRITICAL']}, 'target': {'type': 'slack', 'arn': 'arn:aws:cloudwatch:us-east-1:123456789012:integration/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', 'metadata': {'channel': 'oncall-alerts'}}}], tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
            Create an alert on the number of matching rows
            The following example creates an alert whose threshold is compared against how many rows the query returns, rather than a value within them. COUNT_OF_RESULTS takes no thresholdField. Notifications are created disabled, so the alert evaluates and records state without sending anything, and an empty result set is treated as OK rather than as missing data. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly', name='service-checkout-5xx-responses', description='Counts checkout responses that returned a server error.', rule={'telemetryRule': {'query': {'language': 'SQL', 'expression': 'SELECT * FROM "logs.default" WHERE resource[\'attributes\'][\'service.name\'] = \'checkout\' AND attributes[\'http.response.status_code\'] >= 500'}, 'condition': {'thresholdMode': 'COUNT_OF_RESULTS', 'comparator': 'GT', 'warningThreshold': 10.0, 'criticalThreshold': 50.0}, 'evaluation': {'intervalSeconds': 60, 'pendingDurationSeconds': 120}, 'noData': {'treatAs': 'OK'}}}, notifications_enabled=False)
            Create an alert from a PromQL query
            The following example creates an alert from a PromQL expression instead of SQL. A PromQL rule compares against the series value, which is carried as the `value` field, so the condition is FIELD_VALUE with thresholdField set to `value`. Notifications go to an Amazon SNS topic, whose ARN is the topic itself rather than an integration. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly', name='checkout-error-rate-promql', description='Alerts on the checkout server error rate over a five-minute window.', rule={'telemetryRule': {'query': {'language': 'PROMQL', 'expression': 'sum by (service_name) (rate(http_server_errors_total{service_name="checkout"}[5m]))'}, 'condition': {'thresholdMode': 'FIELD_VALUE', 'thresholdField': 'value', 'comparator': 'GT', 'warningThreshold': 0.05, 'criticalThreshold': 0.1}, 'evaluation': {'intervalSeconds': 300, 'pendingDurationSeconds': 300}, 'noData': {'treatAs': 'NODATA'}}}, notification_rules=[{'trigger': {'stateValues': ['WARNING', 'CRITICAL']}, 'target': {'type': 'sns', 'arn': 'arn:aws:sns:us-east-1:123456789012:checkout-oncall'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_alert_input.CreateAlertInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_alert_output.CreateAlertOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_alert

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_alert.async_create_alert(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_alert_input.CreateAlertInput = {
            "space_id": space_id,
            "profile_id": profile_id,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            input_["description"] = description
        if notifications_enabled is not None:
            input_["notifications_enabled"] = notifications_enabled
        if tags is not None:
            input_["tags"] = tags
        if notification_rules is not None:
            input_["notification_rules"] = notification_rules
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

    async def create_domain(
        self,
        name: str,
        identity_providers: "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        identity_provider_configuration: Optional[
            "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_domain_output.CreateDomainOutput":
        """Creates a domain with identity provider configuration. Use GetDomain to retrieve the domain, UpdateDomain to change its configuration, and CreateSpace to add spaces within it.

        Args:
            name: A name that identifies the domain. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            identity_providers: The identity providers to configure for the domain.
            identity_provider_configuration: Identity provider configuration for the domain.
            tags: The tags to associate with the domain.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a domain
            The following example creates an Identity Center domain and configures it with an Identity Center instance. The name must be 3-63 characters of lowercase letters, numbers, and hyphens, and the endpoint URLs are derived from it. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_domain(name='prod-observability', identity_providers=['IDC'], identity_provider_configuration={'identityCenterConfiguration': {'identityCenterInstanceArn': 'arn:aws:sso:::instance/ssoins-1234567890abcdef'}}, tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_domain_output.CreateDomainOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_domain_input.CreateDomainInput = {
            "name": name,
            "identity_providers": identity_providers,
        }
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if tags is not None:
            input_["tags"] = tags
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

    async def create_domain_access_grant_for_organization(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        name: str,
        principal: "capo_cloudwatchomni.types.organization_access_grant_principal.OrganizationAccessGrantPrincipal",
        permission: "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_domain_access_grant_for_organization_output.CreateDomainAccessGrantForOrganizationOutput":
        """Creates an AccessGrant that authorizes a principal to administer an organization domain.

        Args:
            domain_id: The ID of the organization domain to create the grant on.
            name: A name that identifies the access grant.
            principal: The principal receiving the grant.
            permission: The permission to grant.
            tags: The tags to associate with the access grant.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an organization domain access grant
            The following example grants an Identity Center user administrative access to an organization domain. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_domain_access_grant_for_organization(domain_id='d-1a2b3c4d5e', name='org-domain-admin', principal={'principalType': 'IDC_USER', 'principalId': '94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f'}, permission='ADMIN', tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_domain_access_grant_for_organization_input.CreateDomainAccessGrantForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_domain_access_grant_for_organization_output.CreateDomainAccessGrantForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain_access_grant_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain_access_grant_for_organization.async_create_domain_access_grant_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_domain_access_grant_for_organization_input.CreateDomainAccessGrantForOrganizationInput = {
            "domain_id": domain_id,
            "name": name,
            "principal": principal,
            "permission": permission,
        }
        if tags is not None:
            input_["tags"] = tags
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

    async def create_domain_for_organization(
        self,
        name: str,
        identity_providers: "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList",
        domain_access_role_arn: "capo_cloudwatchomni.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        identity_provider_configuration: Optional[
            "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_domain_for_organization_output.CreateDomainForOrganizationOutput":
        """Creates an organization-scoped domain for the caller's AWS Organization. Only the organization's management account can call this operation.

        Args:
            name: A name that identifies the organization domain. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            identity_providers: The identity providers to configure for the domain.
            identity_provider_configuration: Identity provider configuration for the domain.
            domain_access_role_arn: The ARN of an IAM role in the management account used for domain access. You must create this role, and its trust policy must allow the service principal to assume it.
            tags: The tags to associate with the domain.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an organization domain
            The following example creates an organization-scoped domain from the organization's management account, configures it with an Identity Center instance, and supplies an IAM role in the management account for domain access. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_domain_for_organization(name='prod-observability-org', identity_providers=['IDC'], identity_provider_configuration={'identityCenterConfiguration': {'identityCenterInstanceArn': 'arn:aws:sso:::instance/ssoins-1234567890abcdef'}}, domain_access_role_arn='arn:aws:iam::123456789012:role/CloudWatchOrganizationDomainAccessRole', tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_domain_for_organization_input.CreateDomainForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_domain_for_organization_output.CreateDomainForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_domain_for_organization.async_create_domain_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_domain_for_organization_input.CreateDomainForOrganizationInput = {
            "name": name,
            "identity_providers": identity_providers,
            "domain_access_role_arn": domain_access_role_arn,
        }
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if tags is not None:
            input_["tags"] = tags
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

    async def create_integration(
        self,
        integration_type: "capo_cloudwatchomni.types.integration_type.IntegrationType",
        name: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        credential: Optional[
            "capo_cloudwatchomni.types.integration_credential.IntegrationCredential"
        ] = None,
        integration_attributes: Optional[
            "capo_cloudwatchomni.types.string_map.StringMap"
        ] = None,
        role_arn: Optional[str] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.create_integration_output.CreateIntegrationOutput":
        """Creates an integration with a third-party provider. Returns the integration identifier and its initial status; when the provider requires interactive consent, an authorization URL is returned for the user to complete setup.

        Args:
            integration_type: The type of third-party provider to integrate with.
            name: The name for the new integration; unique within the account.
            credential: The credential used to authenticate with the third-party provider.
            integration_attributes: Provider-specific attributes to associate with the integration.
            role_arn: The Amazon Resource Name of the IAM role assumed to access the integration.
            tags: Tags to apply to the integration at creation time (Tagris tag-on-create).
            client_token: Idempotency token for safe retries. Retrying with the same token returns the original integration instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an AWS integration
            The following example creates an AWS_INTEGRATION named my-aws-integration, authorized by an IAM role. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_integration(integration_type='AWS_INTEGRATION', name='my-aws-integration', role_arn='arn:aws:iam::123456789012:role/service-role/CloudWatchIntegrationRole', client_token='b3f8c7d6-5b4a-4c3d-9e2f-1a0b2c3d4e5f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_integration_input.CreateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_integration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_integration_input.CreateIntegrationInput = {
            "integration_type": integration_type,
            "name": name,
        }
        if credential is not None:
            input_["credential"] = credential
        if integration_attributes is not None:
            input_["integration_attributes"] = integration_attributes
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
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

    async def create_omni_dashboard(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        name: str,
        body: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_omni_dashboard_output.CreateOmniDashboardOutput":
        """Creates a new dashboard within a space. Use GetOmniDashboard and ListOmniDashboards to retrieve dashboards, UpdateOmniDashboard to modify one, and DeleteOmniDashboard to remove it.

        Args:
            space_id: The unique ID of the space to create the dashboard in.
            name: A name that identifies the dashboard.
            body: The dashboard definition, as a JSON document. Maximum 1 MiB.
            description: An optional description of the dashboard.
            tags: The tags to associate with the dashboard.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a dashboard
            The following example creates a dashboard in a space from a JSON dashboard definition. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_omni_dashboard(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', name='service-health-overview', body='{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors"}}]}', description='Overview of service health metrics.', tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_omni_dashboard_input.CreateOmniDashboardInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_omni_dashboard_output.CreateOmniDashboardOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_omni_dashboard

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_omni_dashboard.async_create_omni_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_omni_dashboard_input.CreateOmniDashboardInput = {
            "space_id": space_id,
            "name": name,
            "body": body,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    async def create_one_time_deep_link_code(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        ttl_seconds: Optional[int] = None,
        redirect_url: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.create_one_time_deep_link_code_output.CreateOneTimeDeepLinkCodeOutput":
        """Generates a one-time code for deep-link authentication. Direct the user's browser to the returned deepLinkUrl before it expires. The code is exchanged for an authenticated, domain-scoped session and can be used only once.

        Args:
            domain_id: The ID of the domain to generate the code for.
            ttl_seconds: How long the code remains valid, in seconds. Defaults to 300.
            redirect_url: The URL to redirect to after the deep-link code is used. Must be an HTTPS URL in the domain with a path of /auth/callback, and cannot include a query string or fragment. If omitted, no redirect is applied.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a one-time deep-link code
            The following example creates a one-time deep-link code for a domain that remains valid for 300 seconds and, once used, redirects the browser to the domain's /auth/callback path. Direct the user's browser to the returned deepLinkUrl before it expires; the code can be used only once. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_one_time_deep_link_code(domain_id='d-1a2b3c4d5e', ttl_seconds=300, redirect_url='https://d-1a2b3c4d5e.cloudwatch-omni.global.app.aws/auth/callback')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_one_time_deep_link_code_input.CreateOneTimeDeepLinkCodeInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_one_time_deep_link_code_output.CreateOneTimeDeepLinkCodeOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_one_time_deep_link_code

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_one_time_deep_link_code.async_create_one_time_deep_link_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_one_time_deep_link_code_input.CreateOneTimeDeepLinkCodeInput = {
            "domain_id": domain_id
        }
        if ttl_seconds is not None:
            input_["ttl_seconds"] = ttl_seconds
        if redirect_url is not None:
            input_["redirect_url"] = redirect_url

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_space(
        self,
        name: str,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        data_access_role_arn: "capo_cloudwatchomni.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        agent_core_evaluation_role_arn: Optional[
            "capo_cloudwatchomni.types.arn.Arn"
        ] = None,
        encryption_configuration: Optional[
            "capo_cloudwatchomni.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.create_space_output.CreateSpaceOutput":
        """Creates a space in a domain. Use GetSpace to retrieve the space, ListSpaces to enumerate spaces, UpdateSpace to modify it, and DeleteSpace to remove it.

        Args:
            name: A name that identifies the space. Must be 3-64 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            domain_id: The ID of the domain to create the space in.
            data_access_role_arn: The ARN of the IAM role used for data access. The role must be in the caller's account.
            agent_core_evaluation_role_arn: The ARN of the IAM role used by AgentCore online evaluation. Must be in the caller's account. Omit if the space does not use AgentCore online evaluation.
            encryption_configuration: How to encrypt the space's data at rest. Omit for service owned encryption, which is equivalent to passing `encryptionStrategy` AWS_OWNED.
            tags: The tags to associate with the space.
            client_token: Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a space
            The following example creates a space in a domain and encrypts its data at rest with a customer managed KMS key. The name must be 3-64 characters of lowercase letters, numbers, and hyphens. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_space(name='prod-observability', domain_id='d-1a2b3c4d5e', data_access_role_arn='arn:aws:iam::123456789012:role/CloudWatchSpaceDataAccessRole', agent_core_evaluation_role_arn='arn:aws:iam::123456789012:role/CloudWatchAgentCoreEvaluationRole', encryption_configuration={'encryptionStrategy': 'CUSTOMER_MANAGED', 'kmsKeyArn': 'arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d'}, tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_space_input.CreateSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_space_output.CreateSpaceOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_space

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_space.async_create_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_space_input.CreateSpaceInput = {
            "name": name,
            "domain_id": domain_id,
            "data_access_role_arn": data_access_role_arn,
        }
        if agent_core_evaluation_role_arn is not None:
            input_["agent_core_evaluation_role_arn"] = agent_core_evaluation_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags
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

    async def create_view(
        self,
        name: "capo_cloudwatchomni.types.view_name.ViewName",
        definition: "capo_cloudwatchomni.types.view_definition.ViewDefinition",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        description: Optional[
            "capo_cloudwatchomni.types.view_description.ViewDescription"
        ] = None,
        tags: Optional["capo_cloudwatchomni.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.create_view_response.CreateViewResponse":
        r"""Creates a new SQL view. A view is a named, reusable SQL query that can be referenced from telemetry queries. View names must be unique within the account and region. Only USER views can be created — MANAGED views are provisioned by AWS.

        Args:
            name: The name of the view. Must begin with the "view." prefix. View names must be unique within the account and region.
            definition: The SQL query that defines the view.
            description: A description of the view.
            tags: Resource tags.
            client_token: Idempotency token for safe retries. Retrying with the same token returns the original view instead of creating a duplicate.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a view
            The following example creates a user view that saves an error-count-by-service query. View names must begin with the view. prefix and be unique within the account and Region. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.create_view(name='view.service_errors', definition='SELECT resource[\'attributes\'][\'service.name\'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE severityText = \'ERROR\' GROUP BY service', description='Error counts by service', tags={'Team': 'observability'}, client_token='3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.create_view_request.CreateViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.create_view_response.CreateViewResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_view

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.create_view.async_create_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.create_view_request.CreateViewRequest = {
            "name": name,
            "definition": definition,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    async def delete_access_grant(
        self,
        grant_id: "capo_cloudwatchomni.types.grant_id.GrantId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_access_grant_output.DeleteAccessGrantOutput":
        """Removes an existing AccessGrant, revoking the access it granted. A service-managed grant cannot be deleted.

        Args:
            grant_id: The ID of the access grant to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an access grant
            The following example deletes an access grant by ID, revoking the access it granted. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_access_grant(grant_id='7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_access_grant_input.DeleteAccessGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_access_grant_output.DeleteAccessGrantOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_access_grant

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_access_grant.async_delete_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_access_grant_input.DeleteAccessGrantInput = {
            "grant_id": grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_profile(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_access_profile_output.DeleteAccessProfileOutput":
        """Removes an access profile. An access profile cannot be deleted while access grants reference it.

        Args:
            space_id: The unique ID of the space.
            profile_id: The unique ID of the access profile to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an access profile
            The following example deletes an access profile from a space. An access profile cannot be deleted while access grants reference it. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_access_profile(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_access_profile_input.DeleteAccessProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_access_profile_output.DeleteAccessProfileOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_access_profile

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_access_profile.async_delete_access_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_access_profile_input.DeleteAccessProfileInput = {
            "space_id": space_id,
            "profile_id": profile_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_alert(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        alert_id: "capo_cloudwatchomni.types.alert_id.AlertId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_alert_output.DeleteAlertOutput":
        """Deletes an alert by its identifier. Idempotent: deleting an alert that has already been removed succeeds without error.

        Args:
            space_id: The unique ID of the space.
            alert_id: The alert to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an alert
            The following example removes an alert from a space. Deleting an alert that has already been removed succeeds without error. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', alert_id='c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_alert_input.DeleteAlertInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_alert_output.DeleteAlertOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_alert

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_alert.async_delete_alert(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_alert_input.DeleteAlertInput = {
            "space_id": space_id,
            "alert_id": alert_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_domain_output.DeleteDomainOutput":
        """Removes a domain and all of its resources. Call this operation in the Region where the domain was created. A domain cannot be deleted while it contains spaces.

        Args:
            domain_id: The unique ID of the domain to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a domain
            The following example deletes a domain in the Region where it was created. The domain must not contain any spaces. A successful response returns an empty body. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_domain(domain_id='d-1a2b3c4d5e')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_domain_input.DeleteDomainInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain_access_grant_for_organization(
        self,
        grant_id: "capo_cloudwatchomni.types.grant_id.GrantId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_output.DeleteDomainAccessGrantForOrganizationOutput":
        """Removes an existing organization access grant, revoking the access it granted. A service-managed grant cannot be deleted.

        Args:
            grant_id: The ID of the access grant to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an organization domain access grant
            The following example deletes an organization domain access grant by ID, revoking the access it granted. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_domain_access_grant_for_organization(grant_id='7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_input.DeleteDomainAccessGrantForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_output.DeleteDomainAccessGrantForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain_access_grant_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain_access_grant_for_organization.async_delete_domain_access_grant_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_domain_access_grant_for_organization_input.DeleteDomainAccessGrantForOrganizationInput = {
            "grant_id": grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain_for_organization(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_domain_for_organization_output.DeleteDomainForOrganizationOutput":
        """Removes an organization domain and all of its resources. Call this operation in the Region where the domain was created. A domain cannot be deleted while it contains spaces.

        Args:
            domain_id: The ID of the organization domain to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an organization domain
            The following example deletes an organization domain in the Region where it was created. The domain must not contain any spaces. A successful response returns an empty body. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_domain_for_organization(domain_id='d-9z8y7x6w5v')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_domain_for_organization_input.DeleteDomainForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_domain_for_organization_output.DeleteDomainForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_domain_for_organization.async_delete_domain_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_domain_for_organization_input.DeleteDomainForOrganizationInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_integration(
        self,
        identifier: "capo_cloudwatchomni.types.integration_identifier.IntegrationIdentifier",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_integration_output.DeleteIntegrationOutput":
        """Deletes an integration. Returns the resulting status.

        Args:
            identifier: Identifies the integration to delete — exactly one of integrationId, integrationArn, or integrationName.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an integration by id
            The following example deletes the integration identified by its id. DeleteIntegration is idempotent and returns an empty response. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_integration(identifier={'integrationId': 'a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_integration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_integration_input.DeleteIntegrationInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_omni_dashboard(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_omni_dashboard_output.DeleteOmniDashboardOutput":
        """Removes a dashboard from a space.

        Args:
            space_id: The unique ID of the space.
            dashboard_id: The unique ID of the dashboard.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a dashboard
            The following example removes a dashboard from a space. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_omni_dashboard(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', dashboard_id='c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_omni_dashboard_input.DeleteOmniDashboardInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_omni_dashboard_output.DeleteOmniDashboardOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_omni_dashboard

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_omni_dashboard.async_delete_omni_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_omni_dashboard_input.DeleteOmniDashboardInput = {
            "space_id": space_id,
            "dashboard_id": dashboard_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_space(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_space_output.DeleteSpaceOutput":
        """Removes a space and all of its resources.

        Args:
            space_id: The unique ID of the space to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a space
            The following example removes a space and all of its resources. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_space(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_space_input.DeleteSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_space_output.DeleteSpaceOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_space

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_space.async_delete_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_space_input.DeleteSpaceInput = {
            "space_id": space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_view(
        self,
        name: "capo_cloudwatchomni.types.view_name.ViewName",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.delete_view_response.DeleteViewResponse":
        """Deletes the specified view. Queries that reference the view fail after it is deleted. Managed views cannot be deleted.

        Args:
            name: The name of the view to delete.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a view
            The following example deletes a view. The response body is empty. Queries that reference the view fail after it is deleted. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.delete_view(name='view.service_errors')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.delete_view_request.DeleteViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.delete_view_response.DeleteViewResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_view

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.delete_view.async_delete_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.delete_view_request.DeleteViewRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grant(
        self,
        grant_id: "capo_cloudwatchomni.types.grant_id.GrantId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_access_grant_output.GetAccessGrantOutput":
        """Retrieves the full detail of a single AccessGrant by ID.

        Args:
            grant_id: The ID of the access grant to retrieve.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an access grant
            The following example retrieves the full detail of a single access grant by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_access_grant(grant_id='7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_access_grant_input.GetAccessGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_access_grant_output.GetAccessGrantOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_access_grant

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_access_grant.async_get_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_access_grant_input.GetAccessGrantInput = {
            "grant_id": grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_profile(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_access_profile_output.GetAccessProfileOutput":
        """Retrieves an access profile by ID. The response indicates whether the calling principal is currently allowed to assume the profile.

        Args:
            space_id: The unique ID of the space.
            profile_id: The unique ID of the access profile.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an access profile
            The following example retrieves an access profile by ID, including whether the calling principal is currently allowed to assume it. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_access_profile(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_access_profile_input.GetAccessProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_access_profile_output.GetAccessProfileOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_access_profile

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_access_profile.async_get_access_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_access_profile_input.GetAccessProfileInput = {
            "space_id": space_id,
            "profile_id": profile_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_alert(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        alert_id: "capo_cloudwatchomni.types.alert_id.AlertId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_alert_output.GetAlertOutput":
        """Retrieves a single alert by its identifier. Use ListAlerts to enumerate alerts in the space.

        Args:
            space_id: The unique ID of the space.
            alert_id: The alert to retrieve.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve an alert
            The following example retrieves an alert by its identifier, including the live evaluation state that CreateAlert does not report. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', alert_id='c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_alert_input.GetAlertInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_alert_output.GetAlertOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_alert

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_alert.async_get_alert(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_alert_input.GetAlertInput = {
            "space_id": space_id,
            "alert_id": alert_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_context_graph(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        node_filters: Optional[
            "capo_cloudwatchomni.types.node_filters.NodeFilters"
        ] = None,
        edge_filters: Optional[
            "capo_cloudwatchomni.types.edge_filters.EdgeFilters"
        ] = None,
        depth: Optional[int] = None,
        max_results: Optional[int] = None,
        max_edges_per_node: Optional[int] = None,
        include_metadata: Optional[bool] = None,
        next_token: Optional[
            "capo_cloudwatchomni.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.get_context_graph_output.GetContextGraphOutput":
        """Queries the context graph with filtering, traversal, and pagination support. Pagination note: nodes and edges are returned together as a coherent subgraph. Pagination cursors advance over nodes (the primary collection); each page includes all edges connecting nodes within that page. Callers should treat nodes as the paginated collection and edges as supplementary relationship data attached to those nodes.

        Args:
            node_filters: Criteria restricting which nodes are returned.
            edge_filters: Criteria restricting which edges are returned.
            start_time: Start of the time range (UTC), inclusive.
            end_time: End of the time range (UTC), inclusive.
            depth: How many hops to traverse out from the nodes matched by nodeFilters. 0 returns only the matched nodes themselves.
            max_results: The maximum number of nodes to return in a single page.
            max_edges_per_node: The maximum number of edges to return per node, bounding the fan-out of a densely connected node.
            include_metadata: Whether to return the metadata block, semantics included, on each node and edge. Off by default because it costs an extra lookup per returned node.
            next_token: Pagination token from a previous response, to retrieve the next page.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Query a service and its immediate dependencies
            The following example returns context graph nodes matching the filter and traverses one hop out to their direct dependencies, over a one-hour window. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_context_graph(node_filters={'nodeType': 'SERVICE', 'namespace': ['ecommerce']}, start_time='2026-09-16T00:00:00Z', end_time='2026-09-16T01:00:00Z', depth=1, max_results=100, include_metadata=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_context_graph_input.GetContextGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_context_graph_output.GetContextGraphOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_context_graph

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_context_graph.async_get_context_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_context_graph_input.GetContextGraphInput = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if node_filters is not None:
            input_["node_filters"] = node_filters
        if edge_filters is not None:
            input_["edge_filters"] = edge_filters
        if depth is not None:
            input_["depth"] = depth
        if max_results is not None:
            input_["max_results"] = max_results
        if max_edges_per_node is not None:
            input_["max_edges_per_node"] = max_edges_per_node
        if include_metadata is not None:
            input_["include_metadata"] = include_metadata
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_context_graph(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        node_filters: Optional[
            "capo_cloudwatchomni.types.node_filters.NodeFilters"
        ] = None,
        edge_filters: Optional[
            "capo_cloudwatchomni.types.edge_filters.EdgeFilters"
        ] = None,
        depth: Optional[int] = None,
        max_results: Optional[int] = None,
        max_edges_per_node: Optional[int] = None,
        include_metadata: Optional[bool] = None,
        next_token: Optional[
            "capo_cloudwatchomni.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.node.Node]":
        _token = next_token
        while True:
            _response = await self.get_context_graph(
                start_time,
                end_time,
                config_overrides=config_overrides,
                node_filters=node_filters,
                edge_filters=edge_filters,
                depth=depth,
                max_results=max_results,
                max_edges_per_node=max_edges_per_node,
                include_metadata=include_metadata,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_domain(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_domain_output.GetDomainOutput":
        """Retrieves the details of a domain by ID.

        Args:
            domain_id: The unique ID of the domain.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a domain
            The following example retrieves the configuration and status of an Identity Center domain by its ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_domain(domain_id='d-1a2b3c4d5e')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_domain_output.GetDomainOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_domain_input.GetDomainInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_access_grant_for_organization(
        self,
        grant_id: "capo_cloudwatchomni.types.grant_id.GrantId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_domain_access_grant_for_organization_output.GetDomainAccessGrantForOrganizationOutput":
        """Retrieves the full detail of a single organization access grant by ID.

        Args:
            grant_id: The ID of the access grant to retrieve.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an organization domain access grant
            The following example retrieves the full detail of a single organization domain access grant by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_domain_access_grant_for_organization(grant_id='7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_domain_access_grant_for_organization_input.GetDomainAccessGrantForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_domain_access_grant_for_organization_output.GetDomainAccessGrantForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain_access_grant_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain_access_grant_for_organization.async_get_domain_access_grant_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_domain_access_grant_for_organization_input.GetDomainAccessGrantForOrganizationInput = {
            "grant_id": grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_for_organization(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_domain_for_organization_output.GetDomainForOrganizationOutput":
        """Retrieves the details of an organization domain by ID.

        Args:
            domain_id: The ID of the organization domain.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an organization domain
            The following example retrieves the configuration and status of an organization-scoped domain by its ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_domain_for_organization(domain_id='d-9z8y7x6w5v')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_domain_for_organization_input.GetDomainForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_domain_for_organization_output.GetDomainForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_domain_for_organization.async_get_domain_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_domain_for_organization_input.GetDomainForOrganizationInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_integration(
        self,
        identifier: "capo_cloudwatchomni.types.integration_identifier.IntegrationIdentifier",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_integration_output.GetIntegrationOutput":
        """Returns the details of a single integration, identified by its identifier, Amazon Resource Name, or name.

        Args:
            identifier: Identifies the integration to return — exactly one of integrationId, integrationArn, or integrationName.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an integration by id
            The following example returns the integration with the given id. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_integration(identifier={'integrationId': 'a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_integration_input.GetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_integration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_integration_input.GetIntegrationInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intelligence_configuration(
        self, *, config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None
    ) -> "capo_cloudwatchomni.types.get_intelligence_configuration_output.GetIntelligenceConfigurationOutput":
        """Retrieves the intelligence configuration for the calling account. Account is identified via FAS (caller identity). Returns the default configuration if none exists yet.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the intelligence configuration
            The following example retrieves the intelligence configuration for the calling account. The request carries no parameters; the account is taken from the caller identity. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_intelligence_configuration()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_intelligence_configuration_input.GetIntelligenceConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_intelligence_configuration_output.GetIntelligenceConfigurationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_intelligence_configuration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_intelligence_configuration.async_get_intelligence_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_intelligence_configuration_input.GetIntelligenceConfigurationInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_omni_dashboard(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_omni_dashboard_output.GetOmniDashboardOutput":
        """Retrieves a dashboard by ID within a space.

        Args:
            space_id: The unique ID of the space.
            dashboard_id: The unique ID of the dashboard.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a dashboard
            The following example retrieves a dashboard by ID within a space, including its full body. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_omni_dashboard(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', dashboard_id='c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_omni_dashboard_input.GetOmniDashboardInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_omni_dashboard_output.GetOmniDashboardOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_omni_dashboard

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_omni_dashboard.async_get_omni_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_omni_dashboard_input.GetOmniDashboardInput = {
            "space_id": space_id,
            "dashboard_id": dashboard_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_space(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_space_output.GetSpaceOutput":
        """Retrieves the details of a space by ID.

        Args:
            space_id: The unique ID of the space.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a space
            The following example retrieves the details of a space by ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_space(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_space_input.GetSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_space_output.GetSpaceOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_space

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_space.async_get_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_space_input.GetSpaceInput = {
            "space_id": space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_space_credentials_for_organization(
        self,
        context: "capo_cloudwatchomni.types.space_credential_request_context.SpaceCredentialRequestContext",
        credential_type: "capo_cloudwatchomni.types.organization_credential_type.OrganizationCredentialType",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_space_credentials_for_organization_output.GetSpaceCredentialsForOrganizationOutput":
        """Returns temporary credentials for a space in an organization member account. The credentials are valid for one hour. The caller must be the organization's management account or a delegated administrator with access to the target space. The target account must be an active member of the same organization as the domain, and the space must already exist.

        Args:
            context: Context for credential resolution.
            credential_type: Selects which member-account credential to return. Set this to SPACE_OPERATION.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get space credentials for an organization member account
            The following example returns temporary, space-scoped AWS credentials for an existing space in an organization member account, selected by spaceId. The credentials are valid for one hour, as reflected by the expiration timestamp. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_space_credentials_for_organization(context={'spaceId': 'a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d'}, credential_type='SPACE_OPERATION')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_space_credentials_for_organization_input.GetSpaceCredentialsForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_space_credentials_for_organization_output.GetSpaceCredentialsForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_space_credentials_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_space_credentials_for_organization.async_get_space_credentials_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_space_credentials_for_organization_input.GetSpaceCredentialsForOrganizationInput = {
            "context": context,
            "credential_type": credential_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_telemetry_query_results(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.get_telemetry_query_results_response.GetTelemetryQueryResultsResponse":
        """Returns the results for the specified query.

        Args:
            query_id: The unique ID of the query.
            next_token: A token to retrieve the next page of results.
            max_results: The maximum number of result rows to return per page.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get telemetry query results
            The following example retrieves a page of results for a completed query, along with execution statistics. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_telemetry_query_results(query_id='3b2a1c0d-7e6f-4a5b-8c9d-0e1f2a3b4c5d', max_results=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_telemetry_query_results_request.GetTelemetryQueryResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_telemetry_query_results_response.GetTelemetryQueryResultsResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_telemetry_query_results

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_telemetry_query_results.async_get_telemetry_query_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_telemetry_query_results_request.GetTelemetryQueryResultsRequest = {
            "query_id": query_id
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

    async def iter_get_telemetry_query_results(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.row.Row]":
        _token = next_token
        while True:
            _response = await self.get_telemetry_query_results(
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_view(
        self,
        name: "capo_cloudwatchomni.types.view_name.ViewName",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.get_view_response.GetViewResponse":
        """Returns the definition and metadata of the specified view.

        Args:
            name: The name of the view.

        Raises:
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a view
            The following example returns the definition and metadata of a view. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.get_view(name='view.service_errors')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.get_view_request.GetViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.get_view_response.GetViewResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_view

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.get_view.async_get_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.get_view_request.GetViewRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_access_grants(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        space_id: Optional["capo_cloudwatchomni.types.space_id.SpaceId"] = None,
        principal_id: Optional[
            "capo_cloudwatchomni.types.principal_id.PrincipalId"
        ] = None,
        principal_type: Optional[
            "capo_cloudwatchomni.types.access_grant_principal_type.AccessGrantPrincipalType"
        ] = None,
        permission: Optional[
            "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_access_grants_output.ListAccessGrantsOutput":
        """Returns AccessGrants, with optional filtering by domain, space, principal, or permission. A grant is returned only when it matches every filter supplied. With no filters, returns the grants for the current account and Region.

        Args:
            domain_id: Filter by domain ID.
            space_id: Filter by space ID.
            principal_id: Filter by principal ID.
            principal_type: Filter by principal type.
            permission: Filter by permission level.
            next_token: A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours.
            max_results: The maximum number of access grants to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List access grants in a space
            The following example lists the first page of access grants in a space and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_access_grants(domain_id='d-1a2b3c4d5e', space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_access_grants_input.ListAccessGrantsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_access_grants_output.ListAccessGrantsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_access_grants

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_access_grants.async_list_access_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_access_grants_input.ListAccessGrantsInput = {}
        if domain_id is not None:
            input_["domain_id"] = domain_id
        if space_id is not None:
            input_["space_id"] = space_id
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if principal_type is not None:
            input_["principal_type"] = principal_type
        if permission is not None:
            input_["permission"] = permission
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

    async def iter_list_access_grants(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        space_id: Optional["capo_cloudwatchomni.types.space_id.SpaceId"] = None,
        principal_id: Optional[
            "capo_cloudwatchomni.types.principal_id.PrincipalId"
        ] = None,
        principal_type: Optional[
            "capo_cloudwatchomni.types.access_grant_principal_type.AccessGrantPrincipalType"
        ] = None,
        permission: Optional[
            "capo_cloudwatchomni.types.access_grant_permission.AccessGrantPermission"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.access_grant_summary.AccessGrantSummary]":
        _token = next_token
        while True:
            _response = await self.list_access_grants(
                config_overrides=config_overrides,
                domain_id=domain_id,
                space_id=space_id,
                principal_id=principal_id,
                principal_type=principal_type,
                permission=permission,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_profiles(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_cloudwatchomni.types.list_access_profiles_output.ListAccessProfilesOutput"
    ):
        """Returns the access profiles in a space.

        Args:
            space_id: The unique ID of the space.
            next_token: A token to retrieve the next page of results.
            max_results: The maximum number of access profiles to return per page. Defaults to 100.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List access profiles in a space
            The following example lists the first page of access profiles in a space and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_access_profiles(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_access_profiles_input.ListAccessProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_access_profiles_output.ListAccessProfilesOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_access_profiles

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_access_profiles.async_list_access_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_access_profiles_input.ListAccessProfilesInput = {
            "space_id": space_id
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

    async def iter_list_access_profiles(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.access_profile_summary.AccessProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_access_profiles(
                space_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_alerts(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        filter_criteria: Optional[
            "capo_cloudwatchomni.types.alert_filter_criteria.AlertFilterCriteria"
        ] = None,
        sort_by: Optional[
            "capo_cloudwatchomni.types.alert_sort_field.AlertSortField"
        ] = None,
        sort_order: Optional[
            "capo_cloudwatchomni.types.alert_sort_order.AlertSortOrder"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_alerts_output.ListAlertsOutput":
        """Lists alerts within a space, optionally filtered by exact name(s), a single name prefix, or exact alertId(s), with pagination. Use GetAlert to retrieve a single alert's full detail.

        Args:
            space_id: The unique ID of the space.
            filter_criteria: Filter criteria narrowing which alerts are returned. All members are optional; the three name/id filters are mutually exclusive.
            sort_by: The field to sort results by.
            sort_order: The order in which to sort results.
            next_token: A token to retrieve the next page of results.
            max_results: The maximum number of alerts to return per page.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List alerts in a space
            The following example lists the first page of alerts in a space, sorted by state, and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_alerts(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', filter_criteria={'namePrefix': 'service-', 'stateValue': ['WARNING', 'CRITICAL']}, sort_by='STATE', sort_order='DESC', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_alerts_input.ListAlertsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_alerts_output.ListAlertsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_alerts

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_alerts.async_list_alerts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_alerts_input.ListAlertsInput = {
            "space_id": space_id
        }
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_alerts(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        filter_criteria: Optional[
            "capo_cloudwatchomni.types.alert_filter_criteria.AlertFilterCriteria"
        ] = None,
        sort_by: Optional[
            "capo_cloudwatchomni.types.alert_sort_field.AlertSortField"
        ] = None,
        sort_order: Optional[
            "capo_cloudwatchomni.types.alert_sort_order.AlertSortOrder"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.alert_summary.AlertSummary]":
        _token = next_token
        while True:
            _response = await self.list_alerts(
                space_id,
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domain_access_grants_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        principal_id: Optional[
            "capo_cloudwatchomni.types.principal_id.PrincipalId"
        ] = None,
        principal_type: Optional[
            "capo_cloudwatchomni.types.organization_grant_principal_type.OrganizationGrantPrincipalType"
        ] = None,
        permission: Optional[
            "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_domain_access_grants_for_organization_output.ListDomainAccessGrantsForOrganizationOutput":
        """Returns organization-level domain access grants, with optional filtering by domain, principal, or permission. A grant is returned only when it matches every filter supplied. With no filters, returns the grants for the caller's organization.

        Args:
            domain_id: Filter by domain ID.
            principal_id: Filter by principal ID.
            principal_type: Filter by principal type.
            permission: Filter by permission level.
            next_token: A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours.
            max_results: The maximum number of access grants to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List organization domain access grants
            The following example lists the first page of organization domain access grants and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_domain_access_grants_for_organization(domain_id='d-1a2b3c4d5e', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_domain_access_grants_for_organization_input.ListDomainAccessGrantsForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_domain_access_grants_for_organization_output.ListDomainAccessGrantsForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_domain_access_grants_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_domain_access_grants_for_organization.async_list_domain_access_grants_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_domain_access_grants_for_organization_input.ListDomainAccessGrantsForOrganizationInput = {}
        if domain_id is not None:
            input_["domain_id"] = domain_id
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if principal_type is not None:
            input_["principal_type"] = principal_type
        if permission is not None:
            input_["permission"] = permission
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

    async def iter_list_domain_access_grants_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        principal_id: Optional[
            "capo_cloudwatchomni.types.principal_id.PrincipalId"
        ] = None,
        principal_type: Optional[
            "capo_cloudwatchomni.types.organization_grant_principal_type.OrganizationGrantPrincipalType"
        ] = None,
        permission: Optional[
            "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission"
        ] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.organization_access_grant_summary.OrganizationAccessGrantSummary]":
        _token = next_token
        while True:
            _response = await self.list_domain_access_grants_for_organization(
                config_overrides=config_overrides,
                domain_id=domain_id,
                principal_id=principal_id,
                principal_type=principal_type,
                permission=permission,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_domains_output.ListDomainsOutput":
        """Returns the caller's domains: the account-scoped domain and the organization-scoped domain, if either exists. At most two domains are returned.

        Args:
            next_token: A token to retrieve the next page of results. Tokens expire after 24 hours.
            max_results: The maximum number of domains to return per page. Defaults to 100.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List domains
            The following example lists the caller's domains. At most two are returned — the account-scoped domain and the organization-scoped domain — so there is no nextToken. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_domains()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_domains_output.ListDomainsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_domains

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_domains_input.ListDomainsInput = {}
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

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_integrations(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        integration_type: Optional[
            "capo_cloudwatchomni.types.integration_type.IntegrationType"
        ] = None,
        status: Optional[
            "capo_cloudwatchomni.types.integration_status.IntegrationStatus"
        ] = None,
        name: Optional[str] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_integrations_output.ListIntegrationsOutput":
        """Lists the integrations in the account, optionally filtered by type, status, or name. Results are paginated.

        Args:
            integration_type: Returns only integrations of this provider type.
            status: Returns only integrations in this status.
            name: Returns only the integration with this exact name.
            next_token: Pagination token from a previous response; omit for the first page.
            max_results: Maximum number of integrations to return in one page.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List integrations of a type
            The following example lists up to 20 AWS_INTEGRATION integrations in the account. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_integrations(integration_type='AWS_INTEGRATION', max_results=20)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_integrations_input.ListIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_integrations

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_integrations.async_list_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_integrations_input.ListIntegrationsInput = {}
        if integration_type is not None:
            input_["integration_type"] = integration_type
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
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

    async def iter_list_integrations(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        integration_type: Optional[
            "capo_cloudwatchomni.types.integration_type.IntegrationType"
        ] = None,
        status: Optional[
            "capo_cloudwatchomni.types.integration_status.IntegrationStatus"
        ] = None,
        name: Optional[str] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.integration.Integration]":
        _token = next_token
        while True:
            _response = await self.list_integrations(
                config_overrides=config_overrides,
                integration_type=integration_type,
                status=status,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_omni_dashboards(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name_prefix: Optional[str] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_cloudwatchomni.types.list_omni_dashboards_output.ListOmniDashboardsOutput"
    ):
        """Returns the dashboards in a space, optionally filtered by name prefix.

        Args:
            space_id: The unique ID of the space.
            name_prefix: Filter to dashboards whose name starts with this prefix.
            next_token: A token to retrieve the next page of results.
            max_results: The maximum number of dashboards to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List dashboards in a space
            The following example lists the first page of dashboards in a space and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_omni_dashboards(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_omni_dashboards_input.ListOmniDashboardsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_omni_dashboards_output.ListOmniDashboardsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_omni_dashboards

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_omni_dashboards.async_list_omni_dashboards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_omni_dashboards_input.ListOmniDashboardsInput = {
            "space_id": space_id
        }
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
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

    async def iter_list_omni_dashboards(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name_prefix: Optional[str] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.omni_dashboard_summary.OmniDashboardSummary]":
        _token = next_token
        while True:
            _response = await self.list_omni_dashboards(
                space_id,
                config_overrides=config_overrides,
                name_prefix=name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_spaces(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_spaces_output.ListSpacesOutput":
        """Returns the spaces in the account, optionally filtered by domain.

        Args:
            domain_id: Filter by domain ID.
            next_token: A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours.
            max_results: The maximum number of spaces to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List spaces in a domain
            The following example lists the first page of spaces in a domain and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_spaces(domain_id='d-1a2b3c4d5e', max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_spaces_input.ListSpacesInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_spaces_output.ListSpacesOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_spaces

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_spaces.async_list_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_spaces_input.ListSpacesInput = {}
        if domain_id is not None:
            input_["domain_id"] = domain_id
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

    async def iter_list_spaces(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        domain_id: Optional["capo_cloudwatchomni.types.domain_id.DomainId"] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.space_summary.SpaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_spaces(
                config_overrides=config_overrides,
                domain_id=domain_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_spaces_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_spaces_for_organization_output.ListSpacesForOrganizationOutput":
        """Returns the spaces across all member accounts in the organization.

        Args:
            next_token: A token to retrieve the next page of results. Tokens expire after 24 hours.
            max_results: The maximum number of spaces to return per page. Defaults to 100.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List spaces across the organization
            The following example lists the first page of spaces across all member accounts in the organization. The results include spaces owned by different accounts, along with a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_spaces_for_organization(max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_spaces_for_organization_input.ListSpacesForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_spaces_for_organization_output.ListSpacesForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_spaces_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_spaces_for_organization.async_list_spaces_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_spaces_for_organization_input.ListSpacesForOrganizationInput = {}
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

    async def iter_list_spaces_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional["capo_cloudwatchomni.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.space_summary.SpaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_spaces_for_organization(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_telemetry_fields(
        self,
        data_set_name: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        telemetry_type: Optional[
            "capo_cloudwatchomni.types.telemetry_type.TelemetryType"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        next_token: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.list_telemetry_fields_response.ListTelemetryFieldsResponse":
        """Lists fields available for telemetry queries. Returns a list of fields included in the specified dataset, granular to telemetry type. Returned field names reflect the exact stored casing and are case-sensitive when referenced in query expressions; the query engine does not normalize identifier case.

        Args:
            data_set_name: The name of the dataset to list fields for.
            telemetry_type: The type of telemetry to filter fields by.
            start_time: Inclusive start of the lookback window. When omitted, the service defaults to the configured lookback before endTime.
            end_time: Inclusive end of the lookback window. When omitted, the service defaults to the current time.
            next_token: A token to retrieve the next page of results. Reserved for future pagination; the service does not paginate at this time and returns null.

        Raises:
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List fields for a dataset
            The following example lists the log fields available in the specified dataset. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_telemetry_fields(data_set_name='default', telemetry_type='LOGS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_telemetry_fields_request.ListTelemetryFieldsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_telemetry_fields_response.ListTelemetryFieldsResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_telemetry_fields

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_telemetry_fields.async_list_telemetry_fields(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_telemetry_fields_request.ListTelemetryFieldsRequest = {
            "data_set_name": data_set_name
        }
        if telemetry_type is not None:
            input_["telemetry_type"] = telemetry_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_telemetry_fields(
        self,
        data_set_name: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        telemetry_type: Optional[
            "capo_cloudwatchomni.types.telemetry_type.TelemetryType"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.field.Field]":
        _token = next_token
        while True:
            _response = await self.list_telemetry_fields(
                data_set_name,
                config_overrides=config_overrides,
                telemetry_type=telemetry_type,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fields",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_telemetry_query_sessions(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudwatchomni.types.list_telemetry_query_sessions_response.ListTelemetryQuerySessionsResponse":
        """Lists telemetry query sessions. Returns a list of telemetry query sessions owned by the caller.

        Args:
            next_token: A token to retrieve the next page of results.
            max_results: The maximum number of sessions to return per page.

        Raises:
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List telemetry query sessions
            The following example lists the query sessions owned by the caller. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_telemetry_query_sessions(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_telemetry_query_sessions_request.ListTelemetryQuerySessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_telemetry_query_sessions_response.ListTelemetryQuerySessionsResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_telemetry_query_sessions

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_telemetry_query_sessions.async_list_telemetry_query_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_telemetry_query_sessions_request.ListTelemetryQuerySessionsRequest = {}
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

    async def iter_list_telemetry_query_sessions(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = await self.list_telemetry_query_sessions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_views(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        type: Optional["capo_cloudwatchomni.types.view_type.ViewType"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.list_views_response.ListViewsResponse":
        """Lists the views in the caller's account and region. Returns a summary for each view, optionally filtered by view type. View definitions are not included — use GetView to retrieve them.

        Args:
            type: Return only views of this ownership category.
            max_results: The maximum number of views to return per page.
            next_token: A token to retrieve the next page of results.

        Raises:
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the views in an account and Region
            The following example returns a page of view summaries, filtered to user-created views. Definitions are not included — call GetView to retrieve them. A nextToken is returned when more results are available. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.list_views(type='USER', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.list_views_request.ListViewsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.list_views_response.ListViewsResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_views

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.list_views.async_list_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.list_views_request.ListViewsRequest = {}
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

    async def iter_list_views(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        type: Optional["capo_cloudwatchomni.types.view_type.ViewType"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.view_summary.ViewSummary]":
        _token = next_token
        while True:
            _response = await self.list_views(
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

    async def put_intelligence_configuration(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        kms_key_arn: Optional[
            "capo_cloudwatchomni.types.intelligence_kms_key_arn.IntelligenceKmsKeyArn"
        ] = None,
        remove_kms_key: Optional[bool] = None,
        client_token: Optional[
            "capo_cloudwatchomni.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.put_intelligence_configuration_output.PutIntelligenceConfigurationOutput":
        """Creates or updates the intelligence configuration for the calling account. Account is identified via FAS (caller identity).

        Args:
            kms_key_arn: Optional KMS key ARN to configure customer-managed encryption for anomaly data.
            remove_kms_key: Set to true to disassociate the configured KMS key. Mutually exclusive with kmsKeyArn; the service returns ValidationException if both are provided.
            client_token: Idempotency token for safe retries. Repeating a request with the same token applies the update at most once instead of reprocessing it.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Configure a customer-managed KMS key
            The following example sets the customer-managed KMS key used to encrypt the account's intelligence data. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.put_intelligence_configuration(kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d', client_token='b3f8c7d6-5b4a-4c3d-9e2f-1a0b2c3d4e5f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.put_intelligence_configuration_input.PutIntelligenceConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.put_intelligence_configuration_output.PutIntelligenceConfigurationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.put_intelligence_configuration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.put_intelligence_configuration.async_put_intelligence_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.put_intelligence_configuration_input.PutIntelligenceConfigurationInput = {}
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if remove_kms_key is not None:
            input_["remove_kms_key"] = remove_kms_key
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

    async def search_principals(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        search_query: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_cloudwatchomni.types.search_principals_next_token.SearchPrincipalsNextToken"
        ] = None,
    ) -> "capo_cloudwatchomni.types.search_principals_output.SearchPrincipalsOutput":
        """Searches Identity Center for users and groups in a domain. The domain must be configured with Identity Center. To grant access to a result, pass its principalId to CreateAccessGrant with a principalType of IDC_USER for a user or IDC_GROUP for a group.

        Args:
            domain_id: The ID of the domain to search within.
            search_query: A search term to match against user names, display names, and IDs. Pass * to list all principals. Maximum 128 characters.
            max_results: The maximum number of results to return. Defaults to 10. Valid only when searchQuery is *; other searches reject this parameter and return at most 10 results.
            next_token: A token to retrieve the next page of results. Valid only when searchQuery is *; other searches do not paginate and reject this parameter. Tokens expire after 24 hours.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Search principals by name
            The following example searches a domain for principals whose name matches a text query. A text search (any searchQuery other than *) returns at most 10 results and does not paginate, so maxResults and nextToken are not supplied and no nextToken is returned. To grant access to a result, pass its principalId to CreateAccessGrant with a principalType of IDC_USER for a user or IDC_GROUP for a group. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.search_principals(domain_id='d-1a2b3c4d5e', search_query='jane')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.search_principals_input.SearchPrincipalsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.search_principals_output.SearchPrincipalsOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.search_principals

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.search_principals.async_search_principals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.search_principals_input.SearchPrincipalsInput = {
            "domain_id": domain_id,
            "search_query": search_query,
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

    async def iter_search_principals(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        search_query: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_cloudwatchomni.types.search_principals_next_token.SearchPrincipalsNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_cloudwatchomni.types.principal_search_result.PrincipalSearchResult]":
        _token = next_token
        while True:
            _response = await self.search_principals(
                domain_id,
                search_query,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_telemetry_query(
        self,
        query_string: str,
        session_id: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.start_telemetry_query_response.StartTelemetryQueryResponse":
        r"""Starts a telemetry query within a session. Submits the provided query string for execution in the specified session. Use GetTelemetryQueryResults to poll for results and check query status.

        Args:
            query_string: The query string to execute.
            session_id: The unique ID of the session.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start a telemetry query
            The following example submits a SQL query within a session and returns the query ID used to poll for results. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.start_telemetry_query(session_id='9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f', query_string='SELECT `@timestamp`, `@message` FROM "logs.default" WHERE `@timestamp` BETWEEN NOW() - INTERVAL \'1 HOUR\' AND NOW() ORDER BY `@timestamp` DESC LIMIT 100')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.start_telemetry_query_request.StartTelemetryQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.start_telemetry_query_response.StartTelemetryQueryResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.start_telemetry_query

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.start_telemetry_query.async_start_telemetry_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.start_telemetry_query_request.StartTelemetryQueryRequest = {
            "query_string": query_string,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_telemetry_query_session(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        session_name: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.start_telemetry_query_session_response.StartTelemetryQuerySessionResponse":
        """Starts a new telemetry query session. A session provides a logical grouping for one or more telemetry queries. The returned session ID is required when starting queries via StartTelemetryQuery.

        Args:
            session_name: A human-readable name for the session. Names under `/aws/` are reserved for service integrations.

        Raises:
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start a telemetry query session
            The following example starts a session for grouping telemetry queries and returns its session ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.start_telemetry_query_session(session_name='prod-latency-investigation')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.start_telemetry_query_session_request.StartTelemetryQuerySessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.start_telemetry_query_session_response.StartTelemetryQuerySessionResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.start_telemetry_query_session

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.start_telemetry_query_session.async_start_telemetry_query_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.start_telemetry_query_session_request.StartTelemetryQuerySessionRequest = {}
        if session_name is not None:
            input_["session_name"] = session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_telemetry_query(
        self,
        query_id: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.stop_telemetry_query_response.StopTelemetryQueryResponse":
        """Stops a running telemetry query.

        Args:
            query_id: The unique ID of the query.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stop a running telemetry query
            The following example stops a running query by its ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.stop_telemetry_query(query_id='3b2a1c0d-7e6f-4a5b-8c9d-0e1f2a3b4c5d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.stop_telemetry_query_request.StopTelemetryQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.stop_telemetry_query_response.StopTelemetryQueryResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.stop_telemetry_query

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.stop_telemetry_query.async_stop_telemetry_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.stop_telemetry_query_request.StopTelemetryQueryRequest = {
            "query_id": query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_telemetry_query_session(
        self,
        session_id: str,
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
    ) -> "capo_cloudwatchomni.types.stop_telemetry_query_session_response.StopTelemetryQuerySessionResponse":
        """Stops a telemetry query session. Terminates the specified session. After a session is stopped it cannot be reused.

        Args:
            session_id: The unique ID of the session.

        Raises:
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stop a telemetry query session
            The following example terminates the specified session. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.stop_telemetry_query_session(session_id='9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.stop_telemetry_query_session_request.StopTelemetryQuerySessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.stop_telemetry_query_session_response.StopTelemetryQuerySessionResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.stop_telemetry_query_session

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.stop_telemetry_query_session.async_stop_telemetry_query_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.stop_telemetry_query_session_request.StopTelemetryQuerySessionRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_access_profile(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name: Optional[
            "capo_cloudwatchomni.types.access_profile_name.AccessProfileName"
        ] = None,
        description: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.update_access_profile_output.UpdateAccessProfileOutput":
        """Updates the name or description of an access profile. Only the provided fields are changed; omitted fields are left unchanged.

        Args:
            space_id: The unique ID of the space.
            profile_id: The unique ID of the access profile to update.
            name: A new name for the access profile. Omit to leave unchanged.
            description: A new description of the access profile. Omit to leave unchanged.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update an access profile description
            The following example updates only the description of an access profile; the name is left unchanged. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_access_profile(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', profile_id='analyst-readonly', description='Read-only access for analysts and on-call responders.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_access_profile_input.UpdateAccessProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_access_profile_output.UpdateAccessProfileOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_access_profile

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_access_profile.async_update_access_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_access_profile_input.UpdateAccessProfileInput = {
            "space_id": space_id,
            "profile_id": profile_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_alert(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        alert_id: "capo_cloudwatchomni.types.alert_id.AlertId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        profile_id: Optional["capo_cloudwatchomni.types.profile_id.ProfileId"] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        rule: Optional["capo_cloudwatchomni.types.rule.Rule"] = None,
        notifications_enabled: Optional[bool] = None,
        notification_rules: Optional[
            "capo_cloudwatchomni.types.notification_rule_list.NotificationRuleList"
        ] = None,
    ) -> "capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput":
        """Updates an existing alert. Only non-null fields overwrite existing values.

        Args:
            space_id: The unique ID of the space.
            alert_id: The alert to update.
            profile_id: The ID of the access profile associated with the alert.
            name: A new display name for the alert. Omit to leave the name unchanged (apply-if-present / PATCH). Same constraints as CreateAlert.name; the name is not the alert's identity, so a rename never changes the alertId.
            description: A new description of the alert. Omit to leave unchanged.
            rule: The rule that defines how the alert is evaluated. Omit to leave unchanged. Each sub-block is replaced whole when present: {@code query}, {@code condition}, {@code evaluation} and {@code noData} are applied only when supplied, and within a supplied block an omitted optional member is cleared to unset (null/absent) rather than preserved from the stored alert or defaulted. See {@link AlertCondition} and {@link AlertEvaluation}.
            notifications_enabled: Whether actions (notifications) are enabled for this alert. Omitted = leave existing value unchanged.
            notification_rules: Replaces the entire notification rule list when present; full-replace, not merge. Omitted = leave existing rules unchanged. An empty list clears all rules (the alert keeps evaluating; only notifications stop).

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Raise an alert's thresholds
            The following example replaces only the condition of an alert's rule; the query, the evaluation cadence and the notification rules are left unchanged. A supplied condition is replaced whole rather than merged, so every threshold to keep is sent again. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_alert(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', alert_id='c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f', rule={'telemetryRule': {'condition': {'thresholdMode': 'FIELD_VALUE', 'thresholdField': 'error_count', 'comparator': 'GT', 'warningThreshold': 100.0, 'criticalThreshold': 400.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_alert_input.UpdateAlertInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_alert

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_alert.async_update_alert(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_alert_input.UpdateAlertInput = {
            "space_id": space_id,
            "alert_id": alert_id,
        }
        if profile_id is not None:
            input_["profile_id"] = profile_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule
        if notifications_enabled is not None:
            input_["notifications_enabled"] = notifications_enabled
        if notification_rules is not None:
            input_["notification_rules"] = notification_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name: Optional[str] = None,
        identity_providers: Optional[
            "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList"
        ] = None,
        identity_provider_configuration: Optional[
            "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
    ) -> "capo_cloudwatchomni.types.update_domain_output.UpdateDomainOutput":
        """Updates a domain's name or identity provider configuration. Only the provided fields are changed; omitted fields are left unchanged. Renaming a domain also changes the endpoint URLs derived from its name.

        Args:
            domain_id: The unique ID of the domain to update.
            name: A new name for the domain. Omit to leave unchanged. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            identity_providers: The identity providers to configure for the domain.
            identity_provider_configuration: Identity provider configuration for the domain.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename a domain
            The following example performs a partial update that changes only the domain name; the omitted fields are left unchanged. Renaming the domain also updates the endpoint URLs derived from its name, and updatedAt advances past createdAt. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_domain(domain_id='d-1a2b3c4d5e', name='prod-observability-metrics')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_domain_input.UpdateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_domain_output.UpdateDomainOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_domain

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_domain_input.UpdateDomainInput = {
            "domain_id": domain_id
        }
        if name is not None:
            input_["name"] = name
        if identity_providers is not None:
            input_["identity_providers"] = identity_providers
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_for_organization(
        self,
        domain_id: "capo_cloudwatchomni.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name: Optional[str] = None,
        identity_providers: Optional[
            "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList"
        ] = None,
        identity_provider_configuration: Optional[
            "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
    ) -> "capo_cloudwatchomni.types.update_domain_for_organization_output.UpdateDomainForOrganizationOutput":
        """Updates an organization domain's name or identity provider configuration. Call this operation in the Region where the domain was created. Only the provided fields are changed; omitted fields are left unchanged. Renaming a domain also changes the endpoint URLs derived from its name.

        Args:
            domain_id: The ID of the organization domain to update.
            name: A new name for the organization domain. Omit to leave unchanged. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            identity_providers: The identity providers to configure for the domain. Omit to leave unchanged.
            identity_provider_configuration: Identity provider configuration for the domain. Omit to leave unchanged.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename an organization domain
            The following example performs a partial update that changes only the organization domain name; the omitted fields are left unchanged. The endpoint URLs derived from the name are updated, and updatedAt advances past createdAt. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_domain_for_organization(domain_id='d-9z8y7x6w5v', name='prod-observability-org-metrics')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_domain_for_organization_input.UpdateDomainForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_domain_for_organization_output.UpdateDomainForOrganizationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_domain_for_organization

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_domain_for_organization.async_update_domain_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_domain_for_organization_input.UpdateDomainForOrganizationInput = {
            "domain_id": domain_id
        }
        if name is not None:
            input_["name"] = name
        if identity_providers is not None:
            input_["identity_providers"] = identity_providers
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_integration(
        self,
        identifier: "capo_cloudwatchomni.types.integration_identifier.IntegrationIdentifier",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        credential: Optional[
            "capo_cloudwatchomni.types.integration_credential.IntegrationCredential"
        ] = None,
        integration_attributes: Optional[
            "capo_cloudwatchomni.types.string_map.StringMap"
        ] = None,
        role_arn: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.update_integration_output.UpdateIntegrationOutput":
        """Updates an existing integration, identified by its id, ARN, or name. Only the fields you provide are changed.

        Args:
            identifier: Identifies the integration to update — exactly one of integrationId, integrationArn, or integrationName.
            credential: The replacement credential used to authenticate with the provider.
            integration_attributes: The provider-specific attributes to associate with the integration.
            role_arn: The Amazon Resource Name of the IAM role assumed to access the integration.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update an integration's attributes
            The following example replaces the provider-specific attributes of the integration identified by its id. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_integration(identifier={'integrationId': 'a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d'}, integration_attributes={'notificationChannel': 'ops-oncall'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_integration

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_integration_input.UpdateIntegrationInput = {
            "identifier": identifier
        }
        if credential is not None:
            input_["credential"] = credential
        if integration_attributes is not None:
            input_["integration_attributes"] = integration_attributes
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_omni_dashboard(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        body: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> "capo_cloudwatchomni.types.update_omni_dashboard_output.UpdateOmniDashboardOutput":
        """Updates an existing dashboard within a space. Only the provided fields are changed; omitted fields are left unchanged.

        Args:
            space_id: The unique ID of the space.
            dashboard_id: The unique ID of the dashboard.
            body: The new dashboard definition, as a JSON document. Maximum 1 MiB. Omit to leave unchanged.
            name: A new name for the dashboard. Omit to leave unchanged.
            description: A new description of the dashboard. Omit to leave unchanged.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a dashboard body
            The following example updates only the body of a dashboard; the name and description are left unchanged. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_omni_dashboard(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', dashboard_id='c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f', body='{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"],["AWS/Lambda","Throttles","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors and Throttles"}}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_omni_dashboard_input.UpdateOmniDashboardInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_omni_dashboard_output.UpdateOmniDashboardOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_omni_dashboard

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_omni_dashboard.async_update_omni_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_omni_dashboard_input.UpdateOmniDashboardInput = {
            "space_id": space_id,
            "dashboard_id": dashboard_id,
        }
        if body is not None:
            input_["body"] = body
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_space(
        self,
        space_id: "capo_cloudwatchomni.types.space_id.SpaceId",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        name: Optional[str] = None,
        encryption_configuration: Optional[
            "capo_cloudwatchomni.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_cloudwatchomni.types.update_space_output.UpdateSpaceOutput":
        """Updates a space. Only the provided fields are changed; omitted fields are left unchanged.

        Args:
            space_id: The unique ID of the space to update.
            name: A new name for the space. Omit to leave unchanged. Must be 3-64 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
            encryption_configuration: How to encrypt the space's data at rest. Omit to leave encryption unchanged. Pass `encryptionStrategy` AWS_OWNED to stop using a customer managed key and revert to service owned encryption.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: A service quota was exceeded.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename a space
            The following example updates only the name of a space; omitted fields are left unchanged. The response returns the full space with a later updatedAt timestamp. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_space(space_id='a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d', name='prod-observability-team')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_space_input.UpdateSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_space_output.UpdateSpaceOutput"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_space

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_space.async_update_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_space_input.UpdateSpaceInput = {
            "space_id": space_id
        }
        if name is not None:
            input_["name"] = name
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_view(
        self,
        name: "capo_cloudwatchomni.types.view_name.ViewName",
        *,
        config_overrides: Optional[AsyncCloudWatchOmniClientConfig] = None,
        definition: Optional[
            "capo_cloudwatchomni.types.view_definition.ViewDefinition"
        ] = None,
        description: Optional[
            "capo_cloudwatchomni.types.view_description.ViewDescription"
        ] = None,
    ) -> "capo_cloudwatchomni.types.update_view_response.UpdateViewResponse":
        r"""Updates an existing view's definition and/or description. Only the fields you provide are changed. Managed views cannot be updated.

        Args:
            name: The name of the view to update.
            definition: The new SQL query that defines the view. Omit to leave unchanged.
            description: The new description of the view. Omit to leave unchanged.

        Raises:
            capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException: The caller is not authorized to perform this action.
            capo_cloudwatchomni.errors.conflict_exception.ConflictException: The operation could not be completed because of a conflict with the current state of the resource.
            capo_cloudwatchomni.errors.internal_server_exception.InternalServerException: An unexpected error occurred while processing the request.
            capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_cloudwatchomni.errors.throttling_exception.ThrottlingException: The request was throttled due to exceeding the allowed request rate.
            capo_cloudwatchomni.errors.validation_exception.ValidationException: A parameter is specified incorrectly.
            capo_cloudwatchomni.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a view's definition
            The following example changes only the definition; the omitted description is left unchanged. Managed views cannot be updated. The response carries the view's effective configuration. Payloads are shown as JSON; on the wire they are CBOR-encoded.

            >>> await client.update_view(name='view.service_errors', definition='SELECT resource[\'attributes\'][\'service.name\'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE status[\'code\'] IN (\'2\', \'ERROR\') GROUP BY service')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudwatchomni.types.update_view_request.UpdateViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudwatchomni.types.update_view_response.UpdateViewResponse"
        ]:
            import capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_view

            (
                output,
                http_response,
            ) = await capo_cloudwatchomni._operations.cloud_watch_omni_frontend.update_view.async_update_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatchomni.types.update_view_request.UpdateViewRequest = {
            "name": name
        }
        if definition is not None:
            input_["definition"] = definition
        if description is not None:
            input_["description"] = description

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
