"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ElasticLoadBalancing_v10``."""

import time
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_elastic_load_balancing_v2._auth._signers
import capo_elastic_load_balancing_v2._auth._sigv4
from capo_elastic_load_balancing_v2._async import anysleep
from capo_elastic_load_balancing_v2._auth._identity import Credentials
from capo_elastic_load_balancing_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elastic_load_balancing_v2._auth._zapros_handler import AuthMiddleware
from capo_elastic_load_balancing_v2._pagination import resolve_path as _resolve_path
from capo_elastic_load_balancing_v2._services._aws_config import aaws_config
from capo_elastic_load_balancing_v2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from capo_elastic_load_balancing_v2.errors import (
    ServiceError,
    WaiterTimeoutError,
)

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.actions
    import capo_elastic_load_balancing_v2.types.add_listener_certificates_input
    import capo_elastic_load_balancing_v2.types.add_listener_certificates_output
    import capo_elastic_load_balancing_v2.types.add_tags_input
    import capo_elastic_load_balancing_v2.types.add_tags_output
    import capo_elastic_load_balancing_v2.types.add_trust_store_revocations_input
    import capo_elastic_load_balancing_v2.types.add_trust_store_revocations_output
    import capo_elastic_load_balancing_v2.types.alpn_policy_name
    import capo_elastic_load_balancing_v2.types.certificate
    import capo_elastic_load_balancing_v2.types.certificate_list
    import capo_elastic_load_balancing_v2.types.create_listener_input
    import capo_elastic_load_balancing_v2.types.create_listener_output
    import capo_elastic_load_balancing_v2.types.create_load_balancer_input
    import capo_elastic_load_balancing_v2.types.create_load_balancer_output
    import capo_elastic_load_balancing_v2.types.create_rule_input
    import capo_elastic_load_balancing_v2.types.create_rule_output
    import capo_elastic_load_balancing_v2.types.create_target_group_input
    import capo_elastic_load_balancing_v2.types.create_target_group_output
    import capo_elastic_load_balancing_v2.types.create_trust_store_input
    import capo_elastic_load_balancing_v2.types.create_trust_store_output
    import capo_elastic_load_balancing_v2.types.customer_owned_ipv4_pool
    import capo_elastic_load_balancing_v2.types.delete_listener_input
    import capo_elastic_load_balancing_v2.types.delete_listener_output
    import capo_elastic_load_balancing_v2.types.delete_load_balancer_input
    import capo_elastic_load_balancing_v2.types.delete_load_balancer_output
    import capo_elastic_load_balancing_v2.types.delete_rule_input
    import capo_elastic_load_balancing_v2.types.delete_rule_output
    import capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_input
    import capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_output
    import capo_elastic_load_balancing_v2.types.delete_target_group_input
    import capo_elastic_load_balancing_v2.types.delete_target_group_output
    import capo_elastic_load_balancing_v2.types.delete_trust_store_input
    import capo_elastic_load_balancing_v2.types.delete_trust_store_output
    import capo_elastic_load_balancing_v2.types.deregister_targets_input
    import capo_elastic_load_balancing_v2.types.deregister_targets_output
    import capo_elastic_load_balancing_v2.types.describe_account_limits_input
    import capo_elastic_load_balancing_v2.types.describe_account_limits_output
    import capo_elastic_load_balancing_v2.types.describe_capacity_reservation_input
    import capo_elastic_load_balancing_v2.types.describe_capacity_reservation_output
    import capo_elastic_load_balancing_v2.types.describe_listener_attributes_input
    import capo_elastic_load_balancing_v2.types.describe_listener_attributes_output
    import capo_elastic_load_balancing_v2.types.describe_listener_certificates_input
    import capo_elastic_load_balancing_v2.types.describe_listener_certificates_output
    import capo_elastic_load_balancing_v2.types.describe_listeners_input
    import capo_elastic_load_balancing_v2.types.describe_listeners_output
    import capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_input
    import capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_output
    import capo_elastic_load_balancing_v2.types.describe_load_balancers_input
    import capo_elastic_load_balancing_v2.types.describe_load_balancers_output
    import capo_elastic_load_balancing_v2.types.describe_rules_input
    import capo_elastic_load_balancing_v2.types.describe_rules_output
    import capo_elastic_load_balancing_v2.types.describe_ssl_policies_input
    import capo_elastic_load_balancing_v2.types.describe_ssl_policies_output
    import capo_elastic_load_balancing_v2.types.describe_tags_input
    import capo_elastic_load_balancing_v2.types.describe_tags_output
    import capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input
    import capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output
    import capo_elastic_load_balancing_v2.types.describe_target_groups_input
    import capo_elastic_load_balancing_v2.types.describe_target_groups_output
    import capo_elastic_load_balancing_v2.types.describe_target_health_input
    import capo_elastic_load_balancing_v2.types.describe_target_health_output
    import capo_elastic_load_balancing_v2.types.describe_trust_store_associations_input
    import capo_elastic_load_balancing_v2.types.describe_trust_store_associations_output
    import capo_elastic_load_balancing_v2.types.describe_trust_store_revocation
    import capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_input
    import capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_output
    import capo_elastic_load_balancing_v2.types.describe_trust_stores_input
    import capo_elastic_load_balancing_v2.types.describe_trust_stores_output
    import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum
    import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum
    import capo_elastic_load_balancing_v2.types.get_resource_policy_input
    import capo_elastic_load_balancing_v2.types.get_resource_policy_output
    import capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_input
    import capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_output
    import capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_input
    import capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_output
    import capo_elastic_load_balancing_v2.types.health_check_enabled
    import capo_elastic_load_balancing_v2.types.health_check_interval_seconds
    import capo_elastic_load_balancing_v2.types.health_check_port
    import capo_elastic_load_balancing_v2.types.health_check_threshold_count
    import capo_elastic_load_balancing_v2.types.health_check_timeout_seconds
    import capo_elastic_load_balancing_v2.types.ip_address_type
    import capo_elastic_load_balancing_v2.types.ipam_pools
    import capo_elastic_load_balancing_v2.types.limit
    import capo_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options
    import capo_elastic_load_balancing_v2.types.listener
    import capo_elastic_load_balancing_v2.types.listener_arn
    import capo_elastic_load_balancing_v2.types.listener_arns
    import capo_elastic_load_balancing_v2.types.listener_attributes
    import capo_elastic_load_balancing_v2.types.load_balancer
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.load_balancer_arns
    import capo_elastic_load_balancing_v2.types.load_balancer_attributes
    import capo_elastic_load_balancing_v2.types.load_balancer_name
    import capo_elastic_load_balancing_v2.types.load_balancer_names
    import capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum
    import capo_elastic_load_balancing_v2.types.load_balancer_type_enum
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.matcher
    import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity
    import capo_elastic_load_balancing_v2.types.modify_capacity_reservation_input
    import capo_elastic_load_balancing_v2.types.modify_capacity_reservation_output
    import capo_elastic_load_balancing_v2.types.modify_ip_pools_input
    import capo_elastic_load_balancing_v2.types.modify_ip_pools_output
    import capo_elastic_load_balancing_v2.types.modify_listener_attributes_input
    import capo_elastic_load_balancing_v2.types.modify_listener_attributes_output
    import capo_elastic_load_balancing_v2.types.modify_listener_input
    import capo_elastic_load_balancing_v2.types.modify_listener_output
    import capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_input
    import capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_output
    import capo_elastic_load_balancing_v2.types.modify_rule_input
    import capo_elastic_load_balancing_v2.types.modify_rule_output
    import capo_elastic_load_balancing_v2.types.modify_target_group_attributes_input
    import capo_elastic_load_balancing_v2.types.modify_target_group_attributes_output
    import capo_elastic_load_balancing_v2.types.modify_target_group_input
    import capo_elastic_load_balancing_v2.types.modify_target_group_output
    import capo_elastic_load_balancing_v2.types.modify_trust_store_input
    import capo_elastic_load_balancing_v2.types.modify_trust_store_output
    import capo_elastic_load_balancing_v2.types.mutual_authentication_attributes
    import capo_elastic_load_balancing_v2.types.page_size
    import capo_elastic_load_balancing_v2.types.path
    import capo_elastic_load_balancing_v2.types.port
    import capo_elastic_load_balancing_v2.types.protocol_enum
    import capo_elastic_load_balancing_v2.types.protocol_version
    import capo_elastic_load_balancing_v2.types.register_targets_input
    import capo_elastic_load_balancing_v2.types.register_targets_output
    import capo_elastic_load_balancing_v2.types.remove_ipam_pools
    import capo_elastic_load_balancing_v2.types.remove_listener_certificates_input
    import capo_elastic_load_balancing_v2.types.remove_listener_certificates_output
    import capo_elastic_load_balancing_v2.types.remove_tags_input
    import capo_elastic_load_balancing_v2.types.remove_tags_output
    import capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_input
    import capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_output
    import capo_elastic_load_balancing_v2.types.reset_capacity_reservation
    import capo_elastic_load_balancing_v2.types.reset_transforms
    import capo_elastic_load_balancing_v2.types.resource_arn
    import capo_elastic_load_balancing_v2.types.resource_arns
    import capo_elastic_load_balancing_v2.types.revocation_contents
    import capo_elastic_load_balancing_v2.types.revocation_id
    import capo_elastic_load_balancing_v2.types.revocation_ids
    import capo_elastic_load_balancing_v2.types.rule
    import capo_elastic_load_balancing_v2.types.rule_arn
    import capo_elastic_load_balancing_v2.types.rule_arns
    import capo_elastic_load_balancing_v2.types.rule_condition_list
    import capo_elastic_load_balancing_v2.types.rule_priority
    import capo_elastic_load_balancing_v2.types.rule_priority_list
    import capo_elastic_load_balancing_v2.types.rule_transform_list
    import capo_elastic_load_balancing_v2.types.s3_bucket
    import capo_elastic_load_balancing_v2.types.s3_key
    import capo_elastic_load_balancing_v2.types.s3_object_version
    import capo_elastic_load_balancing_v2.types.security_groups
    import capo_elastic_load_balancing_v2.types.set_ip_address_type_input
    import capo_elastic_load_balancing_v2.types.set_ip_address_type_output
    import capo_elastic_load_balancing_v2.types.set_rule_priorities_input
    import capo_elastic_load_balancing_v2.types.set_rule_priorities_output
    import capo_elastic_load_balancing_v2.types.set_security_groups_input
    import capo_elastic_load_balancing_v2.types.set_security_groups_output
    import capo_elastic_load_balancing_v2.types.set_subnets_input
    import capo_elastic_load_balancing_v2.types.set_subnets_output
    import capo_elastic_load_balancing_v2.types.ssl_policy_name
    import capo_elastic_load_balancing_v2.types.ssl_policy_names
    import capo_elastic_load_balancing_v2.types.subnet_mappings
    import capo_elastic_load_balancing_v2.types.subnets
    import capo_elastic_load_balancing_v2.types.tag_keys
    import capo_elastic_load_balancing_v2.types.tag_list
    import capo_elastic_load_balancing_v2.types.target_control_port
    import capo_elastic_load_balancing_v2.types.target_descriptions
    import capo_elastic_load_balancing_v2.types.target_group
    import capo_elastic_load_balancing_v2.types.target_group_arn
    import capo_elastic_load_balancing_v2.types.target_group_arns
    import capo_elastic_load_balancing_v2.types.target_group_attributes
    import capo_elastic_load_balancing_v2.types.target_group_ip_address_type_enum
    import capo_elastic_load_balancing_v2.types.target_group_name
    import capo_elastic_load_balancing_v2.types.target_group_names
    import capo_elastic_load_balancing_v2.types.target_type_enum
    import capo_elastic_load_balancing_v2.types.trust_store
    import capo_elastic_load_balancing_v2.types.trust_store_arn
    import capo_elastic_load_balancing_v2.types.trust_store_arns
    import capo_elastic_load_balancing_v2.types.trust_store_association
    import capo_elastic_load_balancing_v2.types.trust_store_name
    import capo_elastic_load_balancing_v2.types.trust_store_names
    import capo_elastic_load_balancing_v2.types.vpc_id


class AsyncElasticLoadBalancingv2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncElasticLoadBalancingv2Client:
    """A client for the ``ElasticLoadBalancingv2`` service.

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
        self._config = AsyncElasticLoadBalancingv2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncElasticLoadBalancingv2ClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def add_listener_certificates(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        certificates: Optional[
            "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.add_listener_certificates_output.AddListenerCertificatesOutput":
        """<p>Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.</p> <p>If the certificate in already in the certificate list, the call is successful but the certificate is not added again.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html">SSL certificates</a> in the <i>Application Load Balancers Guide</i> or <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html">Server certificates</a> in the <i>Network Load Balancers Guide</i>.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            certificates: <p>The certificate to add. You can specify one certificate per call. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified certificate does not exist.</p>
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_certificates_exception.TooManyCertificatesException: <p>You've reached the limit on the number of certificates per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.add_listener_certificates_input.AddListenerCertificatesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.add_listener_certificates_output.AddListenerCertificatesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_listener_certificates

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_listener_certificates.async_add_listener_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.add_listener_certificates_input.AddListenerCertificatesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if certificates is not None:
            input_["certificates"] = certificates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        resource_arns: Optional[
            "capo_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
    ) -> "capo_elastic_load_balancing_v2.types.add_tags_output.AddTagsOutput":
        """<p>Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, trust stores, listeners, and rules.</p> <p>Each tag consists of a key and an optional value. If a resource already has a tag with the same key, <code>AddTags</code> updates its value.</p>

        Args:
            resource_arns: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to a load balancer
            This example adds the specified tags to the specified load balancer.

            >>> await client.add_tags(resource_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188'], tags=[{'Key': 'project', 'Value': 'lima'}, {'Key': 'department', 'Value': 'digital-media'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.add_tags_input.AddTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.add_tags_output.AddTagsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_tags

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.add_tags_input.AddTagsInput = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_trust_store_revocations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        revocation_contents: Optional[
            "capo_elastic_load_balancing_v2.types.revocation_contents.RevocationContents"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput":
        """<p>Adds the specified revocation file to the specified trust store.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            revocation_contents: <p>The revocation file to add.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_revocation_content_exception.InvalidRevocationContentException: <p>The provided revocation file is an invalid format, or uses an incorrect algorithm.</p>
            capo_elastic_load_balancing_v2.errors.revocation_content_not_found_exception.RevocationContentNotFoundException: <p>The specified revocation file does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_trust_store_revocation_entries_exception.TooManyTrustStoreRevocationEntriesException: <p>The specified trust store has too many revocation entries.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.add_trust_store_revocations_input.AddTrustStoreRevocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_trust_store_revocations

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.add_trust_store_revocations.async_add_trust_store_revocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.add_trust_store_revocations_input.AddTrustStoreRevocationsInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if revocation_contents is not None:
            input_["revocation_contents"] = revocation_contents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_listener(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        protocol: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
        ] = None,
        port: Optional["capo_elastic_load_balancing_v2.types.port.Port"] = None,
        ssl_policy: Optional[
            "capo_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
        ] = None,
        certificates: Optional[
            "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
        ] = None,
        default_actions: Optional[
            "capo_elastic_load_balancing_v2.types.actions.Actions"
        ] = None,
        alpn_policy: Optional[
            "capo_elastic_load_balancing_v2.types.alpn_policy_name.AlpnPolicyName"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
        mutual_authentication: Optional[
            "capo_elastic_load_balancing_v2.types.mutual_authentication_attributes.MutualAuthenticationAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput":
        """<p>Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html">Listeners for your Application Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html">Listeners for your Network Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html">Listeners for your Gateway Load Balancers</a> </p> </li> </ul> <p>This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            protocol: <p>The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC. You can’t specify the UDP, TCP_UDP, QUIC, or TCP_QUIC protocol if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.</p>
            port: <p>The port on which the load balancer is listening. You can't specify a port for a Gateway Load Balancer.</p>
            ssl_policy: <p>[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html">Security policies</a> in the <i>Application Load Balancers Guide</i> and <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html">Security policies</a> in the <i>Network Load Balancers Guide</i>.</p>
            certificates: <p>[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>
            default_actions: <p>The actions for the default rule.</p>
            alpn_policy: <p>[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:</p> <ul> <li> <p> <code>HTTP1Only</code> </p> </li> <li> <p> <code>HTTP2Only</code> </p> </li> <li> <p> <code>HTTP2Optional</code> </p> </li> <li> <p> <code>HTTP2Preferred</code> </p> </li> <li> <p> <code>None</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies">ALPN policies</a> in the <i>Network Load Balancers Guide</i>.</p>
            tags: <p>The tags to assign to the listener.</p>
            mutual_authentication: <p>[HTTPS listeners] The mutual authentication configuration information.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception.ALPNPolicyNotSupportedException: <p>The specified ALPN policy is not supported.</p>
            capo_elastic_load_balancing_v2.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified certificate does not exist.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_listener_exception.DuplicateListenerException: <p>A listener with the specified port already exists.</p>
            capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException: <p>The specified configuration is not valid with this protocol.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException: <p>The requested action is not valid.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception.SSLPolicyNotFoundException: <p>The specified SSL policy does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException: <p>You've reached the limit on the number of load balancers per target group.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException: <p>You've reached the limit on the number of actions per rule.</p>
            capo_elastic_load_balancing_v2.errors.too_many_certificates_exception.TooManyCertificatesException: <p>You've reached the limit on the number of certificates per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_listeners_exception.TooManyListenersException: <p>You've reached the limit on the number of listeners per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException: <p>You've reached the limit on the number of times a target can be registered with a load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException: <p>You've reached the limit on the number of targets.</p>
            capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException: <p>You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_ready_exception.TrustStoreNotReadyException: <p>The specified trust store is not active.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an HTTP listener
            This example creates an HTTP listener for the specified load balancer that forwards requests to the specified target group.

            >>> await client.create_listener(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', protocol='HTTP', port=80, default_actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'}])
            To create an HTTPS listener
            This example creates an HTTPS listener for the specified load balancer that forwards requests to the specified target group. Note that you must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).

            >>> await client.create_listener(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', protocol='HTTPS', port=443, ssl_policy='ELBSecurityPolicy-2015-05', certificates=[{'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-server-cert'}], default_actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_listener

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_listener.async_create_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if protocol is not None:
            input_["protocol"] = protocol
        if port is not None:
            input_["port"] = port
        if ssl_policy is not None:
            input_["ssl_policy"] = ssl_policy
        if certificates is not None:
            input_["certificates"] = certificates
        if default_actions is not None:
            input_["default_actions"] = default_actions
        if alpn_policy is not None:
            input_["alpn_policy"] = alpn_policy
        if tags is not None:
            input_["tags"] = tags
        if mutual_authentication is not None:
            input_["mutual_authentication"] = mutual_authentication

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_load_balancer(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        name: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_name.LoadBalancerName"
        ] = None,
        subnets: Optional[
            "capo_elastic_load_balancing_v2.types.subnets.Subnets"
        ] = None,
        subnet_mappings: Optional[
            "capo_elastic_load_balancing_v2.types.subnet_mappings.SubnetMappings"
        ] = None,
        security_groups: Optional[
            "capo_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
        ] = None,
        scheme: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum.LoadBalancerSchemeEnum"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
        type: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_type_enum.LoadBalancerTypeEnum"
        ] = None,
        ip_address_type: Optional[
            "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
        ] = None,
        customer_owned_ipv4_pool: Optional[
            "capo_elastic_load_balancing_v2.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
        ] = None,
        enable_prefix_for_ipv6_source_nat: Optional[
            "capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
        ] = None,
        ipam_pools: Optional[
            "capo_elastic_load_balancing_v2.types.ipam_pools.IpamPools"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.create_load_balancer_output.CreateLoadBalancerOutput":
        """<p>Creates an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html">Application Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html">Network Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html">Gateway Load Balancers</a> </p> </li> </ul> <p>This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.</p>

        Args:
            name: <p>The name of the load balancer.</p> <p>This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".</p>
            subnets: <p>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers and Gateway Load Balancers] You can specify subnets from one or more Availability Zones.</p>
            subnet_mappings: <p>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You can't specify Elastic IP addresses for your subnets.</p>
            security_groups: <p>[Application Load Balancers and Network Load Balancers] The IDs of the security groups for the load balancer.</p>
            scheme: <p>The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.</p> <p>The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.</p> <p>The default is an Internet-facing load balancer.</p> <p>You can't specify a scheme for a Gateway Load Balancer.</p>
            tags: <p>The tags to assign to the load balancer.</p>
            type: <p>The type of load balancer. The default is <code>application</code>.</p>
            ip_address_type: <p>The IP address type. Internal load balancers must use <code>ipv4</code>.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>
            customer_owned_ipv4_pool: <p>[Application Load Balancers on Outposts] The ID of the customer-owned address pool (CoIP pool).</p>
            enable_prefix_for_ipv6_source_nat: <p>[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</p>
            ipam_pools: <p>[Application Load Balancers] The IPAM pools to use with the load balancer.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.allocation_id_not_found_exception.AllocationIdNotFoundException: <p>The specified allocation ID does not exist.</p>
            capo_elastic_load_balancing_v2.errors.availability_zone_not_supported_exception.AvailabilityZoneNotSupportedException: <p>The specified Availability Zone is not supported.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_load_balancer_name_exception.DuplicateLoadBalancerNameException: <p>A load balancer with the specified name already exists.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_scheme_exception.InvalidSchemeException: <p>The requested scheme is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_security_group_exception.InvalidSecurityGroupException: <p>The specified security group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.invalid_subnet_exception.InvalidSubnetException: <p>The specified subnet is out of available addresses.</p>
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.resource_in_use_exception.ResourceInUseException: <p>A specified resource is in use.</p>
            capo_elastic_load_balancing_v2.errors.subnet_not_found_exception.SubnetNotFoundException: <p>The specified subnet does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_load_balancers_exception.TooManyLoadBalancersException: <p>You've reached the limit on the number of load balancers for your Amazon Web Services account.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an Internet-facing load balancer
            This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.

            >>> await client.create_load_balancer(name='my-load-balancer', subnets=['subnet-b7d581c0', 'subnet-8360a9e7'])
            To create an internal load balancer
            This example creates an internal load balancer and enables the Availability Zones for the specified subnets.

            >>> await client.create_load_balancer(name='my-internal-load-balancer', subnets=['subnet-b7d581c0', 'subnet-8360a9e7'], security_groups=[], scheme='internal')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.create_load_balancer_input.CreateLoadBalancerInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.create_load_balancer_output.CreateLoadBalancerOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_load_balancer

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_load_balancer.async_create_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.create_load_balancer_input.CreateLoadBalancerInput = {}
        if name is not None:
            input_["name"] = name
        if subnets is not None:
            input_["subnets"] = subnets
        if subnet_mappings is not None:
            input_["subnet_mappings"] = subnet_mappings
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if scheme is not None:
            input_["scheme"] = scheme
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if customer_owned_ipv4_pool is not None:
            input_["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
        if enable_prefix_for_ipv6_source_nat is not None:
            input_["enable_prefix_for_ipv6_source_nat"] = (
                enable_prefix_for_ipv6_source_nat
            )
        if ipam_pools is not None:
            input_["ipam_pools"] = ipam_pools

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_rule(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        conditions: Optional[
            "capo_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
        ] = None,
        priority: Optional[
            "capo_elastic_load_balancing_v2.types.rule_priority.RulePriority"
        ] = None,
        actions: Optional[
            "capo_elastic_load_balancing_v2.types.actions.Actions"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
        transforms: Optional[
            "capo_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.create_rule_output.CreateRuleOutput":
        """<p>Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer or a dual-stack Network Load Balancer.</p> <p>Each rule consists of a priority, one or more actions, and one or more conditions. Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules">Listener rules</a> in the <i>Application Load Balancers Guide</i> or <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#listener-rules">Listener rules</a> in the <i>Network Load Balancers Guide</i>.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            conditions: <p>The conditions.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            actions: <p>The actions.</p>
            tags: <p>The tags to assign to the rule.</p>
            transforms: <p>The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException: <p>The specified configuration is not valid with this protocol.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException: <p>The requested action is not valid.</p>
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.priority_in_use_exception.PriorityInUseException: <p>The specified priority is in use.</p>
            capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException: <p>You've reached the limit on the number of load balancers per target group.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException: <p>You've reached the limit on the number of actions per rule.</p>
            capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException: <p>You've reached the limit on the number of times a target can be registered with a load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_rules_exception.TooManyRulesException: <p>You've reached the limit on the number of rules per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.too_many_target_groups_exception.TooManyTargetGroupsException: <p>You've reached the limit on the number of target groups for your Amazon Web Services account.</p>
            capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException: <p>You've reached the limit on the number of targets.</p>
            capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException: <p>You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a rule
            This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/*).

            >>> await client.create_rule(listener_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2', conditions=[{'Field': 'path-pattern', 'Values': ['/img/*']}], priority=10, actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'}])
            To create a listener rule that routes IPv4 traffic on a Network Load Balancer
            This example creates a rule on a dual-stack Network Load Balancer that routes IPv4 source traffic to an IPv4 target group.

            >>> await client.create_rule(listener_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/net/my-nlb/1234567890abcdef/1234567890abcdef', conditions=[{'Field': 'source-ip', 'SourceIpConfig': {'IpAddressType': 'ipv4'}}], priority=10, actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-ipv4-targets/1234567890abcdef'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.create_rule_input.CreateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_rule

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.create_rule_input.CreateRuleInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if conditions is not None:
            input_["conditions"] = conditions
        if priority is not None:
            input_["priority"] = priority
        if actions is not None:
            input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags
        if transforms is not None:
            input_["transforms"] = transforms

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_target_group(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        name: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_name.TargetGroupName"
        ] = None,
        protocol: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
        ] = None,
        protocol_version: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_version.ProtocolVersion"
        ] = None,
        port: Optional["capo_elastic_load_balancing_v2.types.port.Port"] = None,
        vpc_id: Optional["capo_elastic_load_balancing_v2.types.vpc_id.VpcId"] = None,
        health_check_protocol: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
        ] = None,
        health_check_port: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
        ] = None,
        health_check_enabled: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_enabled.HealthCheckEnabled"
        ] = None,
        health_check_path: Optional[
            "capo_elastic_load_balancing_v2.types.path.Path"
        ] = None,
        health_check_interval_seconds: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
        ] = None,
        health_check_timeout_seconds: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
        ] = None,
        healthy_threshold_count: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
        ] = None,
        unhealthy_threshold_count: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
        ] = None,
        matcher: Optional[
            "capo_elastic_load_balancing_v2.types.matcher.Matcher"
        ] = None,
        target_type: Optional[
            "capo_elastic_load_balancing_v2.types.target_type_enum.TargetTypeEnum"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
        ip_address_type: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_ip_address_type_enum.TargetGroupIpAddressTypeEnum"
        ] = None,
        target_control_port: Optional[
            "capo_elastic_load_balancing_v2.types.target_control_port.TargetControlPort"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.create_target_group_output.CreateTargetGroupOutput":
        """<p>Creates a target group.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html">Target groups for your Application Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html">Target groups for your Network Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html">Target groups for your Gateway Load Balancers</a> </p> </li> </ul> <p>This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.</p>

        Args:
            name: <p>The name of the target group.</p> <p>This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p>
            protocol: <p>The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP_UDP, QUIC, or TCP_QUIC. For Gateway Load Balancers, the supported protocol is GENEVE. A TCP_UDP listener must be associated with a TCP_UDP target group. A TCP_QUIC listener must be associated with a TCP_QUIC target group. If the target is a Lambda function, this parameter does not apply.</p>
            protocol_version: <p>[HTTP/HTTPS protocol] The protocol version. Specify <code>GRPC</code> to send requests to targets using gRPC. Specify <code>HTTP2</code> to send requests to targets using HTTP/2. The default is <code>HTTP1</code>, which sends requests to targets using HTTP/1.1.</p>
            port: <p>The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.</p>
            vpc_id: <p>The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.</p>
            health_check_protocol: <p>The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. The GENEVE, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols are not supported for health checks.</p>
            health_check_port: <p>The port the load balancer uses when performing health checks on targets. If the protocol is HTTP, HTTPS, TCP, TLS, UDP, TCP_UDP, QUIC, or TCP_QUIC the default is <code>traffic-port</code>, which is the port on which each target receives traffic from the load balancer. If the protocol is GENEVE, the default is port 80.</p>
            health_check_enabled: <p>Indicates whether health checks are enabled. If the target type is <code>lambda</code>, health checks are disabled by default but can be enabled. If the target type is <code>instance</code>, <code>ip</code>, or <code>alb</code>, health checks are always enabled and can't be disabled.</p>
            health_check_path: <p>[HTTP/HTTPS health checks] The destination for health checks on the targets.</p> <p>[HTTP1 or HTTP2 protocol version] The ping path. The default is /.</p> <p>[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.</p>
            health_check_interval_seconds: <p>The approximate amount of time, in seconds, between health checks of an individual target. The range is 5-300. If the target group protocol is TCP, TLS, UDP, TCP_UDP, QUIC, TCP_QUIC, HTTP or HTTPS, the default is 30 seconds. If the target group protocol is GENEVE, the default is 10 seconds. If the target type is <code>lambda</code>, the default is 35 seconds.</p>
            health_check_timeout_seconds: <p>The amount of time, in seconds, during which no response from a target means a failed health check. The range is 2–120 seconds. For target groups with a protocol of HTTP, the default is 6 seconds. For target groups with a protocol of TCP, TLS or HTTPS, the default is 10 seconds. For target groups with a protocol of GENEVE, the default is 5 seconds. If the target type is <code>lambda</code>, the default is 30 seconds.</p>
            healthy_threshold_count: <p>The number of consecutive health check successes required before considering a target healthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 5. For target groups with a protocol of GENEVE, the default is 5. If the target type is <code>lambda</code>, the default is 5.</p>
            unhealthy_threshold_count: <p>The number of consecutive health check failures required before considering a target unhealthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, QUIC, TCP_QUIC, HTTP or HTTPS, the default is 2. For target groups with a protocol of GENEVE, the default is 2. If the target type is <code>lambda</code>, the default is 5.</p>
            matcher: <p>[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP, QUIC, TCP_QUIC, or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.</p>
            target_type: <p>The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.</p> <ul> <li> <p> <code>instance</code> - Register targets by instance ID. This is the default value.</p> </li> <li> <p> <code>ip</code> - Register targets by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.</p> </li> <li> <p> <code>lambda</code> - Register a single Lambda function as a target.</p> </li> <li> <p> <code>alb</code> - Register a single Application Load Balancer as a target.</p> </li> </ul>
            tags: <p>The tags to assign to the target group.</p>
            ip_address_type: <p>The IP address type. The default value is <code>ipv4</code>.</p>
            target_control_port: <p>The port on which the target control agent and application load balancer exchange management traffic for the target optimizer feature.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.duplicate_target_group_name_exception.DuplicateTargetGroupNameException: <p>A target group with the specified name already exists.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.too_many_target_groups_exception.TooManyTargetGroupsException: <p>You've reached the limit on the number of target groups for your Amazon Web Services account.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a target group
            This example creates a target group that you can use to route traffic to targets using HTTP on port 80. This target group uses the default health check configuration.

            >>> await client.create_target_group(name='my-targets', protocol='HTTP', port=80, vpc_id='vpc-3ac0fb5f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.create_target_group_input.CreateTargetGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.create_target_group_output.CreateTargetGroupOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_target_group

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_target_group.async_create_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.create_target_group_input.CreateTargetGroupInput = {}
        if name is not None:
            input_["name"] = name
        if protocol is not None:
            input_["protocol"] = protocol
        if protocol_version is not None:
            input_["protocol_version"] = protocol_version
        if port is not None:
            input_["port"] = port
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if health_check_protocol is not None:
            input_["health_check_protocol"] = health_check_protocol
        if health_check_port is not None:
            input_["health_check_port"] = health_check_port
        if health_check_enabled is not None:
            input_["health_check_enabled"] = health_check_enabled
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if health_check_interval_seconds is not None:
            input_["health_check_interval_seconds"] = health_check_interval_seconds
        if health_check_timeout_seconds is not None:
            input_["health_check_timeout_seconds"] = health_check_timeout_seconds
        if healthy_threshold_count is not None:
            input_["healthy_threshold_count"] = healthy_threshold_count
        if unhealthy_threshold_count is not None:
            input_["unhealthy_threshold_count"] = unhealthy_threshold_count
        if matcher is not None:
            input_["matcher"] = matcher
        if target_type is not None:
            input_["target_type"] = target_type
        if tags is not None:
            input_["tags"] = tags
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if target_control_port is not None:
            input_["target_control_port"] = target_control_port

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_trust_store(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        name: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_name.TrustStoreName"
        ] = None,
        ca_certificates_bundle_s3_bucket: Optional[
            "capo_elastic_load_balancing_v2.types.s3_bucket.S3Bucket"
        ] = None,
        ca_certificates_bundle_s3_key: Optional[
            "capo_elastic_load_balancing_v2.types.s3_key.S3Key"
        ] = None,
        ca_certificates_bundle_s3_object_version: Optional[
            "capo_elastic_load_balancing_v2.types.s3_object_version.S3ObjectVersion"
        ] = None,
        tags: Optional["capo_elastic_load_balancing_v2.types.tag_list.TagList"] = None,
    ) -> "capo_elastic_load_balancing_v2.types.create_trust_store_output.CreateTrustStoreOutput":
        """<p>Creates a trust store.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html">Mutual TLS for Application Load Balancers</a>.</p>

        Args:
            name: <p>The name of the trust store.</p> <p>This name must be unique per region and can't be changed after creation.</p>
            ca_certificates_bundle_s3_bucket: <p>The Amazon S3 bucket for the ca certificates bundle.</p>
            ca_certificates_bundle_s3_key: <p>The Amazon S3 path for the ca certificates bundle.</p>
            ca_certificates_bundle_s3_object_version: <p>The Amazon S3 object version for the ca certificates bundle. If undefined the current version is used.</p>
            tags: <p>The tags to assign to the trust store.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.ca_certificates_bundle_not_found_exception.CaCertificatesBundleNotFoundException: <p>The specified ca certificate bundle does not exist.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_trust_store_name_exception.DuplicateTrustStoreNameException: <p>A trust store with the specified name already exists.</p>
            capo_elastic_load_balancing_v2.errors.invalid_ca_certificates_bundle_exception.InvalidCaCertificatesBundleException: <p>The specified ca certificate bundle is in an invalid format, or corrupt.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.too_many_trust_stores_exception.TooManyTrustStoresException: <p>You've reached the limit on the number of trust stores for your Amazon Web Services account.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.create_trust_store_input.CreateTrustStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.create_trust_store_output.CreateTrustStoreOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_trust_store

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.create_trust_store.async_create_trust_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.create_trust_store_input.CreateTrustStoreInput = {}
        if name is not None:
            input_["name"] = name
        if ca_certificates_bundle_s3_bucket is not None:
            input_["ca_certificates_bundle_s3_bucket"] = (
                ca_certificates_bundle_s3_bucket
            )
        if ca_certificates_bundle_s3_key is not None:
            input_["ca_certificates_bundle_s3_key"] = ca_certificates_bundle_s3_key
        if ca_certificates_bundle_s3_object_version is not None:
            input_["ca_certificates_bundle_s3_object_version"] = (
                ca_certificates_bundle_s3_object_version
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_listener(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_listener_output.DeleteListenerOutput":
        """<p>Deletes the specified listener.</p> <p>Alternatively, your listener is deleted when you delete the load balancer to which it is attached.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.resource_in_use_exception.ResourceInUseException: <p>A specified resource is in use.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a listener
            This example deletes the specified listener.

            >>> await client.delete_listener(listener_arn='arn:aws:elasticloadbalancing:ua-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_listener_input.DeleteListenerInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_listener_output.DeleteListenerOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_listener

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_listener.async_delete_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_listener_input.DeleteListenerInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_load_balancer(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_load_balancer_output.DeleteLoadBalancerOutput":
        """<p>Deletes the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. Deleting a load balancer also deletes its listeners.</p> <p>You can't delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.</p> <p>Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.resource_in_use_exception.ResourceInUseException: <p>A specified resource is in use.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a load balancer
            This example deletes the specified load balancer.

            >>> await client.delete_load_balancer(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_load_balancer_input.DeleteLoadBalancerInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_load_balancer_output.DeleteLoadBalancerOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_load_balancer

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_load_balancer.async_delete_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_load_balancer_input.DeleteLoadBalancerInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        rule_arn: Optional[
            "capo_elastic_load_balancing_v2.types.rule_arn.RuleArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_rule_output.DeleteRuleOutput":
        """<p>Deletes the specified rule.</p> <p>You can't delete the default rule.</p>

        Args:
            rule_arn: <p>The Amazon Resource Name (ARN) of the rule.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a rule
            This example deletes the specified rule.

            >>> await client.delete_rule(rule_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_rule_input.DeleteRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_rule_output.DeleteRuleOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_rule

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_rule_input.DeleteRuleInput = {}
        if rule_arn is not None:
            input_["rule_arn"] = rule_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_shared_trust_store_association(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        resource_arn: Optional[
            "capo_elastic_load_balancing_v2.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_output.DeleteSharedTrustStoreAssociationOutput":
        """<p>Deletes a shared trust store association.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.delete_association_same_account_exception.DeleteAssociationSameAccountException: <p>The specified association can't be within the same account.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_association_not_found_exception.TrustStoreAssociationNotFoundException: <p>The specified association does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a shared trust store association
            This example deletes the association between the specified trust store and the specified load balancer.

            >>> await client.delete_shared_trust_store_association(trust_store_arn='arn:aws:elasticloadbalancing:us-east-1:123456789012:truststore/my-trust-store/73e2d6bc24d8a063', resource_arn='arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-load-balancer/80233fa81d678c2c')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_input.DeleteSharedTrustStoreAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_output.DeleteSharedTrustStoreAssociationOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_shared_trust_store_association

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_shared_trust_store_association.async_delete_shared_trust_store_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_shared_trust_store_association_input.DeleteSharedTrustStoreAssociationInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_target_group(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_target_group_output.DeleteTargetGroupOutput":
        """<p>Deletes the specified target group.</p> <p>You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks. Deleting a target group does not affect its registered targets. For example, any EC2 instances continue to run until you stop or terminate them.</p>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.resource_in_use_exception.ResourceInUseException: <p>A specified resource is in use.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a target group
            This example deletes the specified target group.

            >>> await client.delete_target_group(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_target_group_input.DeleteTargetGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_target_group_output.DeleteTargetGroupOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_target_group

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_target_group.async_delete_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_target_group_input.DeleteTargetGroupInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_trust_store(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.delete_trust_store_output.DeleteTrustStoreOutput":
        """<p>Deletes a trust store.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.trust_store_in_use_exception.TrustStoreInUseException: <p>The specified trust store is currently in use.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.delete_trust_store_input.DeleteTrustStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.delete_trust_store_output.DeleteTrustStoreOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_trust_store

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.delete_trust_store.async_delete_trust_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.delete_trust_store_input.DeleteTrustStoreInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_targets(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
        targets: Optional[
            "capo_elastic_load_balancing_v2.types.target_descriptions.TargetDescriptions"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.deregister_targets_output.DeregisterTargetsOutput":
        """<p>Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.</p> <p>The load balancer stops sending requests to targets that are deregistering, but uses connection draining to ensure that in-flight traffic completes on the existing connections. This deregistration delay is configured by default but can be updated for each target group.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#deregistration-delay"> Deregistration delay</a> in the <i>Application Load Balancers User Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-target-group-attributes.html#deregistration-delay"> Deregistration delay</a> in the <i>Network Load Balancers User Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/edit-target-group-attributes.html#deregistration-delay"> Deregistration delay</a> in the <i>Gateway Load Balancers User Guide</i> </p> </li> </ul> <p>Note: If the specified target does not exist, the action returns successfully.</p>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>
            targets: <p>The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_target_exception.InvalidTargetException: <p>The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a target from a target group
            This example deregisters the specified instance from the specified target group.

            >>> await client.deregister_targets(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067', targets=[{'Id': 'i-0f76fade'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.deregister_targets_input.DeregisterTargetsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.deregister_targets_output.DeregisterTargetsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.deregister_targets

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.deregister_targets.async_deregister_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.deregister_targets_input.DeregisterTargetsInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn
        if targets is not None:
            input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_limits(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_account_limits_output.DescribeAccountLimitsOutput":
        """<p>Describes the current Elastic Load Balancing resource limits for your Amazon Web Services account.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html">Quotas for your Application Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html">Quotas for your Network Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/quotas-limits.html">Quotas for your Gateway Load Balancers</a> </p> </li> </ul>

        Args:
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_account_limits_input.DescribeAccountLimitsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_account_limits_output.DescribeAccountLimitsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_account_limits

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_account_limits.async_describe_account_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_account_limits_input.DescribeAccountLimitsInput = {}
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_account_limits(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.limit.Limit]":
        _token = marker
        while True:
            _response = await self.describe_account_limits(
                config_overrides=config_overrides,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_capacity_reservation(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_capacity_reservation_output.DescribeCapacityReservationOutput":
        """<p>Describes the capacity reservation status for the specified load balancer.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_capacity_reservation_input.DescribeCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_capacity_reservation_output.DescribeCapacityReservationOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_capacity_reservation.async_describe_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_capacity_reservation_input.DescribeCapacityReservationInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_listener_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_listener_attributes_output.DescribeListenerAttributesOutput":
        """<p>Describes the attributes for the specified listener.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe listener attributes
            This example describes the attributes of the specified listener.

            >>> await client.describe_listener_attributes(listener_arn='aws:elasticloadbalancing:us-east-1:123456789012:listener/net/my-listener/73e2d6bc24d8a067/d5dc06411fa5bcea')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_listener_attributes_input.DescribeListenerAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_listener_attributes_output.DescribeListenerAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listener_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listener_attributes.async_describe_listener_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_listener_attributes_input.DescribeListenerAttributesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_listener_certificates(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_listener_certificates_output.DescribeListenerCertificatesOutput":
        """<p>Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.</p> <p>If the default certificate is also in the certificate list, it appears twice in the results (once with <code>IsDefault</code> set to true and once with <code>IsDefault</code> set to false).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html">SSL certificates</a> in the <i>Application Load Balancers Guide</i> or <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html">Server certificates</a> in the <i>Network Load Balancers Guide</i>.</p>

        Args:
            listener_arn: <p>The Amazon Resource Names (ARN) of the listener.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_listener_certificates_input.DescribeListenerCertificatesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_listener_certificates_output.DescribeListenerCertificatesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listener_certificates

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listener_certificates.async_describe_listener_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_listener_certificates_input.DescribeListenerCertificatesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_listener_certificates(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.certificate.Certificate]":
        _token = marker
        while True:
            _response = await self.describe_listener_certificates(
                config_overrides=config_overrides,
                listener_arn=listener_arn,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("certificates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_listeners(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        listener_arns: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arns.ListenerArns"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_listeners_output.DescribeListenersOutput":
        """<p>Describes the specified listeners or the listeners for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. You must specify either a load balancer or one or more listeners.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            listener_arns: <p>The Amazon Resource Names (ARN) of the listeners.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a listener
            This example describes the specified listener.

            >>> await client.describe_listeners(listener_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_listeners_input.DescribeListenersInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_listeners_output.DescribeListenersOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listeners

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_listeners.async_describe_listeners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_listeners_input.DescribeListenersInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if listener_arns is not None:
            input_["listener_arns"] = listener_arns
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_listeners(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        listener_arns: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arns.ListenerArns"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.listener.Listener]":
        _token = marker
        while True:
            _response = await self.describe_listeners(
                config_overrides=config_overrides,
                load_balancer_arn=load_balancer_arn,
                listener_arns=listener_arns,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("listeners",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_load_balancer_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_output.DescribeLoadBalancerAttributesOutput":
        """<p>Describes the attributes for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes">Load balancer attributes</a> in the <i>Application Load Balancers Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes">Load balancer attributes</a> in the <i>Network Load Balancers Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#load-balancer-attributes">Load balancer attributes</a> in the <i>Gateway Load Balancers Guide</i> </p> </li> </ul>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe load balancer attributes
            This example describes the attributes of the specified load balancer.

            >>> await client.describe_load_balancer_attributes(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_input.DescribeLoadBalancerAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_output.DescribeLoadBalancerAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_load_balancer_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_load_balancer_attributes.async_describe_load_balancer_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_load_balancer_attributes_input.DescribeLoadBalancerAttributesInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_load_balancers(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arns: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arns.LoadBalancerArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_load_balancers_output.DescribeLoadBalancersOutput":
        """<p>Describes the specified load balancers or all of your load balancers.</p>

        Args:
            load_balancer_arns: <p>The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.</p>
            names: <p>The names of the load balancers.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a load balancer
            This example describes the specified load balancer.

            >>> await client.describe_load_balancers(load_balancer_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_load_balancers_input.DescribeLoadBalancersInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_load_balancers_output.DescribeLoadBalancersOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_load_balancers

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_load_balancers.async_describe_load_balancers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_load_balancers_input.DescribeLoadBalancersInput = {}
        if load_balancer_arns is not None:
            input_["load_balancer_arns"] = load_balancer_arns
        if names is not None:
            input_["names"] = names
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_load_balancers(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arns: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arns.LoadBalancerArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> (
        "AsyncIterator[capo_elastic_load_balancing_v2.types.load_balancer.LoadBalancer]"
    ):
        _token = marker
        while True:
            _response = await self.describe_load_balancers(
                config_overrides=config_overrides,
                load_balancer_arns=load_balancer_arns,
                names=names,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("load_balancers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def wait_until_load_balancer_exists(
        self,
        *,
        max_wait_time: float,
        min_delay: float = 15,
        max_delay: float = 120,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arns: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arns.LoadBalancerArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_load_balancers_output.DescribeLoadBalancersOutput":
        """Wait for load_balancer_exists.

        Args:
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            load_balancer_arns: <p>The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.</p>
            names: <p>The names of the load balancers.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_elastic_load_balancing_v2.types.describe_load_balancers_output.DescribeLoadBalancersOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_load_balancers(  # noqa: F841
                    config_overrides=config_overrides,
                    load_balancer_arns=load_balancer_arns,
                    names=names,
                    marker=marker,
                    page_size=page_size,
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "LoadBalancerNotFound":
                pass

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("load_balancer_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_rules(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        rule_arns: Optional[
            "capo_elastic_load_balancing_v2.types.rule_arns.RuleArns"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> (
        "capo_elastic_load_balancing_v2.types.describe_rules_output.DescribeRulesOutput"
    ):
        """<p>Describes the specified rules or the rules for the specified listener. You must specify either a listener or rules.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            rule_arns: <p>The Amazon Resource Names (ARN) of the rules.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a rule
            This example describes the specified rule.

            >>> await client.describe_rules(rule_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee'])
            To describe rules for a Network Load Balancer listener
            This example describes the rules for the specified Network Load Balancer listener, including rules that route based on source IP address type.

            >>> await client.describe_rules(listener_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/net/my-nlb/1234567890abcdef/1234567890abcdef')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_rules_input.DescribeRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_rules_output.DescribeRulesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_rules

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_rules.async_describe_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_rules_input.DescribeRulesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if rule_arns is not None:
            input_["rule_arns"] = rule_arns
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_rules(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        rule_arns: Optional[
            "capo_elastic_load_balancing_v2.types.rule_arns.RuleArns"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.rule.Rule]":
        _token = marker
        while True:
            _response = await self.describe_rules(
                config_overrides=config_overrides,
                listener_arn=listener_arn,
                rule_arns=rule_arns,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_ssl_policies(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.ssl_policy_names.SslPolicyNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
        load_balancer_type: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_type_enum.LoadBalancerTypeEnum"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_ssl_policies_output.DescribeSSLPoliciesOutput":
        """<p>Describes the specified policies or all policies used for SSL negotiation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html">Security policies</a> in the <i>Application Load Balancers Guide</i> and <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html">Security policies</a> in the <i>Network Load Balancers Guide</i>.</p>

        Args:
            names: <p>The names of the policies.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>
            load_balancer_type: <p> The type of load balancer. The default lists the SSL policies for all load balancers.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception.SSLPolicyNotFoundException: <p>The specified SSL policy does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a policy used for SSL negotiation
            This example describes the specified policy used for SSL negotiation.

            >>> await client.describe_ssl_policies(names=['ELBSecurityPolicy-2015-05'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_ssl_policies_input.DescribeSSLPoliciesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_ssl_policies_output.DescribeSSLPoliciesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_ssl_policies

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_ssl_policies.async_describe_ssl_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_ssl_policies_input.DescribeSSLPoliciesInput = {}
        if names is not None:
            input_["names"] = names
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size
        if load_balancer_type is not None:
            input_["load_balancer_type"] = load_balancer_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_tags(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        resource_arns: Optional[
            "capo_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput":
        """<p>Describes the tags for the specified Elastic Load Balancing resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.</p>

        Args:
            resource_arns: <p>The Amazon Resource Names (ARN) of the resources. You can specify up to 20 resources in a single call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the tags assigned to a load balancer
            This example describes the tags assigned to the specified load balancer.

            >>> await client.describe_tags(resource_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_tags_input.DescribeTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_tags

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_tags_input.DescribeTagsInput = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_target_group_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput":
        """<p>Describes the attributes for the specified target group.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-attributes">Target group attributes</a> in the <i>Application Load Balancers Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-group-attributes">Target group attributes</a> in the <i>Network Load Balancers Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html#target-group-attributes">Target group attributes</a> in the <i>Gateway Load Balancers Guide</i> </p> </li> </ul>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe target group attributes
            This example describes the attributes of the specified target group.

            >>> await client.describe_target_group_attributes(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.DescribeTargetGroupAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_group_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_group_attributes.async_describe_target_group_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.DescribeTargetGroupAttributesInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_target_groups(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        target_group_arns: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arns.TargetGroupArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_names.TargetGroupNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_target_groups_output.DescribeTargetGroupsOutput":
        """<p>Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            target_group_arns: <p>The Amazon Resource Names (ARN) of the target groups.</p>
            names: <p>The names of the target groups.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a target group
            This example describes the specified target group.

            >>> await client.describe_target_groups(target_group_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_target_groups_input.DescribeTargetGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_target_groups_output.DescribeTargetGroupsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_groups

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_groups.async_describe_target_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_target_groups_input.DescribeTargetGroupsInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if target_group_arns is not None:
            input_["target_group_arns"] = target_group_arns
        if names is not None:
            input_["names"] = names
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_target_groups(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        target_group_arns: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arns.TargetGroupArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_names.TargetGroupNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.target_group.TargetGroup]":
        _token = marker
        while True:
            _response = await self.describe_target_groups(
                config_overrides=config_overrides,
                load_balancer_arn=load_balancer_arn,
                target_group_arns=target_group_arns,
                names=names,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("target_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_target_health(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
        targets: Optional[
            "capo_elastic_load_balancing_v2.types.target_descriptions.TargetDescriptions"
        ] = None,
        include: Optional[
            "capo_elastic_load_balancing_v2.types.list_of_describe_target_health_include_options.ListOfDescribeTargetHealthIncludeOptions"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_target_health_output.DescribeTargetHealthOutput":
        """<p>Describes the health of the specified targets or all of your targets.</p>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>
            targets: <p>The targets.</p>
            include: <p>Used to include anomaly detection information.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.health_unavailable_exception.HealthUnavailableException: <p>The health of the specified targets could not be retrieved due to an internal error.</p>
            capo_elastic_load_balancing_v2.errors.invalid_target_exception.InvalidTargetException: <p>The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the health of the targets for a target group
            This example describes the health of the targets for the specified target group. One target is healthy but the other is not specified in an action, so it can't receive traffic from the load balancer.

            >>> await client.describe_target_health(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067')
            To describe the health of a target
            This example describes the health of the specified target. This target is healthy.

            >>> await client.describe_target_health(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067', targets=[{'Id': 'i-0f76fade', 'Port': 80}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_target_health_input.DescribeTargetHealthInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_target_health_output.DescribeTargetHealthOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_health

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_target_health.async_describe_target_health(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_target_health_input.DescribeTargetHealthInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn
        if targets is not None:
            input_["targets"] = targets
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_trust_store_associations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_trust_store_associations_output.DescribeTrustStoreAssociationsOutput":
        """<p>Describes all resources associated with the specified trust store.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_trust_store_associations_input.DescribeTrustStoreAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_trust_store_associations_output.DescribeTrustStoreAssociationsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_store_associations

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_store_associations.async_describe_trust_store_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_trust_store_associations_input.DescribeTrustStoreAssociationsInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_trust_store_associations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.trust_store_association.TrustStoreAssociation]":
        _token = marker
        while True:
            _response = await self.describe_trust_store_associations(
                config_overrides=config_overrides,
                trust_store_arn=trust_store_arn,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("trust_store_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_trust_store_revocations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        revocation_ids: Optional[
            "capo_elastic_load_balancing_v2.types.revocation_ids.RevocationIds"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_output.DescribeTrustStoreRevocationsOutput":
        """<p>Describes the revocation files in use by the specified trust store or revocation files.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            revocation_ids: <p>The revocation IDs of the revocation files you want to describe.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.revocation_id_not_found_exception.RevocationIdNotFoundException: <p>The specified revocation ID does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_input.DescribeTrustStoreRevocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_output.DescribeTrustStoreRevocationsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_store_revocations

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_store_revocations.async_describe_trust_store_revocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_trust_store_revocations_input.DescribeTrustStoreRevocationsInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if revocation_ids is not None:
            input_["revocation_ids"] = revocation_ids
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_trust_store_revocations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        revocation_ids: Optional[
            "capo_elastic_load_balancing_v2.types.revocation_ids.RevocationIds"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.describe_trust_store_revocation.DescribeTrustStoreRevocation]":
        _token = marker
        while True:
            _response = await self.describe_trust_store_revocations(
                config_overrides=config_overrides,
                trust_store_arn=trust_store_arn,
                revocation_ids=revocation_ids,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("trust_store_revocations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_trust_stores(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arns: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arns.TrustStoreArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_names.TrustStoreNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.describe_trust_stores_output.DescribeTrustStoresOutput":
        """<p>Describes all trust stores for the specified account.</p>

        Args:
            trust_store_arns: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            names: <p>The names of the trust stores.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.describe_trust_stores_input.DescribeTrustStoresInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.describe_trust_stores_output.DescribeTrustStoresOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_stores

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.describe_trust_stores.async_describe_trust_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.describe_trust_stores_input.DescribeTrustStoresInput = {}
        if trust_store_arns is not None:
            input_["trust_store_arns"] = trust_store_arns
        if names is not None:
            input_["names"] = names
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_trust_stores(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arns: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arns.TrustStoreArns"
        ] = None,
        names: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_names.TrustStoreNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing_v2.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing_v2.types.page_size.PageSize"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_load_balancing_v2.types.trust_store.TrustStore]":
        _token = marker
        while True:
            _response = await self.describe_trust_stores(
                config_overrides=config_overrides,
                trust_store_arns=trust_store_arns,
                names=names,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("trust_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def get_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        resource_arn: Optional[
            "capo_elastic_load_balancing_v2.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.get_resource_policy_output.GetResourcePolicyOutput":
        """<p>Retrieves the resource policy for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve a resource policy
            This example retrieves the resource policy for the specified trust store.

            >>> await client.get_resource_policy(resource_arn='arn:aws:elasticloadbalancing:us-east-1:123456789012:truststore/my-trust-store/73e2d6bc24d8a067')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.get_resource_policy_input.GetResourcePolicyInput = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trust_store_ca_certificates_bundle(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_output.GetTrustStoreCaCertificatesBundleOutput":
        """<p>Retrieves the ca certificate bundle.</p> <p>This action returns a pre-signed S3 URI which is active for ten minutes.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_input.GetTrustStoreCaCertificatesBundleInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_output.GetTrustStoreCaCertificatesBundleOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_trust_store_ca_certificates_bundle

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_trust_store_ca_certificates_bundle.async_get_trust_store_ca_certificates_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.get_trust_store_ca_certificates_bundle_input.GetTrustStoreCaCertificatesBundleInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trust_store_revocation_content(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        revocation_id: Optional[
            "capo_elastic_load_balancing_v2.types.revocation_id.RevocationId"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_output.GetTrustStoreRevocationContentOutput":
        """<p>Retrieves the specified revocation file.</p> <p>This action returns a pre-signed S3 URI which is active for ten minutes.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            revocation_id: <p>The revocation ID of the revocation file.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.revocation_id_not_found_exception.RevocationIdNotFoundException: <p>The specified revocation ID does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_input.GetTrustStoreRevocationContentInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_output.GetTrustStoreRevocationContentOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_trust_store_revocation_content

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.get_trust_store_revocation_content.async_get_trust_store_revocation_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.get_trust_store_revocation_content_input.GetTrustStoreRevocationContentInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if revocation_id is not None:
            input_["revocation_id"] = revocation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_capacity_reservation(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        minimum_load_balancer_capacity: Optional[
            "capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.MinimumLoadBalancerCapacity"
        ] = None,
        reset_capacity_reservation: Optional[
            "capo_elastic_load_balancing_v2.types.reset_capacity_reservation.ResetCapacityReservation"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput":
        """<p>Modifies the capacity reservation of the specified load balancer.</p> <p>When modifying capacity reservation, you must include at least one <code>MinimumLoadBalancerCapacity</code> or <code>ResetCapacityReservation</code>.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            minimum_load_balancer_capacity: <p>The minimum load balancer capacity reserved.</p>
            reset_capacity_reservation: <p>Resets the capacity reservation.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.capacity_decrease_requests_limit_exceeded_exception.CapacityDecreaseRequestsLimitExceededException: <p>You've exceeded the daily capacity decrease limit for this reservation.</p>
            capo_elastic_load_balancing_v2.errors.capacity_reservation_pending_exception.CapacityReservationPendingException: <p>There is a pending capacity reservation.</p>
            capo_elastic_load_balancing_v2.errors.capacity_units_limit_exceeded_exception.CapacityUnitsLimitExceededException: <p>You've exceeded the capacity units limit.</p>
            capo_elastic_load_balancing_v2.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is insufficient capacity to reserve.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.prior_request_not_complete_exception.PriorRequestNotCompleteException: <p>This operation is not allowed while a prior request has not been completed.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_capacity_reservation_input.ModifyCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_capacity_reservation.async_modify_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_capacity_reservation_input.ModifyCapacityReservationInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if minimum_load_balancer_capacity is not None:
            input_["minimum_load_balancer_capacity"] = minimum_load_balancer_capacity
        if reset_capacity_reservation is not None:
            input_["reset_capacity_reservation"] = reset_capacity_reservation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_ip_pools(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        ipam_pools: Optional[
            "capo_elastic_load_balancing_v2.types.ipam_pools.IpamPools"
        ] = None,
        remove_ipam_pools: Optional[
            "capo_elastic_load_balancing_v2.types.remove_ipam_pools.RemoveIpamPools"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_ip_pools_output.ModifyIpPoolsOutput":
        """<p>[Application Load Balancers] Modify the IP pool associated to a load balancer.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            ipam_pools: <p>The IPAM pools to be modified.</p>
            remove_ipam_pools: <p>Remove the IP pools in use by the load balancer.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_ip_pools_input.ModifyIpPoolsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_ip_pools_output.ModifyIpPoolsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_ip_pools

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_ip_pools.async_modify_ip_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_ip_pools_input.ModifyIpPoolsInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if ipam_pools is not None:
            input_["ipam_pools"] = ipam_pools
        if remove_ipam_pools is not None:
            input_["remove_ipam_pools"] = remove_ipam_pools

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_listener(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        port: Optional["capo_elastic_load_balancing_v2.types.port.Port"] = None,
        protocol: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
        ] = None,
        ssl_policy: Optional[
            "capo_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
        ] = None,
        certificates: Optional[
            "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
        ] = None,
        default_actions: Optional[
            "capo_elastic_load_balancing_v2.types.actions.Actions"
        ] = None,
        alpn_policy: Optional[
            "capo_elastic_load_balancing_v2.types.alpn_policy_name.AlpnPolicyName"
        ] = None,
        mutual_authentication: Optional[
            "capo_elastic_load_balancing_v2.types.mutual_authentication_attributes.MutualAuthenticationAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_listener_output.ModifyListenerOutput":
        """<p>Replaces the specified properties of the specified listener. Any properties that you do not specify remain unchanged.</p> <p>Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS, you must add the security policy and default certificate properties.</p> <p>To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            port: <p>The port for connections from clients to the load balancer. You can't specify a port for a Gateway Load Balancer.</p>
            protocol: <p>The protocol for connections from clients to the load balancer. Application Load Balancers support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols. You can’t change the protocol to UDP, TCP_UDP, QUIC, or TCP_QUIC if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.</p>
            ssl_policy: <p>[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html">Security policies</a> in the <i>Application Load Balancers Guide</i> or <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html">Security policies</a> in the <i>Network Load Balancers Guide</i>.</p>
            certificates: <p>[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>
            default_actions: <p>The actions for the default rule.</p>
            alpn_policy: <p>[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:</p> <ul> <li> <p> <code>HTTP1Only</code> </p> </li> <li> <p> <code>HTTP2Only</code> </p> </li> <li> <p> <code>HTTP2Optional</code> </p> </li> <li> <p> <code>HTTP2Preferred</code> </p> </li> <li> <p> <code>None</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies">ALPN policies</a> in the <i>Network Load Balancers Guide</i>.</p>
            mutual_authentication: <p>[HTTPS listeners] The mutual authentication configuration information.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception.ALPNPolicyNotSupportedException: <p>The specified ALPN policy is not supported.</p>
            capo_elastic_load_balancing_v2.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified certificate does not exist.</p>
            capo_elastic_load_balancing_v2.errors.duplicate_listener_exception.DuplicateListenerException: <p>A listener with the specified port already exists.</p>
            capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException: <p>The specified configuration is not valid with this protocol.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException: <p>The requested action is not valid.</p>
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception.SSLPolicyNotFoundException: <p>The specified SSL policy does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException: <p>You've reached the limit on the number of load balancers per target group.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException: <p>You've reached the limit on the number of actions per rule.</p>
            capo_elastic_load_balancing_v2.errors.too_many_certificates_exception.TooManyCertificatesException: <p>You've reached the limit on the number of certificates per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_listeners_exception.TooManyListenersException: <p>You've reached the limit on the number of listeners per load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException: <p>You've reached the limit on the number of times a target can be registered with a load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException: <p>You've reached the limit on the number of targets.</p>
            capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException: <p>You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_ready_exception.TrustStoreNotReadyException: <p>The specified trust store is not active.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change the default action for a listener
            This example changes the default action for the specified listener.

            >>> await client.modify_listener(listener_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2', default_actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f'}])
            To change the server certificate
            This example changes the server certificate for the specified HTTPS listener.

            >>> await client.modify_listener(listener_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65', certificates=[{'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-new-server-cert'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_listener_input.ModifyListenerInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_listener_output.ModifyListenerOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_listener

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_listener.async_modify_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_listener_input.ModifyListenerInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if port is not None:
            input_["port"] = port
        if protocol is not None:
            input_["protocol"] = protocol
        if ssl_policy is not None:
            input_["ssl_policy"] = ssl_policy
        if certificates is not None:
            input_["certificates"] = certificates
        if default_actions is not None:
            input_["default_actions"] = default_actions
        if alpn_policy is not None:
            input_["alpn_policy"] = alpn_policy
        if mutual_authentication is not None:
            input_["mutual_authentication"] = mutual_authentication

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_listener_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        attributes: Optional[
            "capo_elastic_load_balancing_v2.types.listener_attributes.ListenerAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_listener_attributes_output.ModifyListenerAttributesOutput":
        """<p>Modifies the specified attributes of the specified listener.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            attributes: <p>The listener attributes.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_listener_attributes_input.ModifyListenerAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_listener_attributes_output.ModifyListenerAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_listener_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_listener_attributes.async_modify_listener_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_listener_attributes_input.ModifyListenerAttributesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_load_balancer_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        attributes: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_attributes.LoadBalancerAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_output.ModifyLoadBalancerAttributesOutput":
        """<p>Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</p> <p>If any of the specified attributes can't be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            attributes: <p>The load balancer attributes.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable deletion protection
            This example enables deletion protection for the specified load balancer.

            >>> await client.modify_load_balancer_attributes(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', attributes=[{'Key': 'deletion_protection.enabled', 'Value': 'true'}])
            To change the idle timeout
            This example changes the idle timeout value for the specified load balancer.

            >>> await client.modify_load_balancer_attributes(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', attributes=[{'Key': 'idle_timeout.timeout_seconds', 'Value': '30'}])
            To enable access logs
            This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service.

            >>> await client.modify_load_balancer_attributes(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', attributes=[{'Key': 'access_logs.s3.enabled', 'Value': 'true'}, {'Key': 'access_logs.s3.bucket', 'Value': 'my-loadbalancer-logs'}, {'Key': 'access_logs.s3.prefix', 'Value': 'myapp'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_input.ModifyLoadBalancerAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_output.ModifyLoadBalancerAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_load_balancer_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_load_balancer_attributes.async_modify_load_balancer_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_load_balancer_attributes_input.ModifyLoadBalancerAttributesInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_rule(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        rule_arn: Optional[
            "capo_elastic_load_balancing_v2.types.rule_arn.RuleArn"
        ] = None,
        conditions: Optional[
            "capo_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
        ] = None,
        actions: Optional[
            "capo_elastic_load_balancing_v2.types.actions.Actions"
        ] = None,
        transforms: Optional[
            "capo_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
        ] = None,
        reset_transforms: Optional[
            "capo_elastic_load_balancing_v2.types.reset_transforms.ResetTransforms"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_rule_output.ModifyRuleOutput":
        """<p>Replaces the specified properties of the specified rule. Any properties that you do not specify are unchanged.</p> <p>To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.</p>

        Args:
            rule_arn: <p>The Amazon Resource Name (ARN) of the rule.</p>
            conditions: <p>The conditions.</p>
            actions: <p>The actions.</p>
            transforms: <p>The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform. If you specify <code>Transforms</code>, you can't specify <code>ResetTransforms</code>.</p>
            reset_transforms: <p>Indicates whether to remove all transforms from the rule. If you specify <code>ResetTransforms</code>, you can't specify <code>Transforms</code>.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException: <p>The specified configuration is not valid with this protocol.</p>
            capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException: <p>The requested action is not valid.</p>
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException: <p>You've reached the limit on the number of load balancers per target group.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException: <p>You've reached the limit on the number of actions per rule.</p>
            capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException: <p>You've reached the limit on the number of times a target can be registered with a load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException: <p>You've reached the limit on the number of targets.</p>
            capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException: <p>You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.</p>
            capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol is not supported.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify a rule
            This example modifies the condition for the specified rule.

            >>> await client.modify_rule(rule_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee', conditions=[{'Field': 'path-pattern', 'Values': ['/images/*']}])
            To modify a Network Load Balancer listener rule
            This example modifies an NLB listener rule to forward traffic to a different target group.

            >>> await client.modify_rule(rule_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/net/my-nlb/1234567890abcdef/1234567890abcdef/1234567890abcdef', actions=[{'Type': 'forward', 'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-ipv4-targets/1234567890abcdef'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_rule_input.ModifyRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_rule_output.ModifyRuleOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_rule

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_rule.async_modify_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_rule_input.ModifyRuleInput = {}
        if rule_arn is not None:
            input_["rule_arn"] = rule_arn
        if conditions is not None:
            input_["conditions"] = conditions
        if actions is not None:
            input_["actions"] = actions
        if transforms is not None:
            input_["transforms"] = transforms
        if reset_transforms is not None:
            input_["reset_transforms"] = reset_transforms

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_target_group(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
        health_check_protocol: Optional[
            "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
        ] = None,
        health_check_port: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
        ] = None,
        health_check_path: Optional[
            "capo_elastic_load_balancing_v2.types.path.Path"
        ] = None,
        health_check_enabled: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_enabled.HealthCheckEnabled"
        ] = None,
        health_check_interval_seconds: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
        ] = None,
        health_check_timeout_seconds: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
        ] = None,
        healthy_threshold_count: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
        ] = None,
        unhealthy_threshold_count: Optional[
            "capo_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
        ] = None,
        matcher: Optional[
            "capo_elastic_load_balancing_v2.types.matcher.Matcher"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_target_group_output.ModifyTargetGroupOutput":
        """<p>Modifies the health checks used when evaluating the health state of the targets in the specified target group.</p>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>
            health_check_protocol: <p>The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. It is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The GENEVE, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols are not supported for health checks.</p>
            health_check_port: <p>The port the load balancer uses when performing health checks on targets.</p>
            health_check_path: <p>[HTTP/HTTPS health checks] The destination for health checks on the targets.</p> <p>[HTTP1 or HTTP2 protocol version] The ping path. The default is /.</p> <p>[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.</p>
            health_check_enabled: <p>Indicates whether health checks are enabled. If the target type is <code>lambda</code>, health checks are disabled by default but can be enabled. If the target type is <code>instance</code>, <code>ip</code>, or <code>alb</code>, health checks are always enabled and can't be disabled.</p>
            health_check_interval_seconds: <p>The approximate amount of time, in seconds, between health checks of an individual target.</p>
            health_check_timeout_seconds: <p>[HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.</p>
            healthy_threshold_count: <p>The number of consecutive health checks successes required before considering an unhealthy target healthy.</p>
            unhealthy_threshold_count: <p>The number of consecutive health check failures required before considering the target unhealthy.</p>
            matcher: <p>[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify the health check configuration for a target group
            This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.

            >>> await client.modify_target_group(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f', health_check_protocol='HTTPS', health_check_port='443')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_target_group_input.ModifyTargetGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_target_group_output.ModifyTargetGroupOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_target_group

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_target_group.async_modify_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_target_group_input.ModifyTargetGroupInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn
        if health_check_protocol is not None:
            input_["health_check_protocol"] = health_check_protocol
        if health_check_port is not None:
            input_["health_check_port"] = health_check_port
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if health_check_enabled is not None:
            input_["health_check_enabled"] = health_check_enabled
        if health_check_interval_seconds is not None:
            input_["health_check_interval_seconds"] = health_check_interval_seconds
        if health_check_timeout_seconds is not None:
            input_["health_check_timeout_seconds"] = health_check_timeout_seconds
        if healthy_threshold_count is not None:
            input_["healthy_threshold_count"] = healthy_threshold_count
        if unhealthy_threshold_count is not None:
            input_["unhealthy_threshold_count"] = unhealthy_threshold_count
        if matcher is not None:
            input_["matcher"] = matcher

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_target_group_attributes(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
        attributes: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_attributes.TargetGroupAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_target_group_attributes_output.ModifyTargetGroupAttributesOutput":
        """<p>Modifies the specified attributes of the specified target group.</p>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>
            attributes: <p>The target group attributes.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify the deregistration delay timeout
            This example sets the deregistration delay timeout to the specified value for the specified target group.

            >>> await client.modify_target_group_attributes(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067', attributes=[{'Key': 'deregistration_delay.timeout_seconds', 'Value': '600'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_target_group_attributes_input.ModifyTargetGroupAttributesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_target_group_attributes_output.ModifyTargetGroupAttributesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_target_group_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_target_group_attributes.async_modify_target_group_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_target_group_attributes_input.ModifyTargetGroupAttributesInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_trust_store(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        ca_certificates_bundle_s3_bucket: Optional[
            "capo_elastic_load_balancing_v2.types.s3_bucket.S3Bucket"
        ] = None,
        ca_certificates_bundle_s3_key: Optional[
            "capo_elastic_load_balancing_v2.types.s3_key.S3Key"
        ] = None,
        ca_certificates_bundle_s3_object_version: Optional[
            "capo_elastic_load_balancing_v2.types.s3_object_version.S3ObjectVersion"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.modify_trust_store_output.ModifyTrustStoreOutput":
        """<p>Update the ca certificate bundle for the specified trust store.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            ca_certificates_bundle_s3_bucket: <p>The Amazon S3 bucket for the ca certificates bundle.</p>
            ca_certificates_bundle_s3_key: <p>The Amazon S3 path for the ca certificates bundle.</p>
            ca_certificates_bundle_s3_object_version: <p>The Amazon S3 object version for the ca certificates bundle. If undefined the current version is used.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.ca_certificates_bundle_not_found_exception.CaCertificatesBundleNotFoundException: <p>The specified ca certificate bundle does not exist.</p>
            capo_elastic_load_balancing_v2.errors.invalid_ca_certificates_bundle_exception.InvalidCaCertificatesBundleException: <p>The specified ca certificate bundle is in an invalid format, or corrupt.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.modify_trust_store_input.ModifyTrustStoreInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.modify_trust_store_output.ModifyTrustStoreOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_trust_store

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.modify_trust_store.async_modify_trust_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.modify_trust_store_input.ModifyTrustStoreInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if ca_certificates_bundle_s3_bucket is not None:
            input_["ca_certificates_bundle_s3_bucket"] = (
                ca_certificates_bundle_s3_bucket
            )
        if ca_certificates_bundle_s3_key is not None:
            input_["ca_certificates_bundle_s3_key"] = ca_certificates_bundle_s3_key
        if ca_certificates_bundle_s3_object_version is not None:
            input_["ca_certificates_bundle_s3_object_version"] = (
                ca_certificates_bundle_s3_object_version
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_targets(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        target_group_arn: Optional[
            "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
        ] = None,
        targets: Optional[
            "capo_elastic_load_balancing_v2.types.target_descriptions.TargetDescriptions"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.register_targets_output.RegisterTargetsOutput":
        """<p>Registers the specified targets with the specified target group.</p> <p>If the target is an EC2 instance, it must be in the <code>running</code> state when you register it.</p> <p>By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.</p> <p>For more information, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html">Register targets for your Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html">Register targets for your Network Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-group-register-targets.html">Register targets for your Gateway Load Balancer</a> </p> </li> </ul>

        Args:
            target_group_arn: <p>The Amazon Resource Name (ARN) of the target group.</p>
            targets: <p>The targets.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_target_exception.InvalidTargetException: <p>The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException: <p>You've reached the limit on the number of times a target can be registered with a load balancer.</p>
            capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException: <p>You've reached the limit on the number of targets.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register targets with a target group
            This example registers the specified instances with the specified target group.

            >>> await client.register_targets(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067', targets=[{'Id': 'i-80c8dd94'}, {'Id': 'i-ceddcd4d'}])
            To register targets with a target group using port overrides
            This example registers the specified instance with the specified target group using multiple ports. This enables you to register ECS containers on the same instance as targets in the target group.

            >>> await client.register_targets(target_group_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/3bb63f11dfb0faf9', targets=[{'Id': 'i-80c8dd94', 'Port': 80}, {'Id': 'i-80c8dd94', 'Port': 766}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.register_targets_input.RegisterTargetsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.register_targets_output.RegisterTargetsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.register_targets

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.register_targets.async_register_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.register_targets_input.RegisterTargetsInput = {}
        if target_group_arn is not None:
            input_["target_group_arn"] = target_group_arn
        if targets is not None:
            input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_listener_certificates(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        listener_arn: Optional[
            "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
        ] = None,
        certificates: Optional[
            "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.remove_listener_certificates_output.RemoveListenerCertificatesOutput":
        """<p>Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.</p>

        Args:
            listener_arn: <p>The Amazon Resource Name (ARN) of the listener.</p>
            certificates: <p>The certificate to remove. You can specify one certificate per call. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.remove_listener_certificates_input.RemoveListenerCertificatesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.remove_listener_certificates_output.RemoveListenerCertificatesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_listener_certificates

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_listener_certificates.async_remove_listener_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.remove_listener_certificates_input.RemoveListenerCertificatesInput = {}
        if listener_arn is not None:
            input_["listener_arn"] = listener_arn
        if certificates is not None:
            input_["certificates"] = certificates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        resource_arns: Optional[
            "capo_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
        ] = None,
        tag_keys: Optional[
            "capo_elastic_load_balancing_v2.types.tag_keys.TagKeys"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.remove_tags_output.RemoveTagsOutput":
        """<p>Removes the specified tags from the specified Elastic Load Balancing resources. You can remove the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.</p>

        Args:
            resource_arns: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys for the tags to remove.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException: <p>The specified listener does not exist.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException: <p>The specified target group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the limit on the number of tags for this resource.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a load balancer
            This example removes the specified tags from the specified load balancer.

            >>> await client.remove_tags(resource_arns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188'], tag_keys=['project', 'department'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.remove_tags_input.RemoveTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.remove_tags_output.RemoveTagsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_tags

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_tags.async_remove_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.remove_tags_input.RemoveTagsInput = {}
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_trust_store_revocations(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        trust_store_arn: Optional[
            "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
        ] = None,
        revocation_ids: Optional[
            "capo_elastic_load_balancing_v2.types.revocation_ids.RevocationIds"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_output.RemoveTrustStoreRevocationsOutput":
        """<p>Removes the specified revocation file from the specified trust store.</p>

        Args:
            trust_store_arn: <p>The Amazon Resource Name (ARN) of the trust store.</p>
            revocation_ids: <p>The revocation IDs of the revocation files you want to remove.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.revocation_id_not_found_exception.RevocationIdNotFoundException: <p>The specified revocation ID does not exist.</p>
            capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException: <p>The specified trust store does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_input.RemoveTrustStoreRevocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_output.RemoveTrustStoreRevocationsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_trust_store_revocations

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.remove_trust_store_revocations.async_remove_trust_store_revocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.remove_trust_store_revocations_input.RemoveTrustStoreRevocationsInput = {}
        if trust_store_arn is not None:
            input_["trust_store_arn"] = trust_store_arn
        if revocation_ids is not None:
            input_["revocation_ids"] = revocation_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_ip_address_type(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        ip_address_type: Optional[
            "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.set_ip_address_type_output.SetIpAddressTypeOutput":
        """<p>Sets the type of IP addresses used by the subnets of the specified load balancer.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            ip_address_type: <p>The IP address type. Internal load balancers must use <code>ipv4</code>.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>Application Load Balancer authentication supports IPv4 addresses only when connecting to an Identity Provider (IdP) or Amazon Cognito endpoint. Without a public IPv4 address the load balancer can't complete the authentication process, resulting in HTTP 500 errors.</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_subnet_exception.InvalidSubnetException: <p>The specified subnet is out of available addresses.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.set_ip_address_type_input.SetIpAddressTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.set_ip_address_type_output.SetIpAddressTypeOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_ip_address_type

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_ip_address_type.async_set_ip_address_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.set_ip_address_type_input.SetIpAddressTypeInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_rule_priorities(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        rule_priorities: Optional[
            "capo_elastic_load_balancing_v2.types.rule_priority_list.RulePriorityList"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.set_rule_priorities_output.SetRulePrioritiesOutput":
        """<p>Sets the priorities of the specified rules.</p> <p>You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.</p>

        Args:
            rule_priorities: <p>The rule priorities.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing_v2.errors.priority_in_use_exception.PriorityInUseException: <p>The specified priority is in use.</p>
            capo_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException: <p>The specified rule does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set the rule priority
            This example sets the priority of the specified rule.

            >>> await client.set_rule_priorities(rule_priorities=[{'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3', 'Priority': 5}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.set_rule_priorities_input.SetRulePrioritiesInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.set_rule_priorities_output.SetRulePrioritiesOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_rule_priorities

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_rule_priorities.async_set_rule_priorities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.set_rule_priorities_input.SetRulePrioritiesInput = {}
        if rule_priorities is not None:
            input_["rule_priorities"] = rule_priorities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_security_groups(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        security_groups: Optional[
            "capo_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
        ] = None,
        enforce_security_group_inbound_rules_on_private_link_traffic: Optional[
            "capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.set_security_groups_output.SetSecurityGroupsOutput":
        """<p>Associates the specified security groups with the specified Application Load Balancer or Network Load Balancer. The specified security groups override the previously associated security groups.</p> <p>You can't perform this operation on a Network Load Balancer unless you specified a security group for the load balancer when you created it.</p> <p>You can't associate a security group with a Gateway Load Balancer.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            security_groups: <p>The IDs of the security groups.</p>
            enforce_security_group_inbound_rules_on_private_link_traffic: <p>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through Amazon Web Services PrivateLink. Applies only if the load balancer has an associated security group. The default is <code>on</code>.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_security_group_exception.InvalidSecurityGroupException: <p>The specified security group does not exist.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a security group with a load balancer
            This example associates the specified security group with the specified load balancer.

            >>> await client.set_security_groups(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', security_groups=['sg-5943793c'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.set_security_groups_input.SetSecurityGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.set_security_groups_output.SetSecurityGroupsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_security_groups

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_security_groups.async_set_security_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.set_security_groups_input.SetSecurityGroupsInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if enforce_security_group_inbound_rules_on_private_link_traffic is not None:
            input_["enforce_security_group_inbound_rules_on_private_link_traffic"] = (
                enforce_security_group_inbound_rules_on_private_link_traffic
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_subnets(
        self,
        *,
        config_overrides: Optional[AsyncElasticLoadBalancingv2ClientConfig] = None,
        load_balancer_arn: Optional[
            "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
        ] = None,
        subnets: Optional[
            "capo_elastic_load_balancing_v2.types.subnets.Subnets"
        ] = None,
        subnet_mappings: Optional[
            "capo_elastic_load_balancing_v2.types.subnet_mappings.SubnetMappings"
        ] = None,
        ip_address_type: Optional[
            "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
        ] = None,
        enable_prefix_for_ipv6_source_nat: Optional[
            "capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
        ] = None,
    ) -> "capo_elastic_load_balancing_v2.types.set_subnets_output.SetSubnetsOutput":
        """<p>Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer, Network Load Balancer or Gateway Load Balancer. The specified subnets replace the previously enabled subnets.</p>

        Args:
            load_balancer_arn: <p>The Amazon Resource Name (ARN) of the load balancer.</p>
            subnets: <p>The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.</p>
            subnet_mappings: <p>The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones.</p>
            ip_address_type: <p>The IP address type.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>
            enable_prefix_for_ipv6_source_nat: <p>[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</p>

        Raises:
            capo_elastic_load_balancing_v2.errors.allocation_id_not_found_exception.AllocationIdNotFoundException: <p>The specified allocation ID does not exist.</p>
            capo_elastic_load_balancing_v2.errors.availability_zone_not_supported_exception.AvailabilityZoneNotSupportedException: <p>The specified Availability Zone is not supported.</p>
            capo_elastic_load_balancing_v2.errors.capacity_reservation_pending_exception.CapacityReservationPendingException: <p>There is a pending capacity reservation.</p>
            capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration is not valid.</p>
            capo_elastic_load_balancing_v2.errors.invalid_subnet_exception.InvalidSubnetException: <p>The specified subnet is out of available addresses.</p>
            capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing_v2.errors.subnet_not_found_exception.SubnetNotFoundException: <p>The specified subnet does not exist.</p>
            capo_elastic_load_balancing_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable Availability Zones for a load balancer
            This example enables the Availability Zones for the specified subnets for the specified load balancer.

            >>> await client.set_subnets(load_balancer_arn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188', subnets=['subnet-8360a9e7', 'subnet-b7d581c0'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_load_balancing_v2.types.set_subnets_input.SetSubnetsInput]",
        ) -> AsyncOperationResponse[
            "capo_elastic_load_balancing_v2.types.set_subnets_output.SetSubnetsOutput"
        ]:
            import capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_subnets

            (
                output,
                http_response,
            ) = await capo_elastic_load_balancing_v2._operations.elastic_load_balancing_v10.set_subnets.async_set_subnets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing_v2.types.set_subnets_input.SetSubnetsInput = {}
        if load_balancer_arn is not None:
            input_["load_balancer_arn"] = load_balancer_arn
        if subnets is not None:
            input_["subnets"] = subnets
        if subnet_mappings is not None:
            input_["subnet_mappings"] = subnet_mappings
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if enable_prefix_for_ipv6_source_nat is not None:
            input_["enable_prefix_for_ipv6_source_nat"] = (
                enable_prefix_for_ipv6_source_nat
            )

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
