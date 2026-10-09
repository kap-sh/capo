"""Generated from Smithy shape ``com.amazonaws.route53resolver#Route53Resolver``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_route53resolver._auth._signers
import capo_route53resolver._auth._sigv4
from capo_route53resolver._auth._identity import Credentials
from capo_route53resolver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53resolver._auth._zapros_handler import AuthMiddleware
from capo_route53resolver._pagination import resolve_path as _resolve_path
from capo_route53resolver._services._aws_config import aaws_config
from capo_route53resolver._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_route53resolver.types.action
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.associate_firewall_rule_group_request
    import capo_route53resolver.types.associate_firewall_rule_group_response
    import capo_route53resolver.types.associate_resolver_endpoint_ip_address_request
    import capo_route53resolver.types.associate_resolver_endpoint_ip_address_response
    import capo_route53resolver.types.associate_resolver_query_log_config_request
    import capo_route53resolver.types.associate_resolver_query_log_config_response
    import capo_route53resolver.types.associate_resolver_rule_request
    import capo_route53resolver.types.associate_resolver_rule_response
    import capo_route53resolver.types.autodefined_reverse_flag
    import capo_route53resolver.types.batch_create_firewall_rule_request
    import capo_route53resolver.types.batch_create_firewall_rule_response
    import capo_route53resolver.types.batch_delete_firewall_rule_request
    import capo_route53resolver.types.batch_delete_firewall_rule_response
    import capo_route53resolver.types.batch_update_firewall_rule_request
    import capo_route53resolver.types.batch_update_firewall_rule_response
    import capo_route53resolver.types.block_override_dns_type
    import capo_route53resolver.types.block_override_domain
    import capo_route53resolver.types.block_override_ttl
    import capo_route53resolver.types.block_response
    import capo_route53resolver.types.confidence_threshold
    import capo_route53resolver.types.create_firewall_domain_list_request
    import capo_route53resolver.types.create_firewall_domain_list_response
    import capo_route53resolver.types.create_firewall_rule_entries
    import capo_route53resolver.types.create_firewall_rule_group_request
    import capo_route53resolver.types.create_firewall_rule_group_response
    import capo_route53resolver.types.create_firewall_rule_request
    import capo_route53resolver.types.create_firewall_rule_response
    import capo_route53resolver.types.create_outpost_resolver_request
    import capo_route53resolver.types.create_outpost_resolver_response
    import capo_route53resolver.types.create_resolver_endpoint_request
    import capo_route53resolver.types.create_resolver_endpoint_response
    import capo_route53resolver.types.create_resolver_query_log_config_request
    import capo_route53resolver.types.create_resolver_query_log_config_response
    import capo_route53resolver.types.create_resolver_rule_request
    import capo_route53resolver.types.create_resolver_rule_response
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.delegation_record
    import capo_route53resolver.types.delete_firewall_domain_list_request
    import capo_route53resolver.types.delete_firewall_domain_list_response
    import capo_route53resolver.types.delete_firewall_rule_entries
    import capo_route53resolver.types.delete_firewall_rule_group_request
    import capo_route53resolver.types.delete_firewall_rule_group_response
    import capo_route53resolver.types.delete_firewall_rule_request
    import capo_route53resolver.types.delete_firewall_rule_response
    import capo_route53resolver.types.delete_outpost_resolver_request
    import capo_route53resolver.types.delete_outpost_resolver_response
    import capo_route53resolver.types.delete_resolver_endpoint_request
    import capo_route53resolver.types.delete_resolver_endpoint_response
    import capo_route53resolver.types.delete_resolver_query_log_config_request
    import capo_route53resolver.types.delete_resolver_query_log_config_response
    import capo_route53resolver.types.delete_resolver_rule_request
    import capo_route53resolver.types.delete_resolver_rule_response
    import capo_route53resolver.types.destination_arn
    import capo_route53resolver.types.disassociate_firewall_rule_group_request
    import capo_route53resolver.types.disassociate_firewall_rule_group_response
    import capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_request
    import capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_response
    import capo_route53resolver.types.disassociate_resolver_query_log_config_request
    import capo_route53resolver.types.disassociate_resolver_query_log_config_response
    import capo_route53resolver.types.disassociate_resolver_rule_request
    import capo_route53resolver.types.disassociate_resolver_rule_response
    import capo_route53resolver.types.dns64_enabled
    import capo_route53resolver.types.dns_threat_protection
    import capo_route53resolver.types.domain_list_file_url
    import capo_route53resolver.types.domain_name
    import capo_route53resolver.types.filters
    import capo_route53resolver.types.firewall_config
    import capo_route53resolver.types.firewall_domain_import_operation
    import capo_route53resolver.types.firewall_domain_list_metadata
    import capo_route53resolver.types.firewall_domain_name
    import capo_route53resolver.types.firewall_domain_redirection_action
    import capo_route53resolver.types.firewall_domain_update_operation
    import capo_route53resolver.types.firewall_domains
    import capo_route53resolver.types.firewall_fail_open_status
    import capo_route53resolver.types.firewall_rule
    import capo_route53resolver.types.firewall_rule_group_association
    import capo_route53resolver.types.firewall_rule_group_association_status
    import capo_route53resolver.types.firewall_rule_group_metadata
    import capo_route53resolver.types.firewall_rule_group_policy
    import capo_route53resolver.types.firewall_rule_type
    import capo_route53resolver.types.firewall_rule_type_definition
    import capo_route53resolver.types.get_firewall_config_request
    import capo_route53resolver.types.get_firewall_config_response
    import capo_route53resolver.types.get_firewall_domain_list_request
    import capo_route53resolver.types.get_firewall_domain_list_response
    import capo_route53resolver.types.get_firewall_rule_group_association_request
    import capo_route53resolver.types.get_firewall_rule_group_association_response
    import capo_route53resolver.types.get_firewall_rule_group_policy_request
    import capo_route53resolver.types.get_firewall_rule_group_policy_response
    import capo_route53resolver.types.get_firewall_rule_group_request
    import capo_route53resolver.types.get_firewall_rule_group_response
    import capo_route53resolver.types.get_outpost_resolver_request
    import capo_route53resolver.types.get_outpost_resolver_response
    import capo_route53resolver.types.get_resolver_config_request
    import capo_route53resolver.types.get_resolver_config_response
    import capo_route53resolver.types.get_resolver_dnssec_config_request
    import capo_route53resolver.types.get_resolver_dnssec_config_response
    import capo_route53resolver.types.get_resolver_endpoint_request
    import capo_route53resolver.types.get_resolver_endpoint_response
    import capo_route53resolver.types.get_resolver_query_log_config_association_request
    import capo_route53resolver.types.get_resolver_query_log_config_association_response
    import capo_route53resolver.types.get_resolver_query_log_config_policy_request
    import capo_route53resolver.types.get_resolver_query_log_config_policy_response
    import capo_route53resolver.types.get_resolver_query_log_config_request
    import capo_route53resolver.types.get_resolver_query_log_config_response
    import capo_route53resolver.types.get_resolver_rule_association_request
    import capo_route53resolver.types.get_resolver_rule_association_response
    import capo_route53resolver.types.get_resolver_rule_policy_request
    import capo_route53resolver.types.get_resolver_rule_policy_response
    import capo_route53resolver.types.get_resolver_rule_request
    import capo_route53resolver.types.get_resolver_rule_response
    import capo_route53resolver.types.import_firewall_domains_request
    import capo_route53resolver.types.import_firewall_domains_response
    import capo_route53resolver.types.instance_count
    import capo_route53resolver.types.ip_address_response
    import capo_route53resolver.types.ip_address_update
    import capo_route53resolver.types.ip_addresses_request
    import capo_route53resolver.types.ipv6_internet_access_enabled
    import capo_route53resolver.types.list_domain_max_results
    import capo_route53resolver.types.list_firewall_configs_max_result
    import capo_route53resolver.types.list_firewall_configs_request
    import capo_route53resolver.types.list_firewall_configs_response
    import capo_route53resolver.types.list_firewall_domain_lists_request
    import capo_route53resolver.types.list_firewall_domain_lists_response
    import capo_route53resolver.types.list_firewall_domains_request
    import capo_route53resolver.types.list_firewall_domains_response
    import capo_route53resolver.types.list_firewall_rule_group_associations_request
    import capo_route53resolver.types.list_firewall_rule_group_associations_response
    import capo_route53resolver.types.list_firewall_rule_groups_request
    import capo_route53resolver.types.list_firewall_rule_groups_response
    import capo_route53resolver.types.list_firewall_rule_types_request
    import capo_route53resolver.types.list_firewall_rule_types_response
    import capo_route53resolver.types.list_firewall_rules_request
    import capo_route53resolver.types.list_firewall_rules_response
    import capo_route53resolver.types.list_outpost_resolvers_request
    import capo_route53resolver.types.list_outpost_resolvers_response
    import capo_route53resolver.types.list_resolver_configs_max_result
    import capo_route53resolver.types.list_resolver_configs_request
    import capo_route53resolver.types.list_resolver_configs_response
    import capo_route53resolver.types.list_resolver_dnssec_configs_request
    import capo_route53resolver.types.list_resolver_dnssec_configs_response
    import capo_route53resolver.types.list_resolver_endpoint_ip_addresses_request
    import capo_route53resolver.types.list_resolver_endpoint_ip_addresses_response
    import capo_route53resolver.types.list_resolver_endpoints_request
    import capo_route53resolver.types.list_resolver_endpoints_response
    import capo_route53resolver.types.list_resolver_query_log_config_associations_request
    import capo_route53resolver.types.list_resolver_query_log_config_associations_response
    import capo_route53resolver.types.list_resolver_query_log_configs_request
    import capo_route53resolver.types.list_resolver_query_log_configs_response
    import capo_route53resolver.types.list_resolver_rule_associations_request
    import capo_route53resolver.types.list_resolver_rule_associations_response
    import capo_route53resolver.types.list_resolver_rules_request
    import capo_route53resolver.types.list_resolver_rules_response
    import capo_route53resolver.types.list_tags_for_resource_request
    import capo_route53resolver.types.list_tags_for_resource_response
    import capo_route53resolver.types.max_results
    import capo_route53resolver.types.mutation_protection_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.outpost_arn
    import capo_route53resolver.types.outpost_instance_type
    import capo_route53resolver.types.outpost_resolver
    import capo_route53resolver.types.outpost_resolver_name
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.protocol_list
    import capo_route53resolver.types.put_firewall_rule_group_policy_request
    import capo_route53resolver.types.put_firewall_rule_group_policy_response
    import capo_route53resolver.types.put_resolver_query_log_config_policy_request
    import capo_route53resolver.types.put_resolver_query_log_config_policy_response
    import capo_route53resolver.types.put_resolver_rule_policy_request
    import capo_route53resolver.types.put_resolver_rule_policy_response
    import capo_route53resolver.types.qtype
    import capo_route53resolver.types.resolver_config
    import capo_route53resolver.types.resolver_dnssec_config
    import capo_route53resolver.types.resolver_endpoint
    import capo_route53resolver.types.resolver_endpoint_direction
    import capo_route53resolver.types.resolver_endpoint_type
    import capo_route53resolver.types.resolver_query_log_config
    import capo_route53resolver.types.resolver_query_log_config_association
    import capo_route53resolver.types.resolver_query_log_config_name
    import capo_route53resolver.types.resolver_query_log_config_policy
    import capo_route53resolver.types.resolver_rule
    import capo_route53resolver.types.resolver_rule_association
    import capo_route53resolver.types.resolver_rule_config
    import capo_route53resolver.types.resolver_rule_policy
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rni_enhanced_metrics_enabled
    import capo_route53resolver.types.rule_type_name
    import capo_route53resolver.types.rule_type_option
    import capo_route53resolver.types.security_group_ids
    import capo_route53resolver.types.sort_by_key
    import capo_route53resolver.types.sort_order
    import capo_route53resolver.types.tag
    import capo_route53resolver.types.tag_key_list
    import capo_route53resolver.types.tag_list
    import capo_route53resolver.types.tag_resource_request
    import capo_route53resolver.types.tag_resource_response
    import capo_route53resolver.types.target_list
    import capo_route53resolver.types.target_name_server_metrics_enabled
    import capo_route53resolver.types.untag_resource_request
    import capo_route53resolver.types.untag_resource_response
    import capo_route53resolver.types.update_firewall_config_request
    import capo_route53resolver.types.update_firewall_config_response
    import capo_route53resolver.types.update_firewall_domains_request
    import capo_route53resolver.types.update_firewall_domains_response
    import capo_route53resolver.types.update_firewall_rule_entries
    import capo_route53resolver.types.update_firewall_rule_group_association_request
    import capo_route53resolver.types.update_firewall_rule_group_association_response
    import capo_route53resolver.types.update_firewall_rule_request
    import capo_route53resolver.types.update_firewall_rule_response
    import capo_route53resolver.types.update_ip_addresses
    import capo_route53resolver.types.update_outpost_resolver_request
    import capo_route53resolver.types.update_outpost_resolver_response
    import capo_route53resolver.types.update_resolver_config_request
    import capo_route53resolver.types.update_resolver_config_response
    import capo_route53resolver.types.update_resolver_dnssec_config_request
    import capo_route53resolver.types.update_resolver_dnssec_config_response
    import capo_route53resolver.types.update_resolver_endpoint_request
    import capo_route53resolver.types.update_resolver_endpoint_response
    import capo_route53resolver.types.update_resolver_rule_request
    import capo_route53resolver.types.update_resolver_rule_response
    import capo_route53resolver.types.validation


class AsyncRoute53ResolverClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRoute53ResolverClient:
    """A client for the ``Route53Resolver`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncRoute53ResolverClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53ResolverClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def associate_firewall_rule_group(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        vpc_id: "capo_route53resolver.types.resource_id.ResourceId",
        priority: "capo_route53resolver.types.priority.Priority",
        name: "capo_route53resolver.types.name.Name",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        mutation_protection: Optional[
            "capo_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
        ] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
    ) -> "capo_route53resolver.types.associate_firewall_rule_group_response.AssociateFirewallRuleGroupResponse":
        """<p>Associates a <a>FirewallRuleGroup</a> with a VPC, to provide DNS filtering for the VPC.</p> <p>If the rule group contains any rule configured with the <code>PartnerThreatProtection</code> rule type, the calling account must hold an active Amazon Web Services Marketplace subscription to the named partner. If the subscription is missing, the association request is rejected.</p>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group. </p>
            vpc_id: <p>The unique identifier of the VPC that you want to associate with the rule group. </p>
            priority: <p>The setting that determines the processing order of the rule group among the rule groups that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p> <p>You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it.</p> <p>The allowed values for <code>Priority</code> are between 100 and 9900.</p>
            name: <p>A name that lets you identify the association, to manage and use it.</p>
            mutation_protection: <p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. When you create the association, the default setting is <code>DISABLED</code>. </p>
            tags: <p>A list of the tag keys and values that you want to associate with the rule group association. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.associate_firewall_rule_group_request.AssociateFirewallRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.associate_firewall_rule_group_response.AssociateFirewallRuleGroupResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.associate_firewall_rule_group

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.associate_firewall_rule_group.async_associate_firewall_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.associate_firewall_rule_group_request.AssociateFirewallRuleGroupRequest = {
            "creator_request_id": creator_request_id,
            "firewall_rule_group_id": firewall_rule_group_id,
            "vpc_id": vpc_id,
            "priority": priority,
            "name": name,
        }
        if mutation_protection is not None:
            input_["mutation_protection"] = mutation_protection
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_resolver_endpoint_ip_address(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        ip_address: "capo_route53resolver.types.ip_address_update.IpAddressUpdate",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.associate_resolver_endpoint_ip_address_response.AssociateResolverEndpointIpAddressResponse":
        """<p>Adds IP addresses to an inbound or an outbound Resolver endpoint. If you want to add more than one IP address, submit one <code>AssociateResolverEndpointIpAddress</code> request for each IP address.</p> <p>To remove an IP address from an endpoint, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.html">DisassociateResolverEndpointIpAddress</a>. </p>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to associate IP addresses with.</p>
            ip_address: <p>Either the IPv4 address that you want to add to a Resolver endpoint or a subnet ID. If you specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the specified subnet.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.associate_resolver_endpoint_ip_address_request.AssociateResolverEndpointIpAddressRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.associate_resolver_endpoint_ip_address_response.AssociateResolverEndpointIpAddressResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.associate_resolver_endpoint_ip_address

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.associate_resolver_endpoint_ip_address.async_associate_resolver_endpoint_ip_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.associate_resolver_endpoint_ip_address_request.AssociateResolverEndpointIpAddressRequest = {
            "resolver_endpoint_id": resolver_endpoint_id,
            "ip_address": ip_address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_resolver_query_log_config(
        self,
        resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId",
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.associate_resolver_query_log_config_response.AssociateResolverQueryLogConfigResponse":
        """<p>Associates an Amazon VPC with a specified query logging configuration. Route 53 Resolver logs DNS queries that originate in all of the Amazon VPCs that are associated with a specified query logging configuration. To associate more than one VPC with a configuration, submit one <code>AssociateResolverQueryLogConfig</code> request for each VPC.</p> <note> <p>The VPCs that you associate with a query logging configuration must be in the same Region as the configuration.</p> </note> <p>To remove a VPC from a query logging configuration, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html">DisassociateResolverQueryLogConfig</a>. </p>

        Args:
            resolver_query_log_config_id: <p>The ID of the query logging configuration that you want to associate a VPC with.</p>
            resource_id: <p>The ID of an Amazon VPC that you want this query logging configuration to log queries for.</p> <note> <p>The VPCs and the query logging configuration must be in the same Region.</p> </note>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.associate_resolver_query_log_config_request.AssociateResolverQueryLogConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.associate_resolver_query_log_config_response.AssociateResolverQueryLogConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.associate_resolver_query_log_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.associate_resolver_query_log_config.async_associate_resolver_query_log_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.associate_resolver_query_log_config_request.AssociateResolverQueryLogConfigRequest = {
            "resolver_query_log_config_id": resolver_query_log_config_id,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_resolver_rule(
        self,
        resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId",
        vpc_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
    ) -> "capo_route53resolver.types.associate_resolver_rule_response.AssociateResolverRuleResponse":
        """<p>Associates a Resolver rule with a VPC. When you associate a rule with a VPC, Resolver forwards all DNS queries for the domain name that is specified in the rule and that originate in the VPC. The queries are forwarded to the IP addresses for the DNS resolvers that are specified in the rule. For more information about rules, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html">CreateResolverRule</a>. </p>

        Args:
            resolver_rule_id: <p>The ID of the Resolver rule that you want to associate with the VPC. To list the existing Resolver rules, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html">ListResolverRules</a>.</p>
            name: <p>A name for the association that you're creating between a Resolver rule and a VPC.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>
            vpc_id: <p>The ID of the VPC that you want to associate the Resolver rule with.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource isn't available.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.associate_resolver_rule_request.AssociateResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.associate_resolver_rule_response.AssociateResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.associate_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.associate_resolver_rule.async_associate_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.associate_resolver_rule_request.AssociateResolverRuleRequest = {
            "resolver_rule_id": resolver_rule_id,
            "vpc_id": vpc_id,
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

    async def batch_create_firewall_rule(
        self,
        create_firewall_rule_entries: "capo_route53resolver.types.create_firewall_rule_entries.CreateFirewallRuleEntries",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.batch_create_firewall_rule_response.BatchCreateFirewallRuleResponse":
        """<p>Creates multiple DNS Firewall rules in the specified rule group.</p>

        Args:
            create_firewall_rule_entries: <p>The list of firewall rules to create.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.batch_create_firewall_rule_request.BatchCreateFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.batch_create_firewall_rule_response.BatchCreateFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.batch_create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.batch_create_firewall_rule.async_batch_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.batch_create_firewall_rule_request.BatchCreateFirewallRuleRequest = {
            "create_firewall_rule_entries": create_firewall_rule_entries
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
        delete_firewall_rule_entries: "capo_route53resolver.types.delete_firewall_rule_entries.DeleteFirewallRuleEntries",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.batch_delete_firewall_rule_response.BatchDeleteFirewallRuleResponse":
        """<p>Deletes multiple DNS Firewall rules from the specified rule group.</p>

        Args:
            delete_firewall_rule_entries: <p>The list of firewall rules to delete.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.batch_delete_firewall_rule_request.BatchDeleteFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.batch_delete_firewall_rule_response.BatchDeleteFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.batch_delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.batch_delete_firewall_rule.async_batch_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.batch_delete_firewall_rule_request.BatchDeleteFirewallRuleRequest = {
            "delete_firewall_rule_entries": delete_firewall_rule_entries
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
        update_firewall_rule_entries: "capo_route53resolver.types.update_firewall_rule_entries.UpdateFirewallRuleEntries",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.batch_update_firewall_rule_response.BatchUpdateFirewallRuleResponse":
        """<p>Updates multiple DNS Firewall rules in the specified rule group.</p>

        Args:
            update_firewall_rule_entries: <p>The list of firewall rules to update.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.batch_update_firewall_rule_request.BatchUpdateFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.batch_update_firewall_rule_response.BatchUpdateFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.batch_update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.batch_update_firewall_rule.async_batch_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.batch_update_firewall_rule_request.BatchUpdateFirewallRuleRequest = {
            "update_firewall_rule_entries": update_firewall_rule_entries
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
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        name: "capo_route53resolver.types.name.Name",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
    ) -> "capo_route53resolver.types.create_firewall_domain_list_response.CreateFirewallDomainListResponse":
        """<p>Creates an empty firewall domain list for use in DNS Firewall rules. You can populate the domains for the new list with a file, using <a>ImportFirewallDomains</a>, or with domain strings, using <a>UpdateFirewallDomains</a>. </p>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows you to retry failed requests without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            name: <p>A name that lets you identify the domain list to manage and use it.</p>
            tags: <p>A list of the tag keys and values that you want to associate with the domain list. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_firewall_domain_list_request.CreateFirewallDomainListRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_firewall_domain_list_response.CreateFirewallDomainListResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_firewall_domain_list.async_create_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_firewall_domain_list_request.CreateFirewallDomainListRequest = {
            "creator_request_id": creator_request_id,
            "name": name,
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

    async def create_firewall_rule(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        priority: "capo_route53resolver.types.priority.Priority",
        action: "capo_route53resolver.types.action.Action",
        name: "capo_route53resolver.types.name.Name",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        firewall_domain_list_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        block_response: Optional[
            "capo_route53resolver.types.block_response.BlockResponse"
        ] = None,
        block_override_domain: Optional[
            "capo_route53resolver.types.block_override_domain.BlockOverrideDomain"
        ] = None,
        block_override_dns_type: Optional[
            "capo_route53resolver.types.block_override_dns_type.BlockOverrideDnsType"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53resolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        firewall_domain_redirection_action: Optional[
            "capo_route53resolver.types.firewall_domain_redirection_action.FirewallDomainRedirectionAction"
        ] = None,
        qtype: Optional["capo_route53resolver.types.qtype.Qtype"] = None,
        dns_threat_protection: Optional[
            "capo_route53resolver.types.dns_threat_protection.DnsThreatProtection"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53resolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        firewall_rule_type: Optional[
            "capo_route53resolver.types.firewall_rule_type.FirewallRuleType"
        ] = None,
    ) -> "capo_route53resolver.types.create_firewall_rule_response.CreateFirewallRuleResponse":
        """<p>Creates a single DNS Firewall rule in the specified rule group. The rule can use any one of the following match sources, and the chosen source must be supplied through the matching request field — they are mutually exclusive:</p> <ul> <li> <p> <code>FirewallDomainListId</code> — match a customer-managed or Amazon Web Services-managed domain list.</p> </li> <li> <p> <code>DnsThreatProtection</code> — match a built-in DNS Firewall Advanced threat detector (<code>DGA</code>, <code>DNS_TUNNELING</code>, or <code>DICTIONARY_DGA</code>).</p> </li> <li> <p> <code>FirewallRuleType</code> — match one of the rule-type variants returned by <a>ListFirewallRuleTypes</a>: <code>FirewallAdvancedContentCategory</code>, <code>FirewallAdvancedThreatCategory</code>, <code>DnsThreatProtection</code>, or <code>PartnerThreatProtection</code>. The <code>PartnerThreatProtection</code> variant requires an active Amazon Web Services Marketplace subscription to the named partner product.</p> </li> </ul> <p>For rules that require asynchronous provisioning (today, the <code>PartnerThreatProtection</code> rule type), the rule's <code>Status</code> begins at <code>CREATING</code> and transitions to <code>COMPLETE</code> once the rule is provisioned and the marketplace entitlement is verified. If provisioning fails, <code>Status</code> becomes <code>CREATION_FAILED</code> and <code>StatusMessage</code> contains a human-readable reason; the rule is then immutable and must be removed with <a>DeleteFirewallRule</a>.</p>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows you to retry failed requests without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group where you want to create the rule. </p>
            firewall_domain_list_id: <p>The ID of the domain list that you want to use in the rule. Can't be used together with <code>DnsThreatProtecton</code>.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p> <p>You must specify a unique priority for each rule in a rule group. To make it easier to insert rules later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for the rules in a rule group at any time.</p>
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through. Not available for DNS Firewall Advanced rules.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to Cloud Watch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>. </p> </li> </ul>
            block_response: <p>The way that you want DNS Firewall to block the request, used with the rule action setting <code>BLOCK</code>. </p> <ul> <li> <p> <code>NODATA</code> - Respond indicating that the query was successful, but no response is available for it.</p> </li> <li> <p> <code>NXDOMAIN</code> - Respond indicating that the domain name that's in the query doesn't exist.</p> </li> <li> <p> <code>OVERRIDE</code> - Provide a custom override in the response. This option requires custom handling details in the rule's <code>BlockOverride*</code> settings. </p> </li> </ul> <p>This setting is required if the rule action setting is <code>BLOCK</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            name: <p>A name that lets you identify the rule in the rule group.</p>
            firewall_domain_redirection_action: <p> How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME. </p> <p> <code>INSPECT_REDIRECTION_DOMAIN</code>: (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.</p> <p> <code>TRUST_REDIRECTION_DOMAIN</code>: Inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the domain in the redirection list to the domain list.</p>
            qtype: <p> The DNS query type you want the rule to evaluate. Allowed values are; </p> <ul> <li> <p> A: Returns an IPv4 address.</p> </li> <li> <p>AAAA: Returns an Ipv6 address.</p> </li> <li> <p>CAA: Restricts CAs that can create SSL/TLS certifications for the domain.</p> </li> <li> <p>CNAME: Returns another domain name.</p> </li> <li> <p>DS: Record that identifies the DNSSEC signing key of a delegated zone.</p> </li> <li> <p>MX: Specifies mail servers.</p> </li> <li> <p>NAPTR: Regular-expression-based rewriting of domain names.</p> </li> <li> <p>NS: Authoritative name servers.</p> </li> <li> <p>PTR: Maps an IP address to a domain name.</p> </li> <li> <p>SOA: Start of authority record for the zone.</p> </li> <li> <p>SPF: Lists the servers authorized to send emails from a domain.</p> </li> <li> <p>SRV: Application specific values that identify servers.</p> </li> <li> <p>TXT: Verifies email senders and application-specific values.</p> </li> <li> <p>A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">List of DNS record types</a>.</p> </li> </ul>
            dns_threat_protection: <p> The type of the DNS Firewall Advanced rule. This setting is mutually exclusive with <code>FirewallDomainListId</code> and <code>FirewallRuleType</code>. Valid values are: </p> <ul> <li> <p> <code>DGA</code>: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.</p> </li> <li> <p> <code>DNS_TUNNELING</code>: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.</p> </li> <li> <p> <code>DICTIONARY_DGA</code>: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.</p> </li> </ul>
            confidence_threshold: <p> The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean: </p> <ul> <li> <p> <code>LOW</code>: Provides the highest detection rate for threats, but also increases false positives.</p> </li> <li> <p> <code>MEDIUM</code>: Provides a balance between detecting threats and false positives.</p> </li> <li> <p> <code>HIGH</code>: Detects only the most well corroborated threats with a low rate of false positives. </p> </li> </ul>
            firewall_rule_type: <p>The rule type configuration for the firewall rule. This is a tagged union — set exactly one of its members. This setting is mutually exclusive with the top-level <code>FirewallDomainListId</code> and <code>DnsThreatProtection</code> fields. Use one of:</p> <ul> <li> <p> <code>FirewallAdvancedContentCategory</code> — match an Amazon Web Services-managed content category (for example, <code>VIOLENCE_AND_HATE_SPEECH</code>).</p> </li> <li> <p> <code>FirewallAdvancedThreatCategory</code> — match an Amazon Web Services-managed advanced threat category (for example, <code>PHISHING</code>).</p> </li> <li> <p> <code>DnsThreatProtection</code> — match a built-in DNS Firewall Advanced threat detector (<code>DGA</code>, <code>DNS_TUNNELING</code>, or <code>DICTIONARY_DGA</code>).</p> </li> <li> <p> <code>PartnerThreatProtection</code> — match a third-party threat feed delivered through Amazon Web Services Marketplace. The selected partner must be an active subscription on the calling account.</p> </li> </ul> <p>To enumerate the values supported in your account, call <a>ListFirewallRuleTypes</a>.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_firewall_rule_request.CreateFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_firewall_rule_response.CreateFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_firewall_rule.async_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_firewall_rule_request.CreateFirewallRuleRequest = {
            "creator_request_id": creator_request_id,
            "firewall_rule_group_id": firewall_rule_group_id,
            "priority": priority,
            "action": action,
            "name": name,
        }
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if block_response is not None:
            input_["block_response"] = block_response
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if firewall_domain_redirection_action is not None:
            input_["firewall_domain_redirection_action"] = (
                firewall_domain_redirection_action
            )
        if qtype is not None:
            input_["qtype"] = qtype
        if dns_threat_protection is not None:
            input_["dns_threat_protection"] = dns_threat_protection
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if firewall_rule_type is not None:
            input_["firewall_rule_type"] = firewall_rule_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_firewall_rule_group(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        name: "capo_route53resolver.types.name.Name",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
    ) -> "capo_route53resolver.types.create_firewall_rule_group_response.CreateFirewallRuleGroupResponse":
        """<p>Creates an empty DNS Firewall rule group for filtering DNS network traffic in a VPC. You can add rules to the new rule group by calling <a>CreateFirewallRule</a>. </p>

        Args:
            creator_request_id: <p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>
            name: <p>A name that lets you identify the rule group, to manage and use it.</p>
            tags: <p>A list of the tag keys and values that you want to associate with the rule group. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_firewall_rule_group_request.CreateFirewallRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_firewall_rule_group_response.CreateFirewallRuleGroupResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_firewall_rule_group

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_firewall_rule_group.async_create_firewall_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_firewall_rule_group_request.CreateFirewallRuleGroupRequest = {
            "creator_request_id": creator_request_id,
            "name": name,
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

    async def create_outpost_resolver(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        name: "capo_route53resolver.types.outpost_resolver_name.OutpostResolverName",
        preferred_instance_type: "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType",
        outpost_arn: "capo_route53resolver.types.outpost_arn.OutpostArn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        instance_count: Optional[
            "capo_route53resolver.types.instance_count.InstanceCount"
        ] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
    ) -> "capo_route53resolver.types.create_outpost_resolver_response.CreateOutpostResolverResponse":
        """<p>Creates a Route 53 Resolver on an Outpost.</p> <note> <p>This operation applies to first-generation Outposts only. On second-generation Outposts, Resolver is enabled by default and managed automatically by Amazon Web Services, so you don't need to create it.</p> </note>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. </p> <p> <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp.</p>
            name: <p>A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.</p>
            instance_count: <p>Number of Amazon EC2 instances for the Resolver on Outpost. The default and minimal value is 4.</p>
            preferred_instance_type: <p> The Amazon EC2 instance type. If you specify this, you must also specify a value for the <code>OutpostArn</code>. </p>
            outpost_arn: <p>The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the <code>PreferredInstanceType</code>.</p>
            tags: <p> A string that helps identify the Route 53 Resolvers on Outpost. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Fulfilling the request would cause one or more quotas to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_outpost_resolver_request.CreateOutpostResolverRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_outpost_resolver_response.CreateOutpostResolverResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_outpost_resolver

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_outpost_resolver.async_create_outpost_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_outpost_resolver_request.CreateOutpostResolverRequest = {
            "creator_request_id": creator_request_id,
            "name": name,
            "preferred_instance_type": preferred_instance_type,
            "outpost_arn": outpost_arn,
        }
        if instance_count is not None:
            input_["instance_count"] = instance_count
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resolver_endpoint(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        security_group_ids: "capo_route53resolver.types.security_group_ids.SecurityGroupIds",
        direction: "capo_route53resolver.types.resolver_endpoint_direction.ResolverEndpointDirection",
        ip_addresses: "capo_route53resolver.types.ip_addresses_request.IpAddressesRequest",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
        outpost_arn: Optional[
            "capo_route53resolver.types.outpost_arn.OutpostArn"
        ] = None,
        preferred_instance_type: Optional[
            "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
        ] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
        resolver_endpoint_type: Optional[
            "capo_route53resolver.types.resolver_endpoint_type.ResolverEndpointType"
        ] = None,
        protocols: Optional[
            "capo_route53resolver.types.protocol_list.ProtocolList"
        ] = None,
        rni_enhanced_metrics_enabled: Optional[
            "capo_route53resolver.types.rni_enhanced_metrics_enabled.RniEnhancedMetricsEnabled"
        ] = None,
        target_name_server_metrics_enabled: Optional[
            "capo_route53resolver.types.target_name_server_metrics_enabled.TargetNameServerMetricsEnabled"
        ] = None,
        dns64_enabled: Optional[
            "capo_route53resolver.types.dns64_enabled.Dns64Enabled"
        ] = None,
        ipv6_internet_access_enabled: Optional[
            "capo_route53resolver.types.ipv6_internet_access_enabled.Ipv6InternetAccessEnabled"
        ] = None,
    ) -> "capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse":
        """<p>Creates a Resolver endpoint. There are two types of Resolver endpoints, inbound and outbound:</p> <ul> <li> <p>An <i>inbound Resolver endpoint</i> forwards DNS queries to the DNS service for a VPC from your network.</p> </li> <li> <p>An <i>outbound Resolver endpoint</i> forwards DNS queries from the DNS service for a VPC to your network.</p> </li> </ul>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            name: <p>A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.</p>
            security_group_ids: <p>The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound Resolver endpoints) or outbound rules (for outbound Resolver endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.</p> <p>Some security group rules will cause your connection to be tracked. For outbound resolver endpoint, it can potentially impact the maximum queries per second from outbound endpoint to your target name server. For inbound resolver endpoint, it can bring down the overall maximum queries per second per IP address to as low as 1500. To avoid connection tracking caused by security group, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connectionsl">Untracked connections</a>.</p>
            direction: <p>Specify the applicable value:</p> <ul> <li> <p> <code>INBOUND</code>: Resolver forwards DNS queries to the DNS service for a VPC from your network.</p> </li> <li> <p> <code>OUTBOUND</code>: Resolver forwards DNS queries from the DNS service for a VPC to your network.</p> </li> <li> <p> <code>INBOUND_DELEGATION</code>: Resolver delegates queries to Route 53 private hosted zones from your network.</p> </li> </ul>
            ip_addresses: <p>The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC. </p> <note> <p>Even though the minimum is 1, Route 53 requires that you create at least two.</p> </note> <p>We recommend using <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html">VPC Resolver on Outposts</a> to create endpoints on Outposts Racks.</p> <important> <p>Outposts subnets with <a href="https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html">Local Network Interface (LNI)</a> enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility">Subnet compatibility for Resolver endpoints</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important>
            outpost_arn: <p>The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the <code>PreferredInstanceType</code>. </p> <note> <p>Resolver endpoints on Outposts are supported on first-generation Outposts only. Inbound and outbound Resolver endpoints aren't supported on second-generation Outposts.</p> </note>
            preferred_instance_type: <p>The instance type. If you specify this, you must also specify a value for the <code>OutpostArn</code>.</p>
            tags: <p>A list of the tag keys and values that you want to associate with the endpoint.</p>
            resolver_endpoint_type: <p> For the endpoint type you can choose either IPv4, IPv6, or dual-stack. A dual-stack endpoint means that it will resolve via both IPv4 and IPv6. This endpoint type is applied to all IP addresses. </p>
            protocols: <p> The protocols you want to use for the endpoint. DoH-FIPS is applicable for default inbound endpoints only. </p> <p>For a default inbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 and DoH-FIPS in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>DoH-FIPS alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <p>For a delegation inbound endpoint you can use Do53 only.</p> <p>For an outbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul>
            rni_enhanced_metrics_enabled: <p>Specifies whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published. Default is false.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>
            target_name_server_metrics_enabled: <p>Specifies whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. Default is false. This is not supported for inbound Resolver endpoints.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>
            dns64_enabled: <p>Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to <code>true</code>, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the <code>64:ff9b::/96</code> prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation. Default is false.</p>
            ipv6_internet_access_enabled: <p>Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to <code>true</code>, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway. Default is false.</p> <important> <p>When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html">Amazon EC2 security group connection tracking</a> and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html">Resolver endpoint scaling</a>.</p> </important>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_resolver_endpoint_request.CreateResolverEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_resolver_endpoint

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_resolver_endpoint.async_create_resolver_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_resolver_endpoint_request.CreateResolverEndpointRequest = {
            "creator_request_id": creator_request_id,
            "security_group_ids": security_group_ids,
            "direction": direction,
            "ip_addresses": ip_addresses,
        }
        if name is not None:
            input_["name"] = name
        if outpost_arn is not None:
            input_["outpost_arn"] = outpost_arn
        if preferred_instance_type is not None:
            input_["preferred_instance_type"] = preferred_instance_type
        if tags is not None:
            input_["tags"] = tags
        if resolver_endpoint_type is not None:
            input_["resolver_endpoint_type"] = resolver_endpoint_type
        if protocols is not None:
            input_["protocols"] = protocols
        if rni_enhanced_metrics_enabled is not None:
            input_["rni_enhanced_metrics_enabled"] = rni_enhanced_metrics_enabled
        if target_name_server_metrics_enabled is not None:
            input_["target_name_server_metrics_enabled"] = (
                target_name_server_metrics_enabled
            )
        if dns64_enabled is not None:
            input_["dns64_enabled"] = dns64_enabled
        if ipv6_internet_access_enabled is not None:
            input_["ipv6_internet_access_enabled"] = ipv6_internet_access_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resolver_query_log_config(
        self,
        name: "capo_route53resolver.types.resolver_query_log_config_name.ResolverQueryLogConfigName",
        destination_arn: "capo_route53resolver.types.destination_arn.DestinationArn",
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
    ) -> "capo_route53resolver.types.create_resolver_query_log_config_response.CreateResolverQueryLogConfigResponse":
        """<p>Creates a Resolver query logging configuration, which defines where you want Resolver to save DNS query logs that originate in your VPCs. Resolver can log queries only for VPCs that are in the same Region as the query logging configuration.</p> <p>To specify which VPCs you want to log queries for, you use <code>AssociateResolverQueryLogConfig</code>. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html">AssociateResolverQueryLogConfig</a>. </p> <p>You can optionally use Resource Access Manager (RAM) to share a query logging configuration with other Amazon Web Services accounts. The other accounts can then associate VPCs with the configuration. The query logs that Resolver creates for a configuration include all DNS queries that originate in all VPCs that are associated with the configuration.</p>

        Args:
            name: <p>The name that you want to give the query logging configuration.</p>
            destination_arn: <p>The ARN of the resource that you want Resolver to send query logs. You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream. Examples of valid values include the following:</p> <ul> <li> <p> <b>S3 bucket</b>: </p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket</code> </p> <p>You can optionally append a file prefix to the end of the ARN.</p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket/development/</code> </p> </li> <li> <p> <b>CloudWatch Logs log group</b>: </p> <p> <code>arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*</code> </p> </li> <li> <p> <b>Kinesis Data Firehose delivery stream</b>:</p> <p> <code>arn:aws:kinesis:us-east-2:0123456789:stream/my_stream_name</code> </p> </li> </ul>
            creator_request_id: <p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            tags: <p>A list of the tag keys and values that you want to associate with the query logging configuration.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_resolver_query_log_config_request.CreateResolverQueryLogConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_resolver_query_log_config_response.CreateResolverQueryLogConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_resolver_query_log_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_resolver_query_log_config.async_create_resolver_query_log_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_resolver_query_log_config_request.CreateResolverQueryLogConfigRequest = {
            "name": name,
            "destination_arn": destination_arn,
            "creator_request_id": creator_request_id,
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

    async def create_resolver_rule(
        self,
        creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId",
        rule_type: "capo_route53resolver.types.rule_type_option.RuleTypeOption",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
        domain_name: Optional[
            "capo_route53resolver.types.domain_name.DomainName"
        ] = None,
        target_ips: Optional[
            "capo_route53resolver.types.target_list.TargetList"
        ] = None,
        resolver_endpoint_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        tags: Optional["capo_route53resolver.types.tag_list.TagList"] = None,
        delegation_record: Optional[
            "capo_route53resolver.types.delegation_record.DelegationRecord"
        ] = None,
    ) -> "capo_route53resolver.types.create_resolver_rule_response.CreateResolverRuleResponse":
        """<p>For DNS queries that originate in your VPCs, specifies which Resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.</p>

        Args:
            creator_request_id: <p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>
            name: <p>A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>
            rule_type: <p>When you want to forward DNS queries for specified domain name to resolvers on your network, specify <code>FORWARD</code> or <code>DELEGATE</code>.</p> <p>When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify <code>SYSTEM</code>.</p> <p>For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify <code>FORWARD</code> for <code>RuleType</code>. To then have Resolver process queries for apex.example.com, you create a rule and specify <code>SYSTEM</code> for <code>RuleType</code>.</p> <p>Currently, only Resolver can create rules that have a value of <code>RECURSIVE</code> for <code>RuleType</code>.</p>
            domain_name: <p>DNS queries for this domain name are forwarded to the IP addresses that you specify in <code>TargetIps</code>. If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).</p>
            target_ips: <p>The IPs that you want Resolver to forward DNS queries to. You can specify either Ipv4 or Ipv6 addresses but not both in the same rule. Separate IP addresses with a space.</p> <p> <code>TargetIps</code> is available only when the value of <code>Rule type</code> is <code>FORWARD</code>. You should not provide TargetIps when the Rule type is <code>DELEGATE</code>.</p> <note> <p>when creating a DELEGATE rule, you must not provide the <code>TargetIps</code> parameter. If you provide the <code>TargetIps</code>, you may receive an ERROR message similar to "Delegate resolver rules need to specify a nameserver name". This error means you should not provide <code>TargetIps</code>.</p> </note>
            resolver_endpoint_id: <p>The ID of the outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in <code>TargetIps</code>.</p>
            tags: <p>A list of the tag keys and values that you want to associate with the endpoint.</p>
            delegation_record: <p> DNS queries with the delegation records that match this domain name are forwarded to the resolvers on your network. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource isn't available.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.create_resolver_rule_request.CreateResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.create_resolver_rule_response.CreateResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.create_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.create_resolver_rule.async_create_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.create_resolver_rule_request.CreateResolverRuleRequest = {
            "creator_request_id": creator_request_id,
            "rule_type": rule_type,
        }
        if name is not None:
            input_["name"] = name
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if target_ips is not None:
            input_["target_ips"] = target_ips
        if resolver_endpoint_id is not None:
            input_["resolver_endpoint_id"] = resolver_endpoint_id
        if tags is not None:
            input_["tags"] = tags
        if delegation_record is not None:
            input_["delegation_record"] = delegation_record

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_firewall_domain_list(
        self,
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_firewall_domain_list_response.DeleteFirewallDomainListResponse":
        """<p>Deletes the specified domain list. </p>

        Args:
            firewall_domain_list_id: <p>The ID of the domain list that you want to delete. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_firewall_domain_list_request.DeleteFirewallDomainListRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_firewall_domain_list_response.DeleteFirewallDomainListResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_firewall_domain_list.async_delete_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_firewall_domain_list_request.DeleteFirewallDomainListRequest = {
            "firewall_domain_list_id": firewall_domain_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_firewall_rule(
        self,
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        firewall_domain_list_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        firewall_threat_protection_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        qtype: Optional["capo_route53resolver.types.qtype.Qtype"] = None,
    ) -> "capo_route53resolver.types.delete_firewall_rule_response.DeleteFirewallRuleResponse":
        """<p>Deletes the specified firewall rule. Identify the rule using either <code>FirewallDomainListId</code> (for domain-list and DNS Firewall Advanced rules) or <code>FirewallThreatProtectionId</code> (for partner-managed and DNS Firewall Advanced rules) — together with <code>FirewallRuleGroupId</code>.</p> <p> <code>DeleteFirewallRule</code> is the only operation that succeeds against a rule whose <code>Status</code> is <code>CREATION_FAILED</code>.</p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group that you want to delete the rule from. </p>
            firewall_domain_list_id: <p>The ID of the domain list that's used in the rule. </p>
            firewall_threat_protection_id: <p> The ID that is created for a DNS Firewall Advanced rule. </p>
            qtype: <p> The DNS query type that the rule you are deleting evaluates. Allowed values are; </p> <ul> <li> <p> A: Returns an IPv4 address.</p> </li> <li> <p>AAAA: Returns an Ipv6 address.</p> </li> <li> <p>CAA: Restricts CAs that can create SSL/TLS certifications for the domain.</p> </li> <li> <p>CNAME: Returns another domain name.</p> </li> <li> <p>DS: Record that identifies the DNSSEC signing key of a delegated zone.</p> </li> <li> <p>MX: Specifies mail servers.</p> </li> <li> <p>NAPTR: Regular-expression-based rewriting of domain names.</p> </li> <li> <p>NS: Authoritative name servers.</p> </li> <li> <p>PTR: Maps an IP address to a domain name.</p> </li> <li> <p>SOA: Start of authority record for the zone.</p> </li> <li> <p>SPF: Lists the servers authorized to send emails from a domain.</p> </li> <li> <p>SRV: Application specific values that identify servers.</p> </li> <li> <p>TXT: Verifies email senders and application-specific values.</p> </li> <li> <p>A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">List of DNS record types</a>.</p> </li> </ul>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_firewall_rule_request.DeleteFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_firewall_rule_response.DeleteFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_firewall_rule.async_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_firewall_rule_request.DeleteFirewallRuleRequest = {
            "firewall_rule_group_id": firewall_rule_group_id
        }
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if firewall_threat_protection_id is not None:
            input_["firewall_threat_protection_id"] = firewall_threat_protection_id
        if qtype is not None:
            input_["qtype"] = qtype

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_firewall_rule_group(
        self,
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_firewall_rule_group_response.DeleteFirewallRuleGroupResponse":
        """<p>Deletes the specified firewall rule group. </p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group that you want to delete. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_firewall_rule_group_request.DeleteFirewallRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_firewall_rule_group_response.DeleteFirewallRuleGroupResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_firewall_rule_group

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_firewall_rule_group.async_delete_firewall_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_firewall_rule_group_request.DeleteFirewallRuleGroupRequest = {
            "firewall_rule_group_id": firewall_rule_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_outpost_resolver(
        self,
        id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_outpost_resolver_response.DeleteOutpostResolverResponse":
        """<p>Deletes a Resolver on the Outpost.</p> <note> <p>This operation applies to first-generation Outposts only. On second-generation Outposts, Resolver is managed automatically by Amazon Web Services and can't be deleted directly. To opt out of Resolver on second-generation Outposts, contact Amazon Web Services Support.</p> </note>

        Args:
            id: <p>A unique string that identifies the Resolver on the Outpost.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_outpost_resolver_request.DeleteOutpostResolverRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_outpost_resolver_response.DeleteOutpostResolverResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_outpost_resolver

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_outpost_resolver.async_delete_outpost_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_outpost_resolver_request.DeleteOutpostResolverRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resolver_endpoint(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_resolver_endpoint_response.DeleteResolverEndpointResponse":
        """<p>Deletes a Resolver endpoint. The effect of deleting a Resolver endpoint depends on whether it's an inbound or an outbound Resolver endpoint:</p> <ul> <li> <p> <b>Inbound</b>: DNS queries from your network are no longer routed to the DNS service for the specified VPC.</p> </li> <li> <p> <b>Outbound</b>: DNS queries from a VPC are no longer routed to your network.</p> </li> </ul>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to delete.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_resolver_endpoint_request.DeleteResolverEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_resolver_endpoint_response.DeleteResolverEndpointResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_resolver_endpoint

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_resolver_endpoint.async_delete_resolver_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_resolver_endpoint_request.DeleteResolverEndpointRequest = {
            "resolver_endpoint_id": resolver_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resolver_query_log_config(
        self,
        resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_resolver_query_log_config_response.DeleteResolverQueryLogConfigResponse":
        """<p>Deletes a query logging configuration. When you delete a configuration, Resolver stops logging DNS queries for all of the Amazon VPCs that are associated with the configuration. This also applies if the query logging configuration is shared with other Amazon Web Services accounts, and the other accounts have associated VPCs with the shared configuration.</p> <p>Before you can delete a query logging configuration, you must first disassociate all VPCs from the configuration. See <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html">DisassociateResolverQueryLogConfig</a>.</p> <p>If you used Resource Access Manager (RAM) to share a query logging configuration with other accounts, you must stop sharing the configuration before you can delete a configuration. The accounts that you shared the configuration with can first disassociate VPCs that they associated with the configuration, but that's not necessary. If you stop sharing the configuration, those VPCs are automatically disassociated from the configuration.</p>

        Args:
            resolver_query_log_config_id: <p>The ID of the query logging configuration that you want to delete.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_resolver_query_log_config_request.DeleteResolverQueryLogConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_resolver_query_log_config_response.DeleteResolverQueryLogConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_resolver_query_log_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_resolver_query_log_config.async_delete_resolver_query_log_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_resolver_query_log_config_request.DeleteResolverQueryLogConfigRequest = {
            "resolver_query_log_config_id": resolver_query_log_config_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resolver_rule(
        self,
        resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.delete_resolver_rule_response.DeleteResolverRuleResponse":
        """<p>Deletes a Resolver rule. Before you can delete a Resolver rule, you must disassociate it from all the VPCs that you associated the Resolver rule with. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html">DisassociateResolverRule</a>.</p>

        Args:
            resolver_rule_id: <p>The ID of the Resolver rule that you want to delete.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you tried to update or delete is currently in use.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.delete_resolver_rule_request.DeleteResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.delete_resolver_rule_response.DeleteResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.delete_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.delete_resolver_rule.async_delete_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.delete_resolver_rule_request.DeleteResolverRuleRequest = {
            "resolver_rule_id": resolver_rule_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_firewall_rule_group(
        self,
        firewall_rule_group_association_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.disassociate_firewall_rule_group_response.DisassociateFirewallRuleGroupResponse":
        """<p>Disassociates a <a>FirewallRuleGroup</a> from a VPC, to remove DNS filtering from the VPC. </p>

        Args:
            firewall_rule_group_association_id: <p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.disassociate_firewall_rule_group_request.DisassociateFirewallRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.disassociate_firewall_rule_group_response.DisassociateFirewallRuleGroupResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.disassociate_firewall_rule_group

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.disassociate_firewall_rule_group.async_disassociate_firewall_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.disassociate_firewall_rule_group_request.DisassociateFirewallRuleGroupRequest = {
            "firewall_rule_group_association_id": firewall_rule_group_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_resolver_endpoint_ip_address(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        ip_address: "capo_route53resolver.types.ip_address_update.IpAddressUpdate",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_response.DisassociateResolverEndpointIpAddressResponse":
        """<p>Removes IP addresses from an inbound or an outbound Resolver endpoint. If you want to remove more than one IP address, submit one <code>DisassociateResolverEndpointIpAddress</code> request for each IP address.</p> <p>To add an IP address to an endpoint, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.html">AssociateResolverEndpointIpAddress</a>. </p>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to disassociate an IP address from.</p>
            ip_address: <p>The IPv4 address that you want to remove from a Resolver endpoint.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_exists_exception.ResourceExistsException: <p>The resource that you tried to create already exists.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_request.DisassociateResolverEndpointIpAddressRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_response.DisassociateResolverEndpointIpAddressResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.disassociate_resolver_endpoint_ip_address

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.disassociate_resolver_endpoint_ip_address.async_disassociate_resolver_endpoint_ip_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.disassociate_resolver_endpoint_ip_address_request.DisassociateResolverEndpointIpAddressRequest = {
            "resolver_endpoint_id": resolver_endpoint_id,
            "ip_address": ip_address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_resolver_query_log_config(
        self,
        resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId",
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.disassociate_resolver_query_log_config_response.DisassociateResolverQueryLogConfigResponse":
        """<p>Disassociates a VPC from a query logging configuration.</p> <note> <p>Before you can delete a query logging configuration, you must first disassociate all VPCs from the configuration. If you used Resource Access Manager (RAM) to share a query logging configuration with other accounts, VPCs can be disassociated from the configuration in the following ways:</p> <ul> <li> <p>The accounts that you shared the configuration with can disassociate VPCs from the configuration.</p> </li> <li> <p>You can stop sharing the configuration.</p> </li> </ul> </note>

        Args:
            resolver_query_log_config_id: <p>The ID of the query logging configuration that you want to disassociate a specified VPC from.</p>
            resource_id: <p>The ID of the Amazon VPC that you want to disassociate from a specified query logging configuration.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.disassociate_resolver_query_log_config_request.DisassociateResolverQueryLogConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.disassociate_resolver_query_log_config_response.DisassociateResolverQueryLogConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.disassociate_resolver_query_log_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.disassociate_resolver_query_log_config.async_disassociate_resolver_query_log_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.disassociate_resolver_query_log_config_request.DisassociateResolverQueryLogConfigRequest = {
            "resolver_query_log_config_id": resolver_query_log_config_id,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_resolver_rule(
        self,
        vpc_id: "capo_route53resolver.types.resource_id.ResourceId",
        resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.disassociate_resolver_rule_response.DisassociateResolverRuleResponse":
        """<p>Removes the association between a specified Resolver rule and a specified VPC.</p> <important> <p>If you disassociate a Resolver rule from a VPC, Resolver stops forwarding DNS queries for the domain name that you specified in the Resolver rule. </p> </important>

        Args:
            vpc_id: <p>The ID of the VPC that you want to disassociate the Resolver rule from.</p>
            resolver_rule_id: <p>The ID of the Resolver rule that you want to disassociate from the specified VPC.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.disassociate_resolver_rule_request.DisassociateResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.disassociate_resolver_rule_response.DisassociateResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.disassociate_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.disassociate_resolver_rule.async_disassociate_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.disassociate_resolver_rule_request.DisassociateResolverRuleRequest = {
            "vpc_id": vpc_id,
            "resolver_rule_id": resolver_rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_firewall_config_response.GetFirewallConfigResponse":
        """<p>Retrieves the configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC). </p>

        Args:
            resource_id: <p>The ID of the VPC from Amazon VPC that the configuration is for.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_firewall_config_request.GetFirewallConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_firewall_config_response.GetFirewallConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_firewall_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_firewall_config.async_get_firewall_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_firewall_config_request.GetFirewallConfigRequest = {
            "resource_id": resource_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_domain_list(
        self,
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_firewall_domain_list_response.GetFirewallDomainListResponse":
        """<p>Retrieves the specified firewall domain list.</p>

        Args:
            firewall_domain_list_id: <p>The ID of the domain list. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_firewall_domain_list_request.GetFirewallDomainListRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_firewall_domain_list_response.GetFirewallDomainListResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_firewall_domain_list.async_get_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_firewall_domain_list_request.GetFirewallDomainListRequest = {
            "firewall_domain_list_id": firewall_domain_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_rule_group(
        self,
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_firewall_rule_group_response.GetFirewallRuleGroupResponse":
        """<p>Retrieves the specified firewall rule group. </p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_firewall_rule_group_request.GetFirewallRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_firewall_rule_group_response.GetFirewallRuleGroupResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_firewall_rule_group

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_firewall_rule_group.async_get_firewall_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_firewall_rule_group_request.GetFirewallRuleGroupRequest = {
            "firewall_rule_group_id": firewall_rule_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_rule_group_association(
        self,
        firewall_rule_group_association_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_firewall_rule_group_association_response.GetFirewallRuleGroupAssociationResponse":
        """<p>Retrieves a firewall rule group association, which enables DNS filtering for a VPC with one rule group. A VPC can have more than one firewall rule group association, and a rule group can be associated with more than one VPC.</p>

        Args:
            firewall_rule_group_association_id: <p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_firewall_rule_group_association_request.GetFirewallRuleGroupAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_firewall_rule_group_association_response.GetFirewallRuleGroupAssociationResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_firewall_rule_group_association

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_firewall_rule_group_association.async_get_firewall_rule_group_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_firewall_rule_group_association_request.GetFirewallRuleGroupAssociationRequest = {
            "firewall_rule_group_association_id": firewall_rule_group_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_firewall_rule_group_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_firewall_rule_group_policy_response.GetFirewallRuleGroupPolicyResponse":
        """<p>Returns the Identity and Access Management (Amazon Web Services IAM) policy for sharing the specified rule group. You can use the policy to share the rule group using Resource Access Manager (RAM). </p>

        Args:
            arn: <p>The ARN (Amazon Resource Name) for the rule group.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_firewall_rule_group_policy_request.GetFirewallRuleGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_firewall_rule_group_policy_response.GetFirewallRuleGroupPolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_firewall_rule_group_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_firewall_rule_group_policy.async_get_firewall_rule_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_firewall_rule_group_policy_request.GetFirewallRuleGroupPolicyRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_outpost_resolver(
        self,
        id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_outpost_resolver_response.GetOutpostResolverResponse":
        """<p>Gets information about a specified Resolver on the Outpost, such as its instance count and type, name, and the current status of the Resolver.</p>

        Args:
            id: <p>The ID of the Resolver on the Outpost.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_outpost_resolver_request.GetOutpostResolverRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_outpost_resolver_response.GetOutpostResolverResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_outpost_resolver

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_outpost_resolver.async_get_outpost_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_outpost_resolver_request.GetOutpostResolverRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_config_response.GetResolverConfigResponse":
        """<p>Retrieves the behavior configuration of Route 53 Resolver behavior for a single VPC from Amazon Virtual Private Cloud.</p>

        Args:
            resource_id: <p>Resource ID of the Amazon VPC that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_config_request.GetResolverConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_config_response.GetResolverConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_config.async_get_resolver_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_config_request.GetResolverConfigRequest = {
            "resource_id": resource_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_dnssec_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_dnssec_config_response.GetResolverDnssecConfigResponse":
        """<p>Gets DNSSEC validation information for a specified resource.</p>

        Args:
            resource_id: <p>The ID of the virtual private cloud (VPC) for the DNSSEC validation status.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_dnssec_config_request.GetResolverDnssecConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_dnssec_config_response.GetResolverDnssecConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_dnssec_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_dnssec_config.async_get_resolver_dnssec_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_dnssec_config_request.GetResolverDnssecConfigRequest = {
            "resource_id": resource_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_endpoint(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_endpoint_response.GetResolverEndpointResponse":
        """<p>Gets information about a specified Resolver endpoint, such as whether it's an inbound or an outbound Resolver endpoint, and the current status of the endpoint.</p>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_endpoint_request.GetResolverEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_endpoint_response.GetResolverEndpointResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_endpoint

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_endpoint.async_get_resolver_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_endpoint_request.GetResolverEndpointRequest = {
            "resolver_endpoint_id": resolver_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_query_log_config(
        self,
        resolver_query_log_config_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_query_log_config_response.GetResolverQueryLogConfigResponse":
        """<p>Gets information about a specified Resolver query logging configuration, such as the number of VPCs that the configuration is logging queries for and the location that logs are sent to. </p>

        Args:
            resolver_query_log_config_id: <p>The ID of the Resolver query logging configuration that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_query_log_config_request.GetResolverQueryLogConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_query_log_config_response.GetResolverQueryLogConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config.async_get_resolver_query_log_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_query_log_config_request.GetResolverQueryLogConfigRequest = {
            "resolver_query_log_config_id": resolver_query_log_config_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_query_log_config_association(
        self,
        resolver_query_log_config_association_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_query_log_config_association_response.GetResolverQueryLogConfigAssociationResponse":
        """<p>Gets information about a specified association between a Resolver query logging configuration and an Amazon VPC. When you associate a VPC with a query logging configuration, Resolver logs DNS queries that originate in that VPC.</p>

        Args:
            resolver_query_log_config_association_id: <p>The ID of the Resolver query logging configuration association that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_query_log_config_association_request.GetResolverQueryLogConfigAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_query_log_config_association_response.GetResolverQueryLogConfigAssociationResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config_association

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config_association.async_get_resolver_query_log_config_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_query_log_config_association_request.GetResolverQueryLogConfigAssociationRequest = {
            "resolver_query_log_config_association_id": resolver_query_log_config_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_query_log_config_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_query_log_config_policy_response.GetResolverQueryLogConfigPolicyResponse":
        """<p>Gets information about a query logging policy. A query logging policy specifies the Resolver query logging operations and resources that you want to allow another Amazon Web Services account to be able to use.</p>

        Args:
            arn: <p>The ARN of the query logging configuration that you want to get the query logging policy for.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.unknown_resource_exception.UnknownResourceException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_query_log_config_policy_request.GetResolverQueryLogConfigPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_query_log_config_policy_response.GetResolverQueryLogConfigPolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_query_log_config_policy.async_get_resolver_query_log_config_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_query_log_config_policy_request.GetResolverQueryLogConfigPolicyRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_rule(
        self,
        resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> (
        "capo_route53resolver.types.get_resolver_rule_response.GetResolverRuleResponse"
    ):
        """<p>Gets information about a specified Resolver rule, such as the domain name that the rule forwards DNS queries for and the ID of the outbound Resolver endpoint that the rule is associated with.</p>

        Args:
            resolver_rule_id: <p>The ID of the Resolver rule that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_rule_request.GetResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_rule_response.GetResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_rule.async_get_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_rule_request.GetResolverRuleRequest = {
            "resolver_rule_id": resolver_rule_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_rule_association(
        self,
        resolver_rule_association_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_rule_association_response.GetResolverRuleAssociationResponse":
        """<p>Gets information about an association between a specified Resolver rule and a VPC. You associate a Resolver rule and a VPC using <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html">AssociateResolverRule</a>. </p>

        Args:
            resolver_rule_association_id: <p>The ID of the Resolver rule association that you want to get information about.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_rule_association_request.GetResolverRuleAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_rule_association_response.GetResolverRuleAssociationResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_rule_association

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_rule_association.async_get_resolver_rule_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_rule_association_request.GetResolverRuleAssociationRequest = {
            "resolver_rule_association_id": resolver_rule_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resolver_rule_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.get_resolver_rule_policy_response.GetResolverRulePolicyResponse":
        """<p>Gets information about the Resolver rule policy for a specified rule. A Resolver rule policy includes the rule that you want to share with another account, the account that you want to share the rule with, and the Resolver operations that you want to allow the account to use. </p>

        Args:
            arn: <p>The ID of the Resolver rule that you want to get the Resolver rule policy for.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.unknown_resource_exception.UnknownResourceException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.get_resolver_rule_policy_request.GetResolverRulePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.get_resolver_rule_policy_response.GetResolverRulePolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.get_resolver_rule_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.get_resolver_rule_policy.async_get_resolver_rule_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.get_resolver_rule_policy_request.GetResolverRulePolicyRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        operation: "capo_route53resolver.types.firewall_domain_import_operation.FirewallDomainImportOperation",
        domain_file_url: "capo_route53resolver.types.domain_list_file_url.DomainListFileUrl",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.import_firewall_domains_response.ImportFirewallDomainsResponse":
        """<p>Imports domain names from a file into a domain list, for use in a DNS firewall rule group. </p> <p>Each domain specification in your domain list must satisfy the following requirements: </p> <ul> <li> <p>It can optionally start with <code>*</code> (asterisk).</p> </li> <li> <p>With the exception of the optional starting asterisk, it must only contain the following characters: <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, <code>-</code> (hyphen).</p> </li> <li> <p>It must be from 1-255 characters in length. </p> </li> </ul>

        Args:
            firewall_domain_list_id: <p>The ID of the domain list that you want to modify with the import operation.</p>
            operation: <p>What you want DNS Firewall to do with the domains that are listed in the file. This must be set to <code>REPLACE</code>, which updates the domain list to exactly match the list in the file. </p>
            domain_file_url: <p>The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.</p> <p>The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.import_firewall_domains_request.ImportFirewallDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.import_firewall_domains_response.ImportFirewallDomainsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.import_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.import_firewall_domains.async_import_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.import_firewall_domains_request.ImportFirewallDomainsRequest = {
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
            "domain_file_url": domain_file_url,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_firewall_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_firewall_configs_max_result.ListFirewallConfigsMaxResult"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_configs_response.ListFirewallConfigsResponse":
        """<p>Retrieves the firewall configurations that you have defined. DNS Firewall uses the configurations to manage firewall behavior for your VPCs. </p> <p>A single call might return only a partial list of the configurations. For information, see <code>MaxResults</code>. </p>

        Args:
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_configs_request.ListFirewallConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_configs_response.ListFirewallConfigsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_configs

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_configs.async_list_firewall_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_configs_request.ListFirewallConfigsRequest = {}
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

    async def iter_list_firewall_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_firewall_configs_max_result.ListFirewallConfigsMaxResult"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_config.FirewallConfig]":
        _token = next_token
        while True:
            _response = await self.list_firewall_configs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_firewall_domain_lists(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_domain_lists_response.ListFirewallDomainListsResponse":
        """<p>Retrieves the firewall domain lists that you have defined. For each firewall domain list, you can retrieve the domains that are defined for a list by calling <a>ListFirewallDomains</a>. </p> <p>A single call to this list operation might return only a partial list of the domain lists. For information, see <code>MaxResults</code>. </p>

        Args:
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_domain_lists_request.ListFirewallDomainListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_domain_lists_response.ListFirewallDomainListsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_domain_lists

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_domain_lists.async_list_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_domain_lists_request.ListFirewallDomainListsRequest = {}
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

    async def iter_list_firewall_domain_lists(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_domain_list_metadata.FirewallDomainListMetadata]":
        _token = next_token
        while True:
            _response = await self.list_firewall_domain_lists(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_domain_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_domain_max_results.ListDomainMaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_domains_response.ListFirewallDomainsResponse":
        """<p>Retrieves the domains that you have defined for the specified firewall domain list. </p> <p>A single call might return only a partial list of the domains. For information, see <code>MaxResults</code>. </p>

        Args:
            firewall_domain_list_id: <p>The ID of the domain list whose domains you want to retrieve. </p>
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_domains_request.ListFirewallDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_domains_response.ListFirewallDomainsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_domains.async_list_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_domains_request.ListFirewallDomainsRequest = {
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
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_domain_max_results.ListDomainMaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_domain_name.FirewallDomainName]":
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

    async def list_firewall_rule_group_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        firewall_rule_group_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        vpc_id: Optional["capo_route53resolver.types.resource_id.ResourceId"] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        status: Optional[
            "capo_route53resolver.types.firewall_rule_group_association_status.FirewallRuleGroupAssociationStatus"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_rule_group_associations_response.ListFirewallRuleGroupAssociationsResponse":
        """<p>Retrieves the firewall rule group associations that you have defined. Each association enables DNS filtering for a VPC with one rule group. </p> <p>A single call might return only a partial list of the associations. For information, see <code>MaxResults</code>. </p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group that you want to retrieve the associations for. Leave this blank to retrieve associations for any rule group. </p>
            vpc_id: <p>The unique identifier of the VPC that you want to retrieve the associations for. Leave this blank to retrieve associations for any VPC. </p>
            priority: <p>The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p>
            status: <p>The association <code>Status</code> setting that you want DNS Firewall to filter on for the list. If you don't specify this, then DNS Firewall returns all associations, regardless of status.</p>
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_rule_group_associations_request.ListFirewallRuleGroupAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_rule_group_associations_response.ListFirewallRuleGroupAssociationsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_rule_group_associations

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_rule_group_associations.async_list_firewall_rule_group_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_rule_group_associations_request.ListFirewallRuleGroupAssociationsRequest = {}
        if firewall_rule_group_id is not None:
            input_["firewall_rule_group_id"] = firewall_rule_group_id
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if priority is not None:
            input_["priority"] = priority
        if status is not None:
            input_["status"] = status
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

    async def iter_list_firewall_rule_group_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        firewall_rule_group_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        vpc_id: Optional["capo_route53resolver.types.resource_id.ResourceId"] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        status: Optional[
            "capo_route53resolver.types.firewall_rule_group_association_status.FirewallRuleGroupAssociationStatus"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_rule_group_association.FirewallRuleGroupAssociation]":
        _token = next_token
        while True:
            _response = await self.list_firewall_rule_group_associations(
                config_overrides=config_overrides,
                firewall_rule_group_id=firewall_rule_group_id,
                vpc_id=vpc_id,
                priority=priority,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_rule_group_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_firewall_rule_groups(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_rule_groups_response.ListFirewallRuleGroupsResponse":
        """<p>Retrieves the minimal high-level information for the rule groups that you have defined. </p> <p>A single call might return only a partial list of the rule groups. For information, see <code>MaxResults</code>. </p>

        Args:
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_rule_groups_request.ListFirewallRuleGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_rule_groups_response.ListFirewallRuleGroupsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_rule_groups

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_rule_groups.async_list_firewall_rule_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_rule_groups_request.ListFirewallRuleGroupsRequest = {}
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

    async def iter_list_firewall_rule_groups(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_rule_group_metadata.FirewallRuleGroupMetadata]":
        _token = next_token
        while True:
            _response = await self.list_firewall_rule_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_rule_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_firewall_rules(
        self,
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        action: Optional["capo_route53resolver.types.action.Action"] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_rules_response.ListFirewallRulesResponse":
        """<p>Retrieves the firewall rules that you have defined for the specified firewall rule group. DNS Firewall uses the rules in a rule group to filter DNS network traffic for a VPC.</p> <p>A single call might return only a partial list of the rules. For information, see <code>MaxResults</code>.</p> <p>For rules that require asynchronous provisioning, the response includes <code>Status</code> (see <a>FirewallRuleStatus</a>) and, on failure, <code>StatusMessage</code> with the reason.</p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group that you want to retrieve the rules for. </p>
            priority: <p>Optional additional filter for the rules to retrieve.</p> <p>The setting that determines the processing order of the rules in a rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>
            action: <p>Optional additional filter for the rules to retrieve.</p> <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through. Not availabe for DNS Firewall Advanced rules.</p> </li> <li> <p> <code>ALERT</code> - Permit the request to go through but send an alert to the logs.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. If this is specified, additional handling details are provided in the rule's <code>BlockResponse</code> setting. </p> </li> </ul>
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>
            next_token: <p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_rules_request.ListFirewallRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_rules_response.ListFirewallRulesResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_rules

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_rules.async_list_firewall_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_rules_request.ListFirewallRulesRequest = {
            "firewall_rule_group_id": firewall_rule_group_id
        }
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action
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

    async def iter_list_firewall_rules(
        self,
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        action: Optional["capo_route53resolver.types.action.Action"] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_rule.FirewallRule]":
        _token = next_token
        while True:
            _response = await self.list_firewall_rules(
                firewall_rule_group_id,
                config_overrides=config_overrides,
                priority=priority,
                action=action,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_firewall_rule_types(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        rule_type: Optional[
            "capo_route53resolver.types.rule_type_name.RuleTypeName"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_firewall_rule_types_response.ListFirewallRuleTypesResponse":
        """<p>Retrieves the rule-type variants that can be used in the <code>FirewallRuleType</code> field of <a>CreateFirewallRule</a> and <a>UpdateFirewallRule</a>. Each returned <a>FirewallRuleTypeDefinition</a> identifies one variant + value combination — for example, <code>FirewallAdvancedContentCategory</code> + <code>VIOLENCE_AND_HATE_SPEECH</code>, or <code>PartnerThreatProtection</code> + a partner-managed feed.</p> <p>The supported <code>RuleType</code> filter values are <code>FirewallAdvancedContentCategory</code>, <code>FirewallAdvancedThreatCategory</code>, <code>DnsThreatProtection</code>, and <code>PartnerThreatProtection</code>. When a returned definition's variant requires an external subscription (currently only <code>PartnerThreatProtection</code>), the response also includes a <a>SubscriptionInfo</a> identifying the Amazon Web Services Marketplace product that backs it; absence of <code>SubscriptionInfo</code> means the variant is fully managed by Amazon Web Services and requires no separate subscription.</p>

        Args:
            rule_type: <p>An optional filter that restricts the response to a single <a>FirewallRuleType</a> variant. Supported values: <code>FirewallAdvancedContentCategory</code>, <code>FirewallAdvancedThreatCategory</code>, <code>DnsThreatProtection</code>, and <code>PartnerThreatProtection</code>. If omitted, definitions across all variants are returned.</p>
            max_results: <p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>For the first call to this list request, omit this value. When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver provides a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_firewall_rule_types_request.ListFirewallRuleTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_firewall_rule_types_response.ListFirewallRuleTypesResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_firewall_rule_types

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_firewall_rule_types.async_list_firewall_rule_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_firewall_rule_types_request.ListFirewallRuleTypesRequest = {}
        if rule_type is not None:
            input_["rule_type"] = rule_type
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

    async def iter_list_firewall_rule_types(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        rule_type: Optional[
            "capo_route53resolver.types.rule_type_name.RuleTypeName"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.firewall_rule_type_definition.FirewallRuleTypeDefinition]":
        _token = next_token
        while True:
            _response = await self.list_firewall_rule_types(
                config_overrides=config_overrides,
                rule_type=rule_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("firewall_rule_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_outpost_resolvers(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        outpost_arn: Optional[
            "capo_route53resolver.types.outpost_arn.OutpostArn"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_outpost_resolvers_response.ListOutpostResolversResponse":
        """<p>Lists all the Resolvers on Outposts that were created using the current Amazon Web Services account.</p>

        Args:
            outpost_arn: <p>The Amazon Resource Name (ARN) of the Outpost.</p>
            max_results: <p>The maximum number of Resolvers on the Outpost that you want to return in the response to a <code>ListOutpostResolver</code> request. If you don't specify a value for <code>MaxResults</code>, the request returns up to 100 Resolvers.</p>
            next_token: <p>For the first <code>ListOutpostResolver</code> request, omit this value.</p> <p></p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_outpost_resolvers_request.ListOutpostResolversRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_outpost_resolvers_response.ListOutpostResolversResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_outpost_resolvers

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_outpost_resolvers.async_list_outpost_resolvers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_outpost_resolvers_request.ListOutpostResolversRequest = {}
        if outpost_arn is not None:
            input_["outpost_arn"] = outpost_arn
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

    async def iter_list_outpost_resolvers(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        outpost_arn: Optional[
            "capo_route53resolver.types.outpost_arn.OutpostArn"
        ] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.outpost_resolver.OutpostResolver]":
        _token = next_token
        while True:
            _response = await self.list_outpost_resolvers(
                config_overrides=config_overrides,
                outpost_arn=outpost_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("outpost_resolvers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_resolver_configs_max_result.ListResolverConfigsMaxResult"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_resolver_configs_response.ListResolverConfigsResponse":
        """<p>Retrieves the Resolver configurations that you have defined. Route 53 Resolver uses the configurations to manage DNS resolution behavior for your VPCs.</p>

        Args:
            max_results: <p>The maximum number of Resolver configurations that you want to return in the response to a <code>ListResolverConfigs</code> request. If you don't specify a value for <code>MaxResults</code>, up to 100 Resolver configurations are returned.</p>
            next_token: <p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> Resolver configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListResolverConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_configs_request.ListResolverConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_configs_response.ListResolverConfigsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_configs

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_configs.async_list_resolver_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_configs_request.ListResolverConfigsRequest = {}
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

    async def iter_list_resolver_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.list_resolver_configs_max_result.ListResolverConfigsMaxResult"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_config.ResolverConfig]":
        _token = next_token
        while True:
            _response = await self.list_resolver_configs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resolver_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_dnssec_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "capo_route53resolver.types.list_resolver_dnssec_configs_response.ListResolverDnssecConfigsResponse":
        """<p>Lists the configurations for DNSSEC validation that are associated with the current Amazon Web Services account.</p>

        Args:
            max_results: <p> <i>Optional</i>: An integer that specifies the maximum number of DNSSEC configuration results that you want Amazon Route 53 to return. If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 100 configuration per page.</p>
            next_token: <p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> DNSSEC configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListResolverDnssecConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>
            filters: <p>An optional specification to return a subset of objects.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_dnssec_configs_request.ListResolverDnssecConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_dnssec_configs_response.ListResolverDnssecConfigsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_dnssec_configs

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_dnssec_configs.async_list_resolver_dnssec_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_dnssec_configs_request.ListResolverDnssecConfigsRequest = {}
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

    async def iter_list_resolver_dnssec_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_dnssec_config.ResolverDnssecConfig]":
        _token = next_token
        while True:
            _response = await self.list_resolver_dnssec_configs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("resolver_dnssec_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_endpoint_ip_addresses(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_resolver_endpoint_ip_addresses_response.ListResolverEndpointIpAddressesResponse":
        """<p>Gets the IP addresses for a specified Resolver endpoint.</p>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to get IP addresses for.</p>
            max_results: <p>The maximum number of IP addresses that you want to return in the response to a <code>ListResolverEndpointIpAddresses</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 IP addresses. </p>
            next_token: <p>For the first <code>ListResolverEndpointIpAddresses</code> request, omit this value.</p> <p>If the specified Resolver endpoint has more than <code>MaxResults</code> IP addresses, you can submit another <code>ListResolverEndpointIpAddresses</code> request to get the next group of IP addresses. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_endpoint_ip_addresses_request.ListResolverEndpointIpAddressesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_endpoint_ip_addresses_response.ListResolverEndpointIpAddressesResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_endpoint_ip_addresses

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_endpoint_ip_addresses.async_list_resolver_endpoint_ip_addresses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_endpoint_ip_addresses_request.ListResolverEndpointIpAddressesRequest = {
            "resolver_endpoint_id": resolver_endpoint_id
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

    async def iter_list_resolver_endpoint_ip_addresses(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.ip_address_response.IpAddressResponse]":
        _token = next_token
        while True:
            _response = await self.list_resolver_endpoint_ip_addresses(
                resolver_endpoint_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ip_addresses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "capo_route53resolver.types.list_resolver_endpoints_response.ListResolverEndpointsResponse":
        """<p>Lists all the Resolver endpoints that were created using the current Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of Resolver endpoints that you want to return in the response to a <code>ListResolverEndpoints</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 Resolver endpoints. </p>
            next_token: <p>For the first <code>ListResolverEndpoints</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> Resolver endpoints, you can submit another <code>ListResolverEndpoints</code> request to get the next group of Resolver endpoints. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>
            filters: <p>An optional specification to return a subset of Resolver endpoints, such as all inbound Resolver endpoints.</p> <note> <p>If you submit a second or subsequent <code>ListResolverEndpoints</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_endpoints_request.ListResolverEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_endpoints_response.ListResolverEndpointsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_endpoints

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_endpoints.async_list_resolver_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_endpoints_request.ListResolverEndpointsRequest = {}
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

    async def iter_list_resolver_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_endpoint.ResolverEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_resolver_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("resolver_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_query_log_config_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
        sort_by: Optional["capo_route53resolver.types.sort_by_key.SortByKey"] = None,
        sort_order: Optional["capo_route53resolver.types.sort_order.SortOrder"] = None,
    ) -> "capo_route53resolver.types.list_resolver_query_log_config_associations_response.ListResolverQueryLogConfigAssociationsResponse":
        """<p>Lists information about associations between Amazon VPCs and query logging configurations.</p>

        Args:
            max_results: <p>The maximum number of query logging associations that you want to return in the response to a <code>ListResolverQueryLogConfigAssociations</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 query logging associations. </p>
            next_token: <p>For the first <code>ListResolverQueryLogConfigAssociations</code> request, omit this value.</p> <p>If there are more than <code>MaxResults</code> query logging associations that match the values that you specify for <code>Filters</code>, you can submit another <code>ListResolverQueryLogConfigAssociations</code> request to get the next group of associations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>
            filters: <p>An optional specification to return a subset of query logging associations.</p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigAssociations</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>
            sort_by: <p>The element that you want Resolver to sort query logging associations by. </p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigAssociations</code> request and specify the <code>NextToken</code> parameter, you must use the same value for <code>SortBy</code>, if any, as in the previous request.</p> </note> <p>Valid values include the following elements:</p> <ul> <li> <p> <code>CreationTime</code>: The ID of the query logging association.</p> </li> <li> <p> <code>Error</code>: If the value of <code>Status</code> is <code>FAILED</code>, the value of <code>Error</code> indicates the cause: </p> <ul> <li> <p> <code>DESTINATION_NOT_FOUND</code>: The specified destination (for example, an Amazon S3 bucket) was deleted.</p> </li> <li> <p> <code>ACCESS_DENIED</code>: Permissions don't allow sending logs to the destination.</p> </li> </ul> <p>If <code>Status</code> is a value other than <code>FAILED</code>, <code>ERROR</code> is null.</p> </li> <li> <p> <code>Id</code>: The ID of the query logging association</p> </li> <li> <p> <code>ResolverQueryLogConfigId</code>: The ID of the query logging configuration</p> </li> <li> <p> <code>ResourceId</code>: The ID of the VPC that is associated with the query logging configuration</p> </li> <li> <p> <code>Status</code>: The current status of the configuration. Valid values include the following:</p> <ul> <li> <p> <code>CREATING</code>: Resolver is creating an association between an Amazon VPC and a query logging configuration.</p> </li> <li> <p> <code>CREATED</code>: The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.</p> </li> <li> <p> <code>DELETING</code>: Resolver is deleting this query logging association.</p> </li> <li> <p> <code>FAILED</code>: Resolver either couldn't create or couldn't delete the query logging association. Here are two common causes:</p> <ul> <li> <p>The specified destination (for example, an Amazon S3 bucket) was deleted.</p> </li> <li> <p>Permissions don't allow sending logs to the destination.</p> </li> </ul> </li> </ul> </li> </ul>
            sort_order: <p>If you specified a value for <code>SortBy</code>, the order that you want query logging associations to be listed in, <code>ASCENDING</code> or <code>DESCENDING</code>.</p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigAssociations</code> request and specify the <code>NextToken</code> parameter, you must use the same value for <code>SortOrder</code>, if any, as in the previous request.</p> </note>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_query_log_config_associations_request.ListResolverQueryLogConfigAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_query_log_config_associations_response.ListResolverQueryLogConfigAssociationsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_query_log_config_associations

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_query_log_config_associations.async_list_resolver_query_log_config_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_query_log_config_associations_request.ListResolverQueryLogConfigAssociationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resolver_query_log_config_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
        sort_by: Optional["capo_route53resolver.types.sort_by_key.SortByKey"] = None,
        sort_order: Optional["capo_route53resolver.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_query_log_config_association.ResolverQueryLogConfigAssociation]":
        _token = next_token
        while True:
            _response = await self.list_resolver_query_log_config_associations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(
                _response, ("resolver_query_log_config_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_query_log_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
        sort_by: Optional["capo_route53resolver.types.sort_by_key.SortByKey"] = None,
        sort_order: Optional["capo_route53resolver.types.sort_order.SortOrder"] = None,
    ) -> "capo_route53resolver.types.list_resolver_query_log_configs_response.ListResolverQueryLogConfigsResponse":
        """<p>Lists information about the specified query logging configurations. Each configuration defines where you want Resolver to save DNS query logs and specifies the VPCs that you want to log queries for.</p>

        Args:
            max_results: <p>The maximum number of query logging configurations that you want to return in the response to a <code>ListResolverQueryLogConfigs</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 query logging configurations. </p>
            next_token: <p>For the first <code>ListResolverQueryLogConfigs</code> request, omit this value.</p> <p>If there are more than <code>MaxResults</code> query logging configurations that match the values that you specify for <code>Filters</code>, you can submit another <code>ListResolverQueryLogConfigs</code> request to get the next group of configurations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>
            filters: <p>An optional specification to return a subset of query logging configurations.</p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigs</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>
            sort_by: <p>The element that you want Resolver to sort query logging configurations by. </p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigs</code> request and specify the <code>NextToken</code> parameter, you must use the same value for <code>SortBy</code>, if any, as in the previous request.</p> </note> <p>Valid values include the following elements:</p> <ul> <li> <p> <code>Arn</code>: The ARN of the query logging configuration</p> </li> <li> <p> <code>AssociationCount</code>: The number of VPCs that are associated with the specified configuration </p> </li> <li> <p> <code>CreationTime</code>: The date and time that Resolver returned when the configuration was created</p> </li> <li> <p> <code>CreatorRequestId</code>: The value that was specified for <code>CreatorRequestId</code> when the configuration was created</p> </li> <li> <p> <code>DestinationArn</code>: The location that logs are sent to</p> </li> <li> <p> <code>Id</code>: The ID of the configuration</p> </li> <li> <p> <code>Name</code>: The name of the configuration</p> </li> <li> <p> <code>OwnerId</code>: The Amazon Web Services account number of the account that created the configuration</p> </li> <li> <p> <code>ShareStatus</code>: Whether the configuration is shared with other Amazon Web Services accounts or shared with the current account by another Amazon Web Services account. Sharing is configured through Resource Access Manager (RAM).</p> </li> <li> <p> <code>Status</code>: The current status of the configuration. Valid values include the following:</p> <ul> <li> <p> <code>CREATING</code>: Resolver is creating the query logging configuration.</p> </li> <li> <p> <code>CREATED</code>: The query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.</p> </li> <li> <p> <code>DELETING</code>: Resolver is deleting this query logging configuration.</p> </li> <li> <p> <code>FAILED</code>: Resolver either couldn't create or couldn't delete the query logging configuration. Here are two common causes:</p> <ul> <li> <p>The specified destination (for example, an Amazon S3 bucket) was deleted.</p> </li> <li> <p>Permissions don't allow sending logs to the destination.</p> </li> </ul> </li> </ul> </li> </ul>
            sort_order: <p>If you specified a value for <code>SortBy</code>, the order that you want query logging configurations to be listed in, <code>ASCENDING</code> or <code>DESCENDING</code>.</p> <note> <p>If you submit a second or subsequent <code>ListResolverQueryLogConfigs</code> request and specify the <code>NextToken</code> parameter, you must use the same value for <code>SortOrder</code>, if any, as in the previous request.</p> </note>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_query_log_configs_request.ListResolverQueryLogConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_query_log_configs_response.ListResolverQueryLogConfigsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_query_log_configs

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_query_log_configs.async_list_resolver_query_log_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_query_log_configs_request.ListResolverQueryLogConfigsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resolver_query_log_configs(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
        sort_by: Optional["capo_route53resolver.types.sort_by_key.SortByKey"] = None,
        sort_order: Optional["capo_route53resolver.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_query_log_config.ResolverQueryLogConfig]":
        _token = next_token
        while True:
            _response = await self.list_resolver_query_log_configs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("resolver_query_log_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_rule_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "capo_route53resolver.types.list_resolver_rule_associations_response.ListResolverRuleAssociationsResponse":
        """<p>Lists the associations that were created between Resolver rules and VPCs using the current Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of rule associations that you want to return in the response to a <code>ListResolverRuleAssociations</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 rule associations. </p>
            next_token: <p>For the first <code>ListResolverRuleAssociation</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> rule associations, you can submit another <code>ListResolverRuleAssociation</code> request to get the next group of rule associations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>
            filters: <p>An optional specification to return a subset of Resolver rules, such as Resolver rules that are associated with the same VPC ID.</p> <note> <p>If you submit a second or subsequent <code>ListResolverRuleAssociations</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_rule_associations_request.ListResolverRuleAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_rule_associations_response.ListResolverRuleAssociationsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_rule_associations

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_rule_associations.async_list_resolver_rule_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_rule_associations_request.ListResolverRuleAssociationsRequest = {}
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

    async def iter_list_resolver_rule_associations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_rule_association.ResolverRuleAssociation]":
        _token = next_token
        while True:
            _response = await self.list_resolver_rule_associations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("resolver_rule_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resolver_rules(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "capo_route53resolver.types.list_resolver_rules_response.ListResolverRulesResponse":
        """<p>Lists the Resolver rules that were created using the current Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of Resolver rules that you want to return in the response to a <code>ListResolverRules</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 Resolver rules.</p>
            next_token: <p>For the first <code>ListResolverRules</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> Resolver rules, you can submit another <code>ListResolverRules</code> request to get the next group of Resolver rules. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>
            filters: <p>An optional specification to return a subset of Resolver rules, such as all Resolver rules that are associated with the same Resolver endpoint.</p> <note> <p>If you submit a second or subsequent <code>ListResolverRules</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_resolver_rules_request.ListResolverRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_resolver_rules_response.ListResolverRulesResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_resolver_rules

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_resolver_rules.async_list_resolver_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_resolver_rules_request.ListResolverRulesRequest = {}
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

    async def iter_list_resolver_rules(
        self,
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
        filters: Optional["capo_route53resolver.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.resolver_rule.ResolverRule]":
        _token = next_token
        while True:
            _response = await self.list_resolver_rules(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("resolver_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_route53resolver.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "capo_route53resolver.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags that you associated with the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that you want to list tags for.</p>
            max_results: <p>The maximum number of tags that you want to return in the response to a <code>ListTagsForResource</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 tags.</p>
            next_token: <p>For the first <code>ListTagsForResource</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> tags, you can submit another <code>ListTagsForResource</code> request to get the next group of tags for the resource. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The value that you specified for <code>NextToken</code> in a <code>List</code> request isn't valid.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_route53resolver.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        max_results: Optional[
            "capo_route53resolver.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53resolver.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_route53resolver.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_firewall_rule_group_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        firewall_rule_group_policy: "capo_route53resolver.types.firewall_rule_group_policy.FirewallRuleGroupPolicy",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.put_firewall_rule_group_policy_response.PutFirewallRuleGroupPolicyResponse":
        """<p>Attaches an Identity and Access Management (Amazon Web Services IAM) policy for sharing the rule group. You can use the policy to share the rule group using Resource Access Manager (RAM). </p>

        Args:
            arn: <p>The ARN (Amazon Resource Name) for the rule group that you want to share.</p>
            firewall_rule_group_policy: <p>The Identity and Access Management (Amazon Web Services IAM) policy to attach to the rule group.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.put_firewall_rule_group_policy_request.PutFirewallRuleGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.put_firewall_rule_group_policy_response.PutFirewallRuleGroupPolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.put_firewall_rule_group_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.put_firewall_rule_group_policy.async_put_firewall_rule_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.put_firewall_rule_group_policy_request.PutFirewallRuleGroupPolicyRequest = {
            "arn": arn,
            "firewall_rule_group_policy": firewall_rule_group_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resolver_query_log_config_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        resolver_query_log_config_policy: "capo_route53resolver.types.resolver_query_log_config_policy.ResolverQueryLogConfigPolicy",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.put_resolver_query_log_config_policy_response.PutResolverQueryLogConfigPolicyResponse":
        """<p>Specifies an Amazon Web Services account that you want to share a query logging configuration with, the query logging configuration that you want to share, and the operations that you want the account to be able to perform on the configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the account that you want to share rules with.</p>
            resolver_query_log_config_policy: <p>An Identity and Access Management policy statement that lists the query logging configurations that you want to share with another Amazon Web Services account and the operations that you want the account to be able to perform. You can specify the following operations in the <code>Actions</code> section of the statement:</p> <ul> <li> <p> <code>route53resolver:AssociateResolverQueryLogConfig</code> </p> </li> <li> <p> <code>route53resolver:DisassociateResolverQueryLogConfig</code> </p> </li> <li> <p> <code>route53resolver:ListResolverQueryLogConfigs</code> </p> </li> </ul> <p>In the <code>Resource</code> section of the statement, you specify the ARNs for the query logging configurations that you want to share with the account that you specified in <code>Arn</code>. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_policy_document.InvalidPolicyDocument: <p>The specified Resolver rule policy is invalid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.unknown_resource_exception.UnknownResourceException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.put_resolver_query_log_config_policy_request.PutResolverQueryLogConfigPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.put_resolver_query_log_config_policy_response.PutResolverQueryLogConfigPolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.put_resolver_query_log_config_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.put_resolver_query_log_config_policy.async_put_resolver_query_log_config_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.put_resolver_query_log_config_policy_request.PutResolverQueryLogConfigPolicyRequest = {
            "arn": arn,
            "resolver_query_log_config_policy": resolver_query_log_config_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resolver_rule_policy(
        self,
        arn: "capo_route53resolver.types.arn.Arn",
        resolver_rule_policy: "capo_route53resolver.types.resolver_rule_policy.ResolverRulePolicy",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.put_resolver_rule_policy_response.PutResolverRulePolicyResponse":
        """<p>Specifies an Amazon Web Services rule that you want to share with another account, the account that you want to share the rule with, and the operations that you want the account to be able to perform on the rule.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the rule that you want to share with another account.</p>
            resolver_rule_policy: <p>An Identity and Access Management policy statement that lists the rules that you want to share with another Amazon Web Services account and the operations that you want the account to be able to perform. You can specify the following operations in the <code>Action</code> section of the statement:</p> <ul> <li> <p> <code>route53resolver:GetResolverRule</code> </p> </li> <li> <p> <code>route53resolver:AssociateResolverRule</code> </p> </li> <li> <p> <code>route53resolver:DisassociateResolverRule</code> </p> </li> <li> <p> <code>route53resolver:ListResolverRules</code> </p> </li> <li> <p> <code>route53resolver:ListResolverRuleAssociations</code> </p> </li> </ul> <p>In the <code>Resource</code> section of the statement, specify the ARN for the rule that you want to share with another account. Specify the same ARN that you specified in <code>Arn</code>.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_policy_document.InvalidPolicyDocument: <p>The specified Resolver rule policy is invalid.</p>
            capo_route53resolver.errors.unknown_resource_exception.UnknownResourceException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.put_resolver_rule_policy_request.PutResolverRulePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.put_resolver_rule_policy_response.PutResolverRulePolicyResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.put_resolver_rule_policy

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.put_resolver_rule_policy.async_put_resolver_rule_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.put_resolver_rule_policy_request.PutResolverRulePolicyRequest = {
            "arn": arn,
            "resolver_rule_policy": resolver_rule_policy,
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
        resource_arn: "capo_route53resolver.types.arn.Arn",
        tags: "capo_route53resolver.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that you want to add tags to. To get the ARN for a resource, use the applicable <code>Get</code> or <code>List</code> command: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html">GetResolverEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html">GetResolverRule</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRuleAssociation.html">GetResolverRuleAssociation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html">ListResolverEndpoints</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html">ListResolverRuleAssociations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html">ListResolverRules</a> </p> </li> </ul>
            tags: <p>The tags that you want to add to the specified resource.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.invalid_tag_exception.InvalidTagException: <p>The specified tag is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.tag_resource

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_route53resolver.types.arn.Arn",
        tag_keys: "capo_route53resolver.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that you want to remove tags from. To get the ARN for a resource, use the applicable <code>Get</code> or <code>List</code> command: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html">GetResolverEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html">GetResolverRule</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRuleAssociation.html">GetResolverRuleAssociation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html">ListResolverEndpoints</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html">ListResolverRuleAssociations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html">ListResolverRules</a> </p> </li> </ul>
            tag_keys: <p>The tags that you want to remove to the specified resource.</p>

        Raises:
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.untag_resource

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_firewall_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        firewall_fail_open: "capo_route53resolver.types.firewall_fail_open_status.FirewallFailOpenStatus",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.update_firewall_config_response.UpdateFirewallConfigResponse":
        """<p>Updates the configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC). </p>

        Args:
            resource_id: <p>The ID of the VPC that the configuration is for.</p>
            firewall_fail_open: <p>Determines how Route 53 Resolver handles queries during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply. </p> <ul> <li> <p>By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall blocks queries that it is unable to evaluate properly. </p> </li> <li> <p>If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them. </p> </li> </ul> <p>This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_firewall_config_request.UpdateFirewallConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_firewall_config_response.UpdateFirewallConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_firewall_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_firewall_config.async_update_firewall_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_firewall_config_request.UpdateFirewallConfigRequest = {
            "resource_id": resource_id,
            "firewall_fail_open": firewall_fail_open,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId",
        operation: "capo_route53resolver.types.firewall_domain_update_operation.FirewallDomainUpdateOperation",
        domains: "capo_route53resolver.types.firewall_domains.FirewallDomains",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.update_firewall_domains_response.UpdateFirewallDomainsResponse":
        """<p>Updates the firewall domain list from an array of domain specifications. </p>

        Args:
            firewall_domain_list_id: <p>The ID of the domain list whose domains you want to update. </p>
            operation: <p>What you want DNS Firewall to do with the domains that you are providing: </p> <ul> <li> <p> <code>ADD</code> - Add the domains to the ones that are already in the domain list. </p> </li> <li> <p> <code>REMOVE</code> - Search the domain list for the domains and remove them from the list.</p> </li> <li> <p> <code>REPLACE</code> - Update the domain list to exactly match the list that you are providing. </p> </li> </ul>
            domains: <p>A list of domains to use in the update operation.</p> <important> <p>There is a limit of 1000 domains per request.</p> </important> <p>Each domain specification in your domain list must satisfy the following requirements: </p> <ul> <li> <p>It can optionally start with <code>*</code> (asterisk).</p> </li> <li> <p>With the exception of the optional starting asterisk, it must only contain the following characters: <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, <code>-</code> (hyphen).</p> </li> <li> <p>It must be from 1-255 characters in length. </p> </li> </ul>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_firewall_domains_request.UpdateFirewallDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_firewall_domains_response.UpdateFirewallDomainsResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_firewall_domains.async_update_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_firewall_domains_request.UpdateFirewallDomainsRequest = {
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
            "domains": domains,
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
        firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        firewall_domain_list_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        firewall_threat_protection_id: Optional[
            "capo_route53resolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        action: Optional["capo_route53resolver.types.action.Action"] = None,
        block_response: Optional[
            "capo_route53resolver.types.block_response.BlockResponse"
        ] = None,
        block_override_domain: Optional[
            "capo_route53resolver.types.block_override_domain.BlockOverrideDomain"
        ] = None,
        block_override_dns_type: Optional[
            "capo_route53resolver.types.block_override_dns_type.BlockOverrideDnsType"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53resolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
        firewall_domain_redirection_action: Optional[
            "capo_route53resolver.types.firewall_domain_redirection_action.FirewallDomainRedirectionAction"
        ] = None,
        qtype: Optional["capo_route53resolver.types.qtype.Qtype"] = None,
        dns_threat_protection: Optional[
            "capo_route53resolver.types.dns_threat_protection.DnsThreatProtection"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53resolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        firewall_rule_type: Optional[
            "capo_route53resolver.types.firewall_rule_type.FirewallRuleType"
        ] = None,
    ) -> "capo_route53resolver.types.update_firewall_rule_response.UpdateFirewallRuleResponse":
        """<p>Updates the specified firewall rule. The rule's <code>FirewallRuleType</code>, <code>FirewallDomainListId</code>, and top-level <code>DnsThreatProtection</code> match source cannot be changed after creation. Rules whose <code>Status</code> is <code>CREATING</code> or <code>CREATION_FAILED</code> cannot be updated; remove a failed rule with <a>DeleteFirewallRule</a>.</p>

        Args:
            firewall_rule_group_id: <p>The unique identifier of the firewall rule group for the rule. </p>
            firewall_domain_list_id: <p>The ID of the domain list to use in the rule. </p>
            firewall_threat_protection_id: <p> The DNS Firewall Advanced rule ID. </p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p> <p>You must specify a unique priority for each rule in a rule group. To make it easier to insert rules later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for the rules in a rule group at any time.</p>
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through. Not available for DNS Firewall Advanced rules.</p> </li> <li> <p> <code>ALERT</code> - Permit the request to go through but send an alert to the logs.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>. </p> </li> </ul>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p> <ul> <li> <p> <code>NODATA</code> - Respond indicating that the query was successful, but no response is available for it.</p> </li> <li> <p> <code>NXDOMAIN</code> - Respond indicating that the domain name that's in the query doesn't exist.</p> </li> <li> <p> <code>OVERRIDE</code> - Provide a custom override in the response. This option requires custom handling details in the rule's <code>BlockOverride*</code> settings. </p> </li> </ul>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            name: <p>The name of the rule.</p>
            firewall_domain_redirection_action: <p> How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME. </p> <p> <code>INSPECT_REDIRECTION_DOMAIN</code>: (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.</p> <p> <code>TRUST_REDIRECTION_DOMAIN</code>: Inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the domain in the redirection list to the domain list.</p>
            qtype: <p> The DNS query type you want the rule to evaluate. Allowed values are; </p> <ul> <li> <p> A: Returns an IPv4 address.</p> </li> <li> <p>AAAA: Returns an Ipv6 address.</p> </li> <li> <p>CAA: Restricts CAs that can create SSL/TLS certifications for the domain.</p> </li> <li> <p>CNAME: Returns another domain name.</p> </li> <li> <p>DS: Record that identifies the DNSSEC signing key of a delegated zone.</p> </li> <li> <p>MX: Specifies mail servers.</p> </li> <li> <p>NAPTR: Regular-expression-based rewriting of domain names.</p> </li> <li> <p>NS: Authoritative name servers.</p> </li> <li> <p>PTR: Maps an IP address to a domain name.</p> </li> <li> <p>SOA: Start of authority record for the zone.</p> </li> <li> <p>SPF: Lists the servers authorized to send emails from a domain.</p> </li> <li> <p>SRV: Application specific values that identify servers.</p> </li> <li> <p>TXT: Verifies email senders and application-specific values.</p> </li> <li> <p>A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">List of DNS record types</a>.</p> <note> <p>If you set up a firewall BLOCK rule with action NXDOMAIN on query type equals AAAA, this action will not be applied to synthetic IPv6 addresses generated when DNS64 is enabled. </p> </note> </li> </ul>
            dns_threat_protection: <p> The type of the DNS Firewall Advanced rule. This setting is mutually exclusive with <code>FirewallDomainListId</code> and <code>FirewallRuleType</code>. Valid values are: </p> <ul> <li> <p> <code>DGA</code>: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.</p> </li> <li> <p> <code>DNS_TUNNELING</code>: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.</p> </li> <li> <p> <code>DICTIONARY_DGA</code>: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.</p> </li> </ul>
            confidence_threshold: <p> The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean: </p> <ul> <li> <p> <code>LOW</code>: Provides the highest detection rate for threats, but also increases false positives.</p> </li> <li> <p> <code>MEDIUM</code>: Provides a balance between detecting threats and false positives.</p> </li> <li> <p> <code>HIGH</code>: Detects only the most well corroborated threats with a low rate of false positives. </p> </li> </ul>
            firewall_rule_type: <p>The rule type configuration for the firewall rule. This is a tagged union — set exactly one of its members. This setting is mutually exclusive with the top-level <code>FirewallDomainListId</code> and <code>DnsThreatProtection</code> fields. Use one of:</p> <ul> <li> <p> <code>FirewallAdvancedContentCategory</code> — match an Amazon Web Services-managed content category (for example, <code>VIOLENCE_AND_HATE_SPEECH</code>).</p> </li> <li> <p> <code>FirewallAdvancedThreatCategory</code> — match an Amazon Web Services-managed advanced threat category (for example, <code>PHISHING</code>).</p> </li> <li> <p> <code>DnsThreatProtection</code> — match a built-in DNS Firewall Advanced threat detector (<code>DGA</code>, <code>DNS_TUNNELING</code>, or <code>DICTIONARY_DGA</code>).</p> </li> <li> <p> <code>PartnerThreatProtection</code> — match a third-party threat feed delivered through Amazon Web Services Marketplace. The selected partner must be an active subscription on the calling account.</p> </li> </ul> <p>To enumerate the values supported in your account, call <a>ListFirewallRuleTypes</a>.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_firewall_rule_request.UpdateFirewallRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_firewall_rule_response.UpdateFirewallRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_firewall_rule.async_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_firewall_rule_request.UpdateFirewallRuleRequest = {
            "firewall_rule_group_id": firewall_rule_group_id
        }
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if firewall_threat_protection_id is not None:
            input_["firewall_threat_protection_id"] = firewall_threat_protection_id
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action
        if block_response is not None:
            input_["block_response"] = block_response
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if name is not None:
            input_["name"] = name
        if firewall_domain_redirection_action is not None:
            input_["firewall_domain_redirection_action"] = (
                firewall_domain_redirection_action
            )
        if qtype is not None:
            input_["qtype"] = qtype
        if dns_threat_protection is not None:
            input_["dns_threat_protection"] = dns_threat_protection
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if firewall_rule_type is not None:
            input_["firewall_rule_type"] = firewall_rule_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_firewall_rule_group_association(
        self,
        firewall_rule_group_association_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        priority: Optional["capo_route53resolver.types.priority.Priority"] = None,
        mutation_protection: Optional[
            "capo_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
        ] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
    ) -> "capo_route53resolver.types.update_firewall_rule_group_association_response.UpdateFirewallRuleGroupAssociationResponse":
        """<p>Changes the association of a <a>FirewallRuleGroup</a> with a VPC. The association enables DNS filtering for the VPC. </p>

        Args:
            firewall_rule_group_association_id: <p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>
            priority: <p>The setting that determines the processing order of the rule group among the rule groups that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p> <p>You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for a rule group association after you create it.</p>
            mutation_protection: <p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. </p>
            name: <p>The name of the rule group association.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_firewall_rule_group_association_request.UpdateFirewallRuleGroupAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_firewall_rule_group_association_response.UpdateFirewallRuleGroupAssociationResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_firewall_rule_group_association

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_firewall_rule_group_association.async_update_firewall_rule_group_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_firewall_rule_group_association_request.UpdateFirewallRuleGroupAssociationRequest = {
            "firewall_rule_group_association_id": firewall_rule_group_association_id
        }
        if priority is not None:
            input_["priority"] = priority
        if mutation_protection is not None:
            input_["mutation_protection"] = mutation_protection
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_outpost_resolver(
        self,
        id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        name: Optional[
            "capo_route53resolver.types.outpost_resolver_name.OutpostResolverName"
        ] = None,
        instance_count: Optional[
            "capo_route53resolver.types.instance_count.InstanceCount"
        ] = None,
        preferred_instance_type: Optional[
            "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
        ] = None,
    ) -> "capo_route53resolver.types.update_outpost_resolver_response.UpdateOutpostResolverResponse":
        """<p>You can use <code>UpdateOutpostResolver</code> to update the instance count, type, or name of a Resolver on an Outpost.</p> <note> <p>This operation applies to first-generation Outposts only. On second-generation Outposts, Resolver is managed automatically by Amazon Web Services and can't be updated directly.</p> </note>

        Args:
            id: <p>A unique string that identifies Resolver on an Outpost.</p>
            name: <p>Name of the Resolver on the Outpost.</p>
            instance_count: <p>The Amazon EC2 instance count for a Resolver on the Outpost.</p>
            preferred_instance_type: <p> Amazon EC2 instance type. </p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.conflict_exception.ConflictException: <p>The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Fulfilling the request would cause one or more quotas to be exceeded.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_outpost_resolver_request.UpdateOutpostResolverRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_outpost_resolver_response.UpdateOutpostResolverResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_outpost_resolver

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_outpost_resolver.async_update_outpost_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_outpost_resolver_request.UpdateOutpostResolverRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if instance_count is not None:
            input_["instance_count"] = instance_count
        if preferred_instance_type is not None:
            input_["preferred_instance_type"] = preferred_instance_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resolver_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        autodefined_reverse_flag: "capo_route53resolver.types.autodefined_reverse_flag.AutodefinedReverseFlag",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.update_resolver_config_response.UpdateResolverConfigResponse":
        """<p>Updates the behavior configuration of Route 53 Resolver behavior for a single VPC from Amazon Virtual Private Cloud.</p>

        Args:
            resource_id: <p>The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.</p>
            autodefined_reverse_flag: <p>Indicates whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. Disabling this option will also affect EC2-Classic instances using ClassicLink. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html">ClassicLink</a> in the <i>Amazon EC2 guide</i>.</p> <important> <p>We are retiring EC2-Classic on August 15, 2022. We recommend that you migrate from EC2-Classic to a VPC. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html">Migrate from EC2-Classic to a VPC</a> in the <i>Amazon EC2 guide</i> and the blog <a href="http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/">EC2-Classic Networking is Retiring – Here’s How to Prepare</a>.</p> </important> <note> <p>It can take some time for the status change to be completed.</p> </note> <p></p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource isn't available.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.validation_exception.ValidationException: <p>You have provided an invalid command. If you ran the <code>UpdateFirewallDomains</code> request. supported values are <code>ADD</code>, <code>REMOVE</code>, or <code>REPLACE</code> a domain.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_resolver_config_request.UpdateResolverConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_resolver_config_response.UpdateResolverConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_resolver_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_resolver_config.async_update_resolver_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_resolver_config_request.UpdateResolverConfigRequest = {
            "resource_id": resource_id,
            "autodefined_reverse_flag": autodefined_reverse_flag,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resolver_dnssec_config(
        self,
        resource_id: "capo_route53resolver.types.resource_id.ResourceId",
        validation: "capo_route53resolver.types.validation.Validation",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.update_resolver_dnssec_config_response.UpdateResolverDnssecConfigResponse":
        """<p>Updates an existing DNSSEC validation configuration. If there is no existing DNSSEC validation configuration, one is created.</p>

        Args:
            resource_id: <p>The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation status for.</p>
            validation: <p>The new value that you are specifying for DNSSEC validation for the VPC. The value can be <code>ENABLE</code> or <code>DISABLE</code>. Be aware that it can take time for a validation status change to be completed.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_resolver_dnssec_config_request.UpdateResolverDnssecConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_resolver_dnssec_config_response.UpdateResolverDnssecConfigResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_resolver_dnssec_config

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_resolver_dnssec_config.async_update_resolver_dnssec_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_resolver_dnssec_config_request.UpdateResolverDnssecConfigRequest = {
            "resource_id": resource_id,
            "validation": validation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resolver_endpoint(
        self,
        resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
        name: Optional["capo_route53resolver.types.name.Name"] = None,
        resolver_endpoint_type: Optional[
            "capo_route53resolver.types.resolver_endpoint_type.ResolverEndpointType"
        ] = None,
        update_ip_addresses: Optional[
            "capo_route53resolver.types.update_ip_addresses.UpdateIpAddresses"
        ] = None,
        protocols: Optional[
            "capo_route53resolver.types.protocol_list.ProtocolList"
        ] = None,
        rni_enhanced_metrics_enabled: Optional[
            "capo_route53resolver.types.rni_enhanced_metrics_enabled.RniEnhancedMetricsEnabled"
        ] = None,
        target_name_server_metrics_enabled: Optional[
            "capo_route53resolver.types.target_name_server_metrics_enabled.TargetNameServerMetricsEnabled"
        ] = None,
        dns64_enabled: Optional[
            "capo_route53resolver.types.dns64_enabled.Dns64Enabled"
        ] = None,
        ipv6_internet_access_enabled: Optional[
            "capo_route53resolver.types.ipv6_internet_access_enabled.Ipv6InternetAccessEnabled"
        ] = None,
    ) -> "capo_route53resolver.types.update_resolver_endpoint_response.UpdateResolverEndpointResponse":
        """<p>Updates the name, or endpoint type for an inbound or an outbound Resolver endpoint. You can only update between IPV4 and DUALSTACK, IPV6 endpoint type can't be updated to other type. </p>

        Args:
            resolver_endpoint_id: <p>The ID of the Resolver endpoint that you want to update.</p>
            name: <p>The name of the Resolver endpoint that you want to update.</p>
            resolver_endpoint_type: <p> Specifies the endpoint type for what type of IP address the endpoint uses to forward DNS queries. </p> <p>Updating to <code>IPV6</code> type isn't currently supported.</p>
            update_ip_addresses: <p> Specifies the IPv6 address when you update the Resolver endpoint from IPv4 to dual-stack. If you don't specify an IPv6 address, one will be automatically chosen from your subnet. </p>
            protocols: <p> The protocols you want to use for the endpoint. DoH-FIPS is applicable for default inbound endpoints only. </p> <p>For a default inbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 and DoH-FIPS in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>DoH-FIPS alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <p>For a delegation inbound endpoint you can use Do53 only.</p> <p>For an outbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <important> <p> You can't change the protocol of an inbound endpoint directly from only Do53 to only DoH, or DoH-FIPS. This is to prevent a sudden disruption to incoming traffic that relies on Do53. To change the protocol from Do53 to DoH, or DoH-FIPS, you must first enable both Do53 and DoH, or Do53 and DoH-FIPS, to make sure that all incoming traffic has transferred to using the DoH protocol, or DoH-FIPS, and then remove the Do53.</p> </important>
            rni_enhanced_metrics_enabled: <p>Updates whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>
            target_name_server_metrics_enabled: <p>Updates whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. This setting is not supported for inbound Resolver endpoints.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>
            dns64_enabled: <p>Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to <code>true</code>, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the <code>64:ff9b::/96</code> prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation.</p>
            ipv6_internet_access_enabled: <p>Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to <code>true</code>, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.</p> <important> <p>When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html">Amazon EC2 security group connection tracking</a> and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html">Resolver endpoint scaling</a>.</p> </important>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_resolver_endpoint_request.UpdateResolverEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_resolver_endpoint_response.UpdateResolverEndpointResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_resolver_endpoint

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_resolver_endpoint.async_update_resolver_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_resolver_endpoint_request.UpdateResolverEndpointRequest = {
            "resolver_endpoint_id": resolver_endpoint_id
        }
        if name is not None:
            input_["name"] = name
        if resolver_endpoint_type is not None:
            input_["resolver_endpoint_type"] = resolver_endpoint_type
        if update_ip_addresses is not None:
            input_["update_ip_addresses"] = update_ip_addresses
        if protocols is not None:
            input_["protocols"] = protocols
        if rni_enhanced_metrics_enabled is not None:
            input_["rni_enhanced_metrics_enabled"] = rni_enhanced_metrics_enabled
        if target_name_server_metrics_enabled is not None:
            input_["target_name_server_metrics_enabled"] = (
                target_name_server_metrics_enabled
            )
        if dns64_enabled is not None:
            input_["dns64_enabled"] = dns64_enabled
        if ipv6_internet_access_enabled is not None:
            input_["ipv6_internet_access_enabled"] = ipv6_internet_access_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resolver_rule(
        self,
        resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId",
        config: "capo_route53resolver.types.resolver_rule_config.ResolverRuleConfig",
        *,
        config_overrides: Optional[AsyncRoute53ResolverClientConfig] = None,
    ) -> "capo_route53resolver.types.update_resolver_rule_response.UpdateResolverRuleResponse":
        """<p>Updates settings for a specified Resolver rule. <code>ResolverRuleId</code> is required, and all other parameters are optional. If you don't specify a parameter, it retains its current value.</p>

        Args:
            resolver_rule_id: <p>The ID of the Resolver rule that you want to update.</p>
            config: <p>The new settings for the Resolver rule.</p>

        Raises:
            capo_route53resolver.errors.access_denied_exception.AccessDeniedException: <p>The current account doesn't have the IAM permissions required to perform the specified Resolver operation.</p> <p>This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.</p>
            capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException: <p>We encountered an unknown error. Try again in a few minutes.</p>
            capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in this request are not valid.</p>
            capo_route53resolver.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException: <p>The request caused one or more limits to be exceeded.</p>
            capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_route53resolver.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource isn't available.</p>
            capo_route53resolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Try again in a few minutes.</p>
            capo_route53resolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53resolver.types.update_resolver_rule_request.UpdateResolverRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_route53resolver.types.update_resolver_rule_response.UpdateResolverRuleResponse"
        ]:
            import capo_route53resolver._operations.route53_resolver.update_resolver_rule

            (
                output,
                http_response,
            ) = await capo_route53resolver._operations.route53_resolver.update_resolver_rule.async_update_resolver_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53resolver.types.update_resolver_rule_request.UpdateResolverRuleRequest = {
            "resolver_rule_id": resolver_rule_id,
            "config": config,
        }

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
