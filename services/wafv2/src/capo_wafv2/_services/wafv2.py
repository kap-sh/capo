"""Generated from Smithy shape ``com.amazonaws.wafv2#AWSWAF_20190729``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_wafv2._auth._signers
import capo_wafv2._auth._sigv4
from capo_wafv2._auth._identity import Credentials
from capo_wafv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_wafv2._auth._zapros_handler import AuthMiddleware
from capo_wafv2._services._aws_config import aws_config
from capo_wafv2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_wafv2.types.api_key
    import capo_wafv2.types.api_key_token_domains
    import capo_wafv2.types.application_config
    import capo_wafv2.types.associate_web_acl_request
    import capo_wafv2.types.associate_web_acl_response
    import capo_wafv2.types.association_config
    import capo_wafv2.types.capacity_unit
    import capo_wafv2.types.captcha_config
    import capo_wafv2.types.challenge_config
    import capo_wafv2.types.check_capacity_request
    import capo_wafv2.types.check_capacity_response
    import capo_wafv2.types.create_api_key_request
    import capo_wafv2.types.create_api_key_response
    import capo_wafv2.types.create_ip_set_request
    import capo_wafv2.types.create_ip_set_response
    import capo_wafv2.types.create_regex_pattern_set_request
    import capo_wafv2.types.create_regex_pattern_set_response
    import capo_wafv2.types.create_rule_group_request
    import capo_wafv2.types.create_rule_group_response
    import capo_wafv2.types.create_web_acl_request
    import capo_wafv2.types.create_web_acl_response
    import capo_wafv2.types.currency
    import capo_wafv2.types.custom_response_bodies
    import capo_wafv2.types.data_protection_config
    import capo_wafv2.types.default_action
    import capo_wafv2.types.delete_api_key_request
    import capo_wafv2.types.delete_api_key_response
    import capo_wafv2.types.delete_firewall_manager_rule_groups_request
    import capo_wafv2.types.delete_firewall_manager_rule_groups_response
    import capo_wafv2.types.delete_ip_set_request
    import capo_wafv2.types.delete_ip_set_response
    import capo_wafv2.types.delete_logging_configuration_request
    import capo_wafv2.types.delete_logging_configuration_response
    import capo_wafv2.types.delete_permission_policy_request
    import capo_wafv2.types.delete_permission_policy_response
    import capo_wafv2.types.delete_regex_pattern_set_request
    import capo_wafv2.types.delete_regex_pattern_set_response
    import capo_wafv2.types.delete_rule_group_request
    import capo_wafv2.types.delete_rule_group_response
    import capo_wafv2.types.delete_web_acl_request
    import capo_wafv2.types.delete_web_acl_response
    import capo_wafv2.types.describe_all_managed_products_request
    import capo_wafv2.types.describe_all_managed_products_response
    import capo_wafv2.types.describe_managed_products_by_vendor_request
    import capo_wafv2.types.describe_managed_products_by_vendor_response
    import capo_wafv2.types.describe_managed_rule_group_request
    import capo_wafv2.types.describe_managed_rule_group_response
    import capo_wafv2.types.disassociate_web_acl_request
    import capo_wafv2.types.disassociate_web_acl_response
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.generate_mobile_sdk_release_url_request
    import capo_wafv2.types.generate_mobile_sdk_release_url_response
    import capo_wafv2.types.get_decrypted_api_key_request
    import capo_wafv2.types.get_decrypted_api_key_response
    import capo_wafv2.types.get_ip_set_request
    import capo_wafv2.types.get_ip_set_response
    import capo_wafv2.types.get_logging_configuration_request
    import capo_wafv2.types.get_logging_configuration_response
    import capo_wafv2.types.get_managed_rule_set_request
    import capo_wafv2.types.get_managed_rule_set_response
    import capo_wafv2.types.get_mobile_sdk_release_request
    import capo_wafv2.types.get_mobile_sdk_release_response
    import capo_wafv2.types.get_permission_policy_request
    import capo_wafv2.types.get_permission_policy_response
    import capo_wafv2.types.get_rate_based_statement_managed_keys_request
    import capo_wafv2.types.get_rate_based_statement_managed_keys_response
    import capo_wafv2.types.get_regex_pattern_set_request
    import capo_wafv2.types.get_regex_pattern_set_response
    import capo_wafv2.types.get_revenue_statistics_request
    import capo_wafv2.types.get_revenue_statistics_response
    import capo_wafv2.types.get_revenue_statistics_summary_request
    import capo_wafv2.types.get_revenue_statistics_summary_response
    import capo_wafv2.types.get_revenue_statistics_time_series_request
    import capo_wafv2.types.get_revenue_statistics_time_series_response
    import capo_wafv2.types.get_rule_group_request
    import capo_wafv2.types.get_rule_group_response
    import capo_wafv2.types.get_sampled_requests_request
    import capo_wafv2.types.get_sampled_requests_response
    import capo_wafv2.types.get_top_path_statistics_by_traffic_request
    import capo_wafv2.types.get_top_path_statistics_by_traffic_response
    import capo_wafv2.types.get_web_acl_for_resource_request
    import capo_wafv2.types.get_web_acl_for_resource_response
    import capo_wafv2.types.get_web_acl_request
    import capo_wafv2.types.get_web_acl_response
    import capo_wafv2.types.group_by_type
    import capo_wafv2.types.interval_type
    import capo_wafv2.types.ip_address_version
    import capo_wafv2.types.ip_addresses
    import capo_wafv2.types.list_api_keys_request
    import capo_wafv2.types.list_api_keys_response
    import capo_wafv2.types.list_available_managed_rule_group_versions_request
    import capo_wafv2.types.list_available_managed_rule_group_versions_response
    import capo_wafv2.types.list_available_managed_rule_groups_request
    import capo_wafv2.types.list_available_managed_rule_groups_response
    import capo_wafv2.types.list_ip_sets_request
    import capo_wafv2.types.list_ip_sets_response
    import capo_wafv2.types.list_logging_configurations_request
    import capo_wafv2.types.list_logging_configurations_response
    import capo_wafv2.types.list_managed_rule_sets_request
    import capo_wafv2.types.list_managed_rule_sets_response
    import capo_wafv2.types.list_max_items
    import capo_wafv2.types.list_mobile_sdk_releases_request
    import capo_wafv2.types.list_mobile_sdk_releases_response
    import capo_wafv2.types.list_regex_pattern_sets_request
    import capo_wafv2.types.list_regex_pattern_sets_response
    import capo_wafv2.types.list_resources_for_web_acl_request
    import capo_wafv2.types.list_resources_for_web_acl_response
    import capo_wafv2.types.list_rule_groups_request
    import capo_wafv2.types.list_rule_groups_response
    import capo_wafv2.types.list_settlement_records_request
    import capo_wafv2.types.list_settlement_records_response
    import capo_wafv2.types.list_tags_for_resource_request
    import capo_wafv2.types.list_tags_for_resource_response
    import capo_wafv2.types.list_web_ac_ls_request
    import capo_wafv2.types.list_web_ac_ls_response
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.log_scope
    import capo_wafv2.types.log_type
    import capo_wafv2.types.logging_configuration
    import capo_wafv2.types.max_data_points
    import capo_wafv2.types.metric_name
    import capo_wafv2.types.monetization_config
    import capo_wafv2.types.monetization_filter_list
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.number_of_top_traffic_bots_per_path
    import capo_wafv2.types.on_source_d_do_s_protection_config
    import capo_wafv2.types.pagination_limit
    import capo_wafv2.types.path_statistics_limit
    import capo_wafv2.types.platform
    import capo_wafv2.types.policy_string
    import capo_wafv2.types.put_logging_configuration_request
    import capo_wafv2.types.put_logging_configuration_response
    import capo_wafv2.types.put_managed_rule_set_versions_request
    import capo_wafv2.types.put_managed_rule_set_versions_response
    import capo_wafv2.types.put_permission_policy_request
    import capo_wafv2.types.put_permission_policy_response
    import capo_wafv2.types.ranking_sort_by
    import capo_wafv2.types.ranking_statistic_type
    import capo_wafv2.types.regular_expression_list
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.resource_type
    import capo_wafv2.types.rules
    import capo_wafv2.types.scope
    import capo_wafv2.types.settlement_record_limit
    import capo_wafv2.types.settlement_sort_by
    import capo_wafv2.types.sort_order
    import capo_wafv2.types.tag_key_list
    import capo_wafv2.types.tag_list
    import capo_wafv2.types.tag_resource_request
    import capo_wafv2.types.tag_resource_response
    import capo_wafv2.types.time_series_statistic_type
    import capo_wafv2.types.time_window
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.token_domains
    import capo_wafv2.types.untag_resource_request
    import capo_wafv2.types.untag_resource_response
    import capo_wafv2.types.update_ip_set_request
    import capo_wafv2.types.update_ip_set_response
    import capo_wafv2.types.update_managed_rule_set_version_expiry_date_request
    import capo_wafv2.types.update_managed_rule_set_version_expiry_date_response
    import capo_wafv2.types.update_regex_pattern_set_request
    import capo_wafv2.types.update_regex_pattern_set_response
    import capo_wafv2.types.update_rule_group_request
    import capo_wafv2.types.update_rule_group_response
    import capo_wafv2.types.update_web_acl_request
    import capo_wafv2.types.update_web_acl_response
    import capo_wafv2.types.uri_path_prefix_string
    import capo_wafv2.types.vendor_name
    import capo_wafv2.types.version_key_string
    import capo_wafv2.types.versions_to_publish
    import capo_wafv2.types.visibility_config


class WAFV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class WAFV2Client:
    """A client for the ``WAFV2`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = WAFV2ClientConfig(
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
        self, config_overrides: Optional[WAFV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WAFV2ClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def associate_web_acl(
        self,
        web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.associate_web_acl_response.AssociateWebACLResponse":
        """<p>Associates a web ACL with a resource, to protect the resource. </p> <p>Use this for all resource types except for Amazon CloudFront distributions. For Amazon CloudFront, call <code>UpdateDistribution</code> for the distribution and provide the Amazon Resource Name (ARN) of the web ACL in the web ACL ID. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html">UpdateDistribution</a> in the <i>Amazon CloudFront Developer Guide</i>. </p> <p> <b>Required permissions for customer-managed IAM policies</b> </p> <p>This call requires permissions that are specific to the protected resource type. For details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL">Permissions for AssociateWebACL</a> in the <i>WAF Developer Guide</i>. </p> <p> <b>Temporary inconsistencies during updates</b> </p> <p>When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. </p> <p>The following are examples of the temporary inconsistencies that you might notice during change propagation: </p> <ul> <li> <p>After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. </p> </li> <li> <p>After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.</p> </li> <li> <p>After you change a rule action setting, you might see the old action in some places and the new action in others. </p> </li> <li> <p>After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.</p> </li> </ul>

        Args:
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to associate with the web ACL. </p> <p>The ARN must be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:<i>partition</i>:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway REST API: <code>arn:<i>partition</i>:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> <li> <p>For an AppSync GraphQL API: <code>arn:<i>partition</i>:appsync:<i>region</i>:<i>account-id</i>:apis/<i>GraphQLApiId</i> </code> </p> </li> <li> <p>For an Amazon Cognito user pool: <code>arn:<i>partition</i>:cognito-idp:<i>region</i>:<i>account-id</i>:userpool/<i>user-pool-id</i> </code> </p> </li> <li> <p>For an App Runner service: <code>arn:<i>partition</i>:apprunner:<i>region</i>:<i>account-id</i>:service/<i>apprunner-service-name</i>/<i>apprunner-service-id</i> </code> </p> </li> <li> <p>For an Amazon Web Services Verified Access instance: <code>arn:<i>partition</i>:ec2:<i>region</i>:<i>account-id</i>:verified-access-instance/<i>instance-id</i> </code> </p> </li> <li> <p>For an Amplify application: <code>arn:<i>partition</i>:amplify:<i>region</i>:<i>account-id</i>:apps/<i>app-id</i> </code> </p> </li> <li> <p>For an Amazon Bedrock AgentCore Gateway: <code>arn:<i>partition</i>:bedrock-agentcore:<i>region</i>:<i>account-id</i>:gateway/<i>gateway-id</i> </code> </p> </li> </ul>

        Raises:
            capo_wafv2.errors.waf_feature_not_included_in_pricing_plan_exception.WAFFeatureNotIncludedInPricingPlanException: <p>The operation failed because the specified WAF feature isn't supported by the CloudFront pricing plan associated with the web ACL.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.associate_web_acl_request.AssociateWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.associate_web_acl_response.AssociateWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.associate_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.associate_web_acl.associate_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.associate_web_acl_request.AssociateWebACLRequest = {
            "web_acl_arn": web_acl_arn,
            "resource_arn": resource_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def check_capacity(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        rules: "capo_wafv2.types.rules.Rules",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.check_capacity_response.CheckCapacityResponse":
        """<p>Returns the web ACL capacity unit (WCU) requirements for a specified scope and set of rules. You can use this to check the capacity requirements for the rules you want to use in a <a>RuleGroup</a> or <a>WebACL</a>. </p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            rules: <p>An array of <a>Rule</a> that you're configuring to use in a rule group or web ACL. </p>

        Raises:
            capo_wafv2.errors.waf_expired_managed_rule_group_version_exception.WAFExpiredManagedRuleGroupVersionException: <p>The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling <a>ListAvailableManagedRuleGroupVersions</a>.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet. </p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.check_capacity_request.CheckCapacityRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.check_capacity_response.CheckCapacityResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.check_capacity

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.check_capacity.check_capacity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.check_capacity_request.CheckCapacityRequest = {
            "scope": scope,
            "rules": rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_api_key(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        token_domains: "capo_wafv2.types.api_key_token_domains.APIKeyTokenDomains",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.create_api_key_response.CreateAPIKeyResponse":
        """<p>Creates an API key that contains a set of token domains.</p> <p>API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p> <p>You can use a single key for up to 5 domains. After you generate a key, you can copy it for use in your JavaScript integration. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            token_domains: <p>The client application domains that you want to use this API key for. </p> <p>Example JSON: <code>"TokenDomains": ["abc.com", "store.abc.com"]</code> </p> <p>Public suffixes aren't allowed. For example, you can't use <code>gov.au</code> or <code>co.uk</code> as token domains.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.create_api_key_request.CreateAPIKeyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.create_api_key_response.CreateAPIKeyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.create_api_key

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.create_api_key.create_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.create_api_key_request.CreateAPIKeyRequest = {
            "scope": scope,
            "token_domains": token_domains,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_ip_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        ip_address_version: "capo_wafv2.types.ip_address_version.IPAddressVersion",
        addresses: "capo_wafv2.types.ip_addresses.IPAddresses",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        tags: Optional["capo_wafv2.types.tag_list.TagList"] = None,
    ) -> "capo_wafv2.types.create_ip_set_response.CreateIPSetResponse":
        """<p>Creates an <a>IPSet</a>, which you use to identify web requests that originate from specific IP addresses or ranges of IP addresses. For example, if you're receiving a lot of requests from a ranges of IP addresses, you can configure WAF to block them using an IPSet that lists those IP addresses. </p>

        Args:
            name: <p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            description: <p>A description of the IP set that helps with identification. </p>
            ip_address_version: <p>The version of the IP addresses, either <code>IPV4</code> or <code>IPV6</code>. </p>
            addresses: <p>Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4 and IPv6 CIDR ranges except for <code>/0</code>. </p> <p>Example address strings: </p> <ul> <li> <p>For requests that originated from the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>Example JSON <code>Addresses</code> specifications: </p> <ul> <li> <p>Empty array: <code>"Addresses": []</code> </p> </li> <li> <p>Array with one address: <code>"Addresses": ["192.0.2.44/32"]</code> </p> </li> <li> <p>Array with three addresses: <code>"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]</code> </p> </li> <li> <p>INVALID specification: <code>"Addresses": [""]</code> INVALID </p> </li> </ul>
            tags: <p>An array of key:value pairs to associate with the resource.</p>

        Raises:
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.create_ip_set_request.CreateIPSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.create_ip_set_response.CreateIPSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.create_ip_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.create_ip_set.create_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.create_ip_set_request.CreateIPSetRequest = {
            "name": name,
            "scope": scope,
            "ip_address_version": ip_address_version,
            "addresses": addresses,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_regex_pattern_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        regular_expression_list: "capo_wafv2.types.regular_expression_list.RegularExpressionList",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        tags: Optional["capo_wafv2.types.tag_list.TagList"] = None,
    ) -> "capo_wafv2.types.create_regex_pattern_set_response.CreateRegexPatternSetResponse":
        """<p>Creates a <a>RegexPatternSet</a>, which you reference in a <a>RegexPatternSetReferenceStatement</a>, to have WAF inspect a web request component for the specified patterns.</p>

        Args:
            name: <p>The name of the set. You cannot change the name after you create the set.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            description: <p>A description of the set that helps with identification. </p>
            regular_expression_list: <p>Array of regular expression strings. </p>
            tags: <p>An array of key:value pairs to associate with the resource.</p>

        Raises:
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.create_regex_pattern_set_request.CreateRegexPatternSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.create_regex_pattern_set_response.CreateRegexPatternSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.create_regex_pattern_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.create_regex_pattern_set.create_regex_pattern_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.create_regex_pattern_set_request.CreateRegexPatternSetRequest = {
            "name": name,
            "scope": scope,
            "regular_expression_list": regular_expression_list,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rule_group(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        capacity: "capo_wafv2.types.capacity_unit.CapacityUnit",
        visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        rules: Optional["capo_wafv2.types.rules.Rules"] = None,
        tags: Optional["capo_wafv2.types.tag_list.TagList"] = None,
        custom_response_bodies: Optional[
            "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
        ] = None,
        monetization_config: Optional[
            "capo_wafv2.types.monetization_config.MonetizationConfig"
        ] = None,
    ) -> "capo_wafv2.types.create_rule_group_response.CreateRuleGroupResponse":
        """<p>Creates a <a>RuleGroup</a> per the specifications provided. </p> <p> A rule group defines a collection of rules to inspect and control web requests that you can use in a <a>WebACL</a>. When you create a rule group, you define an immutable capacity limit. If you update a rule group, you must stay within the capacity. This allows others to reuse the rule group with confidence in its capacity requirements. </p>

        Args:
            name: <p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            capacity: <p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, WAF enforces this limit. You can check the capacity for a set of rules using <a>CheckCapacity</a>.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>
            description: <p>A description of the rule group that helps with identification. </p>
            rules: <p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>
            visibility_config: <p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>
            tags: <p>An array of key:value pairs to associate with the resource.</p>
            custom_response_bodies: <p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>
            monetization_config: <p>The monetization configuration for the rule group. Provide this when any rule in the rule group uses the <code>Monetize</code> action.</p>

        Raises:
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.create_rule_group_request.CreateRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.create_rule_group_response.CreateRuleGroupResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.create_rule_group

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.create_rule_group.create_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.create_rule_group_request.CreateRuleGroupRequest = {
            "name": name,
            "scope": scope,
            "capacity": capacity,
            "visibility_config": visibility_config,
        }
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if tags is not None:
            input_["tags"] = tags
        if custom_response_bodies is not None:
            input_["custom_response_bodies"] = custom_response_bodies
        if monetization_config is not None:
            input_["monetization_config"] = monetization_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_web_acl(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        default_action: "capo_wafv2.types.default_action.DefaultAction",
        visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        rules: Optional["capo_wafv2.types.rules.Rules"] = None,
        data_protection_config: Optional[
            "capo_wafv2.types.data_protection_config.DataProtectionConfig"
        ] = None,
        tags: Optional["capo_wafv2.types.tag_list.TagList"] = None,
        custom_response_bodies: Optional[
            "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
        ] = None,
        captcha_config: Optional[
            "capo_wafv2.types.captcha_config.CaptchaConfig"
        ] = None,
        challenge_config: Optional[
            "capo_wafv2.types.challenge_config.ChallengeConfig"
        ] = None,
        token_domains: Optional["capo_wafv2.types.token_domains.TokenDomains"] = None,
        association_config: Optional[
            "capo_wafv2.types.association_config.AssociationConfig"
        ] = None,
        on_source_d_do_s_protection_config: Optional[
            "capo_wafv2.types.on_source_d_do_s_protection_config.OnSourceDDoSProtectionConfig"
        ] = None,
        application_config: Optional[
            "capo_wafv2.types.application_config.ApplicationConfig"
        ] = None,
        monetization_config: Optional[
            "capo_wafv2.types.monetization_config.MonetizationConfig"
        ] = None,
    ) -> "capo_wafv2.types.create_web_acl_response.CreateWebACLResponse":
        """<p>Creates a <a>WebACL</a> per the specifications provided.</p> <p> A web ACL defines a collection of rules to use to inspect and control web requests. Each rule has a statement that defines what to look for in web requests and an action that WAF applies to requests that match the statement. In the web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a web ACL can be a combination of the types <a>Rule</a>, <a>RuleGroup</a>, and managed rule group. You can associate a web ACL with one or more Amazon Web Services resources to protect. The resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner service, Amplify application, Amazon Web Services Verified Access instance, and Amazon Bedrock AgentCore Gateway. </p>

        Args:
            name: <p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            default_action: <p>The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. </p>
            description: <p>A description of the web ACL that helps with identification. </p>
            rules: <p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>
            visibility_config: <p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>
            data_protection_config: <p>Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option. </p> <p>The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging. </p>
            tags: <p>An array of key:value pairs to associate with the resource.</p>
            custom_response_bodies: <p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>
            captcha_config: <p>Specifies how WAF should handle <code>CAPTCHA</code> evaluations for rules that don't have their own <code>CaptchaConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>CaptchaConfig</code>. </p>
            challenge_config: <p>Specifies how WAF should handle challenge evaluations for rules that don't have their own <code>ChallengeConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>ChallengeConfig</code>. </p>
            token_domains: <p>Specifies the domains that WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When WAF provides a token, it uses the domain of the Amazon Web Services resource that the web ACL is protecting. If you don't specify a list of token domains, WAF accepts tokens only for the domain of the protected resource. With a token domain list, WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.</p> <p>Example JSON: <code>"TokenDomains": { "mywebsite.com", "myotherwebsite.com" }</code> </p> <p>Public suffixes aren't allowed. For example, you can't use <code>gov.au</code> or <code>co.uk</code> as token domains.</p>
            association_config: <p>Specifies custom configurations for the associations between the web ACL and protected resources. </p> <p>Use this to customize the maximum size of the request body that your protected resources forward to WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes). </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>
            on_source_d_do_s_protection_config: <p>Specifies the type of DDoS protection to apply to web request data for a web ACL. For most scenarios, it is recommended to use the default protection level, <code>ACTIVE_UNDER_DDOS</code>. If a web ACL is associated with multiple Application Load Balancers, the changes you make to DDoS protection in that web ACL will apply to all associated Application Load Balancers.</p>
            application_config: <p>Configures the ability for the WAF console to store and retrieve application attributes during the web ACL creation process. Application attributes help WAF give recommendations for protection packs.</p>
            monetization_config: <p>The monetization configuration for the web ACL. Provide this when any rule in the web ACL uses the <code>Monetize</code> action.</p>

        Raises:
            capo_wafv2.errors.waf_configuration_warning_exception.WAFConfigurationWarningException: <p>The operation failed because you are inspecting the web request body, headers, or cookies without specifying how to handle oversize components. Rules that inspect the body must either provide an <code>OversizeHandling</code> configuration or they must be preceded by a <code>SizeConstraintStatement</code> that blocks the body content from being too large. Rules that inspect the headers or cookies must provide an <code>OversizeHandling</code> configuration. </p> <p>Provide the handling configuration and retry your operation.</p> <p>Alternately, you can suppress this warning by adding the following tag to the resource that you provide to this operation: <code>Tag</code> (key:<code>WAF:OversizeFieldsHandlingConstraintOptOut</code>, value:<code>true</code>).</p>
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_expired_managed_rule_group_version_exception.WAFExpiredManagedRuleGroupVersionException: <p>The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling <a>ListAvailableManagedRuleGroupVersions</a>.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.create_web_acl_request.CreateWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.create_web_acl_response.CreateWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.create_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.create_web_acl.create_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.create_web_acl_request.CreateWebACLRequest = {
            "name": name,
            "scope": scope,
            "default_action": default_action,
            "visibility_config": visibility_config,
        }
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if data_protection_config is not None:
            input_["data_protection_config"] = data_protection_config
        if tags is not None:
            input_["tags"] = tags
        if custom_response_bodies is not None:
            input_["custom_response_bodies"] = custom_response_bodies
        if captcha_config is not None:
            input_["captcha_config"] = captcha_config
        if challenge_config is not None:
            input_["challenge_config"] = challenge_config
        if token_domains is not None:
            input_["token_domains"] = token_domains
        if association_config is not None:
            input_["association_config"] = association_config
        if on_source_d_do_s_protection_config is not None:
            input_["on_source_d_do_s_protection_config"] = (
                on_source_d_do_s_protection_config
            )
        if application_config is not None:
            input_["application_config"] = application_config
        if monetization_config is not None:
            input_["monetization_config"] = monetization_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api_key(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        api_key: "capo_wafv2.types.api_key.APIKey",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_api_key_response.DeleteAPIKeyResponse":
        """<p>Deletes the specified API key. </p> <p>After you delete a key, it can take up to 24 hours for WAF to disallow use of the key in all regions. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            api_key: <p>The encrypted API key that you want to delete. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_api_key_request.DeleteAPIKeyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_api_key_response.DeleteAPIKeyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_api_key

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_api_key.delete_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_api_key_request.DeleteAPIKeyRequest = {
            "scope": scope,
            "api_key": api_key,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_firewall_manager_rule_groups(
        self,
        web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        web_acl_lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_firewall_manager_rule_groups_response.DeleteFirewallManagerRuleGroupsResponse":
        """<p>Deletes all rule groups that are managed by Firewall Manager from the specified <a>WebACL</a>. </p> <p>You can only use this if <code>ManagedByFirewallManager</code> and <code>RetrofittedByFirewallManager</code> are both false in the web ACL. </p>

        Args:
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the web ACL.</p>
            web_acl_lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_firewall_manager_rule_groups_request.DeleteFirewallManagerRuleGroupsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_firewall_manager_rule_groups_response.DeleteFirewallManagerRuleGroupsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_firewall_manager_rule_groups

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_firewall_manager_rule_groups.delete_firewall_manager_rule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_firewall_manager_rule_groups_request.DeleteFirewallManagerRuleGroupsRequest = {
            "web_acl_arn": web_acl_arn,
            "web_acl_lock_token": web_acl_lock_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_ip_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_ip_set_response.DeleteIPSetResponse":
        """<p>Deletes the specified <a>IPSet</a>. </p>

        Args:
            name: <p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_associated_item_exception.WAFAssociatedItemException: <p>WAF couldn’t perform the operation because your resource is being used by another resource or it’s associated with another resource. </p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_ip_set_request.DeleteIPSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_ip_set_response.DeleteIPSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_ip_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_ip_set.delete_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_ip_set_request.DeleteIPSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_logging_configuration(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        log_type: Optional["capo_wafv2.types.log_type.LogType"] = None,
        log_scope: Optional["capo_wafv2.types.log_scope.LogScope"] = None,
    ) -> "capo_wafv2.types.delete_logging_configuration_response.DeleteLoggingConfigurationResponse":
        """<p>Deletes the <a>LoggingConfiguration</a> from the specified web ACL.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web ACL from which you want to delete the <a>LoggingConfiguration</a>.</p>
            log_type: <p>Used to distinguish between various logging options. Currently, there is one option.</p> <p>Default: <code>WAF_LOGS</code> </p>
            log_scope: <p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_logging_configuration_response.DeleteLoggingConfigurationResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_logging_configuration

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_logging_configuration.delete_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest = {
            "resource_arn": resource_arn
        }
        if log_type is not None:
            input_["log_type"] = log_type
        if log_scope is not None:
            input_["log_scope"] = log_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_permission_policy(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_permission_policy_response.DeletePermissionPolicyResponse":
        """<p>Permanently deletes an IAM policy from the specified rule group.</p> <p>You must be the owner of the rule group to perform this operation.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rule group from which you want to delete the policy.</p> <p>You must be the owner of the rule group to perform this operation.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_permission_policy_request.DeletePermissionPolicyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_permission_policy_response.DeletePermissionPolicyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_permission_policy

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_permission_policy.delete_permission_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_permission_policy_request.DeletePermissionPolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_regex_pattern_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_regex_pattern_set_response.DeleteRegexPatternSetResponse":
        """<p>Deletes the specified <a>RegexPatternSet</a>.</p>

        Args:
            name: <p>The name of the set. You cannot change the name after you create the set.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_associated_item_exception.WAFAssociatedItemException: <p>WAF couldn’t perform the operation because your resource is being used by another resource or it’s associated with another resource. </p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_regex_pattern_set_request.DeleteRegexPatternSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_regex_pattern_set_response.DeleteRegexPatternSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_regex_pattern_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_regex_pattern_set.delete_regex_pattern_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_regex_pattern_set_request.DeleteRegexPatternSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rule_group(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_rule_group_response.DeleteRuleGroupResponse":
        """<p>Deletes the specified <a>RuleGroup</a>.</p>

        Args:
            name: <p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_associated_item_exception.WAFAssociatedItemException: <p>WAF couldn’t perform the operation because your resource is being used by another resource or it’s associated with another resource. </p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_rule_group_request.DeleteRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_rule_group_response.DeleteRuleGroupResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_rule_group

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_rule_group.delete_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_rule_group_request.DeleteRuleGroupRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_web_acl(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.delete_web_acl_response.DeleteWebACLResponse":
        """<p>Deletes the specified <a>WebACL</a>. </p> <p>You can only use this if <code>ManagedByFirewallManager</code> is false in the web ACL. </p> <note> <p>Before deleting any web ACL, first disassociate it from all resources.</p> <ul> <li> <p>To retrieve a list of the resources that are associated with a web ACL, use the following calls:</p> <ul> <li> <p>For Amazon CloudFront distributions, use the CloudFront call <code>ListDistributionsByWebACLId</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html">ListDistributionsByWebACLId</a> in the <i>Amazon CloudFront API Reference</i>. </p> </li> <li> <p>For all other resources, call <a>ListResourcesForWebACL</a>.</p> </li> </ul> </li> <li> <p>To disassociate a resource from a web ACL, use the following calls:</p> <ul> <li> <p>For Amazon CloudFront distributions, provide an empty web ACL ID in the CloudFront call <code>UpdateDistribution</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html">UpdateDistribution</a> in the <i>Amazon CloudFront API Reference</i>. </p> </li> <li> <p>For all other resources, call <a>DisassociateWebACL</a>.</p> </li> </ul> </li> </ul> </note>

        Args:
            name: <p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_associated_item_exception.WAFAssociatedItemException: <p>WAF couldn’t perform the operation because your resource is being used by another resource or it’s associated with another resource. </p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.delete_web_acl_request.DeleteWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.delete_web_acl_response.DeleteWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.delete_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.delete_web_acl.delete_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.delete_web_acl_request.DeleteWebACLRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_all_managed_products(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.describe_all_managed_products_response.DescribeAllManagedProductsResponse":
        """<p>Provides high-level information for the Amazon Web Services Managed Rules rule groups and Amazon Web Services Marketplace managed rule groups. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.describe_all_managed_products_request.DescribeAllManagedProductsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.describe_all_managed_products_response.DescribeAllManagedProductsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.describe_all_managed_products

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.describe_all_managed_products.describe_all_managed_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.describe_all_managed_products_request.DescribeAllManagedProductsRequest = {
            "scope": scope
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_managed_products_by_vendor(
        self,
        vendor_name: "capo_wafv2.types.vendor_name.VendorName",
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.describe_managed_products_by_vendor_response.DescribeManagedProductsByVendorResponse":
        """<p>Provides high-level information for the managed rule groups owned by a specific vendor. </p>

        Args:
            vendor_name: <p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.describe_managed_products_by_vendor_request.DescribeManagedProductsByVendorRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.describe_managed_products_by_vendor_response.DescribeManagedProductsByVendorResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.describe_managed_products_by_vendor

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.describe_managed_products_by_vendor.describe_managed_products_by_vendor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.describe_managed_products_by_vendor_request.DescribeManagedProductsByVendorRequest = {
            "vendor_name": vendor_name,
            "scope": scope,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_managed_rule_group(
        self,
        vendor_name: "capo_wafv2.types.vendor_name.VendorName",
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        version_name: Optional[
            "capo_wafv2.types.version_key_string.VersionKeyString"
        ] = None,
    ) -> "capo_wafv2.types.describe_managed_rule_group_response.DescribeManagedRuleGroupResponse":
        """<p>Provides high-level information for a managed rule group, including descriptions of the rules. </p>

        Args:
            vendor_name: <p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>
            name: <p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            version_name: <p>The version of the rule group. You can only use a version that is not scheduled for expiration. If you don't provide this, WAF uses the vendor's default version. </p>

        Raises:
            capo_wafv2.errors.waf_expired_managed_rule_group_version_exception.WAFExpiredManagedRuleGroupVersionException: <p>The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling <a>ListAvailableManagedRuleGroupVersions</a>.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.describe_managed_rule_group_request.DescribeManagedRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.describe_managed_rule_group_response.DescribeManagedRuleGroupResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.describe_managed_rule_group

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.describe_managed_rule_group.describe_managed_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.describe_managed_rule_group_request.DescribeManagedRuleGroupRequest = {
            "vendor_name": vendor_name,
            "name": name,
            "scope": scope,
        }
        if version_name is not None:
            input_["version_name"] = version_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_web_acl(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.disassociate_web_acl_response.DisassociateWebACLResponse":
        """<p>Disassociates the specified resource from its web ACL association, if it has one. </p> <p>Use this for all resource types except for Amazon CloudFront distributions. For Amazon CloudFront, call <code>UpdateDistribution</code> for the distribution and provide an empty web ACL ID. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html">UpdateDistribution</a> in the <i>Amazon CloudFront API Reference</i>. </p> <p> <b>Required permissions for customer-managed IAM policies</b> </p> <p>This call requires permissions that are specific to the protected resource type. For details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-DisassociateWebACL">Permissions for DisassociateWebACL</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to disassociate from the web ACL. </p> <p>The ARN must be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:<i>partition</i>:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway REST API: <code>arn:<i>partition</i>:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> <li> <p>For an AppSync GraphQL API: <code>arn:<i>partition</i>:appsync:<i>region</i>:<i>account-id</i>:apis/<i>GraphQLApiId</i> </code> </p> </li> <li> <p>For an Amazon Cognito user pool: <code>arn:<i>partition</i>:cognito-idp:<i>region</i>:<i>account-id</i>:userpool/<i>user-pool-id</i> </code> </p> </li> <li> <p>For an App Runner service: <code>arn:<i>partition</i>:apprunner:<i>region</i>:<i>account-id</i>:service/<i>apprunner-service-name</i>/<i>apprunner-service-id</i> </code> </p> </li> <li> <p>For an Amazon Web Services Verified Access instance: <code>arn:<i>partition</i>:ec2:<i>region</i>:<i>account-id</i>:verified-access-instance/<i>instance-id</i> </code> </p> </li> <li> <p>For an Amplify application: <code>arn:<i>partition</i>:amplify:<i>region</i>:<i>account-id</i>:apps/<i>app-id</i> </code> </p> </li> <li> <p>For an Amazon Bedrock AgentCore Gateway: <code>arn:<i>partition</i>:bedrock-agentcore:<i>region</i>:<i>account-id</i>:gateway/<i>gateway-id</i> </code> </p> </li> </ul>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.disassociate_web_acl_request.DisassociateWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.disassociate_web_acl_response.DisassociateWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.disassociate_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.disassociate_web_acl.disassociate_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.disassociate_web_acl_request.DisassociateWebACLRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_mobile_sdk_release_url(
        self,
        platform: "capo_wafv2.types.platform.Platform",
        release_version: "capo_wafv2.types.version_key_string.VersionKeyString",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.generate_mobile_sdk_release_url_response.GenerateMobileSdkReleaseUrlResponse":
        """<p>Generates a presigned download URL for the specified release of the mobile SDK.</p> <p>The mobile SDK is not generally available. Customers who have access to the mobile SDK can use it to establish and manage WAF tokens for use in HTTP(S) requests from a mobile device to WAF. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            platform: <p>The device platform.</p>
            release_version: <p>The release version. For the latest available version, specify <code>LATEST</code>.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.generate_mobile_sdk_release_url_request.GenerateMobileSdkReleaseUrlRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.generate_mobile_sdk_release_url_response.GenerateMobileSdkReleaseUrlResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.generate_mobile_sdk_release_url

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.generate_mobile_sdk_release_url.generate_mobile_sdk_release_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.generate_mobile_sdk_release_url_request.GenerateMobileSdkReleaseUrlRequest = {
            "platform": platform,
            "release_version": release_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_decrypted_api_key(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        api_key: "capo_wafv2.types.api_key.APIKey",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_decrypted_api_key_response.GetDecryptedAPIKeyResponse":
        """<p>Returns your API key in decrypted form. Use this to check the token domains that you have defined for the key. </p> <p>API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            api_key: <p>The encrypted API key. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_decrypted_api_key_request.GetDecryptedAPIKeyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_decrypted_api_key_response.GetDecryptedAPIKeyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_decrypted_api_key

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_decrypted_api_key.get_decrypted_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_decrypted_api_key_request.GetDecryptedAPIKeyRequest = {
            "scope": scope,
            "api_key": api_key,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ip_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_ip_set_response.GetIPSetResponse":
        """<p>Retrieves the specified <a>IPSet</a>.</p>

        Args:
            name: <p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_ip_set_request.GetIPSetRequest]",
        ) -> OperationResponse["capo_wafv2.types.get_ip_set_response.GetIPSetResponse"]:
            import capo_wafv2._operations.awswaf_20190729.get_ip_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_ip_set.get_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_ip_set_request.GetIPSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_logging_configuration(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        log_type: Optional["capo_wafv2.types.log_type.LogType"] = None,
        log_scope: Optional["capo_wafv2.types.log_scope.LogScope"] = None,
    ) -> "capo_wafv2.types.get_logging_configuration_response.GetLoggingConfigurationResponse":
        """<p>Returns the <a>LoggingConfiguration</a> for the specified web ACL.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web ACL for which you want to get the <a>LoggingConfiguration</a>.</p>
            log_type: <p>Used to distinguish between various logging options. Currently, there is one option.</p> <p>Default: <code>WAF_LOGS</code> </p>
            log_scope: <p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_logging_configuration_request.GetLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_logging_configuration_response.GetLoggingConfigurationResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_logging_configuration

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_logging_configuration.get_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_logging_configuration_request.GetLoggingConfigurationRequest = {
            "resource_arn": resource_arn
        }
        if log_type is not None:
            input_["log_type"] = log_type
        if log_scope is not None:
            input_["log_scope"] = log_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_rule_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_managed_rule_set_response.GetManagedRuleSetResponse":
        """<p>Retrieves the specified managed rule set. </p> <note> <p>This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers. </p> <p>Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are <code>ListManagedRuleSets</code>, <code>GetManagedRuleSet</code>, <code>PutManagedRuleSetVersions</code>, and <code>UpdateManagedRuleSetVersionExpiryDate</code>.</p> </note>

        Args:
            name: <p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_managed_rule_set_request.GetManagedRuleSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_managed_rule_set_response.GetManagedRuleSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_managed_rule_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_managed_rule_set.get_managed_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_managed_rule_set_request.GetManagedRuleSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_mobile_sdk_release(
        self,
        platform: "capo_wafv2.types.platform.Platform",
        release_version: "capo_wafv2.types.version_key_string.VersionKeyString",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_mobile_sdk_release_response.GetMobileSdkReleaseResponse":
        """<p>Retrieves information for the specified mobile SDK release, including release notes and tags.</p> <p>The mobile SDK is not generally available. Customers who have access to the mobile SDK can use it to establish and manage WAF tokens for use in HTTP(S) requests from a mobile device to WAF. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            platform: <p>The device platform.</p>
            release_version: <p>The release version. For the latest available version, specify <code>LATEST</code>.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_mobile_sdk_release_request.GetMobileSdkReleaseRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_mobile_sdk_release_response.GetMobileSdkReleaseResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_mobile_sdk_release

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_mobile_sdk_release.get_mobile_sdk_release(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_mobile_sdk_release_request.GetMobileSdkReleaseRequest = {
            "platform": platform,
            "release_version": release_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_permission_policy(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_permission_policy_response.GetPermissionPolicyResponse":
        """<p>Returns the IAM policy that is attached to the specified rule group.</p> <p>You must be the owner of the rule group to perform this operation.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rule group for which you want to get the policy.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_permission_policy_request.GetPermissionPolicyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_permission_policy_response.GetPermissionPolicyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_permission_policy

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_permission_policy.get_permission_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_permission_policy_request.GetPermissionPolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rate_based_statement_managed_keys(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        web_acl_name: "capo_wafv2.types.entity_name.EntityName",
        web_acl_id: "capo_wafv2.types.entity_id.EntityId",
        rule_name: "capo_wafv2.types.entity_name.EntityName",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        rule_group_rule_name: Optional[
            "capo_wafv2.types.entity_name.EntityName"
        ] = None,
    ) -> "capo_wafv2.types.get_rate_based_statement_managed_keys_response.GetRateBasedStatementManagedKeysResponse":
        """<p>Retrieves the IP addresses that are currently blocked by a rate-based rule instance. This is only available for rate-based rules that aggregate solely on the IP address or on the forwarded IP address. </p> <p>The maximum number of addresses that can be blocked for a single rate-based rule instance is 10,000. If more than 10,000 addresses exceed the rate limit, those with the highest rates are blocked.</p> <p>For a rate-based rule that you've defined inside a rule group, provide the name of the rule group reference statement in your request, in addition to the rate-based rule name and the web ACL name. </p> <p>WAF monitors web requests and manages keys independently for each unique combination of web ACL, optional rule group, and rate-based rule. For example, if you define a rate-based rule inside a rule group, and then use the rule group in a web ACL, WAF monitors web requests and manages keys for that web ACL, rule group reference statement, and rate-based rule instance. If you use the same rule group in a second web ACL, WAF monitors web requests and manages keys for this second usage completely independent of your first. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            web_acl_name: <p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>
            web_acl_id: <p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            rule_group_rule_name: <p>The name of the rule group reference statement in your web ACL. This is required only when you have the rate-based rule nested inside a rule group. </p>
            rule_name: <p>The name of the rate-based rule to get the keys for. If you have the rule defined inside a rule group that you're using in your web ACL, also provide the name of the rule group reference statement in the request parameter <code>RuleGroupRuleName</code>.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_unsupported_aggregate_key_type_exception.WAFUnsupportedAggregateKeyTypeException: <p>The rule that you've named doesn't aggregate solely on the IP address or solely on the forwarded IP address. This call is only available for rate-based rules with an <code>AggregateKeyType</code> setting of <code>IP</code> or <code>FORWARDED_IP</code>.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_rate_based_statement_managed_keys_request.GetRateBasedStatementManagedKeysRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_rate_based_statement_managed_keys_response.GetRateBasedStatementManagedKeysResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_rate_based_statement_managed_keys

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_rate_based_statement_managed_keys.get_rate_based_statement_managed_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_rate_based_statement_managed_keys_request.GetRateBasedStatementManagedKeysRequest = {
            "scope": scope,
            "web_acl_name": web_acl_name,
            "web_acl_id": web_acl_id,
            "rule_name": rule_name,
        }
        if rule_group_rule_name is not None:
            input_["rule_group_rule_name"] = rule_group_rule_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_regex_pattern_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_regex_pattern_set_response.GetRegexPatternSetResponse":
        """<p>Retrieves the specified <a>RegexPatternSet</a>.</p>

        Args:
            name: <p>The name of the set. You cannot change the name after you create the set.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_regex_pattern_set_request.GetRegexPatternSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_regex_pattern_set_response.GetRegexPatternSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_regex_pattern_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_regex_pattern_set.get_regex_pattern_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_regex_pattern_set_request.GetRegexPatternSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_revenue_statistics(
        self,
        statistic_type: "capo_wafv2.types.ranking_statistic_type.RankingStatisticType",
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        scope: "capo_wafv2.types.scope.Scope",
        currency: "capo_wafv2.types.currency.Currency",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        group_by: Optional["capo_wafv2.types.group_by_type.GroupByType"] = None,
        filters: Optional[
            "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
        ] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional[
            "capo_wafv2.types.path_statistics_limit.PathStatisticsLimit"
        ] = None,
        sort_by: Optional["capo_wafv2.types.ranking_sort_by.RankingSortBy"] = None,
        sort_order: Optional["capo_wafv2.types.sort_order.SortOrder"] = None,
    ) -> (
        "capo_wafv2.types.get_revenue_statistics_response.GetRevenueStatisticsResponse"
    ):
        """<p>Retrieves ranked monetization statistics. Use the <code>StatisticType</code> parameter to specify the ranking: <code>TOP_SOURCES_BY_REVENUE</code> for top sources by revenue, or <code>TOP_PATHS_BY_REVENUE</code> for top content paths by revenue. This operation is only available for <code>CLOUDFRONT</code> scope. The maximum supported time window is 90 days. When no <code>CurrencyMode</code> filter is provided, results default to <code>REAL</code>. To retrieve test data, include a <code>CurrencyMode</code> filter with the value <code>TEST</code>.</p>

        Args:
            statistic_type: <p> <code>TOP_SOURCES_BY_REVENUE</code> ranks revenue from AI bot traffic, grouped by the dimension you specify in the <code>GroupBy</code> parameter (<code>NAME</code>, <code>CATEGORY</code>, <code>INTENT</code>, <code>ORGANIZATION</code>, or <code>WEBACL</code>); <code>GroupBy</code> is required for this statistic type. <code>TOP_PATHS_BY_REVENUE</code> ranks revenue by path.</p>
            time_window: <p>The time range for the query. Specify start and end timestamps.</p>
            scope: <p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>
            currency: <p>The currency for the revenue amounts in the response.</p>
            group_by: <p>The dimension to group results by: <code>NAME</code>, <code>CATEGORY</code>, <code>INTENT</code>, <code>ORGANIZATION</code>, or <code>WEBACL</code>. Required when <code>StatisticType</code> is <code>TOP_SOURCES_BY_REVENUE</code>. Not required for <code>TOP_PATHS_BY_REVENUE</code>, where results are grouped by content path. If <code>StatisticType</code> is <code>TOP_SOURCES_BY_REVENUE</code> and <code>GroupBy</code> is omitted, the request is rejected with a <code>WAFInvalidParameterException</code>.</p>
            filters: <p>Optional filters to narrow the results.</p>
            next_marker: <p>When you get a paginated response, this marker indicates that additional results are available. Use it in a subsequent request to retrieve the next page of results.</p>
            limit: <p>The maximum number of results to return.</p>
            sort_by: <p>The field to sort results by: <code>REVENUE</code>, <code>PERCENTAGE</code>, or <code>NAME</code>.</p>
            sort_order: <p>The sort order: <code>ASC</code> for ascending or <code>DESC</code> for descending.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_revenue_statistics_request.GetRevenueStatisticsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_revenue_statistics_response.GetRevenueStatisticsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_revenue_statistics

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_revenue_statistics.get_revenue_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_revenue_statistics_request.GetRevenueStatisticsRequest = {
            "statistic_type": statistic_type,
            "time_window": time_window,
            "scope": scope,
            "currency": currency,
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if filters is not None:
            input_["filters"] = filters
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_revenue_statistics_summary(
        self,
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        scope: "capo_wafv2.types.scope.Scope",
        currency: "capo_wafv2.types.currency.Currency",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        filters: Optional[
            "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
        ] = None,
    ) -> "capo_wafv2.types.get_revenue_statistics_summary_response.GetRevenueStatisticsSummaryResponse":
        """<p>Retrieves a summary of monetization revenue for the specified time window. Returns total revenue, revenue by verification tier, total settlements, and total HTTP 402 responses served. This operation is only available for <code>CLOUDFRONT</code> scope. The maximum supported time window is 90 days. When no <code>CurrencyMode</code> filter is provided, results default to <code>REAL</code>. To retrieve test data, include a <code>CurrencyMode</code> filter with the value <code>TEST</code>.</p>

        Args:
            time_window: <p>The time range for the revenue summary query. Specify start and end timestamps.</p>
            scope: <p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>). AI bot monetization is only available for <code>CLOUDFRONT</code> scope.</p>
            currency: <p>The currency for the revenue amounts in the response. Currently only <code>USDC</code> is supported.</p>
            filters: <p>Optional filters to narrow the results. You can filter by source name, category, organization, intent, verified status, content path, web ACL ARN, or currency mode.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_revenue_statistics_summary_request.GetRevenueStatisticsSummaryRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_revenue_statistics_summary_response.GetRevenueStatisticsSummaryResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_revenue_statistics_summary

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_revenue_statistics_summary.get_revenue_statistics_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_revenue_statistics_summary_request.GetRevenueStatisticsSummaryRequest = {
            "time_window": time_window,
            "scope": scope,
            "currency": currency,
        }
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_revenue_statistics_time_series(
        self,
        statistic_type: "capo_wafv2.types.time_series_statistic_type.TimeSeriesStatisticType",
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        scope: "capo_wafv2.types.scope.Scope",
        interval: "capo_wafv2.types.interval_type.IntervalType",
        currency: "capo_wafv2.types.currency.Currency",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        group_by: Optional["capo_wafv2.types.group_by_type.GroupByType"] = None,
        filters: Optional[
            "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
        ] = None,
        limit: Optional["capo_wafv2.types.max_data_points.MaxDataPoints"] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
    ) -> "capo_wafv2.types.get_revenue_statistics_time_series_response.GetRevenueStatisticsTimeSeriesResponse":
        """<p>Retrieves time series data for monetization revenue. Returns data points aggregated at the specified interval for the given time window. This operation is only available for <code>CLOUDFRONT</code> scope. The maximum supported time window is 90 days. When no <code>CurrencyMode</code> filter is provided, results default to <code>REAL</code>. To retrieve test data, include a <code>CurrencyMode</code> filter with the value <code>TEST</code>.</p>

        Args:
            statistic_type: <p>The type of time series data to retrieve: <code>DATE_HISTOGRAM</code> for revenue over time, or <code>PAYMENT_TRAFFIC</code> for payment traffic patterns.</p>
            time_window: <p>The time range for the query. Specify start and end timestamps.</p>
            scope: <p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>
            interval: <p>The time interval for aggregating data points: <code>MINUTELY</code>, <code>FIVE_MINUTELY</code>, <code>HOURLY</code>, or <code>DAILY</code>.</p>
            currency: <p>The currency for the amounts in the response.</p>
            group_by: <p>The dimension to group results by.</p>
            filters: <p>Optional filters to narrow the results.</p>
            limit: <p>The maximum number of data points to return. Minimum: 1. Maximum: 10000.</p>
            next_marker: <p>When you get a paginated response, this marker indicates that additional results are available.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_revenue_statistics_time_series_request.GetRevenueStatisticsTimeSeriesRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_revenue_statistics_time_series_response.GetRevenueStatisticsTimeSeriesResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_revenue_statistics_time_series

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_revenue_statistics_time_series.get_revenue_statistics_time_series(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_revenue_statistics_time_series_request.GetRevenueStatisticsTimeSeriesRequest = {
            "statistic_type": statistic_type,
            "time_window": time_window,
            "scope": scope,
            "interval": interval,
            "currency": currency,
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_marker is not None:
            input_["next_marker"] = next_marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rule_group(
        self,
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        name: Optional["capo_wafv2.types.entity_name.EntityName"] = None,
        scope: Optional["capo_wafv2.types.scope.Scope"] = None,
        id: Optional["capo_wafv2.types.entity_id.EntityId"] = None,
        arn: Optional["capo_wafv2.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_wafv2.types.get_rule_group_response.GetRuleGroupResponse":
        """<p>Retrieves the specified <a>RuleGroup</a>.</p>

        Args:
            name: <p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            arn: <p>The Amazon Resource Name (ARN) of the entity.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_rule_group_request.GetRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_rule_group_response.GetRuleGroupResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_rule_group

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_rule_group.get_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_rule_group_request.GetRuleGroupRequest = {}
        if name is not None:
            input_["name"] = name
        if scope is not None:
            input_["scope"] = scope
        if id is not None:
            input_["id"] = id
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sampled_requests(
        self,
        web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        rule_metric_name: "capo_wafv2.types.metric_name.MetricName",
        scope: "capo_wafv2.types.scope.Scope",
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        max_items: "capo_wafv2.types.list_max_items.ListMaxItems",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_sampled_requests_response.GetSampledRequestsResponse":
        """<p>Gets detailed information about a specified number of requests--a sample--that WAF randomly selects from among the first 5,000 requests that your Amazon Web Services resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.</p> <p> <code>GetSampledRequests</code> returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, <code>GetSampledRequests</code> returns an updated time range. This new time range indicates the actual period during which WAF selected the requests in the sample.</p>

        Args:
            web_acl_arn: <p>The Amazon resource name (ARN) of the <code>WebACL</code> for which you want a sample of requests.</p>
            rule_metric_name: <p>The metric name assigned to the <code>Rule</code> or <code>RuleGroup</code> dimension for which you want a sample of requests.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            time_window: <p>The start date and time and the end date and time of the range for which you want <code>GetSampledRequests</code> to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours. If you specify a start time that's earlier than three hours ago, WAF sets it to three hours ago.</p>
            max_items: <p>The number of requests that you want WAF to return from among the first 5,000 requests that your Amazon Web Services resource received during the time range. If your resource received fewer requests than the value of <code>MaxItems</code>, <code>GetSampledRequests</code> returns information about all of them. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_sampled_requests_request.GetSampledRequestsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_sampled_requests_response.GetSampledRequestsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_sampled_requests

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_sampled_requests.get_sampled_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_sampled_requests_request.GetSampledRequestsRequest = {
            "web_acl_arn": web_acl_arn,
            "rule_metric_name": rule_metric_name,
            "scope": scope,
            "time_window": time_window,
            "max_items": max_items,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_top_path_statistics_by_traffic(
        self,
        web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        scope: "capo_wafv2.types.scope.Scope",
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        limit: "capo_wafv2.types.path_statistics_limit.PathStatisticsLimit",
        number_of_top_traffic_bots_per_path: "capo_wafv2.types.number_of_top_traffic_bots_per_path.NumberOfTopTrafficBotsPerPath",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        uri_path_prefix: Optional[
            "capo_wafv2.types.uri_path_prefix_string.UriPathPrefixString"
        ] = None,
        bot_category: Optional["capo_wafv2.types.filter_string.FilterString"] = None,
        bot_organization: Optional[
            "capo_wafv2.types.filter_string.FilterString"
        ] = None,
        bot_name: Optional["capo_wafv2.types.filter_string.FilterString"] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
    ) -> "capo_wafv2.types.get_top_path_statistics_by_traffic_response.GetTopPathStatisticsByTrafficResponse":
        """<p>Retrieves aggregated statistics about the top URI paths accessed by bot traffic for a specified web ACL and time window. You can use this operation to analyze which paths on your web application receive the most bot traffic and identify the specific bots accessing those paths. The operation supports filtering by bot category, organization, or name, and allows you to drill down into specific path prefixes to view detailed URI-level statistics.</p>

        Args:
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the web ACL for which you want to retrieve path statistics.</p>
            scope: <p>Specifies whether the web ACL is for an Amazon Web Services CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer, an AppSync GraphQL API, an Amazon Cognito user pool, an Amazon Web Services App Runner service, or an Amazon Web Services Verified Access instance.</p>
            uri_path_prefix: <p>A URI path prefix to filter the results. When you specify this parameter, the operation returns statistics for individual URIs within the specified path prefix. For example, if you specify <code>/api</code>, the response includes statistics for paths like <code>/api/v1/users</code> and <code>/api/v2/orders</code>. If you don't specify this parameter, the operation returns top-level path statistics.</p>
            time_window: <p>The time window for which you want to retrieve path statistics. The time window must be within the data retention period for your web ACL.</p>
            bot_category: <p>Filters the results to include only traffic from bots in the specified category. For example, you can filter by <code>ai</code> to see only AI crawler traffic, or <code>search_engine</code> to see only search engine bot traffic. When you apply this filter, the <code>Source</code> field is populated in the response.</p>
            bot_organization: <p>Filters the results to include only traffic from bots belonging to the specified organization. For example, you can filter by <code>openai</code> or <code>google</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>
            bot_name: <p>Filters the results to include only traffic from the specified bot. For example, you can filter by <code>gptbot</code> or <code>googlebot</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>
            limit: <p>The maximum number of path statistics to return. Valid values are 1 to 100.</p>
            number_of_top_traffic_bots_per_path: <p>The maximum number of top bots to include in the statistics for each path. Valid values are 1 to 10.</p>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>

        Raises:
            capo_wafv2.errors.waf_feature_not_included_in_pricing_plan_exception.WAFFeatureNotIncludedInPricingPlanException: <p>The operation failed because the specified WAF feature isn't supported by the CloudFront pricing plan associated with the web ACL.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_top_path_statistics_by_traffic_request.GetTopPathStatisticsByTrafficRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_top_path_statistics_by_traffic_response.GetTopPathStatisticsByTrafficResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_top_path_statistics_by_traffic

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_top_path_statistics_by_traffic.get_top_path_statistics_by_traffic(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_top_path_statistics_by_traffic_request.GetTopPathStatisticsByTrafficRequest = {
            "web_acl_arn": web_acl_arn,
            "scope": scope,
            "time_window": time_window,
            "limit": limit,
            "number_of_top_traffic_bots_per_path": number_of_top_traffic_bots_per_path,
        }
        if uri_path_prefix is not None:
            input_["uri_path_prefix"] = uri_path_prefix
        if bot_category is not None:
            input_["bot_category"] = bot_category
        if bot_organization is not None:
            input_["bot_organization"] = bot_organization
        if bot_name is not None:
            input_["bot_name"] = bot_name
        if next_marker is not None:
            input_["next_marker"] = next_marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_web_acl(
        self,
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        name: Optional["capo_wafv2.types.entity_name.EntityName"] = None,
        scope: Optional["capo_wafv2.types.scope.Scope"] = None,
        id: Optional["capo_wafv2.types.entity_id.EntityId"] = None,
        arn: Optional["capo_wafv2.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_wafv2.types.get_web_acl_response.GetWebACLResponse":
        """<p>Retrieves the specified <a>WebACL</a>.</p>

        Args:
            name: <p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            arn: <p>The Amazon Resource Name (ARN) of the web ACL that you want to retrieve. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_web_acl_request.GetWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_web_acl_response.GetWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_web_acl.get_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_web_acl_request.GetWebACLRequest = {}
        if name is not None:
            input_["name"] = name
        if scope is not None:
            input_["scope"] = scope
        if id is not None:
            input_["id"] = id
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_web_acl_for_resource(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.get_web_acl_for_resource_response.GetWebACLForResourceResponse":
        """<p>Retrieves the <a>WebACL</a> for the specified resource. </p> <p>This call uses <code>GetWebACL</code>, to verify that your account has permission to access the retrieved web ACL. If you get an error that indicates that your account isn't authorized to perform <code>wafv2:GetWebACL</code> on the resource, that error won't be included in your CloudTrail event history. </p> <p>For Amazon CloudFront, don't use this call. Instead, call the CloudFront action <code>GetDistributionConfig</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistributionConfig.html">GetDistributionConfig</a> in the <i>Amazon CloudFront API Reference</i>. </p> <p> <b>Required permissions for customer-managed IAM policies</b> </p> <p>This call requires permissions that are specific to the protected resource type. For details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-GetWebACLForResource">Permissions for GetWebACLForResource</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose web ACL you want to retrieve. </p> <p>The ARN must be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:<i>partition</i>:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway REST API: <code>arn:<i>partition</i>:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> <li> <p>For an AppSync GraphQL API: <code>arn:<i>partition</i>:appsync:<i>region</i>:<i>account-id</i>:apis/<i>GraphQLApiId</i> </code> </p> </li> <li> <p>For an Amazon Cognito user pool: <code>arn:<i>partition</i>:cognito-idp:<i>region</i>:<i>account-id</i>:userpool/<i>user-pool-id</i> </code> </p> </li> <li> <p>For an App Runner service: <code>arn:<i>partition</i>:apprunner:<i>region</i>:<i>account-id</i>:service/<i>apprunner-service-name</i>/<i>apprunner-service-id</i> </code> </p> </li> <li> <p>For an Amazon Web Services Verified Access instance: <code>arn:<i>partition</i>:ec2:<i>region</i>:<i>account-id</i>:verified-access-instance/<i>instance-id</i> </code> </p> </li> <li> <p>For an Amplify application: <code>arn:<i>partition</i>:amplify:<i>region</i>:<i>account-id</i>:apps/<i>app-id</i> </code> </p> </li> <li> <p>For an Amazon Bedrock AgentCore Gateway: <code>arn:<i>partition</i>:bedrock-agentcore:<i>region</i>:<i>account-id</i>:gateway/<i>gateway-id</i> </code> </p> </li> </ul>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.get_web_acl_for_resource_request.GetWebACLForResourceRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.get_web_acl_for_resource_response.GetWebACLForResourceResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.get_web_acl_for_resource

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.get_web_acl_for_resource.get_web_acl_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.get_web_acl_for_resource_request.GetWebACLForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_api_keys(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_api_keys_response.ListAPIKeysResponse":
        """<p>Retrieves a list of the API keys that you've defined for the specified scope. </p> <p>API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_api_keys_request.ListAPIKeysRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_api_keys_response.ListAPIKeysResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_api_keys

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_api_keys.list_api_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_api_keys_request.ListAPIKeysRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_available_managed_rule_groups(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_available_managed_rule_groups_response.ListAvailableManagedRuleGroupsResponse":
        """<p>Retrieves an array of managed rule groups that are available for you to use. This list includes all Amazon Web Services Managed Rules rule groups and all of the Amazon Web Services Marketplace managed rule groups that you're subscribed to.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_available_managed_rule_groups_request.ListAvailableManagedRuleGroupsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_available_managed_rule_groups_response.ListAvailableManagedRuleGroupsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_available_managed_rule_groups

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_available_managed_rule_groups.list_available_managed_rule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_available_managed_rule_groups_request.ListAvailableManagedRuleGroupsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_available_managed_rule_group_versions(
        self,
        vendor_name: "capo_wafv2.types.vendor_name.VendorName",
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_available_managed_rule_group_versions_response.ListAvailableManagedRuleGroupVersionsResponse":
        """<p>Returns a list of the available versions for the specified managed rule group. </p>

        Args:
            vendor_name: <p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>
            name: <p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_available_managed_rule_group_versions_request.ListAvailableManagedRuleGroupVersionsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_available_managed_rule_group_versions_response.ListAvailableManagedRuleGroupVersionsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_available_managed_rule_group_versions

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_available_managed_rule_group_versions.list_available_managed_rule_group_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_available_managed_rule_group_versions_request.ListAvailableManagedRuleGroupVersionsRequest = {
            "vendor_name": vendor_name,
            "name": name,
            "scope": scope,
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ip_sets(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_ip_sets_response.ListIPSetsResponse":
        """<p>Retrieves an array of <a>IPSetSummary</a> objects for the IP sets that you manage.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_ip_sets_request.ListIPSetsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_ip_sets_response.ListIPSetsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_ip_sets

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_ip_sets.list_ip_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_ip_sets_request.ListIPSetsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_logging_configurations(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
        log_scope: Optional["capo_wafv2.types.log_scope.LogScope"] = None,
    ) -> "capo_wafv2.types.list_logging_configurations_response.ListLoggingConfigurationsResponse":
        """<p>Retrieves an array of your <a>LoggingConfiguration</a> objects.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            log_scope: <p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_logging_configurations_request.ListLoggingConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_logging_configurations_response.ListLoggingConfigurationsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_logging_configurations

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_logging_configurations.list_logging_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_logging_configurations_request.ListLoggingConfigurationsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit
        if log_scope is not None:
            input_["log_scope"] = log_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_rule_sets(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_managed_rule_sets_response.ListManagedRuleSetsResponse":
        """<p>Retrieves the managed rule sets that you own. </p> <note> <p>This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers. </p> <p>Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are <code>ListManagedRuleSets</code>, <code>GetManagedRuleSet</code>, <code>PutManagedRuleSetVersions</code>, and <code>UpdateManagedRuleSetVersionExpiryDate</code>.</p> </note>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_managed_rule_sets_request.ListManagedRuleSetsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_managed_rule_sets_response.ListManagedRuleSetsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_managed_rule_sets

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_managed_rule_sets.list_managed_rule_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_managed_rule_sets_request.ListManagedRuleSetsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_mobile_sdk_releases(
        self,
        platform: "capo_wafv2.types.platform.Platform",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_mobile_sdk_releases_response.ListMobileSdkReleasesResponse":
        """<p>Retrieves a list of the available releases for the mobile SDK and the specified device platform. </p> <p>The mobile SDK is not generally available. Customers who have access to the mobile SDK can use it to establish and manage WAF tokens for use in HTTP(S) requests from a mobile device to WAF. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            platform: <p>The device platform to retrieve the list for.</p>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_mobile_sdk_releases_request.ListMobileSdkReleasesRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_mobile_sdk_releases_response.ListMobileSdkReleasesResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_mobile_sdk_releases

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_mobile_sdk_releases.list_mobile_sdk_releases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_mobile_sdk_releases_request.ListMobileSdkReleasesRequest = {
            "platform": platform
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_regex_pattern_sets(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> (
        "capo_wafv2.types.list_regex_pattern_sets_response.ListRegexPatternSetsResponse"
    ):
        """<p>Retrieves an array of <a>RegexPatternSetSummary</a> objects for the regex pattern sets that you manage.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_regex_pattern_sets_request.ListRegexPatternSetsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_regex_pattern_sets_response.ListRegexPatternSetsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_regex_pattern_sets

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_regex_pattern_sets.list_regex_pattern_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_regex_pattern_sets_request.ListRegexPatternSetsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_resources_for_web_acl(
        self,
        web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        resource_type: Optional["capo_wafv2.types.resource_type.ResourceType"] = None,
    ) -> "capo_wafv2.types.list_resources_for_web_acl_response.ListResourcesForWebACLResponse":
        """<p>Retrieves an array of the Amazon Resource Names (ARNs) for the resources that are associated with the specified web ACL. </p> <p>For Amazon CloudFront, don't use this call. Instead, use the CloudFront call <code>ListDistributionsByWebACLId</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html">ListDistributionsByWebACLId</a> in the <i>Amazon CloudFront API Reference</i>. </p> <p> <b>Required permissions for customer-managed IAM policies</b> </p> <p>This call requires permissions that are specific to the protected resource type. For details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-ListResourcesForWebACL">Permissions for ListResourcesForWebACL</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the web ACL.</p>
            resource_type: <p>Retrieves the web ACLs that are used by the specified resource type. </p> <p>For Amazon CloudFront, don't use this call. Instead, use the CloudFront call <code>ListDistributionsByWebACLId</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html">ListDistributionsByWebACLId</a> in the <i>Amazon CloudFront API Reference</i>. </p> <note> <p>If you don't provide a resource type, the call uses the resource type <code>APPLICATION_LOAD_BALANCER</code>. </p> </note> <p>Default: <code>APPLICATION_LOAD_BALANCER</code> </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_resources_for_web_acl_request.ListResourcesForWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_resources_for_web_acl_response.ListResourcesForWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_resources_for_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_resources_for_web_acl.list_resources_for_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_resources_for_web_acl_request.ListResourcesForWebACLRequest = {
            "web_acl_arn": web_acl_arn
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_rule_groups(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_rule_groups_response.ListRuleGroupsResponse":
        """<p>Retrieves an array of <a>RuleGroupSummary</a> objects for the rule groups that you manage. </p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_rule_groups_request.ListRuleGroupsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_rule_groups_response.ListRuleGroupsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_rule_groups

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_rule_groups.list_rule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_rule_groups_request.ListRuleGroupsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_settlement_records(
        self,
        time_window: "capo_wafv2.types.time_window.TimeWindow",
        scope: "capo_wafv2.types.scope.Scope",
        currency: "capo_wafv2.types.currency.Currency",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        filters: Optional[
            "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
        ] = None,
        sort_by: Optional[
            "capo_wafv2.types.settlement_sort_by.SettlementSortBy"
        ] = None,
        sort_order: Optional["capo_wafv2.types.sort_order.SortOrder"] = None,
        limit: Optional[
            "capo_wafv2.types.settlement_record_limit.SettlementRecordLimit"
        ] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
    ) -> "capo_wafv2.types.list_settlement_records_response.ListSettlementRecordsResponse":
        """<p>Retrieves individual settlement transaction records for monetization. Each record represents a single payment transaction between a client and your protected resource. This operation is only available for <code>CLOUDFRONT</code> scope. The maximum supported time window is 90 days. When no <code>CurrencyMode</code> filter is provided, results default to <code>REAL</code>. To retrieve test data, include a <code>CurrencyMode</code> filter with the value <code>TEST</code>.</p>

        Args:
            time_window: <p>The time range for the query. Specify start and end timestamps.</p>
            scope: <p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>
            currency: <p>The currency for the amounts in the response.</p>
            filters: <p>Optional filters to narrow the results. You can filter by payer address, status, source name, network, or other settlement fields.</p>
            sort_by: <p>The field to sort settlement records by: <code>TIMESTAMP</code>, <code>AMOUNT</code>, <code>NAME</code>, or <code>STATUS</code>.</p>
            sort_order: <p>The sort order: <code>ASC</code> for ascending or <code>DESC</code> for descending.</p>
            limit: <p>The maximum number of settlement records to return. Minimum: 1. Maximum: 100.</p>
            next_marker: <p>When you get a paginated response, this marker indicates that additional results are available.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_settlement_records_request.ListSettlementRecordsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_settlement_records_response.ListSettlementRecordsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_settlement_records

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_settlement_records.list_settlement_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_settlement_records_request.ListSettlementRecordsRequest = {
            "time_window": time_window,
            "scope": scope,
            "currency": currency,
        }
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if limit is not None:
            input_["limit"] = limit
        if next_marker is not None:
            input_["next_marker"] = next_marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the <a>TagInfoForResource</a> for the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p> <p>You can tag the Amazon Web Services resources that you manage through WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't manage or view tags through the WAF console. </p>

        Args:
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_tags_for_resource

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_web_ac_ls(
        self,
        scope: "capo_wafv2.types.scope.Scope",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        next_marker: Optional["capo_wafv2.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_wafv2.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_wafv2.types.list_web_ac_ls_response.ListWebACLsResponse":
        """<p>Retrieves an array of <a>WebACLSummary</a> objects for the web ACLs that you manage.</p>

        Args:
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            next_marker: <p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>
            limit: <p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.list_web_ac_ls_request.ListWebACLsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.list_web_ac_ls_response.ListWebACLsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.list_web_ac_ls

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.list_web_ac_ls.list_web_ac_ls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.list_web_ac_ls_request.ListWebACLsRequest = {
            "scope": scope
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_logging_configuration(
        self,
        logging_configuration: "capo_wafv2.types.logging_configuration.LoggingConfiguration",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.put_logging_configuration_response.PutLoggingConfigurationResponse":
        """<p>Enables the specified <a>LoggingConfiguration</a>, to start logging from a web ACL, according to the configuration provided. </p> <p>If you configure data protection for the web ACL, the protection applies to the data that WAF sends to the logs. </p> <note> <p>This operation completely replaces any mutable specifications that you already have for a logging configuration with the ones that you provide to this call. </p> <p>To modify an existing logging configuration, do the following: </p> <ol> <li> <p>Retrieve it by calling <a>GetLoggingConfiguration</a> </p> </li> <li> <p>Update its settings as needed</p> </li> <li> <p>Provide the complete logging configuration specification to this call</p> </li> </ol> </note> <note> <p>You can define one logging destination per web ACL.</p> </note> <p>You can access information about the traffic that WAF inspects using the following steps:</p> <ol> <li> <p>Create your logging destination. You can use an Amazon CloudWatch Logs log group, an Amazon Simple Storage Service (Amazon S3) bucket, or an Amazon Kinesis Data Firehose. </p> <p>The name that you give the destination must start with <code>aws-waf-logs-</code>. Depending on the type of destination, you might need to configure additional settings or permissions. </p> <p>For configuration requirements and pricing information for each destination type, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging.html">Logging web ACL traffic</a> in the <i>WAF Developer Guide</i>.</p> </li> <li> <p>Associate your logging destination to your web ACL using a <code>PutLoggingConfiguration</code> request.</p> </li> </ol> <p>When you successfully enable logging using a <code>PutLoggingConfiguration</code> request, WAF creates an additional role or policy that is required to write logs to the logging destination. For an Amazon CloudWatch Logs log group, WAF creates a resource policy on the log group. For an Amazon S3 bucket, WAF creates a bucket policy. For an Amazon Kinesis Data Firehose, WAF creates a service-linked role.</p> <p>For additional information about web ACL logging, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging.html">Logging web ACL traffic information</a> in the <i>WAF Developer Guide</i>.</p>

        Args:
            logging_configuration: <p></p>

        Raises:
            capo_wafv2.errors.waf_feature_not_included_in_pricing_plan_exception.WAFFeatureNotIncludedInPricingPlanException: <p>The operation failed because the specified WAF feature isn't supported by the CloudFront pricing plan associated with the web ACL.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_log_destination_permission_issue_exception.WAFLogDestinationPermissionIssueException: <p>The operation failed because you don't have the permissions that your logging configuration requires. For information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging.html">Logging web ACL traffic information</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_service_linked_role_error_exception.WAFServiceLinkedRoleErrorException: <p>WAF is not able to access the service linked role. This can be caused by a previous <code>PutLoggingConfiguration</code> request, which can lock the service linked role for about 20 seconds. Please try your request again. The service linked role can also be locked by a previous <code>DeleteServiceLinkedRole</code> request, which can lock the role for 15 minutes or more. If you recently made a call to <code>DeleteServiceLinkedRole</code>, wait at least 15 minutes and try the request again. If you receive this same exception again, you will have to wait additional time until the role is unlocked.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.put_logging_configuration_request.PutLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.put_logging_configuration_response.PutLoggingConfigurationResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.put_logging_configuration

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.put_logging_configuration.put_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.put_logging_configuration_request.PutLoggingConfigurationRequest = {
            "logging_configuration": logging_configuration
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_managed_rule_set_versions(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        recommended_version: Optional[
            "capo_wafv2.types.version_key_string.VersionKeyString"
        ] = None,
        versions_to_publish: Optional[
            "capo_wafv2.types.versions_to_publish.VersionsToPublish"
        ] = None,
    ) -> "capo_wafv2.types.put_managed_rule_set_versions_response.PutManagedRuleSetVersionsResponse":
        """<p>Defines the versions of your managed rule set that you are offering to the customers. Customers see your offerings as managed rule groups with versioning.</p> <note> <p>This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers. </p> <p>Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are <code>ListManagedRuleSets</code>, <code>GetManagedRuleSet</code>, <code>PutManagedRuleSetVersions</code>, and <code>UpdateManagedRuleSetVersionExpiryDate</code>.</p> </note> <p>Customers retrieve their managed rule group list by calling <a>ListAvailableManagedRuleGroups</a>. The name that you provide here for your managed rule set is the name the customer sees for the corresponding managed rule group. Customers can retrieve the available versions for a managed rule group by calling <a>ListAvailableManagedRuleGroupVersions</a>. You provide a rule group specification for each version. For each managed rule set, you must specify a version that you recommend using. </p> <p>To initiate the expiration of a managed rule group version, use <a>UpdateManagedRuleSetVersionExpiryDate</a>.</p>

        Args:
            name: <p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>
            recommended_version: <p>The version of the named managed rule group that you'd like your customers to choose, from among your version offerings. </p>
            versions_to_publish: <p>The versions of the named managed rule group that you want to offer to your customers. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.put_managed_rule_set_versions_request.PutManagedRuleSetVersionsRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.put_managed_rule_set_versions_response.PutManagedRuleSetVersionsResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.put_managed_rule_set_versions

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.put_managed_rule_set_versions.put_managed_rule_set_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.put_managed_rule_set_versions_request.PutManagedRuleSetVersionsRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
        }
        if recommended_version is not None:
            input_["recommended_version"] = recommended_version
        if versions_to_publish is not None:
            input_["versions_to_publish"] = versions_to_publish

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_permission_policy(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        policy: "capo_wafv2.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.put_permission_policy_response.PutPermissionPolicyResponse":
        """<p>Use this to share a rule group with other accounts.</p> <p>This action attaches an IAM policy to the specified resource. You must be the owner of the rule group to perform this operation.</p> <p>This action is subject to the following restrictions:</p> <ul> <li> <p>You can attach only one policy with each <code>PutPermissionPolicy</code> request.</p> </li> <li> <p>The ARN in the request must be a valid WAF <a>RuleGroup</a> ARN and the rule group must exist in the same Region.</p> </li> <li> <p>The user making the request must be the owner of the rule group.</p> </li> </ul> <p>If a rule group has been shared with your account, you can access it through the call <code>GetRuleGroup</code>, and you can reference it in <code>CreateWebACL</code> and <code>UpdateWebACL</code>. Rule groups that are shared with you don't appear in your WAF console rule groups listing. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the <a>RuleGroup</a> to which you want to attach the policy.</p>
            policy: <p>The policy to attach to the specified rule group. </p> <p>The policy specifications must conform to the following:</p> <ul> <li> <p>The policy must be composed using IAM Policy version 2012-10-17.</p> </li> <li> <p>The policy must include specifications for <code>Effect</code>, <code>Action</code>, and <code>Principal</code>.</p> </li> <li> <p> <code>Effect</code> must specify <code>Allow</code>.</p> </li> <li> <p> <code>Action</code> must specify <code>wafv2:CreateWebACL</code>, <code>wafv2:UpdateWebACL</code>, and <code>wafv2:PutFirewallManagerRuleGroups</code> and may optionally specify <code>wafv2:GetRuleGroup</code>. WAF rejects any extra actions or wildcard actions in the policy.</p> </li> <li> <p>The policy must not include a <code>Resource</code> parameter.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM Policies</a>. </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_permission_policy_exception.WAFInvalidPermissionPolicyException: <p>The operation failed because the specified policy isn't in the proper format. </p> <p>The policy specifications must conform to the following:</p> <ul> <li> <p>The policy must be composed using IAM Policy version 2012-10-17.</p> </li> <li> <p>The policy must include specifications for <code>Effect</code>, <code>Action</code>, and <code>Principal</code>.</p> </li> <li> <p> <code>Effect</code> must specify <code>Allow</code>.</p> </li> <li> <p> <code>Action</code> must specify <code>wafv2:CreateWebACL</code>, <code>wafv2:UpdateWebACL</code>, and <code>wafv2:PutFirewallManagerRuleGroups</code> and may optionally specify <code>wafv2:GetRuleGroup</code>. WAF rejects any extra actions or wildcard actions in the policy.</p> </li> <li> <p>The policy must not include a <code>Resource</code> parameter.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM Policies</a>. </p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.put_permission_policy_request.PutPermissionPolicyRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.put_permission_policy_response.PutPermissionPolicyResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.put_permission_policy

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.put_permission_policy.put_permission_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.put_permission_policy_request.PutPermissionPolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        tags: "capo_wafv2.types.tag_list.TagList",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with the specified Amazon Web Services resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p> <p>You can tag the Amazon Web Services resources that you manage through WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't manage or view tags through the WAF console. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>An array of key:value pairs to associate with the resource.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.tag_resource

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_wafv2.types.resource_arn.ResourceArn",
        tag_keys: "capo_wafv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates tags from an Amazon Web Services resource. Tags are key:value pairs that you can associate with Amazon Web Services resources. For example, the tag key might be "customer" and the tag value might be "companyA." You can specify one or more tags to add to each container. You can add up to 50 tags to each Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>An array of keys identifying the tags to disassociate from the resource.</p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException: <p>An error occurred during the tagging operation. Retry your request.</p>
            capo_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p>WAF couldn’t perform your tagging operation because of an internal error. Retry your request.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.untag_resource

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ip_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        addresses: "capo_wafv2.types.ip_addresses.IPAddresses",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
    ) -> "capo_wafv2.types.update_ip_set_response.UpdateIPSetResponse":
        """<p>Updates the specified <a>IPSet</a>. </p> <note> <p>This operation completely replaces the mutable specifications that you already have for the IP set with the ones that you provide to this call. </p> <p>To modify an IP set, do the following: </p> <ol> <li> <p>Retrieve it by calling <a>GetIPSet</a> </p> </li> <li> <p>Update its settings as needed</p> </li> <li> <p>Provide the complete IP set specification to this call</p> </li> </ol> </note> <p> <b>Temporary inconsistencies during updates</b> </p> <p>When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. </p> <p>The following are examples of the temporary inconsistencies that you might notice during change propagation: </p> <ul> <li> <p>After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. </p> </li> <li> <p>After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.</p> </li> <li> <p>After you change a rule action setting, you might see the old action in some places and the new action in others. </p> </li> <li> <p>After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.</p> </li> </ul>

        Args:
            name: <p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            description: <p>A description of the IP set that helps with identification. </p>
            addresses: <p>Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4 and IPv6 CIDR ranges except for <code>/0</code>. </p> <p>Example address strings: </p> <ul> <li> <p>For requests that originated from the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>Example JSON <code>Addresses</code> specifications: </p> <ul> <li> <p>Empty array: <code>"Addresses": []</code> </p> </li> <li> <p>Array with one address: <code>"Addresses": ["192.0.2.44/32"]</code> </p> </li> <li> <p>Array with three addresses: <code>"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]</code> </p> </li> <li> <p>INVALID specification: <code>"Addresses": [""]</code> INVALID </p> </li> </ul>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.update_ip_set_request.UpdateIPSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.update_ip_set_response.UpdateIPSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.update_ip_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.update_ip_set.update_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.update_ip_set_request.UpdateIPSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "addresses": addresses,
            "lock_token": lock_token,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_managed_rule_set_version_expiry_date(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        version_to_expire: "capo_wafv2.types.version_key_string.VersionKeyString",
        expiry_timestamp: "capo_wafv2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
    ) -> "capo_wafv2.types.update_managed_rule_set_version_expiry_date_response.UpdateManagedRuleSetVersionExpiryDateResponse":
        """<p>Updates the expiration information for your managed rule set. Use this to initiate the expiration of a managed rule group version. After you initiate expiration for a version, WAF excludes it from the response to <a>ListAvailableManagedRuleGroupVersions</a> for the managed rule group. </p> <note> <p>This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers. </p> <p>Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are <code>ListManagedRuleSets</code>, <code>GetManagedRuleSet</code>, <code>PutManagedRuleSetVersions</code>, and <code>UpdateManagedRuleSetVersionExpiryDate</code>.</p> </note>

        Args:
            name: <p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>
            version_to_expire: <p>The version that you want to remove from your list of offerings for the named managed rule group. </p>
            expiry_timestamp: <p>The time that you want the version to expire.</p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>

        Raises:
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.update_managed_rule_set_version_expiry_date_request.UpdateManagedRuleSetVersionExpiryDateRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.update_managed_rule_set_version_expiry_date_response.UpdateManagedRuleSetVersionExpiryDateResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.update_managed_rule_set_version_expiry_date

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.update_managed_rule_set_version_expiry_date.update_managed_rule_set_version_expiry_date(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.update_managed_rule_set_version_expiry_date_request.UpdateManagedRuleSetVersionExpiryDateRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "lock_token": lock_token,
            "version_to_expire": version_to_expire,
            "expiry_timestamp": expiry_timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_regex_pattern_set(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        regular_expression_list: "capo_wafv2.types.regular_expression_list.RegularExpressionList",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
    ) -> "capo_wafv2.types.update_regex_pattern_set_response.UpdateRegexPatternSetResponse":
        """<p>Updates the specified <a>RegexPatternSet</a>.</p> <note> <p>This operation completely replaces the mutable specifications that you already have for the regex pattern set with the ones that you provide to this call. </p> <p>To modify a regex pattern set, do the following: </p> <ol> <li> <p>Retrieve it by calling <a>GetRegexPatternSet</a> </p> </li> <li> <p>Update its settings as needed</p> </li> <li> <p>Provide the complete regex pattern set specification to this call</p> </li> </ol> </note> <p> <b>Temporary inconsistencies during updates</b> </p> <p>When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. </p> <p>The following are examples of the temporary inconsistencies that you might notice during change propagation: </p> <ul> <li> <p>After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. </p> </li> <li> <p>After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.</p> </li> <li> <p>After you change a rule action setting, you might see the old action in some places and the new action in others. </p> </li> <li> <p>After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.</p> </li> </ul>

        Args:
            name: <p>The name of the set. You cannot change the name after you create the set.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            description: <p>A description of the set that helps with identification. </p>
            regular_expression_list: <p></p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>

        Raises:
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.update_regex_pattern_set_request.UpdateRegexPatternSetRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.update_regex_pattern_set_response.UpdateRegexPatternSetResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.update_regex_pattern_set

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.update_regex_pattern_set.update_regex_pattern_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.update_regex_pattern_set_request.UpdateRegexPatternSetRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "regular_expression_list": regular_expression_list,
            "lock_token": lock_token,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule_group(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        rules: Optional["capo_wafv2.types.rules.Rules"] = None,
        custom_response_bodies: Optional[
            "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
        ] = None,
        monetization_config: Optional[
            "capo_wafv2.types.monetization_config.MonetizationConfig"
        ] = None,
    ) -> "capo_wafv2.types.update_rule_group_response.UpdateRuleGroupResponse":
        """<p>Updates the specified <a>RuleGroup</a>.</p> <note> <p>This operation completely replaces the mutable specifications that you already have for the rule group with the ones that you provide to this call. </p> <p>To modify a rule group, do the following: </p> <ol> <li> <p>Retrieve it by calling <a>GetRuleGroup</a> </p> </li> <li> <p>Update its settings as needed</p> </li> <li> <p>Provide the complete rule group specification to this call</p> </li> </ol> </note> <p> A rule group defines a collection of rules to inspect and control web requests that you can use in a <a>WebACL</a>. When you create a rule group, you define an immutable capacity limit. If you update a rule group, you must stay within the capacity. This allows others to reuse the rule group with confidence in its capacity requirements. </p> <p> <b>Temporary inconsistencies during updates</b> </p> <p>When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. </p> <p>The following are examples of the temporary inconsistencies that you might notice during change propagation: </p> <ul> <li> <p>After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. </p> </li> <li> <p>After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.</p> </li> <li> <p>After you change a rule action setting, you might see the old action in some places and the new action in others. </p> </li> <li> <p>After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.</p> </li> </ul>

        Args:
            name: <p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            description: <p>A description of the rule group that helps with identification. </p>
            rules: <p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>
            visibility_config: <p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>
            custom_response_bodies: <p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>
            monetization_config: <p>The monetization configuration for the rule group. Provide this when any rule in the rule group uses the <code>Monetize</code> action.</p>

        Raises:
            capo_wafv2.errors.waf_configuration_warning_exception.WAFConfigurationWarningException: <p>The operation failed because you are inspecting the web request body, headers, or cookies without specifying how to handle oversize components. Rules that inspect the body must either provide an <code>OversizeHandling</code> configuration or they must be preceded by a <code>SizeConstraintStatement</code> that blocks the body content from being too large. Rules that inspect the headers or cookies must provide an <code>OversizeHandling</code> configuration. </p> <p>Provide the handling configuration and retry your operation.</p> <p>Alternately, you can suppress this warning by adding the following tag to the resource that you provide to this operation: <code>Tag</code> (key:<code>WAF:OversizeFieldsHandlingConstraintOptOut</code>, value:<code>true</code>).</p>
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet. </p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.update_rule_group_request.UpdateRuleGroupRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.update_rule_group_response.UpdateRuleGroupResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.update_rule_group

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.update_rule_group.update_rule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.update_rule_group_request.UpdateRuleGroupRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "visibility_config": visibility_config,
            "lock_token": lock_token,
        }
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if custom_response_bodies is not None:
            input_["custom_response_bodies"] = custom_response_bodies
        if monetization_config is not None:
            input_["monetization_config"] = monetization_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_web_acl(
        self,
        name: "capo_wafv2.types.entity_name.EntityName",
        scope: "capo_wafv2.types.scope.Scope",
        id: "capo_wafv2.types.entity_id.EntityId",
        default_action: "capo_wafv2.types.default_action.DefaultAction",
        visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig",
        lock_token: "capo_wafv2.types.lock_token.LockToken",
        *,
        config_overrides: Optional[WAFV2ClientConfig] = None,
        description: Optional[
            "capo_wafv2.types.entity_description.EntityDescription"
        ] = None,
        rules: Optional["capo_wafv2.types.rules.Rules"] = None,
        data_protection_config: Optional[
            "capo_wafv2.types.data_protection_config.DataProtectionConfig"
        ] = None,
        custom_response_bodies: Optional[
            "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
        ] = None,
        captcha_config: Optional[
            "capo_wafv2.types.captcha_config.CaptchaConfig"
        ] = None,
        challenge_config: Optional[
            "capo_wafv2.types.challenge_config.ChallengeConfig"
        ] = None,
        token_domains: Optional["capo_wafv2.types.token_domains.TokenDomains"] = None,
        association_config: Optional[
            "capo_wafv2.types.association_config.AssociationConfig"
        ] = None,
        on_source_d_do_s_protection_config: Optional[
            "capo_wafv2.types.on_source_d_do_s_protection_config.OnSourceDDoSProtectionConfig"
        ] = None,
        application_config: Optional[
            "capo_wafv2.types.application_config.ApplicationConfig"
        ] = None,
        monetization_config: Optional[
            "capo_wafv2.types.monetization_config.MonetizationConfig"
        ] = None,
    ) -> "capo_wafv2.types.update_web_acl_response.UpdateWebACLResponse":
        """<p>Updates the specified <a>WebACL</a>. While updating a web ACL, WAF provides continuous coverage to the resources that you have associated with the web ACL. </p> <note> <p>This operation completely replaces the mutable specifications that you already have for the web ACL with the ones that you provide to this call. </p> <p>To modify a web ACL, do the following: </p> <ol> <li> <p>Retrieve it by calling <a>GetWebACL</a> </p> </li> <li> <p>Update its settings as needed</p> </li> <li> <p>Provide the complete web ACL specification to this call</p> </li> </ol> </note> <p> A web ACL defines a collection of rules to use to inspect and control web requests. Each rule has a statement that defines what to look for in web requests and an action that WAF applies to requests that match the statement. In the web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a web ACL can be a combination of the types <a>Rule</a>, <a>RuleGroup</a>, and managed rule group. You can associate a web ACL with one or more Amazon Web Services resources to protect. The resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner service, Amplify application, Amazon Web Services Verified Access instance, and Amazon Bedrock AgentCore Gateway. </p> <p> <b>Temporary inconsistencies during updates</b> </p> <p>When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. </p> <p>The following are examples of the temporary inconsistencies that you might notice during change propagation: </p> <ul> <li> <p>After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. </p> </li> <li> <p>After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.</p> </li> <li> <p>After you change a rule action setting, you might see the old action in some places and the new action in others. </p> </li> <li> <p>After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.</p> </li> </ul>

        Args:
            name: <p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>
            scope: <p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>
            id: <p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>
            default_action: <p>The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. </p>
            description: <p>A description of the web ACL that helps with identification. </p>
            rules: <p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>
            visibility_config: <p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>
            data_protection_config: <p>Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option. </p> <p>The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging. </p>
            lock_token: <p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>
            custom_response_bodies: <p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>
            captcha_config: <p>Specifies how WAF should handle <code>CAPTCHA</code> evaluations for rules that don't have their own <code>CaptchaConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>CaptchaConfig</code>. </p>
            challenge_config: <p>Specifies how WAF should handle challenge evaluations for rules that don't have their own <code>ChallengeConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>ChallengeConfig</code>. </p>
            token_domains: <p>Specifies the domains that WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When WAF provides a token, it uses the domain of the Amazon Web Services resource that the web ACL is protecting. If you don't specify a list of token domains, WAF accepts tokens only for the domain of the protected resource. With a token domain list, WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.</p> <p>Example JSON: <code>"TokenDomains": { "mywebsite.com", "myotherwebsite.com" }</code> </p> <p>Public suffixes aren't allowed. For example, you can't use <code>gov.au</code> or <code>co.uk</code> as token domains.</p>
            association_config: <p>Specifies custom configurations for the associations between the web ACL and protected resources. </p> <p>Use this to customize the maximum size of the request body that your protected resources forward to WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes). </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>
            on_source_d_do_s_protection_config: <p>Specifies the type of DDoS protection to apply to web request data for a web ACL. For most scenarios, it is recommended to use the default protection level, <code>ACTIVE_UNDER_DDOS</code>. If a web ACL is associated with multiple Application Load Balancers, the changes you make to DDoS protection in that web ACL will apply to all associated Application Load Balancers.</p>
            application_config: <p>Configures the ability for the WAF console to store and retrieve application attributes. Application attributes help WAF give recommendations for protection packs.</p> <p>When using <code>UpdateWebACL</code>, <code>ApplicationConfig</code> follows these rules:</p> <ul> <li> <p>If you omit <code>ApplicationConfig</code> from the request, all existing entries in the web ACL are retained.</p> </li> <li> <p>If you include <code>ApplicationConfig</code>, entries must match the existing values exactly. Any attempt to modify existing entries will result in an error.</p> </li> </ul>
            monetization_config: <p>The monetization configuration for the web ACL. Provide this when any rule in the web ACL uses the <code>Monetize</code> action.</p>

        Raises:
            capo_wafv2.errors.waf_configuration_warning_exception.WAFConfigurationWarningException: <p>The operation failed because you are inspecting the web request body, headers, or cookies without specifying how to handle oversize components. Rules that inspect the body must either provide an <code>OversizeHandling</code> configuration or they must be preceded by a <code>SizeConstraintStatement</code> that blocks the body content from being too large. Rules that inspect the headers or cookies must provide an <code>OversizeHandling</code> configuration. </p> <p>Provide the handling configuration and retry your operation.</p> <p>Alternately, you can suppress this warning by adding the following tag to the resource that you provide to this operation: <code>Tag</code> (key:<code>WAF:OversizeFieldsHandlingConstraintOptOut</code>, value:<code>true</code>).</p>
            capo_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException: <p>WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.</p>
            capo_wafv2.errors.waf_expired_managed_rule_group_version_exception.WAFExpiredManagedRuleGroupVersionException: <p>The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling <a>ListAvailableManagedRuleGroupVersions</a>.</p>
            capo_wafv2.errors.waf_feature_not_included_in_pricing_plan_exception.WAFFeatureNotIncludedInPricingPlanException: <p>The operation failed because the specified WAF feature isn't supported by the CloudFront pricing plan associated with the web ACL.</p>
            capo_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException: <p>Your request is valid, but WAF couldn’t perform the operation because of a system problem. Retry your request. </p>
            capo_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation isn't valid. </p>
            capo_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because WAF didn't recognize a parameter in the request. For example: </p> <ul> <li> <p>You specified a parameter name or value that isn't valid.</p> </li> <li> <p>Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. </p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>DefaultAction</code> that isn't among the types available at <a>DefaultAction</a>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.</p> </li> </ul>
            capo_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException: <p>WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.</p>
            capo_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of <code>WebACL</code> objects that you can create for an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>
            capo_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. </p>
            capo_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException: <p>WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation. </p>
            capo_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet. </p>
            capo_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException: <p>WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.</p>
            capo_wafv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wafv2.types.update_web_acl_request.UpdateWebACLRequest]",
        ) -> OperationResponse[
            "capo_wafv2.types.update_web_acl_response.UpdateWebACLResponse"
        ]:
            import capo_wafv2._operations.awswaf_20190729.update_web_acl

            output, http_response = (
                capo_wafv2._operations.awswaf_20190729.update_web_acl.update_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wafv2.types.update_web_acl_request.UpdateWebACLRequest = {
            "name": name,
            "scope": scope,
            "id": id,
            "default_action": default_action,
            "visibility_config": visibility_config,
            "lock_token": lock_token,
        }
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if data_protection_config is not None:
            input_["data_protection_config"] = data_protection_config
        if custom_response_bodies is not None:
            input_["custom_response_bodies"] = custom_response_bodies
        if captcha_config is not None:
            input_["captcha_config"] = captcha_config
        if challenge_config is not None:
            input_["challenge_config"] = challenge_config
        if token_domains is not None:
            input_["token_domains"] = token_domains
        if association_config is not None:
            input_["association_config"] = association_config
        if on_source_d_do_s_protection_config is not None:
            input_["on_source_d_do_s_protection_config"] = (
                on_source_d_do_s_protection_config
            )
        if application_config is not None:
            input_["application_config"] = application_config
        if monetization_config is not None:
            input_["monetization_config"] = monetization_config

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
