"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EC2DNSGlobalResolverCustomerAPI``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._auth._identity import Credentials
from capo_route53globalresolver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53globalresolver._auth._zapros_handler import AuthMiddleware
from capo_route53globalresolver._pagination import resolve_path as _resolve_path
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_source import (
    AsyncAccessSource,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_token import (
    AsyncAccessToken,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.dns_view import (
    AsyncDNSView,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_domain_list import (
    AsyncFirewallDomainList,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_rule import (
    AsyncFirewallRule,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.global_resolver import (
    AsyncGlobalResolver,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.hosted_zone_association import (
    AsyncHostedZoneAssociation,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.managed_firewall_domain_list import (
    AsyncManagedFirewallDomainList,
)
from capo_route53globalresolver._services._aws_config import aaws_config
from capo_route53globalresolver._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.access_sources_item
    import capo_route53globalresolver.types.access_token_item
    import capo_route53globalresolver.types.associate_hosted_zone_input
    import capo_route53globalresolver.types.associate_hosted_zone_output
    import capo_route53globalresolver.types.batch_create_firewall_rule_input
    import capo_route53globalresolver.types.batch_create_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_create_firewall_rule_output
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_delete_firewall_rule_output
    import capo_route53globalresolver.types.batch_update_firewall_rule_input
    import capo_route53globalresolver.types.batch_update_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_update_firewall_rule_output
    import capo_route53globalresolver.types.block_override_dns_query_type
    import capo_route53globalresolver.types.block_override_ttl
    import capo_route53globalresolver.types.cidr
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.confidence_threshold
    import capo_route53globalresolver.types.create_access_source_input
    import capo_route53globalresolver.types.create_access_source_output
    import capo_route53globalresolver.types.create_access_token_input
    import capo_route53globalresolver.types.create_access_token_output
    import capo_route53globalresolver.types.create_dns_view_input
    import capo_route53globalresolver.types.create_dns_view_output
    import capo_route53globalresolver.types.create_firewall_domain_list_input
    import capo_route53globalresolver.types.create_firewall_domain_list_output
    import capo_route53globalresolver.types.create_firewall_rule_input
    import capo_route53globalresolver.types.create_firewall_rule_output
    import capo_route53globalresolver.types.create_global_resolver_input
    import capo_route53globalresolver.types.create_global_resolver_output
    import capo_route53globalresolver.types.delete_access_source_input
    import capo_route53globalresolver.types.delete_access_source_output
    import capo_route53globalresolver.types.delete_access_token_input
    import capo_route53globalresolver.types.delete_access_token_output
    import capo_route53globalresolver.types.delete_dns_view_input
    import capo_route53globalresolver.types.delete_dns_view_output
    import capo_route53globalresolver.types.delete_firewall_domain_list_input
    import capo_route53globalresolver.types.delete_firewall_domain_list_output
    import capo_route53globalresolver.types.delete_firewall_rule_input
    import capo_route53globalresolver.types.delete_firewall_rule_output
    import capo_route53globalresolver.types.delete_global_resolver_input
    import capo_route53globalresolver.types.delete_global_resolver_output
    import capo_route53globalresolver.types.disable_dns_view_input
    import capo_route53globalresolver.types.disable_dns_view_output
    import capo_route53globalresolver.types.disassociate_hosted_zone_input
    import capo_route53globalresolver.types.disassociate_hosted_zone_output
    import capo_route53globalresolver.types.dns_advanced_protection
    import capo_route53globalresolver.types.dns_protocol
    import capo_route53globalresolver.types.dns_query_type
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.dns_view_summary
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.domains
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.enable_dns_view_input
    import capo_route53globalresolver.types.enable_dns_view_output
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.firewall_block_response
    import capo_route53globalresolver.types.firewall_domain_lists_item
    import capo_route53globalresolver.types.firewall_rule_action
    import capo_route53globalresolver.types.firewall_rule_priority
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.firewall_rules_item
    import capo_route53globalresolver.types.get_access_source_input
    import capo_route53globalresolver.types.get_access_source_output
    import capo_route53globalresolver.types.get_access_token_input
    import capo_route53globalresolver.types.get_access_token_output
    import capo_route53globalresolver.types.get_dns_view_input
    import capo_route53globalresolver.types.get_dns_view_output
    import capo_route53globalresolver.types.get_firewall_domain_list_input
    import capo_route53globalresolver.types.get_firewall_domain_list_output
    import capo_route53globalresolver.types.get_firewall_rule_input
    import capo_route53globalresolver.types.get_firewall_rule_output
    import capo_route53globalresolver.types.get_global_resolver_input
    import capo_route53globalresolver.types.get_global_resolver_output
    import capo_route53globalresolver.types.get_hosted_zone_association_input
    import capo_route53globalresolver.types.get_hosted_zone_association_output
    import capo_route53globalresolver.types.get_managed_firewall_domain_list_input
    import capo_route53globalresolver.types.get_managed_firewall_domain_list_output
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.global_resolvers_item
    import capo_route53globalresolver.types.hosted_zone_association_summary
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.import_firewall_domains_input
    import capo_route53globalresolver.types.import_firewall_domains_output
    import capo_route53globalresolver.types.ip_address_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.list_access_sources_input
    import capo_route53globalresolver.types.list_access_sources_output
    import capo_route53globalresolver.types.list_access_tokens_input
    import capo_route53globalresolver.types.list_access_tokens_output
    import capo_route53globalresolver.types.list_dns_views_input
    import capo_route53globalresolver.types.list_dns_views_output
    import capo_route53globalresolver.types.list_firewall_domain_lists_input
    import capo_route53globalresolver.types.list_firewall_domain_lists_output
    import capo_route53globalresolver.types.list_firewall_domains_input
    import capo_route53globalresolver.types.list_firewall_domains_output
    import capo_route53globalresolver.types.list_firewall_rules_input
    import capo_route53globalresolver.types.list_firewall_rules_output
    import capo_route53globalresolver.types.list_global_resolvers_input
    import capo_route53globalresolver.types.list_global_resolvers_output
    import capo_route53globalresolver.types.list_hosted_zone_associations_input
    import capo_route53globalresolver.types.list_hosted_zone_associations_output
    import capo_route53globalresolver.types.list_managed_firewall_domain_lists_input
    import capo_route53globalresolver.types.list_managed_firewall_domain_lists_output
    import capo_route53globalresolver.types.list_shared_dns_views_input
    import capo_route53globalresolver.types.list_shared_dns_views_output
    import capo_route53globalresolver.types.list_tags_for_resource_request
    import capo_route53globalresolver.types.list_tags_for_resource_response
    import capo_route53globalresolver.types.managed_firewall_domain_lists_item
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.shared_dns_view_summary
    import capo_route53globalresolver.types.tag_keys
    import capo_route53globalresolver.types.tag_resource_request
    import capo_route53globalresolver.types.tag_resource_response
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.untag_resource_request
    import capo_route53globalresolver.types.untag_resource_response
    import capo_route53globalresolver.types.update_access_source_input
    import capo_route53globalresolver.types.update_access_source_output
    import capo_route53globalresolver.types.update_access_token_input
    import capo_route53globalresolver.types.update_access_token_output
    import capo_route53globalresolver.types.update_dns_view_input
    import capo_route53globalresolver.types.update_dns_view_output
    import capo_route53globalresolver.types.update_firewall_domains_input
    import capo_route53globalresolver.types.update_firewall_domains_output
    import capo_route53globalresolver.types.update_firewall_rule_input
    import capo_route53globalresolver.types.update_firewall_rule_output
    import capo_route53globalresolver.types.update_global_resolver_input
    import capo_route53globalresolver.types.update_global_resolver_output
    import capo_route53globalresolver.types.update_hosted_zone_association_input
    import capo_route53globalresolver.types.update_hosted_zone_association_output


class AsyncRoute53GlobalResolverClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRoute53GlobalResolverClient:
    """A client for the ``Route53GlobalResolver`` service.

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
        self._config = AsyncRoute53GlobalResolverClientConfig(
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
        self.access_source = AsyncAccessSource(self)
        self.access_token = AsyncAccessToken(self)
        self.dns_view = AsyncDNSView(self)
        self.firewall_domain_list = AsyncFirewallDomainList(self)
        self.firewall_rule = AsyncFirewallRule(self)
        self.global_resolver = AsyncGlobalResolver(self)
        self.hosted_zone_association = AsyncHostedZoneAssociation(self)
        self.managed_firewall_domain_list = AsyncManagedFirewallDomainList(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53GlobalResolverClientConfig = config_overrides or {}
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

    async def disassociate_hosted_zone(
        self,
        hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput":
        """<p>Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to disassociate.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource to disassociate the hosted zone from.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone.async_disassociate_hosted_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput = {
            "hosted_zone_id": hosted_zone_id,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_shared_dns_views(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_shared_dns_views_output.ListSharedDNSViewsOutput":
        """<p>Lists the DNS views that have been shared with your Amazon Web Services account through Amazon Web Services Resource Access Manager (Amazon Web Services RAM), with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_shared_dns_views_input.ListSharedDNSViewsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_shared_dns_views_output.ListSharedDNSViewsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_shared_dns_views

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_shared_dns_views.async_list_shared_dns_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_shared_dns_views_input.ListSharedDNSViewsInput = {}
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

    async def iter_list_shared_dns_views(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.shared_dns_view_summary.SharedDNSViewSummary]":
        _token = next_token
        while True:
            _response = await self.list_shared_dns_views(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dns_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        tags: "capo_route53globalresolver.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a Route 53 Global Resolver resource. Tags are key-value pairs that help you organize and identify your resources.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to be tagged.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        tag_keys: "capo_route53globalresolver.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes tags from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys associated with the resource.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_access_source(
        self,
        cidr: "capo_route53globalresolver.types.cidr.Cidr",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput":
        """<p>Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            cidr: <p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            ip_address_type: <p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>
            name: <p>A descriptive name for the access source.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this access source.</p>
            protocol: <p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>
            tags: <p>Tags to associate with the access source.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateAccessSource example

            >>> await client.create_access_source(cidr='85.90.183.3/30', client_token='9fas9-9usdfa-xbi8-kco', dns_view_id='dnsv-123456789', ip_address_type='IPV4', name='My Access Source', protocol='DO53', tags={'Key1': 'Value1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source.async_create_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput = {
            "cidr": cidr,
            "dns_view_id": dns_view_id,
            "protocol": protocol,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_source(
        self,
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput":
        """<p>Retrieves information about an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to retrieve.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source.async_get_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput = {
            "access_source_id": access_source_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_access_source(
        self,
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        cidr: Optional["capo_route53globalresolver.types.cidr.Cidr"] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        protocol: Optional[
            "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput":
        """<p>Updates the configuration of an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to update.</p>
            cidr: <p>The CIDR block for the access source.</p>
            ip_address_type: <p>The IP address type for the access source.</p>
            name: <p>The name of the access source.</p>
            protocol: <p>The protocol for the access source.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source.async_update_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput = {
            "access_source_id": access_source_id
        }
        if cidr is not None:
            input_["cidr"] = cidr
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if protocol is not None:
            input_["protocol"] = protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_source(
        self,
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput":
        """<p>Deletes an access source. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source.async_delete_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput = {
            "access_source_id": access_source_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_access_sources(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput":
        """<p>Lists all access sources with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources.async_list_access_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_access_sources(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.access_sources_item.AccessSourcesItem]":
        _token = next_token
        while True:
            _response = await self.list_access_sources(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("access_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_access_token(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        expires_at: Optional[
            "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput":
        """<p>Creates an access token for a DNS view. Access tokens provide token-based authentication for DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) connections to the Route 53 Global Resolver.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this token.</p>
            expires_at: <p>The date and time when the token expires. Tokens can have a minimum expiration of 30 days and maximum of 365 days from creation.</p>
            name: <p>A descriptive name for the access token.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_access_token_output.CreateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_token.async_create_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_access_token_input.CreateAccessTokenInput = {
            "dns_view_id": dns_view_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_token(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
    ):
        """<p>Retrieves information about an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>ID of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_access_token_output.GetAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_token.async_get_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_access_token_input.GetAccessTokenInput = {
            "access_token_id": access_token_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_access_token(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name_short.ResourceNameShort",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput":
        """<p>Updates the configuration of an access token.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The ID of the token.</p>
            name: <p>The new name of the token.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_access_token_output.UpdateAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_token.async_update_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_access_token_input.UpdateAccessTokenInput = {
            "access_token_id": access_token_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_token(
        self,
        access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput":
        """<p>Deletes an access token. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_token_id: <p>The unique identifier of the access token to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_access_token_output.DeleteAccessTokenOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_token.async_delete_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_access_token_input.DeleteAccessTokenInput = {
            "access_token_id": access_token_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_access_tokens(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput":
        """<p>Lists all access tokens for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>The ID of the DNS view to list the tokens for.</p>
            filters: <p>Filtering parameters.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_access_tokens_output.ListAccessTokensOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_tokens.async_list_access_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_access_tokens_input.ListAccessTokensInput = {
            "dns_view_id": dns_view_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_access_tokens(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.access_token_item.AccessTokenItem]":
        _token = next_token
        while True:
            _response = await self.list_access_tokens(
                dns_view_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("access_tokens",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_dns_view(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        dnssec_validation: Optional[
            "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput":
        """<p>Creates a DNS view within a Route 53 Global Resolver. A DNS view models end users, user groups, networks, and devices, and serves as a parent resource that holds configurations controlling access, authorization, DNS firewall rules, and forwarding rules.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to associate with this DNS view.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            name: <p>A descriptive name for the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.</p>
            firewall_rules_fail_open: <p>Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.</p>
            description: <p>An optional description for the DNS view.</p>
            tags: <p>Tags to associate with the DNS view.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view.async_create_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if dnssec_validation is not None:
            input_["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input_["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input_["firewall_rules_fail_open"] = firewall_rules_fail_open
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dns_view(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput":
        """<p>Retrieves information about a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The ID of the DNS view to retrieve information about.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_dns_view_input.GetDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view.async_get_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_dns_view_input.GetDNSViewInput = {
            "dns_view_id": dns_view_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_dns_view(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dnssec_validation: Optional[
            "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput":
        """<p>Updates the configuration of a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to update.</p>
            name: <p>The name of the DNS view.</p>
            description: <p>A description of the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for the DNS view.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for the DNS view.</p>
            firewall_rules_fail_open: <p>Whether firewall rules should fail open when they cannot be evaluated.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view.async_update_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput = {
            "dns_view_id": dns_view_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if dnssec_validation is not None:
            input_["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input_["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input_["firewall_rules_fail_open"] = firewall_rules_fail_open

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dns_view(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput":
        """<p>Deletes a DNS view. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view.async_delete_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput = {
            "dns_view_id": dns_view_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_dns_views(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput":
        """<p>Lists all DNS views for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The Global Resolver ID.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views.async_list_dns_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput = {
            "global_resolver_id": global_resolver_id
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

    async def iter_list_dns_views(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.dns_view_summary.DNSViewSummary]":
        _token = next_token
        while True:
            _response = await self.list_dns_views(
                global_resolver_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dns_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_dns_view(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput"
    ):
        """<p>Disables a DNS view, preventing it from serving DNS queries.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to disable.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view.async_disable_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput = {
            "dns_view_id": dns_view_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_dns_view(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput":
        """<p>Enables a disabled DNS view, allowing it to serve DNS queries again.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to enable.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view.async_enable_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput = {
            "dns_view_id": dns_view_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_firewall_domain_list(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput":
        """<p>Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>
            description: <p>An optional description for the firewall domain list.</p>
            name: <p>A descriptive name for the firewall domain list.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list.async_create_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_domain_list(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput":
        """<p>Retrieves information about a firewall domain list.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>ID of the domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list.async_get_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_firewall_domain_list(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput":
        """<p>Deletes a firewall domain list. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>The unique identifier of the firewall domain list to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list.async_delete_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_firewall_domain_lists(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        global_resolver_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput":
        """<p>Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists.async_list_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if global_resolver_id is not None:
            input_["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_firewall_domain_lists(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        global_resolver_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.firewall_domain_lists_item.FirewallDomainListsItem]":
        _token = next_token
        while True:
            _response = await self.list_firewall_domain_lists(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                global_resolver_id=global_resolver_id,
            )
            _page = _resolve_path(_response, ("firewall_domain_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def import_firewall_domains(
        self,
        domain_file_url: str,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput":
        """<p>Imports a list of domains from an Amazon S3 file into a firewall domain list. The file should contain one domain per line.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domain_file_url: <p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>
            operation: <p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains.async_import_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput = {
            "domain_file_url": domain_file_url,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput":
        """<p>Lists all the domains in DNS Firewall domain list you have created.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains.async_list_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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

    async def iter_list_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.domain.Domain]":
        _token = next_token
        while True:
            _response = await self.list_firewall_domains(
                firewall_domain_list_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_firewall_domains(
        self,
        domains: "capo_route53globalresolver.types.domains.Domains",
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput":
        """<p>Updates a DNS Firewall domain list from an array of specified domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domains: <p>A list of the domains. You can add up to 1000 domains per request.</p>
            firewall_domain_list_id: <p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>
            operation: <p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains.async_update_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput = {
            "domains": domains,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_firewall_rule(
        self,
        action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        firewall_domain_list_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
        q_type: Optional[
            "capo_route53globalresolver.types.dns_query_type.DnsQueryType"
        ] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput":
        """<p>Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_response: <p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>
            description: <p>An optional description for the firewall rule.</p>
            dns_advanced_protection: <p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>
            firewall_domain_list_id: <p>The ID of the firewall domain list to use in this rule.</p>
            name: <p>A descriptive name for the firewall rule.</p>
            priority: <p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this firewall rule.</p>
            q_type: <p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule.async_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput = {
            "action": action,
            "name": name,
            "dns_view_id": dns_view_id,
        }
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if priority is not None:
            input_["priority"] = priority
        if q_type is not None:
            input_["q_type"] = q_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_rule(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput":
        """<p>Retrieves information about a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>ID of the DNS Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule.async_get_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_firewall_rule(
        self,
        client_token: "capo_route53globalresolver.types.client_token.ClientToken",
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        action: Optional[
            "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
        ] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput":
        """<p>Updates the configuration of a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>
            description: <p>The description for the Firewall rule.</p>
            dns_advanced_protection: <p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>
            firewall_rule_id: <p>The ID of the DNS Firewall rule.</p>
            name: <p>The name of the DNS Firewall rule.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule.async_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput = {
            "client_token": client_token,
            "firewall_rule_id": firewall_rule_id,
        }
        if action is not None:
            input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_firewall_rule(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput":
        """<p>Deletes a DNS firewall rule. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>The unique identifier of the firewall rule to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule.async_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_firewall_rules(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput":
        """<p>Lists all DNS firewall rules for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>ID of the DNS view.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules.async_list_firewall_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput = {
            "dns_view_id": dns_view_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_firewall_rules(
        self,
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.firewall_rules_item.FirewallRulesItem]":
        _token = next_token
        while True:
            _response = await self.list_firewall_rules(
                dns_view_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("firewall_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_create_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput":
        """<p>Creates multiple DNS firewall rules in a single operation. This is more efficient than creating rules individually when you need to set up multiple rules at once.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule.async_batch_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput":
        """<p>Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>An array of the DNS Firewall IDs to be deleted.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule.async_batch_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput":
        """<p>Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The DNS Firewall rule IDs to be updated.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule.async_batch_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_global_resolver(
        self,
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        regions: "capo_route53globalresolver.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        observability_region: Optional[
            "capo_route53globalresolver.types.region.Region"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput":
        """<p>Creates a new Route 53 Global Resolver instance. A Route 53 Global Resolver is a global, internet-accessible DNS resolver that provides secure DNS resolution for both public and private domains through global anycast IP addresses.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique string that identifies the request and ensures idempotency. If you make multiple requests with the same client token, only one Route 53 Global Resolver is created.</p>
            description: <p>An optional description for the Route 53 Global Resolver instance. Maximum length of 1024 characters.</p>
            ip_address_type: <p>The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL_STACK for both IPv4 and IPv6 support.</p>
            name: <p>A descriptive name for the Route 53 Global Resolver instance. Maximum length of 64 characters.</p>
            observability_region: <p>The Amazon Web Services Region where query resolution logs and metrics will be aggregated and delivered. If not specified, logging is not enabled.</p>
            regions: <p>List of Amazon Web Services Regions where the Route 53 Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>
            tags: <p>Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver.async_create_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput = {
            "name": name,
            "regions": regions,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if observability_region is not None:
            input_["observability_region"] = observability_region
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_global_resolver(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput":
        """<p>Retrieves information about a Route 53 Global Resolver instance.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to retrieve information about.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver.async_get_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput = {
            "global_resolver_id": global_resolver_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_global_resolver(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        observability_region: Optional[
            "capo_route53globalresolver.types.region.Region"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        regions: Optional["capo_route53globalresolver.types.regions.Regions"] = None,
    ) -> "capo_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput":
        """<p>Updates the configuration of a Route 53 Global Resolver instance. You can modify the name, description, and observability Region.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Global Resolver.</p>
            name: <p>The name of the Global Resolver.</p>
            observability_region: <p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>
            description: <p>The description of the Global Resolver.</p>
            ip_address_type: <p>The IP address type for the Global Resolver. Valid values are IPV4 or DUAL_STACK for both IPv4 and IPv6 support.</p>
            regions: <p>The list of Amazon Web Services Regions where the Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver.async_update_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput = {
            "global_resolver_id": global_resolver_id
        }
        if name is not None:
            input_["name"] = name
        if observability_region is not None:
            input_["observability_region"] = observability_region
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_global_resolver(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput":
        """<p>Deletes a Route 53 Global Resolver instance. This operation cannot be undone. All associated DNS views, access sources, tokens, and firewall rules are also deleted.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The unique identifier of the Route 53 Global Resolver to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver.async_delete_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput = {
            "global_resolver_id": global_resolver_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_global_resolvers(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput":
        """<p>Lists all Route 53 Global Resolver instances in your account with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of Route 53 Global Resolver instances to return in the response. Valid range is 1-100.</p>
            next_token: <p>The token for the next page of results. This value is returned in the response if there are more results to retrieve.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers.async_list_global_resolvers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput = {}
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

    async def iter_list_global_resolvers(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.global_resolvers_item.GlobalResolversItem]":
        _token = next_token
        while True:
            _response = await self.list_global_resolvers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("global_resolvers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_hosted_zone(
        self,
        hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput":
        """<p>Associates a Route 53 private hosted zone with a Route 53 Global Resolver resource. This allows the resolver to resolve DNS queries for the private hosted zone from anywhere globally.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to associate with the Route 53 Global Resolver resource.</p>
            resource_arn: <p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone will be associated to.</p>
            name: <p>Name for the private hosted zone association.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone.async_associate_hosted_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput = {
            "hosted_zone_id": hosted_zone_id,
            "resource_arn": resource_arn,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_hosted_zone_association(
        self,
        hosted_zone_association_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput":
        """<p>Retrieves information about a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>ID of the private hosted zone association.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association.async_get_hosted_zone_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput = {
            "hosted_zone_association_id": hosted_zone_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_hosted_zone_association(
        self,
        hosted_zone_association_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput":
        """<p>Updates the configuration of a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>The ID of the private hosted zone association.</p>
            name: <p>The name you want to update the hosted zone association to.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association.async_update_hosted_zone_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput = {
            "hosted_zone_association_id": hosted_zone_association_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_hosted_zone_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        resource_arn: Optional[
            "capo_route53globalresolver.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput":
        """<p>Lists hosted zone associations with pagination support. Specify a DNS view through the <code>resourceArn</code> parameter to list the hosted zone associations for that DNS view, or omit it to list all hosted zone associations in your Amazon Web Services account.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the DNS view to list hosted zone associations for. This parameter is optional; if you omit it, all hosted zone associations in your Amazon Web Services account are returned.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations.async_list_hosted_zone_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_hosted_zone_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        resource_arn: Optional[
            "capo_route53globalresolver.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.hosted_zone_association_summary.HostedZoneAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_hosted_zone_associations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_arn=resource_arn,
            )
            _page = _resolve_path(_response, ("hosted_zone_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_managed_firewall_domain_list(
        self,
        managed_firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput":
        """<p>Retrieves information about an Amazon Web Services-managed firewall domain list. Managed domain lists contain domains associated with malicious activity, content categories, or specific threats.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            managed_firewall_domain_list_id: <p>ID of the Managed Domain List.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list.async_get_managed_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput = {
            "managed_firewall_domain_list_id": managed_firewall_domain_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_firewall_domain_lists(
        self,
        managed_firewall_domain_list_type: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput":
        """<p>Returns a paginated list of the Amazon Web Services Managed DNS Lists and the categories for DNS Firewall. The categories are either <code>THREAT</code> or <code>CONTENT</code>.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            managed_firewall_domain_list_type: <p>The category of the Manage DNS list either <code>THREAT</code> or <code>CONTENT</code>.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists.async_list_managed_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput = {
            "managed_firewall_domain_list_type": managed_firewall_domain_list_type
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

    async def iter_list_managed_firewall_domain_lists(
        self,
        managed_firewall_domain_list_type: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_route53globalresolver.types.managed_firewall_domain_lists_item.ManagedFirewallDomainListsItem]":
        _token = next_token
        while True:
            _response = await self.list_managed_firewall_domain_lists(
                managed_firewall_domain_list_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("managed_firewall_domain_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
