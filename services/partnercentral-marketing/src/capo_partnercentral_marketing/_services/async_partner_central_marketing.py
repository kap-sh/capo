"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AWSPartnerDemandGenerator``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_partnercentral_marketing._auth._signers
import capo_partnercentral_marketing._auth._sigv4
from capo_partnercentral_marketing._auth._identity import Credentials
from capo_partnercentral_marketing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_marketing._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_marketing._pagination import resolve_path as _resolve_path
from capo_partnercentral_marketing._resources.aws_partner_demand_generator.campaign_resource import (
    AsyncCampaignResource,
)
from capo_partnercentral_marketing._services._aws_config import aaws_config
from capo_partnercentral_marketing._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
)

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.aws_service_filter_list
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entries
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_request
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_response
    import capo_partnercentral_marketing.types.campaign_asset_export_task_id
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_identifiers
    import capo_partnercentral_marketing.types.campaign_asset_summary
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.campaign_identifier_list
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_social_connections
    import capo_partnercentral_marketing.types.campaign_sort
    import capo_partnercentral_marketing.types.campaign_state_list
    import capo_partnercentral_marketing.types.campaign_summary
    import capo_partnercentral_marketing.types.campaign_template_collection_filter_list
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.campaign_template_summary
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.create_campaign_request
    import capo_partnercentral_marketing.types.create_campaign_response
    import capo_partnercentral_marketing.types.create_social_connection_authorization_url_request
    import capo_partnercentral_marketing.types.create_social_connection_authorization_url_response
    import capo_partnercentral_marketing.types.customer_segment_filter_list
    import capo_partnercentral_marketing.types.deactivate_campaign_asset_request
    import capo_partnercentral_marketing.types.deactivate_campaign_asset_response
    import capo_partnercentral_marketing.types.delete_campaign_asset_request
    import capo_partnercentral_marketing.types.delete_campaign_request
    import capo_partnercentral_marketing.types.delete_social_connection_request
    import capo_partnercentral_marketing.types.engagement_group_id_list
    import capo_partnercentral_marketing.types.field_value_input_list
    import capo_partnercentral_marketing.types.file_ref
    import capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request
    import capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response
    import capo_partnercentral_marketing.types.get_campaign_asset_export_task_request
    import capo_partnercentral_marketing.types.get_campaign_asset_export_task_response
    import capo_partnercentral_marketing.types.get_campaign_asset_request
    import capo_partnercentral_marketing.types.get_campaign_asset_response
    import capo_partnercentral_marketing.types.get_campaign_request
    import capo_partnercentral_marketing.types.get_campaign_response
    import capo_partnercentral_marketing.types.get_campaign_template_request
    import capo_partnercentral_marketing.types.get_campaign_template_response
    import capo_partnercentral_marketing.types.industry_filter_list
    import capo_partnercentral_marketing.types.language_filter_list
    import capo_partnercentral_marketing.types.layout_option_value
    import capo_partnercentral_marketing.types.list_campaign_assets_request
    import capo_partnercentral_marketing.types.list_campaign_assets_response
    import capo_partnercentral_marketing.types.list_campaigns_request
    import capo_partnercentral_marketing.types.list_campaigns_response
    import capo_partnercentral_marketing.types.list_social_connections_request
    import capo_partnercentral_marketing.types.list_social_connections_response
    import capo_partnercentral_marketing.types.list_tags_for_resource_request
    import capo_partnercentral_marketing.types.list_tags_for_resource_response
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.monetary_value
    import capo_partnercentral_marketing.types.next_token
    import capo_partnercentral_marketing.types.partner_address
    import capo_partnercentral_marketing.types.platform
    import capo_partnercentral_marketing.types.privacy_policy_url
    import capo_partnercentral_marketing.types.search_campaign_templates_request
    import capo_partnercentral_marketing.types.search_campaign_templates_response
    import capo_partnercentral_marketing.types.send_mode
    import capo_partnercentral_marketing.types.sender_email
    import capo_partnercentral_marketing.types.social_connection_identifier
    import capo_partnercentral_marketing.types.social_connection_summary
    import capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request
    import capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response
    import capo_partnercentral_marketing.types.start_campaign_asset_export_task_request
    import capo_partnercentral_marketing.types.start_campaign_asset_export_task_response
    import capo_partnercentral_marketing.types.tag_key_list
    import capo_partnercentral_marketing.types.tag_list
    import capo_partnercentral_marketing.types.tag_resource_request
    import capo_partnercentral_marketing.types.tag_resource_response
    import capo_partnercentral_marketing.types.taggable_resource_arn
    import capo_partnercentral_marketing.types.target_audience
    import capo_partnercentral_marketing.types.template_search_text
    import capo_partnercentral_marketing.types.theme_filter_list
    import capo_partnercentral_marketing.types.timestamp
    import capo_partnercentral_marketing.types.untag_resource_request
    import capo_partnercentral_marketing.types.untag_resource_response
    import capo_partnercentral_marketing.types.update_campaign_asset_request
    import capo_partnercentral_marketing.types.update_campaign_asset_response
    import capo_partnercentral_marketing.types.update_campaign_request
    import capo_partnercentral_marketing.types.update_campaign_response
    import capo_partnercentral_marketing.types.use_case_filter_list
    import capo_partnercentral_marketing.types.utc_date


class AsyncPartnerCentralMarketingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPartnerCentralMarketingClient:
    """A client for the ``PartnerCentralMarketing`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
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
        retry_mode: Literal["standard", "adaptive"] | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
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
                AsyncClient(raw_handler)
            )
        self._config = AsyncPartnerCentralMarketingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.campaign_resource = AsyncCampaignResource(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralMarketingClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_social_connection_authorization_url(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        platform: "capo_partnercentral_marketing.types.platform.Platform",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.create_social_connection_authorization_url_response.CreateSocialConnectionAuthorizationUrlResponse":
        """Creates a single-use URL the partner visits to authorize publishing on a platform. Serves a first connect, connecting a further account, and re-authorizing an expired one: consenting with an account that is already connected re-authorizes that connection and keeps its id; any other account adds a connection. Poll ListSocialConnections for the outcome. Deliberately not idempotent and takes no client token: every call must mint a fresh single-use URL, so replaying a cached response would hand back a dead one.

        Args:
            catalog: Catalog the connection belongs to.
            platform: Social platform to authorize.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.create_social_connection_authorization_url_request.CreateSocialConnectionAuthorizationUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.create_social_connection_authorization_url_response.CreateSocialConnectionAuthorizationUrlResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_social_connection_authorization_url

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_social_connection_authorization_url.async_create_social_connection_authorization_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.create_social_connection_authorization_url_response.CreateSocialConnectionAuthorizationUrlResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.create_social_connection_authorization_url_response

            return capo_partnercentral_marketing.types.create_social_connection_authorization_url_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "CreateSocialConnectionAuthorizationUrl", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_marketing.types.create_social_connection_authorization_url_request.CreateSocialConnectionAuthorizationUrlRequest = {
            "catalog": catalog,
            "platform": platform,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_social_connection(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        identifier: "capo_partnercentral_marketing.types.social_connection_identifier.SocialConnectionIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """Revokes and deletes one social connection; other connections on the same platform are untouched. Idempotent: deleting an unknown or already-deleted connection succeeds rather than returning a not-found error.

        Args:
            catalog: Catalog the connection belongs to.
            identifier: Identifier or ARN of the social connection to delete.
            client_token: Idempotency token.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.delete_social_connection_request.DeleteSocialConnectionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_social_connection

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_social_connection.async_delete_social_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteSocialConnection")
        )
        input_: capo_partnercentral_marketing.types.delete_social_connection_request.DeleteSocialConnectionRequest = {
            "catalog": catalog,
            "identifier": identifier,
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

    async def get_campaign_template(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        identifier: "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_template_response.GetCampaignTemplateResponse":
        """Retrieves full detail of one campaign template, including its ordered asset templates with their field schema and layout previews.

        Args:
            catalog: The catalog (AWS or Sandbox).
            identifier: The campaign template's id. A campaign template has no ARN (DG-084).

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a campaign template

            >>> await client.get_campaign_template(catalog='AWS', identifier='tmpl-987xyz654abcd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_template_request.GetCampaignTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_template_response.GetCampaignTemplateResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_template

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_template.async_get_campaign_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_template_response.GetCampaignTemplateResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_template_response

            return capo_partnercentral_marketing.types.get_campaign_template_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetCampaignTemplate", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_template_request.GetCampaignTemplateRequest = {
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

    async def list_social_connections(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        platform: Optional[
            "capo_partnercentral_marketing.types.platform.Platform"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_social_connections_response.ListSocialConnectionsResponse":
        """Lists the partner's social connections, optionally filtered by platform.

        Args:
            catalog: Catalog to list connections from.
            platform: Restrict results to a single social platform.
            max_results: Maximum number of results to return per page.
            next_token: Pagination token from a previous response.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_social_connections_request.ListSocialConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_social_connections_response.ListSocialConnectionsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_social_connections

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_social_connections.async_list_social_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.list_social_connections_response.ListSocialConnectionsResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.list_social_connections_response

            return capo_partnercentral_marketing.types.list_social_connections_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("ListSocialConnections", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.list_social_connections_request.ListSocialConnectionsRequest = {
            "catalog": catalog
        }
        if platform is not None:
            input_["platform"] = platform
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

    async def iter_list_social_connections(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        platform: Optional[
            "capo_partnercentral_marketing.types.platform.Platform"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_marketing.types.social_connection_summary.SocialConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_social_connections(
                catalog,
                config_overrides=config_overrides,
                platform=platform,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Lists the tags applied to a Partner Central Marketing resource.

        Args:
            resource_arn: The ARN of the resource whose tags should be returned.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_partnercentral_marketing.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_campaign_templates(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        search_text: Optional[
            "capo_partnercentral_marketing.types.template_search_text.TemplateSearchText"
        ] = None,
        industry: Optional[
            "capo_partnercentral_marketing.types.industry_filter_list.IndustryFilterList"
        ] = None,
        use_case: Optional[
            "capo_partnercentral_marketing.types.use_case_filter_list.UseCaseFilterList"
        ] = None,
        language: Optional[
            "capo_partnercentral_marketing.types.language_filter_list.LanguageFilterList"
        ] = None,
        aws_services: Optional[
            "capo_partnercentral_marketing.types.aws_service_filter_list.AwsServiceFilterList"
        ] = None,
        customer_segments: Optional[
            "capo_partnercentral_marketing.types.customer_segment_filter_list.CustomerSegmentFilterList"
        ] = None,
        themes: Optional[
            "capo_partnercentral_marketing.types.theme_filter_list.ThemeFilterList"
        ] = None,
        collection: Optional[
            "capo_partnercentral_marketing.types.campaign_template_collection_filter_list.CampaignTemplateCollectionFilterList"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.search_campaign_templates_response.SearchCampaignTemplatesResponse":
        """Searches and browses the AWS-authored campaign template catalog. With no SearchText it returns the whole catalog in the default order, so browse and keyword search share one shape; GetCampaignTemplate reads one template.

        Args:
            catalog: The catalog (AWS or Sandbox). AWS and Sandbox templates may differ.
            search_text: Free-text query matched against the template's name and description. Any word may match, and the last word matches as a prefix when it has 3 or more characters, so `nov` finds Amazon Nova. A template whose name holds the query as a phrase ranks first, then whole-word matches, then prefix-only ones. Omit to browse the whole catalog. Text analysis is derived from each template's own LanguageCode, never from the language filter.
            industry: Restrict to templates in these industries. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match.
            use_case: Restrict to templates with these campaign use cases. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match.
            language: Restrict to templates in these language(s), matched by each template's `LanguageCode`. Values within this member are OR-ed; distinct facet members are AND-ed. Narrows results; it does not reinterpret SearchText.
            aws_services: Restrict to templates promoting these AWS services. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match.
            customer_segments: Restrict to templates for these customer segments. Values within this member are OR-ed; distinct facet members are AND-ed. A template that names no customer segment matches every value.
            themes: Restrict to templates with these themes. Values within this member are OR-ed; distinct facet members are AND-ed. A template that names no theme matches every value.
            collection: Restrict to templates in these collections. Values within this member are OR-ed; distinct facet members are AND-ed. Omit for no restriction; there is no default.
            max_results: Maximum results per page.
            next_token: Pagination token.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Browse the whole catalog

            >>> await client.search_campaign_templates(catalog='AWS')
            Search with a facet filter

            >>> await client.search_campaign_templates(catalog='AWS', search_text='contact center', industry=['TELECOMMUNICATIONS'])
            Browse the Build with AI collection in one language

            >>> await client.search_campaign_templates(catalog='AWS', collection=['BUILD_WITH_AI'], language=['ja'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.search_campaign_templates_request.SearchCampaignTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.search_campaign_templates_response.SearchCampaignTemplatesResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.search_campaign_templates

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.search_campaign_templates.async_search_campaign_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("SearchCampaignTemplates")
        )
        input_: capo_partnercentral_marketing.types.search_campaign_templates_request.SearchCampaignTemplatesRequest = {
            "catalog": catalog
        }
        if search_text is not None:
            input_["search_text"] = search_text
        if industry is not None:
            input_["industry"] = industry
        if use_case is not None:
            input_["use_case"] = use_case
        if language is not None:
            input_["language"] = language
        if aws_services is not None:
            input_["aws_services"] = aws_services
        if customer_segments is not None:
            input_["customer_segments"] = customer_segments
        if themes is not None:
            input_["themes"] = themes
        if collection is not None:
            input_["collection"] = collection
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

    async def iter_search_campaign_templates(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        search_text: Optional[
            "capo_partnercentral_marketing.types.template_search_text.TemplateSearchText"
        ] = None,
        industry: Optional[
            "capo_partnercentral_marketing.types.industry_filter_list.IndustryFilterList"
        ] = None,
        use_case: Optional[
            "capo_partnercentral_marketing.types.use_case_filter_list.UseCaseFilterList"
        ] = None,
        language: Optional[
            "capo_partnercentral_marketing.types.language_filter_list.LanguageFilterList"
        ] = None,
        aws_services: Optional[
            "capo_partnercentral_marketing.types.aws_service_filter_list.AwsServiceFilterList"
        ] = None,
        customer_segments: Optional[
            "capo_partnercentral_marketing.types.customer_segment_filter_list.CustomerSegmentFilterList"
        ] = None,
        themes: Optional[
            "capo_partnercentral_marketing.types.theme_filter_list.ThemeFilterList"
        ] = None,
        collection: Optional[
            "capo_partnercentral_marketing.types.campaign_template_collection_filter_list.CampaignTemplateCollectionFilterList"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_marketing.types.campaign_template_summary.CampaignTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.search_campaign_templates(
                catalog,
                config_overrides=config_overrides,
                search_text=search_text,
                industry=industry,
                use_case=use_case,
                language=language,
                aws_services=aws_services,
                customer_segments=customer_segments,
                themes=themes,
                collection=collection,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("campaign_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_partnercentral_marketing.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> (
        "capo_partnercentral_marketing.types.tag_resource_response.TagResourceResponse"
    ):
        """Adds or replaces tags on a Partner Central Marketing resource. Idempotent: applying a tag that is already present with the same value is a no-op, and supplying a key that already exists replaces its value.

        Args:
            resource_arn: The ARN of the resource to tag.
            tags: The tags to add or replace.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request exceeds a service quota.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.tag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_partnercentral_marketing.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_partnercentral_marketing.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.untag_resource_response.UntagResourceResponse":
        """Removes tags from a Partner Central Marketing resource. Idempotent: removing a key that is not present succeeds.

        Args:
            resource_arn: The ARN of the resource to remove tags from.
            tag_keys: The tag keys to remove. Associated values are removed with them.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.untag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_partnercentral_marketing.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_campaign(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        name: "capo_partnercentral_marketing.types.campaign_name.CampaignName",
        campaign_template_id: "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_marketing.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse":
        """Creates a new marketing campaign. Returns the identity of the new campaign, not the campaign. Growing a response is backward compatible and shrinking one is not, and the caller's next step is a `GetCampaign` anyway — a write that supplies an audience cannot report its scan verdict, because that is decided after it commits.

        Args:
            catalog: The catalog (AWS or Sandbox).
            name: The display name.
            campaign_template_id: The campaign template this campaign draws its assets from. <p>Binds the campaign to a single source template: every asset must come from this template's asset templates, and one from another template is refused at `BatchCreateCampaignAsset`. Immutable once set. Every campaign has one: a campaign's language and its assets' blueprints both come from its template. <p>Templates are AWS-authored and read-only — they are discovered through `SearchCampaignTemplates` and `GetCampaignTemplate`, and there is no create, update or delete operation for one. <p>The template's id only: a campaign template has no ARN (DG-084). The member keeps the `<Resource>Id` name, which is the convention for referencing another resource from a body.
            sender_email: The address every email of this campaign is sent from. <p>Printable ASCII only, with no spaces or line breaks, or field code `PATTERN_MISMATCH`. Then three rules, all checked when the sender is set. Its domain must exactly match, ignoring case, the domain of the partner's alliance lead email in AWS Partner Central (a subdomain does not), or field code `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`. Then, for a sender at example.com, DNS must hold the CNAME `dkim._domainkey.example.com` → `dkim._domainkey.md02.com` (field code `SENDER_DOMAIN_DKIM_MISSING`) and a DMARC record, one TXT `_dmarc.example.com` starting `v=DMARC1` with a `p` of `none`, `quarantine` or `reject` (field code `SENDER_DOMAIN_DMARC_MISSING`). Both DNS codes are reported together when both records are missing. <p>A partner who can't satisfy them can't set a sender, so can't run email campaigns. A shared mail provider's domain, such as gmail.com, can't carry the records. Optional here: a campaign with no sender can be created and edited, but its email assets cannot be activated until one is set.
            privacy_policy_url: The URL of the partner's privacy policy, linked from every email and landing page footer. Optional here: a campaign whose emails or landing pages show it cannot activate them until one is set.
            partner_address: The partner's physical postal address, shown in every email footer and as a landing page's contact line. Optional here: an email that shows it cannot activate until one is set. A landing page that shows it publishes it empty when it is unset, and a document's footer then prints the partner's name alone.
            partner_badge: The partner's badge — a tier or designation badge from AWS Partner Badge Manager — shown in every badge slot of the campaign's emails, landing pages and documents. Optional: until one is set, every badge slot shows the Standalone AWS Partner badge. <p>A PNG or JPEG of at most 2 MB, staged like an asset image and checked the same way: it must have passed the staging scan (`SCAN_REJECTED`, or `SCAN_IN_PROGRESS` while it is pending), and its bytes must be the format its name says (`IMAGE_FORMAT_NOT_SUPPORTED`). Any shape is accepted: a badge is drawn whole, never cropped. Content moderation judges it when an asset that shows it is activated.
            email_target: The campaign's send audience — a CSV of recipient email addresses. <p>The campaign's *target*: who the campaign is sent to, as distinct from a `CampaignAsset`, which is the content that is sent. It sits on the campaign and not on the activation call because a partner assembles it in the same wizard flow that sets the name and the dates — and because attaching it here means it is validated, staged and resolved to a count before anything is activated, rather than at the last click. <p>Required format: a header row naming the email column `Email`, `E-mail`, `Email Address` or `E-mail Address` — compared without case, spaces or punctuation. Other columns are permitted and ignored, and with two email columns the first is used. A file without such a header is refused with field code `EMAIL_COLUMN_MISSING`: the address column is never guessed. The rows reach the delivery platform's importer as the partner wrote them — a partner's audience is never rewritten. <p>At most 5 MB, checked against the object's size before anything is copied, and at most 10,000 distinct addresses, refused with `RECIPIENT_LIST_TOO_LARGE`. A file with no valid address at all is refused with `RECIPIENT_LIST_EMPTY`; otherwise rows without a usable address are not a refusal: they are skipped and counted, and `GetCampaign` reports the counts. Optional here, because a campaign is a container and holds no state to be incomplete in — but an email asset cannot be activated without it, so the requirement moved to the point of activation. <p>Editable at any time, and an edit reaches the delivery platform only when an asset is activated after it. Each email activation loads the audience into a contact list of its own, so an address taken off the file is not sent to by the next activation. <p>The bytes are write-only. No response returns a URL or an `S3Uri` for this file; `GetCampaign` returns the scan verdict, when the list was attached and how its rows resolved, and nothing more.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to: the `Id`s `ListEngagementGroups` returns (AWS Partner Central Selling). 1–10, each named once. <p>Each group is named once: a repeated id is refused with field code `INVALID_VALUE`. Not checked against your groups when saved. StartCampaignAssetActivationTask resolves them to recipients. On a stage that can't resolve groups yet, Start refuses an email while groups are set (`ENGAGEMENT_GROUPS_UNAVAILABLE`), rather than send to `EmailTarget` alone.
            target_audience: Advisory targeting metadata. Refined later, and not validated here.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Not in the past: the campaign completes at the UTC midnight after it (see `CampaignState`). A scheduled send must fall on or before it. Optional here, but required before any asset activates: until it is set, GetCampaign's `ActivationIssues` reports `END_ON_MISSING` and StartCampaignAssetActivationTask refuses (`CAMPAIGN_INCOMPLETE`). Set it with UpdateCampaign.
            client_token: Idempotency token. Same token within 24h returns existing resource.
            tags: Tags to apply at creation. Tag-on-create rather than create-then-tag is a Tagris requirement, not a convenience: it is what lets a tag-based access control policy govern the creation itself. A campaign created untagged and tagged a moment later is briefly outside any such policy. <p>A key beginning `aws:` (any case) is reserved for AWS-applied system tags and is refused with `ValidationException`, as is a key repeated in the list; nothing is created. The tags are recorded before the campaign is written, so a create that cannot record them fails and creates nothing. A retry with the same `ClientToken` returns the campaign the first attempt created and does not re-apply tags — use `TagResource` to change them afterwards. `ListTagsForResource` returns them.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request exceeds a service quota.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a campaign

            >>> await client.create_campaign(catalog='AWS', name='Q4 GenAI Campaign', campaign_template_id='tmpl-a1b2c3d4e5f6g', total_budget={'Amount': '25000.00', 'CurrencyCode': 'USD'}, start_on='2026-11-01', end_on='2026-12-31')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.create_campaign_request

            return capo_partnercentral_marketing.types.create_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest = {
            "catalog": catalog,
            "name": name,
            "campaign_template_id": campaign_template_id,
        }
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on
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

    async def get_campaign(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> (
        "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
    ):
        """Retrieves a campaign by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a campaign

            >>> await client.get_campaign(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign.async_get_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_response

            return capo_partnercentral_marketing.types.get_campaign_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetCampaign", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_campaign(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        social_connections: Optional[
            "capo_partnercentral_marketing.types.campaign_social_connections.CampaignSocialConnections"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse":
        """Edits a campaign in place. Partial update: an omitted field is left unchanged, which is the standard meaning of an `Update` verb — a full replacement would be a `Put`. Change-only, with no way to clear a field back to empty, because the campaign's file members cannot round-trip: they are written as an `s3://` reference and read back as a URL or as metadata, so a replacement payload could not resend an unchanged recipient list without re-uploading it. Refused while an activation task runs (`CAMPAIGN_ACTIVATION_IN_PROGRESS`) and once the campaign is completed (`CAMPAIGN_COMPLETED`, the UTC date is after its `EndOn`). Last-writer-wins, with no concurrency token: this is low-contention metadata owned by one partner.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            name: The display name.
            sender_email: Sets or replaces the address the campaign's emails are sent from. Checked by the same three rules as on `CreateCampaign`, with the same codes, but only when it differs, ignoring case, from the stored sender: re-sending the stored one is not checked, and `StartCampaignAssetActivationTask` re-checks it before an email activates. <p>Replaces, never clears: like every member of this operation, an omitted value leaves the sender as it was, and there is no way to remove one once set.
            privacy_policy_url: Sets or replaces the URL of the partner's privacy policy. Replaces, never clears.
            partner_address: Sets or replaces the partner's postal address. Replaces, never clears.
            partner_badge: Sets or replaces the partner's badge, checked exactly as on `CreateCampaign`. Replaces, never clears: upload the Standalone AWS Partner badge to show it again. The badge an asset already published keeps showing on it until that asset is activated again.
            email_target: Replaces the campaign's attached recipient list. <p>The referenced object is copied and pinned again on every call that supplies it, so the pinned copy always reflects the *last* `UpdateCampaign` that named one. Editing the source object in your own bucket without calling this operation again has no effect. <p>Replaces, never detaches: a partner can swap the list but cannot remove it.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to (see `CreateCampaign`). Replaces the stored list; never clears it. <p>As on `CreateCampaign`: each group once (`INVALID_VALUE` otherwise), not checked against your groups when saved, and resolved at Start where the stage can (`ENGAGEMENT_GROUPS_UNAVAILABLE` where it can't).
            social_connections: Sets the account the campaign's social posts publish from, per platform. Each platform named replaces that platform's choice; a platform not named keeps its own. Replaces, never clears. <p>Not checked against your connections here: a connection can be deleted at any time, so the activation checks the choice. See `Campaign$SocialConnections`.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            target_audience: Target audience configuration.
            client_token: Idempotency token. Accepted and not stored: this is a change-only partial update with last-writer-wins, so re-applying the same call produces the same result and the same response. There is nothing a replay cache would protect.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Editable only while the campaign is open, like everything else here: once the stored `EndOn` has passed the campaign is completed and this update is refused (`CAMPAIGN_COMPLETED`). Refused with `ValidationException` (`INVALID_VALUE`) when it is in the past, or earlier than the day of a scheduled send on one of the campaign's assets: move or cancel that send first. Setting it to today ends the campaign at the next UTC midnight.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename a campaign and raise its budget

            >>> await client.update_campaign(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', name='Q4 GenAI Campaign (EMEA)', total_budget={'Amount': '40000.00', 'CurrencyCode': 'USD'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign.async_update_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_request

            return capo_partnercentral_marketing.types.update_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }
        if name is not None:
            input_["name"] = name
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if social_connections is not None:
            input_["social_connections"] = social_connections
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_campaign(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign, its assets and their stored files. A hard delete with no undo: the campaign leaves ListCampaigns and every read of it returns ResourceNotFoundException. Its tags are removed with it. Refused with ConflictException while the campaign has a live asset (`CAMPAIGN_HAS_ACTIVE_ASSETS`), because deleting the record would orphan what the delivery platform still serves or sends: deactivate those assets first. Also refused while an activation task is running (`CAMPAIGN_ACTIVATION_IN_PROGRESS`). A completed campaign can be deleted. Idempotent in effect: deleting a campaign that is already gone returns ResourceNotFoundException, and nothing is left behind by a retry.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign to delete.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a campaign

            >>> await client.delete_campaign(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteCampaign")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_campaigns(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        campaign_identifiers: Optional[
            "capo_partnercentral_marketing.types.campaign_identifier_list.CampaignIdentifierList"
        ] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        states: Optional[
            "capo_partnercentral_marketing.types.campaign_state_list.CampaignStateList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_marketing.types.campaign_sort.CampaignSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse":
        """Lists campaigns with optional filters and pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifiers: Only these campaigns, each named by its id or its campaign ARN. A campaign that does not exist, was deleted, or whose ARN names another account or catalog is left out rather than refused.
            name: Only campaigns whose name contains this, compared case-insensitively.
            states: Only campaigns in one of these states.
            sort: The order of the results. Default: `CREATED_AT`, `DESCENDING`.
            max_results: Maximum results per page.
            next_token: Pagination token. Bound to the filters and sort it was issued for: a request that changes `CampaignIdentifiers`, `Name`, `States` or `Sort` between pages is refused with `ValidationException`. `MaxResults` may change.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List campaigns

            >>> await client.list_campaigns(catalog='AWS')
            Name the campaigns a page links to

            >>> await client.list_campaigns(catalog='AWS', campaign_identifiers=['arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/campaign/camp-5Hq2m8x4k1p9w', 'camp-8Rt3w6y1n4b2v'])
            Search active campaigns by name, by launch date

            >>> await client.list_campaigns(catalog='AWS', name='genai', states=['ACTIVE'], sort={'SortBy': 'START_ON', 'SortOrder': 'ASCENDING'}, max_results=20)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns.async_list_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCampaigns")
        )
        input_: capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest = {
            "catalog": catalog
        }
        if campaign_identifiers is not None:
            input_["campaign_identifiers"] = campaign_identifiers
        if name is not None:
            input_["name"] = name
        if states is not None:
            input_["states"] = states
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_list_campaigns(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        campaign_identifiers: Optional[
            "capo_partnercentral_marketing.types.campaign_identifier_list.CampaignIdentifierList"
        ] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        states: Optional[
            "capo_partnercentral_marketing.types.campaign_state_list.CampaignStateList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_marketing.types.campaign_sort.CampaignSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_marketing.types.campaign_summary.CampaignSummary]":
        _token = next_token
        while True:
            _response = await self.list_campaigns(
                catalog,
                config_overrides=config_overrides,
                campaign_identifiers=campaign_identifiers,
                name=name,
                states=states,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_create_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        entries: "capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.BatchCreateCampaignAssetEntries",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse":
        """Instantiates one or more of the campaign template's blueprints as assets of this campaign. The only asset-create operation: DG-038 deleted the singular CreateCampaignAsset, and AWS Batch Operations makes exposing a singular alongside a batch optional ("which MAY actually be exposed in addition"). It also replaced kit instantiation -- CreateCampaign creates zero assets, so this is the only path by which an asset comes into existence. Errors here are whole-request only, and nothing is written when one is thrown. Per-entry failures ride in the response's `Errors` list with a 200. ServiceQuotaExceededException is deliberately absent: a campaign holds at most one asset per blueprint (I-15), so the ceiling is the size of the bound kit and a request of unique valid entries cannot exceed it.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            entries: The blueprints to instantiate, one entry each.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Instantiate two of the kit's blueprints

            >>> await client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta0000000lp01'}])
            A partial batch: one entry names a blueprint the campaign's template does not carry

            >>> await client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta00000absent'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset.async_batch_create_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("BatchCreateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "entries": entries,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deactivate_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse":
        """Stops a live campaign asset: an email's scheduled send is withdrawn, a social post is removed before it publishes. On a completed campaign, it also removes a published document, banner or landing page. Synchronous, and safe to repeat. Does not delete the asset record, so a stopped email or social post can be started again. Not every asset can be stopped, and the reasons differ in kind. An email that has begun sending **cannot** be recalled: the send is gone. A document, a banner or a landing page is **refused** with `ASSET_NOT_DEACTIVATABLE` until the campaign has completed (the UTC date is after its `EndOn`). Until then the partner fixes one in place by updating it and activating it again, which keeps its URL, so every email that already linked to it keeps working. Once the campaign has completed, the removal is permanent, because a completed campaign can't activate anything again: - A document's published PDF is deleted. Its URL stops serving within about a minute (the CDN revalidates), and `PublicUrl` is no longer returned. Anything that linked to it, such as a landing page's download button or a sent email, reaches an error page. The export still contains the document. - A banner's or landing page's published object is taken down at the delivery platform, and the images the partner put on it are deleted. A landing page stops capturing leads, and its `PublicUrl` is no longer returned. A partner site that embedded a banner shows nothing there. The platform's own CDN can keep serving a copy a visitor already cached, which collects nothing. A landing page and a document it links to can be removed in either order.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset.async_deactivate_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeactivateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign asset.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an asset

            >>> await client.delete_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset.async_delete_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse":
        """Retrieves an asset by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an asset

            >>> await client.get_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset.async_get_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_asset_response

            return capo_partnercentral_marketing.types.get_campaign_asset_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetCampaignAsset", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse":
        """Reads a campaign's current activation task. Keyed on the **campaign**, with no task identifier, because a campaign has at most one activation task: runs are serialised, so there is no collection to address into. The caller always holds the task id anyway, because Start returned it — the id is a correlation value, not an address. Returns the campaign's most recent task. A new task overwrites the previous one, so this is not a history: the durable per-asset record is on the assets themselves. Returns ResourceNotFoundException when the campaign has never had a task, or when its last one has expired.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose current task to read. This addresses the task, and also authorizes the call.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Read a finished task where one asset failed

            >>> await client.get_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task.async_get_campaign_asset_activation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_export_task_identifier: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse":
        """Retrieves a campaign asset export task by its identifier, reporting its status and, when the task is COMPLETED, a freshly minted short-lived presigned URL for downloading the ZIP archive. The download URL is minted on each call and is valid for at most 15 minutes; clients should download promptly rather than caching it. When the task has FAILED, FailureReason explains why. Poll this operation (roughly every 2-5 seconds) until the task reaches a terminal state.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign that owns the export task. Accepts the campaign id or ARN. Required so the read is authorized on campaign/{CampaignId}; the task must belong to this campaign or the request resolves to not-found.
            campaign_asset_export_task_identifier: The export task to retrieve: the `Id` StartCampaignAssetExportTask returned (`etsk-…`). An id only. An export task has no ARN: none is returned, recorded or authorized on (the read authorizes on its campaign), so there is no ARN to accept (DG-063 D-35).

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task.async_get_campaign_asset_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_export_task_identifier": campaign_asset_export_task_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_campaign_assets(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse":
        """Lists assets for a campaign with pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            max_results: Maximum results per page.
            next_token: Pagination token.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assets for a campaign

            >>> await client.list_campaign_assets(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets.async_list_campaign_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCampaignAssets")
        )
        input_: capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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

    async def iter_list_campaign_assets(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_marketing.types.campaign_asset_summary.CampaignAssetSummary]":
        _token = next_token
        while True:
            _response = await self.list_campaign_assets(
                catalog,
                campaign_identifier,
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

    async def start_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifiers: "capo_partnercentral_marketing.types.campaign_asset_identifiers.CampaignAssetIdentifiers",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse":
        """Activates 1–25 of a campaign's assets as one ordered unit, and returns a task to poll. Takes a **list** because the service owns the ordering. Assets link to one another by URL — an email's call-to-action carries the landing page's URL, the landing page's download field carries the document's — and a URL does not exist until the asset it points at is activated. Those edges are derived by the service from the campaign's pinned template, so reconstructing and topologically sorting them is work the service has already done, and getting it wrong arms an email with a dead link. Name every asset you want live and the service sequences them; "activate everything" is the list with every id in it, which ListCampaignAssets already gave you. Asynchronous, because activating an asset installs or arms behaviour that runs later and an email activation bulk-loads its audience into the delivery platform. Everything decidable **without** a write to the delivery platform is evaluated before this returns; everything else lands on the task. A refusal that applies to one asset does not fail the request: that asset is on the task already FAILED, with its reason, and the rest run. A refusal that applies to the whole request — a malformed list, an unknown campaign, another task already running on this campaign, this service's service-linked role being deleted (ConflictException `SERVICE_LINKED_ROLE_DELETION_IN_PROGRESS`), a campaign setting an asset in the request needs (ValidationException `CAMPAIGN_INCOMPLETE`), a campaign sender that no longer passes `CreateCampaign`'s sender rules while the request names an email (ValidationException with no `FieldList`, whose message ends with one `Reason: <code>` token per failed rule: `PATTERN_MISMATCH`, `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`, or `SENDER_DOMAIN_DKIM_MISSING` and/or `SENDER_DOMAIN_DMARC_MISSING`) — is thrown, and nothing starts. One task runs on a campaign at a time. A second concurrent call is refused with ConflictException / CAMPAIGN_ACTIVATION_IN_PROGRESS, whose `ResourceId` names the task already holding the campaign. Two tasks over *disjoint* asset sets are refused too: the guard is deliberately campaign-wide, because overlapping runs made the per-asset status misleading rather than merely contended.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier, which also authorizes the call.
            campaign_asset_identifiers: The assets to activate, in any order — the service derives the dependency order and ignores the order given here.
            client_token: Idempotency token. Two requests carrying the same token are one request, and the second returns the first one's task rather than starting a second. The deduplication window is the **life of the task record**, not a fixed number of hours: replaying a token after the task has expired starts a new task. Stated because a caller would otherwise assume the usual few-hour guarantee.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Activate a whole campaign kit

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Some assets refused, the rest started anyway

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Every asset refused, so the task is FAILED at once

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-2k7m4p9x1c6qd'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task.async_start_campaign_asset_activation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifiers": campaign_asset_identifiers,
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

    async def start_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse":
        """Starts an asynchronous task that packages a campaign's assets into a single downloadable ZIP archive. Fire-and-return: the campaign is validated (it must exist and not be cancelled), a task record is persisted, an asynchronous execution is started, and the task id is returned with status IN_PROGRESS. This operation does not inspect assets — all resolution, exclusion, and failure are determined by the execution and surfaced only by GetCampaignAssetExportTask. Every campaign is exportable, including one never activated, because renderable assets are composed on demand at export time rather than requiring finished, launched deliverables.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose assets are exported. Accepts the campaign id or ARN.
            client_token: Idempotency token. Two requests carrying the same token within the dedup window are one request and return the same task id.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task.async_start_campaign_asset_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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

    async def update_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        field_values: Optional[
            "capo_partnercentral_marketing.types.field_value_input_list.FieldValueInputList"
        ] = None,
        layout: Optional[
            "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
        ] = None,
        send_mode: Optional[
            "capo_partnercentral_marketing.types.send_mode.SendMode"
        ] = None,
        scheduled_send_at: Optional[
            "capo_partnercentral_marketing.types.timestamp.Timestamp"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse":
        """Updates an asset's field values, layout or send time. Refused with `ConflictException` while the campaign's running activation task still owns the asset (`ASSET_START_IN_PROGRESS`), and for a live email or social post (`ASSET_ALREADY_ACTIVE`): deactivate it first.

                Args:
                    catalog: The catalog (AWS or Sandbox).
                    campaign_identifier: The campaign identifier.
                    campaign_asset_identifier: The asset identifier.
                    field_values: Value-only updates to the asset's pinned template fields, keyed by FieldId. The field schema (labels, descriptions, constraints, placeholders, image defaults) is service-owned and pinned at instantiation, so clients send only the values they are changing. Fields omitted keep their stored values; send the entry with `Value` omitted to clear one. Named `FieldValues` to match the member it edits on `CampaignAsset`, which is the same concept read back. It was `templateFieldUpdates`; the two names for one concept were the defect, not the length.
                    layout: Selects a multi-layout asset's layout: one of the values in `CampaignAsset.layout.options`. PATCH: omitted leaves the selection unchanged, and there is no way to clear it. A value that is not one of the asset's options — or any value on a single-layout asset — is a plain `ValidationException`, and nothing in the call is applied. Every pinned field stays writable whichever layout is selected.
                    send_mode: When a **sendable** asset (`EMAIL`, `SOCIAL_POST`) sends: on activation, or at `ScheduledSendAt`. A mode beside a value rather than a union, on purpose: `ScheduledSendAt` stays a plain `Timestamp`, and the precedent is EventBridge Scheduler's `FlexibleTimeWindow { Mode, MaximumWindowInMinutes }`. The pair is checked as one, and a request where they disagree is refused with `ValidationException` (`INVALID_VALUE`, naming the member) and applies nothing: - `SCHEDULED` requires `ScheduledSendAt`; a reschedule resends `SCHEDULED` with the new time; - `ON_ACTIVATION` forbids `ScheduledSendAt`, and drops any time already stored; - `ScheduledSendAt` without `SendMode` is refused. PATCH: omitted leaves both unchanged. Until a mode is chosen the asset reports `SEND_MODE_MISSING` and does not activate: no default, because an unchosen send mails the real audience. Rejected with `ValidationException` (`NOT_SUPPORTED_FOR_CATEGORY`) for a category that has no send (`LANDING_PAGE`, `DOCUMENT`, `BANNER_AD`). Like every other edit, it reaches the delivery platform at the asset's next activation, and a live email or social post refuses it (`ASSET_ALREADY_ACTIVE`): deactivate first.
                    scheduled_send_at: The send time, with `SendMode: SCHEDULED` and only then. See `SendMode`. Must be at least an hour out (`SEND_WINDOW_TOO_SOON`), unless it is the time already stored: resending the stored mode and time changes nothing and is accepted, so a form that always resubmits does not trip the window. Must also fall on or before the campaign's `EndOn` (by the end of that UTC day): refused with `ValidationException` (`INVALID_VALUE`) otherwise, so nothing is scheduled to send after the campaign completes. Was `scheduleDate`, a `YYYY-MM-DD` string. Retyped because a date alone cannot express a send *time*, which is the whole point of a schedule — and because the resource already spelled the same concept `ScheduledSendAt` on the activation responses. Two spellings of one concept on one resource was the defect.
                    client_token: Idempotency token. Retry-safety only — this is **not** a concurrency token, and sequential edits to one field are last-writer-wins.

                Raises:
                    capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
                    capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
                    capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
                    capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
                    capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
                    capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
                    capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    Update asset content

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'Subject', 'Value': {'Text': 'New subject line'}}])
                    Reschedule a sendable asset

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', send_mode='SCHEDULED', scheduled_send_at=1793491200, client_token='f2a7c1e4-9b3d-4a51-8e6f-0c2d5b8a7e13')
                    Copy an image from a previous campaign's asset
                    The image already stored on another of your assets is copied into this field. It is checked
        against this field's constraints and not scanned again. The call also needs
        partnercentral:GetCampaignAsset on the source campaign.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'CampaignAssetImage': {'CampaignIdentifier': 'camp-2Lp7d9f3j6s1z', 'CampaignAssetIdentifier': 'ast-0f9e8d7c6b5a2', 'FieldId': 'HeaderImage'}}}])
                    Use a suggested image from Build with AI
                    The URL Build with AI returned for a suggested image is sent unchanged as imageReference. The
        image is copied into this asset and not scanned. Any other URL is refused.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 'https://d111111abcdef8.cloudfront.net/suggested-image-url-from-build-with-ai.jpg'}}])
                    An update refused for two fields at once
                    Every failed field is reported in one refusal, and nothing applies — a declined image and an
        over-long headline arrive together in `fieldList`, each with its own `code`. This replaced a
        read-path `fileDetails[]` report (DG-040 Decision 11), so a partner handles image and text
        failures the same way.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 's3://staging-bucket/123456789012/hero.png?versionId=v1'}}, {'FieldId': 'Headline', 'Value': {'Text': 'This headline is far longer than the field allows'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset.async_update_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_asset_request

            return capo_partnercentral_marketing.types.update_campaign_asset_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaignAsset", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }
        if field_values is not None:
            input_["field_values"] = field_values
        if layout is not None:
            input_["layout"] = layout
        if send_mode is not None:
            input_["send_mode"] = send_mode
        if scheduled_send_at is not None:
            input_["scheduled_send_at"] = scheduled_send_at
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
