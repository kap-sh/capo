"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ElasticLoadBalancing_v7``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_elastic_load_balancing._auth._signers
import capo_elastic_load_balancing._auth._sigv4
from capo_elastic_load_balancing._auth._identity import Credentials
from capo_elastic_load_balancing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elastic_load_balancing._auth._zapros_handler import AuthMiddleware
from capo_elastic_load_balancing._pagination import resolve_path as _resolve_path
from capo_elastic_load_balancing._services._aws_config import aws_config
from capo_elastic_load_balancing._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.access_point_port
    import capo_elastic_load_balancing.types.add_availability_zones_input
    import capo_elastic_load_balancing.types.add_availability_zones_output
    import capo_elastic_load_balancing.types.add_tags_input
    import capo_elastic_load_balancing.types.add_tags_output
    import capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input
    import capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output
    import capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_input
    import capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_output
    import capo_elastic_load_balancing.types.availability_zones
    import capo_elastic_load_balancing.types.configure_health_check_input
    import capo_elastic_load_balancing.types.configure_health_check_output
    import capo_elastic_load_balancing.types.cookie_expiration_period
    import capo_elastic_load_balancing.types.cookie_name
    import capo_elastic_load_balancing.types.create_access_point_input
    import capo_elastic_load_balancing.types.create_access_point_output
    import capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_input
    import capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_output
    import capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_input
    import capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_output
    import capo_elastic_load_balancing.types.create_load_balancer_listener_input
    import capo_elastic_load_balancing.types.create_load_balancer_listener_output
    import capo_elastic_load_balancing.types.create_load_balancer_policy_input
    import capo_elastic_load_balancing.types.create_load_balancer_policy_output
    import capo_elastic_load_balancing.types.delete_access_point_input
    import capo_elastic_load_balancing.types.delete_access_point_output
    import capo_elastic_load_balancing.types.delete_load_balancer_listener_input
    import capo_elastic_load_balancing.types.delete_load_balancer_listener_output
    import capo_elastic_load_balancing.types.delete_load_balancer_policy_input
    import capo_elastic_load_balancing.types.delete_load_balancer_policy_output
    import capo_elastic_load_balancing.types.deregister_end_points_input
    import capo_elastic_load_balancing.types.deregister_end_points_output
    import capo_elastic_load_balancing.types.describe_access_points_input
    import capo_elastic_load_balancing.types.describe_access_points_output
    import capo_elastic_load_balancing.types.describe_account_limits_input
    import capo_elastic_load_balancing.types.describe_account_limits_output
    import capo_elastic_load_balancing.types.describe_end_point_state_input
    import capo_elastic_load_balancing.types.describe_end_point_state_output
    import capo_elastic_load_balancing.types.describe_load_balancer_attributes_input
    import capo_elastic_load_balancing.types.describe_load_balancer_attributes_output
    import capo_elastic_load_balancing.types.describe_load_balancer_policies_input
    import capo_elastic_load_balancing.types.describe_load_balancer_policies_output
    import capo_elastic_load_balancing.types.describe_load_balancer_policy_types_input
    import capo_elastic_load_balancing.types.describe_load_balancer_policy_types_output
    import capo_elastic_load_balancing.types.describe_tags_input
    import capo_elastic_load_balancing.types.describe_tags_output
    import capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_input
    import capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_output
    import capo_elastic_load_balancing.types.end_point_port
    import capo_elastic_load_balancing.types.health_check
    import capo_elastic_load_balancing.types.instances
    import capo_elastic_load_balancing.types.listeners
    import capo_elastic_load_balancing.types.load_balancer_attributes
    import capo_elastic_load_balancing.types.load_balancer_description
    import capo_elastic_load_balancing.types.load_balancer_names
    import capo_elastic_load_balancing.types.load_balancer_names_max20
    import capo_elastic_load_balancing.types.load_balancer_scheme
    import capo_elastic_load_balancing.types.marker
    import capo_elastic_load_balancing.types.modify_load_balancer_attributes_input
    import capo_elastic_load_balancing.types.modify_load_balancer_attributes_output
    import capo_elastic_load_balancing.types.page_size
    import capo_elastic_load_balancing.types.policy_attributes
    import capo_elastic_load_balancing.types.policy_name
    import capo_elastic_load_balancing.types.policy_names
    import capo_elastic_load_balancing.types.policy_type_name
    import capo_elastic_load_balancing.types.policy_type_names
    import capo_elastic_load_balancing.types.ports
    import capo_elastic_load_balancing.types.register_end_points_input
    import capo_elastic_load_balancing.types.register_end_points_output
    import capo_elastic_load_balancing.types.remove_availability_zones_input
    import capo_elastic_load_balancing.types.remove_availability_zones_output
    import capo_elastic_load_balancing.types.remove_tags_input
    import capo_elastic_load_balancing.types.remove_tags_output
    import capo_elastic_load_balancing.types.security_groups
    import capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_input
    import capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_output
    import capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_input
    import capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_output
    import capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_input
    import capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_output
    import capo_elastic_load_balancing.types.ssl_certificate_id
    import capo_elastic_load_balancing.types.subnets
    import capo_elastic_load_balancing.types.tag_key_list
    import capo_elastic_load_balancing.types.tag_list


class ElasticLoadBalancingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ElasticLoadBalancingClient:
    """A client for the ``ElasticLoadBalancing`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = ElasticLoadBalancingClientConfig(
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
        self, config_overrides: Optional[ElasticLoadBalancingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElasticLoadBalancingClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def add_tags(
        self,
        load_balancer_names: "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames",
        tags: "capo_elastic_load_balancing.types.tag_list.TagList",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.add_tags_output.AddTagsOutput":
        """<p>Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.</p> <p>Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, <code>AddTags</code> updates its value.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html">Tag Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_names: <p>The name of the load balancer. You can specify one load balancer only.</p>
            tags: <p>The tags.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_elastic_load_balancing.errors.too_many_tags_exception.TooManyTagsException: <p>The quota for the number of tags that can be assigned to a load balancer has been reached.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to a load balancer
            This example adds two tags to the specified load balancer.

            >>> client.add_tags(load_balancer_names=['my-load-balancer'], tags=[{'Key': 'project', 'Value': 'lima'}, {'Key': 'department', 'Value': 'digital-media'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.add_tags_input.AddTagsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.add_tags_output.AddTagsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.add_tags

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.add_tags.add_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.add_tags_input.AddTagsInput = {
            "load_balancer_names": load_balancer_names,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def apply_security_groups_to_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        security_groups: "capo_elastic_load_balancing.types.security_groups.SecurityGroups",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput":
        """<p>Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups">Security Groups for Load Balancers in a VPC</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            security_groups: <p>The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.invalid_security_group_exception.InvalidSecurityGroupException: <p>One or more of the specified security groups do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a security group with a load balancer in a VPC
            This example associates a security group with the specified load balancer in a VPC.

            >>> client.apply_security_groups_to_load_balancer(load_balancer_name='my-load-balancer', security_groups=['sg-fc448899'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.ApplySecurityGroupsToLoadBalancerInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.apply_security_groups_to_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.apply_security_groups_to_load_balancer.apply_security_groups_to_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.ApplySecurityGroupsToLoadBalancerInput = {
            "load_balancer_name": load_balancer_name,
            "security_groups": security_groups,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_load_balancer_to_subnets(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        subnets: "capo_elastic_load_balancing.types.subnets.Subnets",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_output.AttachLoadBalancerToSubnetsOutput":
        """<p>Adds one or more subnets to the set of configured subnets for the specified load balancer.</p> <p>The load balancer evenly distributes requests across all registered subnets. For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html">Add or Remove Subnets for Your Load Balancer in a VPC</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            subnets: <p>The IDs of the subnets to add. You can add only one subnet per Availability Zone.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.invalid_subnet_exception.InvalidSubnetException: <p>The specified VPC has no associated Internet gateway.</p>
            capo_elastic_load_balancing.errors.subnet_not_found_exception.SubnetNotFoundException: <p>One or more of the specified subnets do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To attach subnets to a load balancer
            This example adds the specified subnet to the set of configured subnets for the specified load balancer.

            >>> client.attach_load_balancer_to_subnets(load_balancer_name='my-load-balancer', subnets=['subnet-0ecac448'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_input.AttachLoadBalancerToSubnetsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_output.AttachLoadBalancerToSubnetsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.attach_load_balancer_to_subnets

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.attach_load_balancer_to_subnets.attach_load_balancer_to_subnets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.attach_load_balancer_to_subnets_input.AttachLoadBalancerToSubnetsInput = {
            "load_balancer_name": load_balancer_name,
            "subnets": subnets,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def configure_health_check(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        health_check: "capo_elastic_load_balancing.types.health_check.HealthCheck",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.configure_health_check_output.ConfigureHealthCheckOutput":
        """<p>Specifies the health check settings to use when evaluating the health state of your EC2 instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html">Configure Health Checks for Your Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            health_check: <p>The configuration information.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To specify the health check settings for your backend EC2 instances
            This example specifies the health check settings used to evaluate the health of your backend EC2 instances.

            >>> client.configure_health_check(load_balancer_name='my-load-balancer', health_check={'Target': 'HTTP:80/png', 'Interval': 30, 'Timeout': 3, 'UnhealthyThreshold': 2, 'HealthyThreshold': 2})
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.configure_health_check_input.ConfigureHealthCheckInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.configure_health_check_output.ConfigureHealthCheckOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.configure_health_check

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.configure_health_check.configure_health_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.configure_health_check_input.ConfigureHealthCheckInput = {
            "load_balancer_name": load_balancer_name,
            "health_check": health_check,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_app_cookie_stickiness_policy(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName",
        cookie_name: "capo_elastic_load_balancing.types.cookie_name.CookieName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_output.CreateAppCookieStickinessPolicyOutput":
        """<p>Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.</p> <p>This policy is similar to the policy created by <a>CreateLBCookieStickinessPolicy</a>, except that the lifetime of the special Elastic Load Balancing cookie, <code>AWSELB</code>, follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.</p> <p>If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application">Application-Controlled Session Stickiness</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            policy_name: <p>The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.</p>
            cookie_name: <p>The name of the application cookie used for stickiness.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.duplicate_policy_name_exception.DuplicatePolicyNameException: <p>A policy with the specified name already exists for this load balancer.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.too_many_policies_exception.TooManyPoliciesException: <p>The quota for the number of policies for this load balancer has been reached.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To generate a stickiness policy for your load balancer
            This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.

            >>> client.create_app_cookie_stickiness_policy(load_balancer_name='my-load-balancer', policy_name='my-app-cookie-policy', cookie_name='my-app-cookie')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_input.CreateAppCookieStickinessPolicyInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_output.CreateAppCookieStickinessPolicyOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_app_cookie_stickiness_policy

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_app_cookie_stickiness_policy.create_app_cookie_stickiness_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.create_app_cookie_stickiness_policy_input.CreateAppCookieStickinessPolicyInput = {
            "load_balancer_name": load_balancer_name,
            "policy_name": policy_name,
            "cookie_name": cookie_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lb_cookie_stickiness_policy(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        cookie_expiration_period: Optional[
            "capo_elastic_load_balancing.types.cookie_expiration_period.CookieExpirationPeriod"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_output.CreateLBCookieStickinessPolicyOutput":
        """<p>Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.</p> <p>When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.</p> <p>A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration">Duration-Based Session Stickiness</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            policy_name: <p>The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.</p>
            cookie_expiration_period: <p>The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.duplicate_policy_name_exception.DuplicatePolicyNameException: <p>A policy with the specified name already exists for this load balancer.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.too_many_policies_exception.TooManyPoliciesException: <p>The quota for the number of policies for this load balancer has been reached.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To generate a duration-based stickiness policy for your load balancer
            This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.

            >>> client.create_lb_cookie_stickiness_policy(load_balancer_name='my-load-balancer', policy_name='my-duration-cookie-policy', cookie_expiration_period=60)
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_input.CreateLBCookieStickinessPolicyInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_output.CreateLBCookieStickinessPolicyOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_lb_cookie_stickiness_policy

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_lb_cookie_stickiness_policy.create_lb_cookie_stickiness_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.create_lb_cookie_stickiness_policy_input.CreateLBCookieStickinessPolicyInput = {
            "load_balancer_name": load_balancer_name,
            "policy_name": policy_name,
        }
        if cookie_expiration_period is not None:
            input_["cookie_expiration_period"] = cookie_expiration_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        listeners: "capo_elastic_load_balancing.types.listeners.Listeners",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        availability_zones: Optional[
            "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones"
        ] = None,
        subnets: Optional["capo_elastic_load_balancing.types.subnets.Subnets"] = None,
        security_groups: Optional[
            "capo_elastic_load_balancing.types.security_groups.SecurityGroups"
        ] = None,
        scheme: Optional[
            "capo_elastic_load_balancing.types.load_balancer_scheme.LoadBalancerScheme"
        ] = None,
        tags: Optional["capo_elastic_load_balancing.types.tag_list.TagList"] = None,
    ) -> "capo_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput":
        """<p>Creates a Classic Load Balancer.</p> <p>You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using <a>CreateLoadBalancerListeners</a>, <a>ApplySecurityGroupsToLoadBalancer</a>, <a>AttachLoadBalancerToSubnets</a>, and <a>AddTags</a>.</p> <p>To describe your current load balancers, see <a>DescribeLoadBalancers</a>. When you are finished with a load balancer, you can delete it using <a>DeleteLoadBalancer</a>.</p> <p>You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html">Limits for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p> <p>This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.</p>
            listeners: <p>The listeners.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html">Listeners for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>
            availability_zones: <p>One or more Availability Zones from the same region as the load balancer.</p> <p>You must specify at least one Availability Zone.</p> <p>You can add more Availability Zones after you create the load balancer using <a>EnableAvailabilityZonesForLoadBalancer</a>.</p>
            subnets: <p>The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in <code>AvailabilityZones</code>.</p>
            security_groups: <p>The IDs of the security groups to assign to the load balancer.</p>
            scheme: <p>The type of a load balancer. Valid only for load balancers in a VPC.</p> <p>By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme">Load Balancer Scheme</a> in the <i>Elastic Load Balancing User Guide</i>.</p> <p>Specify <code>internal</code> to create a load balancer with a DNS name that resolves to private IP addresses.</p>
            tags: <p>A list of tags to assign to the load balancer.</p> <p>For more information about tagging your load balancer, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html">Tag Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Raises:
            capo_elastic_load_balancing.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.</p>
            capo_elastic_load_balancing.errors.duplicate_access_point_name_exception.DuplicateAccessPointNameException: <p>The specified load balancer name already exists for this account.</p>
            capo_elastic_load_balancing.errors.duplicate_tag_keys_exception.DuplicateTagKeysException: <p>A tag key was specified more than once.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.invalid_scheme_exception.InvalidSchemeException: <p>The specified value for the schema is not valid. You can only specify a scheme for load balancers in a VPC.</p>
            capo_elastic_load_balancing.errors.invalid_security_group_exception.InvalidSecurityGroupException: <p>One or more of the specified security groups do not exist.</p>
            capo_elastic_load_balancing.errors.invalid_subnet_exception.InvalidSubnetException: <p>The specified VPC has no associated Internet gateway.</p>
            capo_elastic_load_balancing.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not allowed.</p>
            capo_elastic_load_balancing.errors.subnet_not_found_exception.SubnetNotFoundException: <p>One or more of the specified subnets do not exist.</p>
            capo_elastic_load_balancing.errors.too_many_access_points_exception.TooManyAccessPointsException: <p>The quota for the number of load balancers has been reached.</p>
            capo_elastic_load_balancing.errors.too_many_tags_exception.TooManyTagsException: <p>The quota for the number of tags that can be assigned to a load balancer has been reached.</p>
            capo_elastic_load_balancing.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol or signature version is not supported.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an HTTP load balancer in a VPC
            This example creates a load balancer with an HTTP listener in a VPC.

            >>> client.create_load_balancer(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}], subnets=['subnet-15aaab61'], security_groups=['sg-a61988c3'])
            To create an HTTP load balancer in EC2-Classic
            This example creates a load balancer with an HTTP listener in EC2-Classic.

            >>> client.create_load_balancer(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}], availability_zones=['us-west-2a'])
            To create an HTTPS load balancer in a VPC
            This example creates a load balancer with an HTTPS listener in a VPC.

            >>> client.create_load_balancer(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}, {'Protocol': 'HTTPS', 'LoadBalancerPort': 443, 'InstanceProtocol': 'HTTP', 'InstancePort': 80, 'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert'}], subnets=['subnet-15aaab61'], security_groups=['sg-a61988c3'])
            To create an HTTPS load balancer in EC2-Classic
            This example creates a load balancer with an HTTPS listener in EC2-Classic.

            >>> client.create_load_balancer(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}, {'Protocol': 'HTTPS', 'LoadBalancerPort': 443, 'InstanceProtocol': 'HTTP', 'InstancePort': 80, 'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert'}], availability_zones=['us-west-2a'])
            To create an internal load balancer
            This example creates an internal load balancer with an HTTP listener in a VPC.

            >>> client.create_load_balancer(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}], subnets=['subnet-15aaab61'], security_groups=['sg-a61988c3'], scheme='internal')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.create_access_point_input.CreateAccessPointInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer.create_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.create_access_point_input.CreateAccessPointInput = {
            "load_balancer_name": load_balancer_name,
            "listeners": listeners,
        }
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if subnets is not None:
            input_["subnets"] = subnets
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if scheme is not None:
            input_["scheme"] = scheme
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_load_balancer_listeners(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        listeners: "capo_elastic_load_balancing.types.listeners.Listeners",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.create_load_balancer_listener_output.CreateLoadBalancerListenerOutput":
        """<p>Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html">Listeners for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            listeners: <p>The listeners.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.</p>
            capo_elastic_load_balancing.errors.duplicate_listener_exception.DuplicateListenerException: <p>A listener already exists for the specified load balancer name and port, but with a different instance port, protocol, or SSL certificate.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol or signature version is not supported.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an HTTP listener for a load balancer
            This example creates a listener for your load balancer at port 80 using the HTTP protocol.

            >>> client.create_load_balancer_listeners(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTP', 'LoadBalancerPort': 80, 'InstanceProtocol': 'HTTP', 'InstancePort': 80}])
            To create an HTTPS listener for a load balancer
            This example creates a listener for your load balancer at port 443 using the HTTPS protocol.

            >>> client.create_load_balancer_listeners(load_balancer_name='my-load-balancer', listeners=[{'Protocol': 'HTTPS', 'LoadBalancerPort': 443, 'InstanceProtocol': 'HTTP', 'InstancePort': 80, 'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.create_load_balancer_listener_input.CreateLoadBalancerListenerInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.create_load_balancer_listener_output.CreateLoadBalancerListenerOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer_listeners

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer_listeners.create_load_balancer_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.create_load_balancer_listener_input.CreateLoadBalancerListenerInput = {
            "load_balancer_name": load_balancer_name,
            "listeners": listeners,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_load_balancer_policy(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName",
        policy_type_name: "capo_elastic_load_balancing.types.policy_type_name.PolicyTypeName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        policy_attributes: Optional[
            "capo_elastic_load_balancing.types.policy_attributes.PolicyAttributes"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.create_load_balancer_policy_output.CreateLoadBalancerPolicyOutput":
        """<p>Creates a policy with the specified attributes for the specified load balancer.</p> <p>Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            policy_name: <p>The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.</p>
            policy_type_name: <p>The name of the base policy type. To get the list of policy types, use <a>DescribeLoadBalancerPolicyTypes</a>.</p>
            policy_attributes: <p>The policy attributes.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.duplicate_policy_name_exception.DuplicatePolicyNameException: <p>A policy with the specified name already exists for this load balancer.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.policy_type_not_found_exception.PolicyTypeNotFoundException: <p>One or more of the specified policy types do not exist.</p>
            capo_elastic_load_balancing.errors.too_many_policies_exception.TooManyPoliciesException: <p>The quota for the number of policies for this load balancer has been reached.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a policy that enables Proxy Protocol on a load balancer
            This example creates a policy that enables Proxy Protocol on the specified load balancer.

            >>> client.create_load_balancer_policy(load_balancer_name='my-load-balancer', policy_name='my-ProxyProtocol-policy', policy_type_name='ProxyProtocolPolicyType', policy_attributes=[{'AttributeName': 'ProxyProtocol', 'AttributeValue': 'true'}])
            To create a public key policy
            This example creates a public key policy.

            >>> client.create_load_balancer_policy(load_balancer_name='my-load-balancer', policy_name='my-PublicKey-policy', policy_type_name='PublicKeyPolicyType', policy_attributes=[{'AttributeName': 'PublicKey', 'AttributeValue': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwAYUjnfyEyXr1pxjhFWBpMlggUcqoi3kl+dS74kj//c6x7ROtusUaeQCTgIUkayttRDWchuqo1pHC1u+n5xxXnBBe2ejbb2WRsKIQ5rXEeixsjFpFsojpSQKkzhVGI6mJVZBJDVKSHmswnwLBdofLhzvllpovBPTHe+o4haAWvDBALJU0pkSI1FecPHcs2hwxf14zHoXy1e2k36A64nXW43wtfx5qcVSIxtCEOjnYRg7RPvybaGfQ+v6Iaxb/+7J5kEvZhTFQId+bSiJImF1FSUT1W1xwzBZPUbcUkkXDj45vC2s3Z8E+Lk7a3uZhvsQHLZnrfuWjBWGWvZ/MhZYgEXAMPLE'}])
            To create a backend server authentication policy
            This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy.

            >>> client.create_load_balancer_policy(load_balancer_name='my-load-balancer', policy_name='my-authentication-policy', policy_type_name='BackendServerAuthenticationPolicyType', policy_attributes=[{'AttributeName': 'PublicKeyPolicyName', 'AttributeValue': 'my-PublicKey-policy'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.create_load_balancer_policy_input.CreateLoadBalancerPolicyInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.create_load_balancer_policy_output.CreateLoadBalancerPolicyOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer_policy

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.create_load_balancer_policy.create_load_balancer_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.create_load_balancer_policy_input.CreateLoadBalancerPolicyInput = {
            "load_balancer_name": load_balancer_name,
            "policy_name": policy_name,
            "policy_type_name": policy_type_name,
        }
        if policy_attributes is not None:
            input_["policy_attributes"] = policy_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.delete_access_point_output.DeleteAccessPointOutput":
        """<p>Deletes the specified load balancer.</p> <p>If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.</p> <p>If the load balancer does not exist or has already been deleted, the call to <code>DeleteLoadBalancer</code> still succeeds.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>

        Raises:
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a load balancer
            This example deletes the specified load balancer.

            >>> client.delete_load_balancer(load_balancer_name='my-load-balancer')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.delete_access_point_input.DeleteAccessPointInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.delete_access_point_output.DeleteAccessPointOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer.delete_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.delete_access_point_input.DeleteAccessPointInput = {
            "load_balancer_name": load_balancer_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_load_balancer_listeners(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        load_balancer_ports: "capo_elastic_load_balancing.types.ports.Ports",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.delete_load_balancer_listener_output.DeleteLoadBalancerListenerOutput":
        """<p>Deletes the specified listeners from the specified load balancer.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            load_balancer_ports: <p>The client port numbers of the listeners.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a listener from your load balancer
            This example deletes the listener for the specified port from the specified load balancer.

            >>> client.delete_load_balancer_listeners(load_balancer_name='my-load-balancer', load_balancer_ports=[80])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.delete_load_balancer_listener_input.DeleteLoadBalancerListenerInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.delete_load_balancer_listener_output.DeleteLoadBalancerListenerOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer_listeners

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer_listeners.delete_load_balancer_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.delete_load_balancer_listener_input.DeleteLoadBalancerListenerInput = {
            "load_balancer_name": load_balancer_name,
            "load_balancer_ports": load_balancer_ports,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_load_balancer_policy(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.delete_load_balancer_policy_output.DeleteLoadBalancerPolicyOutput":
        """<p>Deletes the specified policy from the specified load balancer. This policy must not be enabled for any listeners.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            policy_name: <p>The name of the policy.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a policy from your load balancer
            This example deletes the specified policy from the specified load balancer. The policy must not be enabled on any listener.

            >>> client.delete_load_balancer_policy(load_balancer_name='my-load-balancer', policy_name='my-duration-cookie-policy')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.delete_load_balancer_policy_input.DeleteLoadBalancerPolicyInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.delete_load_balancer_policy_output.DeleteLoadBalancerPolicyOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer_policy

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.delete_load_balancer_policy.delete_load_balancer_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.delete_load_balancer_policy_input.DeleteLoadBalancerPolicyInput = {
            "load_balancer_name": load_balancer_name,
            "policy_name": policy_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_instances_from_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        instances: "capo_elastic_load_balancing.types.instances.Instances",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.deregister_end_points_output.DeregisterEndPointsOutput":
        """<p>Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.</p> <p>You can use <a>DescribeLoadBalancers</a> to verify that the instance is deregistered from the load balancer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html">Register or De-Register EC2 Instances</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            instances: <p>The IDs of the instances.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_end_point_exception.InvalidEndPointException: <p>The specified endpoint is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister instances from a load balancer
            This example deregisters the specified instance from the specified load balancer.

            >>> client.deregister_instances_from_load_balancer(load_balancer_name='my-load-balancer', instances=[{'InstanceId': 'i-d6f6fae3'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.deregister_end_points_input.DeregisterEndPointsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.deregister_end_points_output.DeregisterEndPointsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.deregister_instances_from_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.deregister_instances_from_load_balancer.deregister_instances_from_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.deregister_end_points_input.DeregisterEndPointsInput = {
            "load_balancer_name": load_balancer_name,
            "instances": instances,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_limits(
        self,
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        marker: Optional["capo_elastic_load_balancing.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.describe_account_limits_output.DescribeAccountLimitsOutput":
        """<p>Describes the current Elastic Load Balancing resource limits for your AWS account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html">Limits for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call.</p>

        Raises:
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_account_limits_input.DescribeAccountLimitsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_account_limits_output.DescribeAccountLimitsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_account_limits

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_account_limits.describe_account_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_account_limits_input.DescribeAccountLimitsInput = {}
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_instance_health(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        instances: Optional[
            "capo_elastic_load_balancing.types.instances.Instances"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput":
        """<p>Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            instances: <p>The IDs of the instances.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_end_point_exception.InvalidEndPointException: <p>The specified endpoint is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the health of the instances for a load balancer
            This example describes the health of the instances for the specified load balancer.

            >>> client.describe_instance_health(load_balancer_name='my-load-balancer')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_end_point_state_input.DescribeEndPointStateInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_instance_health

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_instance_health.describe_instance_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_end_point_state_input.DescribeEndPointStateInput = {
            "load_balancer_name": load_balancer_name
        }
        if instances is not None:
            input_["instances"] = instances

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_load_balancer_attributes(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.describe_load_balancer_attributes_output.DescribeLoadBalancerAttributesOutput":
        """<p>Describes the attributes for the specified load balancer.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.load_balancer_attribute_not_found_exception.LoadBalancerAttributeNotFoundException: <p>The specified load balancer attribute does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the attributes of a load balancer
            This example describes the attributes of the specified load balancer.

            >>> client.describe_load_balancer_attributes(load_balancer_name='my-load-balancer')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_load_balancer_attributes_input.DescribeLoadBalancerAttributesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_load_balancer_attributes_output.DescribeLoadBalancerAttributesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_attributes

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_attributes.describe_load_balancer_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_load_balancer_attributes_input.DescribeLoadBalancerAttributesInput = {
            "load_balancer_name": load_balancer_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_load_balancer_policies(
        self,
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        load_balancer_name: Optional[
            "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
        ] = None,
        policy_names: Optional[
            "capo_elastic_load_balancing.types.policy_names.PolicyNames"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.describe_load_balancer_policies_output.DescribeLoadBalancerPoliciesOutput":
        """<p>Describes the specified policies.</p> <p>If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don't specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the <code>ELBSample-</code> prefix.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            policy_names: <p>The names of the policies.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.policy_not_found_exception.PolicyNotFoundException: <p>One or more of the specified policies do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a policy associated with a load balancer
            This example describes the specified policy associated with the specified load balancer.

            >>> client.describe_load_balancer_policies(load_balancer_name='my-load-balancer', policy_names=['my-authentication-policy'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_load_balancer_policies_input.DescribeLoadBalancerPoliciesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_load_balancer_policies_output.DescribeLoadBalancerPoliciesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_policies

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_policies.describe_load_balancer_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_load_balancer_policies_input.DescribeLoadBalancerPoliciesInput = {}
        if load_balancer_name is not None:
            input_["load_balancer_name"] = load_balancer_name
        if policy_names is not None:
            input_["policy_names"] = policy_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_load_balancer_policy_types(
        self,
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        policy_type_names: Optional[
            "capo_elastic_load_balancing.types.policy_type_names.PolicyTypeNames"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.describe_load_balancer_policy_types_output.DescribeLoadBalancerPolicyTypesOutput":
        """<p>Describes the specified load balancer policy types or all load balancer policy types.</p> <p>The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.</p> <p>You can use <a>CreateLoadBalancerPolicy</a> to create a policy configuration for any of these policy types. Then, depending on the policy type, use either <a>SetLoadBalancerPoliciesOfListener</a> or <a>SetLoadBalancerPoliciesForBackendServer</a> to set the policy.</p>

        Args:
            policy_type_names: <p>The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.</p>

        Raises:
            capo_elastic_load_balancing.errors.policy_type_not_found_exception.PolicyTypeNotFoundException: <p>One or more of the specified policy types do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a load balancer policy type defined by Elastic Load Balancing
            This example describes the specified load balancer policy type.

            >>> client.describe_load_balancer_policy_types(policy_type_names=['ProxyProtocolPolicyType'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_load_balancer_policy_types_input.DescribeLoadBalancerPolicyTypesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_load_balancer_policy_types_output.DescribeLoadBalancerPolicyTypesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_policy_types

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancer_policy_types.describe_load_balancer_policy_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_load_balancer_policy_types_input.DescribeLoadBalancerPolicyTypesInput = {}
        if policy_type_names is not None:
            input_["policy_type_names"] = policy_type_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_load_balancers(
        self,
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        load_balancer_names: Optional[
            "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing.types.page_size.PageSize"
        ] = None,
    ) -> "capo_elastic_load_balancing.types.describe_access_points_output.DescribeAccessPointsOutput":
        """<p>Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.</p>

        Args:
            load_balancer_names: <p>The names of the load balancers.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            page_size: <p>The maximum number of results to return with this call (a number from 1 to 400). The default is 400.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.dependency_throttle_exception.DependencyThrottleException: <p>A request made by Elastic Load Balancing to another service exceeds the maximum request rate permitted for your account.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe one of your load balancers
            This example describes the specified load balancer.

            >>> client.describe_load_balancers(load_balancer_names=['my-load-balancer'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_access_points_input.DescribeAccessPointsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_access_points_output.DescribeAccessPointsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancers

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_load_balancers.describe_load_balancers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_access_points_input.DescribeAccessPointsInput = {}
        if load_balancer_names is not None:
            input_["load_balancer_names"] = load_balancer_names
        if marker is not None:
            input_["marker"] = marker
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_load_balancers(
        self,
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
        load_balancer_names: Optional[
            "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        marker: Optional["capo_elastic_load_balancing.types.marker.Marker"] = None,
        page_size: Optional[
            "capo_elastic_load_balancing.types.page_size.PageSize"
        ] = None,
    ) -> "Iterator[capo_elastic_load_balancing.types.load_balancer_description.LoadBalancerDescription]":
        _token = marker
        while True:
            _response = self.describe_load_balancers(
                config_overrides=config_overrides,
                load_balancer_names=load_balancer_names,
                marker=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("load_balancer_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def describe_tags(
        self,
        load_balancer_names: "capo_elastic_load_balancing.types.load_balancer_names_max20.LoadBalancerNamesMax20",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.describe_tags_output.DescribeTagsOutput":
        """<p>Describes the tags associated with the specified load balancers.</p>

        Args:
            load_balancer_names: <p>The names of the load balancers.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the tags for a load balancer
            This example describes the tags for the specified load balancer.

            >>> client.describe_tags(load_balancer_names=['my-load-balancer'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.describe_tags_input.DescribeTagsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.describe_tags_output.DescribeTagsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_tags

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.describe_tags.describe_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.describe_tags_input.DescribeTagsInput = {
            "load_balancer_names": load_balancer_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_load_balancer_from_subnets(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        subnets: "capo_elastic_load_balancing.types.subnets.Subnets",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_output.DetachLoadBalancerFromSubnetsOutput":
        """<p>Removes the specified subnets from the set of configured subnets for the load balancer.</p> <p>After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the <code>OutOfService</code> state. Then, the load balancer balances the traffic among the remaining routable subnets.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            subnets: <p>The IDs of the subnets.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detach a load balancer from a subnet
            This example detaches the specified load balancer from the specified subnet.

            >>> client.detach_load_balancer_from_subnets(load_balancer_name='my-load-balancer', subnets=['subnet-0ecac448'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_input.DetachLoadBalancerFromSubnetsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_output.DetachLoadBalancerFromSubnetsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.detach_load_balancer_from_subnets

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.detach_load_balancer_from_subnets.detach_load_balancer_from_subnets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.detach_load_balancer_from_subnets_input.DetachLoadBalancerFromSubnetsInput = {
            "load_balancer_name": load_balancer_name,
            "subnets": subnets,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_availability_zones_for_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        availability_zones: "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.remove_availability_zones_output.RemoveAvailabilityZonesOutput":
        """<p>Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.</p> <p>For load balancers in a non-default VPC, use <a>DetachLoadBalancerFromSubnets</a>.</p> <p>There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the <code>OutOfService</code> state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html">Add or Remove Availability Zones</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            availability_zones: <p>The Availability Zones.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable an Availability Zone for a load balancer
            This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer.

            >>> client.disable_availability_zones_for_load_balancer(load_balancer_name='my-load-balancer', availability_zones=['us-west-2a'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.remove_availability_zones_input.RemoveAvailabilityZonesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.remove_availability_zones_output.RemoveAvailabilityZonesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.disable_availability_zones_for_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.disable_availability_zones_for_load_balancer.disable_availability_zones_for_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.remove_availability_zones_input.RemoveAvailabilityZonesInput = {
            "load_balancer_name": load_balancer_name,
            "availability_zones": availability_zones,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_availability_zones_for_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        availability_zones: "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.add_availability_zones_output.AddAvailabilityZonesOutput":
        """<p>Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.</p> <p>For load balancers in a non-default VPC, use <a>AttachLoadBalancerToSubnets</a>.</p> <p>The load balancer evenly distributes requests across all its registered Availability Zones that contain instances. For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html">Add or Remove Availability Zones</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            availability_zones: <p>The Availability Zones. These must be in the same region as the load balancer.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable an Availability Zone for a load balancer
            This example adds the specified Availability Zone to the specified load balancer.

            >>> client.enable_availability_zones_for_load_balancer(load_balancer_name='my-load-balancer', availability_zones=['us-west-2b'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.add_availability_zones_input.AddAvailabilityZonesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.add_availability_zones_output.AddAvailabilityZonesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.enable_availability_zones_for_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.enable_availability_zones_for_load_balancer.enable_availability_zones_for_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.add_availability_zones_input.AddAvailabilityZonesInput = {
            "load_balancer_name": load_balancer_name,
            "availability_zones": availability_zones,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_load_balancer_attributes(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        load_balancer_attributes: "capo_elastic_load_balancing.types.load_balancer_attributes.LoadBalancerAttributes",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.modify_load_balancer_attributes_output.ModifyLoadBalancerAttributesOutput":
        """<p>Modifies the attributes of the specified load balancer.</p> <p>You can modify the load balancer attributes, such as <code>AccessLogs</code>, <code>ConnectionDraining</code>, and <code>CrossZoneLoadBalancing</code> by either enabling or disabling them. Or, you can modify the load balancer attribute <code>ConnectionSettings</code> by specifying an idle connection timeout value for your load balancer.</p> <p>For more information, see the following in the <i>Classic Load Balancers Guide</i>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html">Cross-Zone Load Balancing</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html">Connection Draining</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html">Access Logs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html">Idle Connection Timeout</a> </p> </li> </ul>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            load_balancer_attributes: <p>The attributes for the load balancer.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.load_balancer_attribute_not_found_exception.LoadBalancerAttributeNotFoundException: <p>The specified load balancer attribute does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable cross-zone load balancing
            This example enables cross-zone load balancing for the specified load balancer.

            >>> client.modify_load_balancer_attributes(load_balancer_name='my-load-balancer', load_balancer_attributes={'CrossZoneLoadBalancing': {'Enabled': True}})
            To enable connection draining
            This example enables connection draining for the specified load balancer.

            >>> client.modify_load_balancer_attributes(load_balancer_name='my-load-balancer', load_balancer_attributes={'ConnectionDraining': {'Enabled': True, 'Timeout': 300}})
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.modify_load_balancer_attributes_input.ModifyLoadBalancerAttributesInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.modify_load_balancer_attributes_output.ModifyLoadBalancerAttributesOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.modify_load_balancer_attributes

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.modify_load_balancer_attributes.modify_load_balancer_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.modify_load_balancer_attributes_input.ModifyLoadBalancerAttributesInput = {
            "load_balancer_name": load_balancer_name,
            "load_balancer_attributes": load_balancer_attributes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_instances_with_load_balancer(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        instances: "capo_elastic_load_balancing.types.instances.Instances",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.register_end_points_output.RegisterEndPointsOutput":
        """<p>Adds the specified instances to the specified load balancer.</p> <p>The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.</p> <p>Note that <code>RegisterInstanceWithLoadBalancer</code> completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use <a>DescribeLoadBalancers</a> or <a>DescribeInstanceHealth</a>.</p> <p>After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the <code>OutOfService</code> state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the <code>InService</code> state.</p> <p>To deregister instances from a load balancer, use <a>DeregisterInstancesFromLoadBalancer</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html">Register or De-Register EC2 Instances</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            instances: <p>The IDs of the instances.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_end_point_exception.InvalidEndPointException: <p>The specified endpoint is not valid.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register instances with a load balancer
            This example registers the specified instance with the specified load balancer.

            >>> client.register_instances_with_load_balancer(load_balancer_name='my-load-balancer', instances=[{'InstanceId': 'i-d6f6fae3'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.register_end_points_input.RegisterEndPointsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.register_end_points_output.RegisterEndPointsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.register_instances_with_load_balancer

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.register_instances_with_load_balancer.register_instances_with_load_balancer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.register_end_points_input.RegisterEndPointsInput = {
            "load_balancer_name": load_balancer_name,
            "instances": instances,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags(
        self,
        load_balancer_names: "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames",
        tags: "capo_elastic_load_balancing.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.remove_tags_output.RemoveTagsOutput":
        """<p>Removes one or more tags from the specified load balancer.</p>

        Args:
            load_balancer_names: <p>The name of the load balancer. You can specify a maximum of one load balancer name.</p>
            tags: <p>The list of tag keys to remove.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a load balancer
            This example removes the specified tag from the specified load balancer.

            >>> client.remove_tags(load_balancer_names=['my-load-balancer'], tags=[{'Key': 'project'}])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.remove_tags_input.RemoveTagsInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.remove_tags_output.RemoveTagsOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.remove_tags

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.remove_tags.remove_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.remove_tags_input.RemoveTagsInput = {
            "load_balancer_names": load_balancer_names,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_load_balancer_listener_ssl_certificate(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        load_balancer_port: "capo_elastic_load_balancing.types.access_point_port.AccessPointPort",
        ssl_certificate_id: "capo_elastic_load_balancing.types.ssl_certificate_id.SSLCertificateId",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_output.SetLoadBalancerListenerSSLCertificateOutput":
        """<p>Sets the certificate that terminates the specified listener's SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.</p> <p>For more information about updating your SSL certificate, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html">Replace the SSL Certificate for Your Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            load_balancer_port: <p>The port that uses the specified SSL certificate.</p>
            ssl_certificate_id: <p>The Amazon Resource Name (ARN) of the SSL certificate.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.certificate_not_found_exception.CertificateNotFoundException: <p>The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.listener_not_found_exception.ListenerNotFoundException: <p>The load balancer does not have a listener configured at the specified port.</p>
            capo_elastic_load_balancing.errors.unsupported_protocol_exception.UnsupportedProtocolException: <p>The specified protocol or signature version is not supported.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the SSL certificate for an HTTPS listener
            This example replaces the existing SSL certificate for the specified HTTPS listener.

            >>> client.set_load_balancer_listener_ssl_certificate(load_balancer_name='my-load-balancer', load_balancer_port=443, ssl_certificate_id='arn:aws:iam::123456789012:server-certificate/new-server-cert')
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_input.SetLoadBalancerListenerSSLCertificateInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_output.SetLoadBalancerListenerSSLCertificateOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_listener_ssl_certificate

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_listener_ssl_certificate.set_load_balancer_listener_ssl_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.set_load_balancer_listener_ssl_certificate_input.SetLoadBalancerListenerSSLCertificateInput = {
            "load_balancer_name": load_balancer_name,
            "load_balancer_port": load_balancer_port,
            "ssl_certificate_id": ssl_certificate_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_load_balancer_policies_for_backend_server(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        instance_port: "capo_elastic_load_balancing.types.end_point_port.EndPointPort",
        policy_names: "capo_elastic_load_balancing.types.policy_names.PolicyNames",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_output.SetLoadBalancerPoliciesForBackendServerOutput":
        """<p>Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.</p> <p>Each time you use <code>SetLoadBalancerPoliciesForBackendServer</code> to enable the policies, use the <code>PolicyNames</code> parameter to list the policies that you want to enable.</p> <p>You can use <a>DescribeLoadBalancers</a> or <a>DescribeLoadBalancerPolicies</a> to verify that the policy is associated with the EC2 instance.</p> <p>For more information about enabling back-end instance authentication, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#configure_backendauth_clt">Configure Back-end Instance Authentication</a> in the <i>Classic Load Balancers Guide</i>. For more information about Proxy Protocol, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html">Configure Proxy Protocol Support</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            instance_port: <p>The port number associated with the EC2 instance.</p>
            policy_names: <p>The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.policy_not_found_exception.PolicyNotFoundException: <p>One or more of the specified policies do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To replace the policies associated with a port for a backend instance
            This example replaces the policies that are currently associated with the specified port.

            >>> client.set_load_balancer_policies_for_backend_server(load_balancer_name='my-load-balancer', instance_port=80, policy_names=['my-ProxyProtocol-policy'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_input.SetLoadBalancerPoliciesForBackendServerInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_output.SetLoadBalancerPoliciesForBackendServerOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_policies_for_backend_server

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_policies_for_backend_server.set_load_balancer_policies_for_backend_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.set_load_balancer_policies_for_backend_server_input.SetLoadBalancerPoliciesForBackendServerInput = {
            "load_balancer_name": load_balancer_name,
            "instance_port": instance_port,
            "policy_names": policy_names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_load_balancer_policies_of_listener(
        self,
        load_balancer_name: "capo_elastic_load_balancing.types.access_point_name.AccessPointName",
        load_balancer_port: "capo_elastic_load_balancing.types.access_point_port.AccessPointPort",
        policy_names: "capo_elastic_load_balancing.types.policy_names.PolicyNames",
        *,
        config_overrides: Optional[ElasticLoadBalancingClientConfig] = None,
    ) -> "capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_output.SetLoadBalancerPoliciesOfListenerOutput":
        """<p>Replaces the current set of policies for the specified load balancer port with the specified set of policies.</p> <p>To enable back-end server authentication, use <a>SetLoadBalancerPoliciesForBackendServer</a>.</p> <p>For more information about setting policies, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html">Update the SSL Negotiation Configuration</a>, <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration">Duration-Based Session Stickiness</a>, and <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application">Application-Controlled Session Stickiness</a> in the <i>Classic Load Balancers Guide</i>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            load_balancer_port: <p>The external port of the load balancer.</p>
            policy_names: <p>The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.</p>

        Raises:
            capo_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException: <p>The specified load balancer does not exist.</p>
            capo_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException: <p>The requested configuration change is not valid.</p>
            capo_elastic_load_balancing.errors.listener_not_found_exception.ListenerNotFoundException: <p>The load balancer does not have a listener configured at the specified port.</p>
            capo_elastic_load_balancing.errors.policy_not_found_exception.PolicyNotFoundException: <p>One or more of the specified policies do not exist.</p>
            capo_elastic_load_balancing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To replace the policies associated with a listener
            This example replaces the policies that are currently associated with the specified listener.

            >>> client.set_load_balancer_policies_of_listener(load_balancer_name='my-load-balancer', load_balancer_port=80, policy_names=['my-SSLNegotiation-policy'])
        """

        def _handler(
            req: "OperationRequest[capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_input.SetLoadBalancerPoliciesOfListenerInput]",
        ) -> OperationResponse[
            "capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_output.SetLoadBalancerPoliciesOfListenerOutput"
        ]:
            import capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_policies_of_listener

            output, http_response = (
                capo_elastic_load_balancing._operations.elastic_load_balancing_v7.set_load_balancer_policies_of_listener.set_load_balancer_policies_of_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_load_balancing.types.set_load_balancer_policies_of_listener_input.SetLoadBalancerPoliciesOfListenerInput = {
            "load_balancer_name": load_balancer_name,
            "load_balancer_port": load_balancer_port,
            "policy_names": policy_names,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
