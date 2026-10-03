"""Generated from Smithy shape ``com.amazonaws.waf#AWSWAF_20150824``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_waf._auth._signers
import capo_waf._auth._sigv4
from capo_waf._auth._identity import Credentials
from capo_waf._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_waf._auth._zapros_handler import AuthMiddleware
from capo_waf._services._aws_config import aaws_config
from capo_waf._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_waf.types.byte_match_set_updates
    import capo_waf.types.change_token
    import capo_waf.types.create_byte_match_set_request
    import capo_waf.types.create_byte_match_set_response
    import capo_waf.types.create_geo_match_set_request
    import capo_waf.types.create_geo_match_set_response
    import capo_waf.types.create_ip_set_request
    import capo_waf.types.create_ip_set_response
    import capo_waf.types.create_rate_based_rule_request
    import capo_waf.types.create_rate_based_rule_response
    import capo_waf.types.create_regex_match_set_request
    import capo_waf.types.create_regex_match_set_response
    import capo_waf.types.create_regex_pattern_set_request
    import capo_waf.types.create_regex_pattern_set_response
    import capo_waf.types.create_rule_group_request
    import capo_waf.types.create_rule_group_response
    import capo_waf.types.create_rule_request
    import capo_waf.types.create_rule_response
    import capo_waf.types.create_size_constraint_set_request
    import capo_waf.types.create_size_constraint_set_response
    import capo_waf.types.create_sql_injection_match_set_request
    import capo_waf.types.create_sql_injection_match_set_response
    import capo_waf.types.create_web_acl_migration_stack_request
    import capo_waf.types.create_web_acl_migration_stack_response
    import capo_waf.types.create_web_acl_request
    import capo_waf.types.create_web_acl_response
    import capo_waf.types.create_xss_match_set_request
    import capo_waf.types.create_xss_match_set_response
    import capo_waf.types.delete_byte_match_set_request
    import capo_waf.types.delete_byte_match_set_response
    import capo_waf.types.delete_geo_match_set_request
    import capo_waf.types.delete_geo_match_set_response
    import capo_waf.types.delete_ip_set_request
    import capo_waf.types.delete_ip_set_response
    import capo_waf.types.delete_logging_configuration_request
    import capo_waf.types.delete_logging_configuration_response
    import capo_waf.types.delete_permission_policy_request
    import capo_waf.types.delete_permission_policy_response
    import capo_waf.types.delete_rate_based_rule_request
    import capo_waf.types.delete_rate_based_rule_response
    import capo_waf.types.delete_regex_match_set_request
    import capo_waf.types.delete_regex_match_set_response
    import capo_waf.types.delete_regex_pattern_set_request
    import capo_waf.types.delete_regex_pattern_set_response
    import capo_waf.types.delete_rule_group_request
    import capo_waf.types.delete_rule_group_response
    import capo_waf.types.delete_rule_request
    import capo_waf.types.delete_rule_response
    import capo_waf.types.delete_size_constraint_set_request
    import capo_waf.types.delete_size_constraint_set_response
    import capo_waf.types.delete_sql_injection_match_set_request
    import capo_waf.types.delete_sql_injection_match_set_response
    import capo_waf.types.delete_web_acl_request
    import capo_waf.types.delete_web_acl_response
    import capo_waf.types.delete_xss_match_set_request
    import capo_waf.types.delete_xss_match_set_response
    import capo_waf.types.geo_match_set_updates
    import capo_waf.types.get_byte_match_set_request
    import capo_waf.types.get_byte_match_set_response
    import capo_waf.types.get_change_token_request
    import capo_waf.types.get_change_token_response
    import capo_waf.types.get_change_token_status_request
    import capo_waf.types.get_change_token_status_response
    import capo_waf.types.get_geo_match_set_request
    import capo_waf.types.get_geo_match_set_response
    import capo_waf.types.get_ip_set_request
    import capo_waf.types.get_ip_set_response
    import capo_waf.types.get_logging_configuration_request
    import capo_waf.types.get_logging_configuration_response
    import capo_waf.types.get_permission_policy_request
    import capo_waf.types.get_permission_policy_response
    import capo_waf.types.get_rate_based_rule_managed_keys_request
    import capo_waf.types.get_rate_based_rule_managed_keys_response
    import capo_waf.types.get_rate_based_rule_request
    import capo_waf.types.get_rate_based_rule_response
    import capo_waf.types.get_regex_match_set_request
    import capo_waf.types.get_regex_match_set_response
    import capo_waf.types.get_regex_pattern_set_request
    import capo_waf.types.get_regex_pattern_set_response
    import capo_waf.types.get_rule_group_request
    import capo_waf.types.get_rule_group_response
    import capo_waf.types.get_rule_request
    import capo_waf.types.get_rule_response
    import capo_waf.types.get_sampled_requests_max_items
    import capo_waf.types.get_sampled_requests_request
    import capo_waf.types.get_sampled_requests_response
    import capo_waf.types.get_size_constraint_set_request
    import capo_waf.types.get_size_constraint_set_response
    import capo_waf.types.get_sql_injection_match_set_request
    import capo_waf.types.get_sql_injection_match_set_response
    import capo_waf.types.get_web_acl_request
    import capo_waf.types.get_web_acl_response
    import capo_waf.types.get_xss_match_set_request
    import capo_waf.types.get_xss_match_set_response
    import capo_waf.types.ignore_unsupported_type
    import capo_waf.types.ip_set_updates
    import capo_waf.types.list_activated_rules_in_rule_group_request
    import capo_waf.types.list_activated_rules_in_rule_group_response
    import capo_waf.types.list_byte_match_sets_request
    import capo_waf.types.list_byte_match_sets_response
    import capo_waf.types.list_geo_match_sets_request
    import capo_waf.types.list_geo_match_sets_response
    import capo_waf.types.list_ip_sets_request
    import capo_waf.types.list_ip_sets_response
    import capo_waf.types.list_logging_configurations_request
    import capo_waf.types.list_logging_configurations_response
    import capo_waf.types.list_rate_based_rules_request
    import capo_waf.types.list_rate_based_rules_response
    import capo_waf.types.list_regex_match_sets_request
    import capo_waf.types.list_regex_match_sets_response
    import capo_waf.types.list_regex_pattern_sets_request
    import capo_waf.types.list_regex_pattern_sets_response
    import capo_waf.types.list_rule_groups_request
    import capo_waf.types.list_rule_groups_response
    import capo_waf.types.list_rules_request
    import capo_waf.types.list_rules_response
    import capo_waf.types.list_size_constraint_sets_request
    import capo_waf.types.list_size_constraint_sets_response
    import capo_waf.types.list_sql_injection_match_sets_request
    import capo_waf.types.list_sql_injection_match_sets_response
    import capo_waf.types.list_subscribed_rule_groups_request
    import capo_waf.types.list_subscribed_rule_groups_response
    import capo_waf.types.list_tags_for_resource_request
    import capo_waf.types.list_tags_for_resource_response
    import capo_waf.types.list_web_ac_ls_request
    import capo_waf.types.list_web_ac_ls_response
    import capo_waf.types.list_xss_match_sets_request
    import capo_waf.types.list_xss_match_sets_response
    import capo_waf.types.logging_configuration
    import capo_waf.types.metric_name
    import capo_waf.types.next_marker
    import capo_waf.types.pagination_limit
    import capo_waf.types.policy_string
    import capo_waf.types.put_logging_configuration_request
    import capo_waf.types.put_logging_configuration_response
    import capo_waf.types.put_permission_policy_request
    import capo_waf.types.put_permission_policy_response
    import capo_waf.types.rate_key
    import capo_waf.types.rate_limit
    import capo_waf.types.regex_match_set_updates
    import capo_waf.types.regex_pattern_set_updates
    import capo_waf.types.resource_arn
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name
    import capo_waf.types.rule_group_updates
    import capo_waf.types.rule_updates
    import capo_waf.types.s3_bucket_name
    import capo_waf.types.size_constraint_set_updates
    import capo_waf.types.sql_injection_match_set_updates
    import capo_waf.types.tag_key_list
    import capo_waf.types.tag_list
    import capo_waf.types.tag_resource_request
    import capo_waf.types.tag_resource_response
    import capo_waf.types.time_window
    import capo_waf.types.untag_resource_request
    import capo_waf.types.untag_resource_response
    import capo_waf.types.update_byte_match_set_request
    import capo_waf.types.update_byte_match_set_response
    import capo_waf.types.update_geo_match_set_request
    import capo_waf.types.update_geo_match_set_response
    import capo_waf.types.update_ip_set_request
    import capo_waf.types.update_ip_set_response
    import capo_waf.types.update_rate_based_rule_request
    import capo_waf.types.update_rate_based_rule_response
    import capo_waf.types.update_regex_match_set_request
    import capo_waf.types.update_regex_match_set_response
    import capo_waf.types.update_regex_pattern_set_request
    import capo_waf.types.update_regex_pattern_set_response
    import capo_waf.types.update_rule_group_request
    import capo_waf.types.update_rule_group_response
    import capo_waf.types.update_rule_request
    import capo_waf.types.update_rule_response
    import capo_waf.types.update_size_constraint_set_request
    import capo_waf.types.update_size_constraint_set_response
    import capo_waf.types.update_sql_injection_match_set_request
    import capo_waf.types.update_sql_injection_match_set_response
    import capo_waf.types.update_web_acl_request
    import capo_waf.types.update_web_acl_response
    import capo_waf.types.update_xss_match_set_request
    import capo_waf.types.update_xss_match_set_response
    import capo_waf.types.waf_action
    import capo_waf.types.web_acl_updates
    import capo_waf.types.xss_match_set_updates


class AsyncWAFClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncWAFClient:
    """A client for the ``WAF`` service.

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
        self._config = AsyncWAFClientConfig(
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
        self, config_overrides: Optional[AsyncWAFClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWAFClientConfig = config_overrides or {}
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

    async def create_byte_match_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_byte_match_set_response.CreateByteMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>ByteMatchSet</code>. You then use <a>UpdateByteMatchSet</a> to identify the part of a web request that you want AWS WAF to inspect, such as the values of the <code>User-Agent</code> header or the query string. For example, you can create a <code>ByteMatchSet</code> that matches any requests with <code>User-Agent</code> headers that contain the string <code>BadBot</code>. You can then configure AWS WAF to reject those requests.</p> <p>To create and configure a <code>ByteMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateByteMatchSet</code> request.</p> </li> <li> <p>Submit a <code>CreateByteMatchSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateByteMatchSet</code> request.</p> </li> <li> <p>Submit an <a>UpdateByteMatchSet</a> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>ByteMatchSet</a>. You can't change <code>Name</code> after you create a <code>ByteMatchSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_byte_match_set_request.CreateByteMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_byte_match_set_response.CreateByteMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_byte_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_byte_match_set.async_create_byte_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_byte_match_set_request.CreateByteMatchSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_geo_match_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_geo_match_set_response.CreateGeoMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates an <a>GeoMatchSet</a>, which you use to specify which web requests you want to allow or block based on the country that the requests originate from. For example, if you're receiving a lot of requests from one or more countries and you want to block the requests, you can create an <code>GeoMatchSet</code> that contains those countries and then configure AWS WAF to block the requests. </p> <p>To create and configure a <code>GeoMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateGeoMatchSet</code> request.</p> </li> <li> <p>Submit a <code>CreateGeoMatchSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateGeoMatchSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateGeoMatchSetSet</code> request to specify the countries that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>GeoMatchSet</a>. You can't change <code>Name</code> after you create the <code>GeoMatchSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_geo_match_set_request.CreateGeoMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_geo_match_set_response.CreateGeoMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_geo_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_geo_match_set.async_create_geo_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_geo_match_set_request.CreateGeoMatchSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ip_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_ip_set_response.CreateIPSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates an <a>IPSet</a>, which you use to specify which web requests that you want to allow or block based on the IP addresses that the requests originate from. For example, if you're receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an <code>IPSet</code> that contains those IP addresses and then configure AWS WAF to block the requests. </p> <p>To create and configure an <code>IPSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateIPSet</code> request.</p> </li> <li> <p>Submit a <code>CreateIPSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateIPSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateIPSet</code> request to specify the IP addresses that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>IPSet</a>. You can't change <code>Name</code> after you create the <code>IPSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an IP set
            The following example creates an IP match set named MyIPSetFriendlyName.

            >>> await client.create_ip_set(name='MyIPSetFriendlyName', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_ip_set_request.CreateIPSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_ip_set_response.CreateIPSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_ip_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_ip_set.async_create_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_ip_set_request.CreateIPSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_rate_based_rule(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        metric_name: "capo_waf.types.metric_name.MetricName",
        rate_key: "capo_waf.types.rate_key.RateKey",
        rate_limit: "capo_waf.types.rate_limit.RateLimit",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        tags: Optional["capo_waf.types.tag_list.TagList"] = None,
    ) -> "capo_waf.types.create_rate_based_rule_response.CreateRateBasedRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <a>RateBasedRule</a>. The <code>RateBasedRule</code> contains a <code>RateLimit</code>, which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The <code>RateBasedRule</code> also contains the <code>IPSet</code> objects, <code>ByteMatchSet</code> objects, and other predicates that identify the requests that you want to count or block if these requests exceed the <code>RateLimit</code>.</p> <p>If you add more than one predicate to a <code>RateBasedRule</code>, a request not only must exceed the <code>RateLimit</code>, but it also must match all the conditions to be counted or blocked. For example, suppose you add the following to a <code>RateBasedRule</code>:</p> <ul> <li> <p>An <code>IPSet</code> that matches the IP address <code>192.0.2.44/32</code> </p> </li> <li> <p>A <code>ByteMatchSet</code> that matches <code>BadBot</code> in the <code>User-Agent</code> header</p> </li> </ul> <p>Further, you specify a <code>RateLimit</code> of 1,000.</p> <p>You then add the <code>RateBasedRule</code> to a <code>WebACL</code> and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 <i>and</i> the <code>User-Agent</code> header in the request must contain the value <code>BadBot</code>. Further, requests that match these two conditions must be received at a rate of more than 1,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 1,000 for a five-minute period, AWS WAF no longer blocks the requests.</p> <p>As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a <code>RateBasedRule</code>:</p> <ul> <li> <p>A <code>ByteMatchSet</code> with <code>FieldToMatch</code> of <code>URI</code> </p> </li> <li> <p>A <code>PositionalConstraint</code> of <code>STARTS_WITH</code> </p> </li> <li> <p>A <code>TargetString</code> of <code>login</code> </p> </li> </ul> <p>Further, you specify a <code>RateLimit</code> of 1,000.</p> <p>By adding this <code>RateBasedRule</code> to a <code>WebACL</code>, you could limit requests to your login page without affecting the rest of your site.</p> <p>To create and configure a <code>RateBasedRule</code>, perform the following steps:</p> <ol> <li> <p>Create and update the predicates that you want to include in the rule. For more information, see <a>CreateByteMatchSet</a>, <a>CreateIPSet</a>, and <a>CreateSqlInjectionMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateRule</code> request.</p> </li> <li> <p>Submit a <code>CreateRateBasedRule</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateRule</a> request.</p> </li> <li> <p>Submit an <code>UpdateRateBasedRule</code> request to specify the predicates that you want to include in the rule.</p> </li> <li> <p>Create and update a <code>WebACL</code> that contains the <code>RateBasedRule</code>. For more information, see <a>CreateWebACL</a>.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>RateBasedRule</a>. You can't change the name of a <code>RateBasedRule</code> after you create it.</p>
            metric_name: <p>A friendly name or description for the metrics for this <code>RateBasedRule</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>RateBasedRule</code>.</p>
            rate_key: <p>The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for <code>RateKey</code> is <code>IP</code>. <code>IP</code> indicates that requests that arrive from the same IP address are subject to the <code>RateLimit</code> that is specified in the <code>RateBasedRule</code>.</p>
            rate_limit: <p>The maximum number of requests, which have an identical value in the field that is specified by <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>
            change_token: <p>The <code>ChangeToken</code> that you used to submit the <code>CreateRateBasedRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>
            tags: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_rate_based_rule_request.CreateRateBasedRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_rate_based_rule_response.CreateRateBasedRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_rate_based_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_rate_based_rule.async_create_rate_based_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_rate_based_rule_request.CreateRateBasedRuleRequest = {
            "name": name,
            "metric_name": metric_name,
            "rate_key": rate_key,
            "rate_limit": rate_limit,
            "change_token": change_token,
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

    async def create_regex_match_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_regex_match_set_response.CreateRegexMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <a>RegexMatchSet</a>. You then use <a>UpdateRegexMatchSet</a> to identify the part of a web request that you want AWS WAF to inspect, such as the values of the <code>User-Agent</code> header or the query string. For example, you can create a <code>RegexMatchSet</code> that contains a <code>RegexMatchTuple</code> that looks for any requests with <code>User-Agent</code> headers that match a <code>RegexPatternSet</code> with pattern <code>B[a@]dB[o0]t</code>. You can then configure AWS WAF to reject those requests.</p> <p>To create and configure a <code>RegexMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateRegexMatchSet</code> request.</p> </li> <li> <p>Submit a <code>CreateRegexMatchSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateRegexMatchSet</code> request.</p> </li> <li> <p>Submit an <a>UpdateRegexMatchSet</a> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value, using a <code>RegexPatternSet</code>, that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>RegexMatchSet</a>. You can't change <code>Name</code> after you create a <code>RegexMatchSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_regex_match_set_request.CreateRegexMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_regex_match_set_response.CreateRegexMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_regex_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_regex_match_set.async_create_regex_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_regex_match_set_request.CreateRegexMatchSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_regex_pattern_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> (
        "capo_waf.types.create_regex_pattern_set_response.CreateRegexPatternSetResponse"
    ):
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>RegexPatternSet</code>. You then use <a>UpdateRegexPatternSet</a> to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as <code>B[a@]dB[o0]t</code>. You can then configure AWS WAF to reject those requests.</p> <p>To create and configure a <code>RegexPatternSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateRegexPatternSet</code> request.</p> </li> <li> <p>Submit a <code>CreateRegexPatternSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateRegexPatternSet</code> request.</p> </li> <li> <p>Submit an <a>UpdateRegexPatternSet</a> request to specify the string that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>RegexPatternSet</a>. You can't change <code>Name</code> after you create a <code>RegexPatternSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_regex_pattern_set_request.CreateRegexPatternSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_regex_pattern_set_response.CreateRegexPatternSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_regex_pattern_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_regex_pattern_set.async_create_regex_pattern_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_regex_pattern_set_request.CreateRegexPatternSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_rule(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        metric_name: "capo_waf.types.metric_name.MetricName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        tags: Optional["capo_waf.types.tag_list.TagList"] = None,
    ) -> "capo_waf.types.create_rule_response.CreateRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>Rule</code>, which contains the <code>IPSet</code> objects, <code>ByteMatchSet</code> objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a <code>Rule</code>, a request must match all of the specifications to be allowed or blocked. For example, suppose that you add the following to a <code>Rule</code>:</p> <ul> <li> <p>An <code>IPSet</code> that matches the IP address <code>192.0.2.44/32</code> </p> </li> <li> <p>A <code>ByteMatchSet</code> that matches <code>BadBot</code> in the <code>User-Agent</code> header</p> </li> </ul> <p>You then add the <code>Rule</code> to a <code>WebACL</code> and specify that you want to blocks requests that satisfy the <code>Rule</code>. For a request to be blocked, it must come from the IP address 192.0.2.44 <i>and</i> the <code>User-Agent</code> header in the request must contain the value <code>BadBot</code>.</p> <p>To create and configure a <code>Rule</code>, perform the following steps:</p> <ol> <li> <p>Create and update the predicates that you want to include in the <code>Rule</code>. For more information, see <a>CreateByteMatchSet</a>, <a>CreateIPSet</a>, and <a>CreateSqlInjectionMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateRule</code> request.</p> </li> <li> <p>Submit a <code>CreateRule</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateRule</a> request.</p> </li> <li> <p>Submit an <code>UpdateRule</code> request to specify the predicates that you want to include in the <code>Rule</code>.</p> </li> <li> <p>Create and update a <code>WebACL</code> that contains the <code>Rule</code>. For more information, see <a>CreateWebACL</a>.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>Rule</a>. You can't change the name of a <code>Rule</code> after you create it.</p>
            metric_name: <p>A friendly name or description for the metrics for this <code>Rule</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>Rule</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            tags: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a rule
            The following example creates a rule named WAFByteHeaderRule.

            >>> await client.create_rule(name='WAFByteHeaderRule', metric_name='WAFByteHeaderRule', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_rule_request.CreateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_rule_response.CreateRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_rule_request.CreateRuleRequest = {
            "name": name,
            "metric_name": metric_name,
            "change_token": change_token,
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

    async def create_rule_group(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        metric_name: "capo_waf.types.metric_name.MetricName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        tags: Optional["capo_waf.types.tag_list.TagList"] = None,
    ) -> "capo_waf.types.create_rule_group_response.CreateRuleGroupResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>RuleGroup</code>. A rule group is a collection of predefined rules that you add to a web ACL. You use <a>UpdateRuleGroup</a> to add rules to the rule group.</p> <p>Rule groups are subject to the following limits:</p> <ul> <li> <p>Three rule groups per account. You can request an increase to this limit by contacting customer support.</p> </li> <li> <p>One rule group per web ACL.</p> </li> <li> <p>Ten rules per rule group.</p> </li> </ul> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>RuleGroup</a>. You can't change <code>Name</code> after you create a <code>RuleGroup</code>.</p>
            metric_name: <p>A friendly name or description for the metrics for this <code>RuleGroup</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>RuleGroup</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            tags: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_rule_group_request.CreateRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_rule_group_response.CreateRuleGroupResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_rule_group

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_rule_group.async_create_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_rule_group_request.CreateRuleGroupRequest = {
            "name": name,
            "metric_name": metric_name,
            "change_token": change_token,
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

    async def create_size_constraint_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_size_constraint_set_response.CreateSizeConstraintSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>SizeConstraintSet</code>. You then use <a>UpdateSizeConstraintSet</a> to identify the part of a web request that you want AWS WAF to check for length, such as the length of the <code>User-Agent</code> header or the length of the query string. For example, you can create a <code>SizeConstraintSet</code> that matches any requests that have a query string that is longer than 100 bytes. You can then configure AWS WAF to reject those requests.</p> <p>To create and configure a <code>SizeConstraintSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateSizeConstraintSet</code> request.</p> </li> <li> <p>Submit a <code>CreateSizeConstraintSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateSizeConstraintSet</code> request.</p> </li> <li> <p>Submit an <a>UpdateSizeConstraintSet</a> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>SizeConstraintSet</a>. You can't change <code>Name</code> after you create a <code>SizeConstraintSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a size constraint
            The following example creates size constraint set named MySampleSizeConstraintSet.

            >>> await client.create_size_constraint_set(name='MySampleSizeConstraintSet', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_size_constraint_set_request.CreateSizeConstraintSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_size_constraint_set_response.CreateSizeConstraintSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_size_constraint_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_size_constraint_set.async_create_size_constraint_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_size_constraint_set_request.CreateSizeConstraintSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_sql_injection_match_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_sql_injection_match_set_response.CreateSqlInjectionMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <a>SqlInjectionMatchSet</a>, which you use to allow, block, or count requests that contain snippets of SQL code in a specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.</p> <p>To create and configure a <code>SqlInjectionMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateSqlInjectionMatchSet</code> request.</p> </li> <li> <p>Submit a <code>CreateSqlInjectionMatchSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateSqlInjectionMatchSet</a> request.</p> </li> <li> <p>Submit an <a>UpdateSqlInjectionMatchSet</a> request to specify the parts of web requests in which you want to allow, block, or count malicious SQL code.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description for the <a>SqlInjectionMatchSet</a> that you're creating. You can't change <code>Name</code> after you create the <code>SqlInjectionMatchSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a SQL injection match set
            The following example creates a SQL injection match set named MySQLInjectionMatchSet.

            >>> await client.create_sql_injection_match_set(name='MySQLInjectionMatchSet', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_sql_injection_match_set_request.CreateSqlInjectionMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_sql_injection_match_set_response.CreateSqlInjectionMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_sql_injection_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_sql_injection_match_set.async_create_sql_injection_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_sql_injection_match_set_request.CreateSqlInjectionMatchSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_web_acl(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        metric_name: "capo_waf.types.metric_name.MetricName",
        default_action: "capo_waf.types.waf_action.WafAction",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        tags: Optional["capo_waf.types.tag_list.TagList"] = None,
    ) -> "capo_waf.types.create_web_acl_response.CreateWebACLResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates a <code>WebACL</code>, which contains the <code>Rules</code> that identify the CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates <code>Rules</code> in order based on the value of <code>Priority</code> for each <code>Rule</code>.</p> <p>You also specify a default action, either <code>ALLOW</code> or <code>BLOCK</code>. If a web request doesn't match any of the <code>Rules</code> in a <code>WebACL</code>, AWS WAF responds to the request with the default action. </p> <p>To create and configure a <code>WebACL</code>, perform the following steps:</p> <ol> <li> <p>Create and update the <code>ByteMatchSet</code> objects and other predicates that you want to include in <code>Rules</code>. For more information, see <a>CreateByteMatchSet</a>, <a>UpdateByteMatchSet</a>, <a>CreateIPSet</a>, <a>UpdateIPSet</a>, <a>CreateSqlInjectionMatchSet</a>, and <a>UpdateSqlInjectionMatchSet</a>.</p> </li> <li> <p>Create and update the <code>Rules</code> that you want to include in the <code>WebACL</code>. For more information, see <a>CreateRule</a> and <a>UpdateRule</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateWebACL</code> request.</p> </li> <li> <p>Submit a <code>CreateWebACL</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateWebACL</a> request.</p> </li> <li> <p>Submit an <a>UpdateWebACL</a> request to specify the <code>Rules</code> that you want to include in the <code>WebACL</code>, to specify the default action, and to associate the <code>WebACL</code> with a CloudFront distribution.</p> </li> </ol> <p>For more information about how to use the AWS WAF API, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description of the <a>WebACL</a>. You can't change <code>Name</code> after you create the <code>WebACL</code>.</p>
            metric_name: <p>A friendly name or description for the metrics for this <code>WebACL</code>.The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change <code>MetricName</code> after you create the <code>WebACL</code>.</p>
            default_action: <p>The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the <code>Rule</code> objects that are associated with the <code>WebACL</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            tags: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a web ACL
            The following example creates a web ACL named CreateExample.

            >>> await client.create_web_acl(name='CreateExample', metric_name='CreateExample', default_action={'Type': 'ALLOW'}, change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_web_acl_request.CreateWebACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_web_acl_response.CreateWebACLResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_web_acl

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_web_acl.async_create_web_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_web_acl_request.CreateWebACLRequest = {
            "name": name,
            "metric_name": metric_name,
            "default_action": default_action,
            "change_token": change_token,
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

    async def create_web_acl_migration_stack(
        self,
        web_acl_id: "capo_waf.types.resource_id.ResourceId",
        s3_bucket_name: "capo_waf.types.s3_bucket_name.S3BucketName",
        ignore_unsupported_type: "capo_waf.types.ignore_unsupported_type.IgnoreUnsupportedType",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_web_acl_migration_stack_response.CreateWebACLMigrationStackResponse":
        """<p>Creates an AWS CloudFormation WAFV2 template for the specified web ACL in the specified Amazon S3 bucket. Then, in CloudFormation, you create a stack from the template, to create the web ACL and its resources in AWS WAFV2. Use this to migrate your AWS WAF Classic web ACL to the latest version of AWS WAF.</p> <p>This is part of a larger migration procedure for web ACLs from AWS WAF Classic to the latest version of AWS WAF. For the full procedure, including caveats and manual steps to complete the migration and switch over to the new web ACL, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html">Migrating your AWS WAF Classic resources to AWS WAF</a> in the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. </p>

        Args:
            web_acl_id: <p>The UUID of the WAF Classic web ACL that you want to migrate to WAF v2.</p>
            s3_bucket_name: <p>The name of the Amazon S3 bucket to store the CloudFormation template in. The S3 bucket must be configured as follows for the migration: </p> <ul> <li> <p>The bucket name must start with <code>aws-waf-migration-</code>. For example, <code>aws-waf-migration-my-web-acl</code>.</p> </li> <li> <p>The bucket must be in the Region where you are deploying the template. For example, for a web ACL in us-west-2, you must use an Amazon S3 bucket in us-west-2 and you must deploy the template stack to us-west-2. </p> </li> <li> <p>The bucket policies must permit the migration process to write data. For listings of the bucket policies, see the Examples section. </p> </li> </ul>
            ignore_unsupported_type: <p>Indicates whether to exclude entities that can't be migrated or to stop the migration. Set this to true to ignore unsupported entities in the web ACL during the migration. Otherwise, if AWS WAF encounters unsupported entities, it stops the process and throws an exception. </p>

        Raises:
            capo_waf.errors.waf_entity_migration_exception.WAFEntityMigrationException: <p>The operation failed due to a problem with the migration. The failure cause is provided in the exception, in the <code>MigrationErrorType</code>: </p> <ul> <li> <p> <code>ENTITY_NOT_SUPPORTED</code> - The web ACL has an unsupported entity but the <code>IgnoreUnsupportedType</code> is not set to true.</p> </li> <li> <p> <code>ENTITY_NOT_FOUND</code> - The web ACL doesn't exist. </p> </li> <li> <p> <code>S3_BUCKET_NO_PERMISSION</code> - You don't have permission to perform the <code>PutObject</code> action to the specified Amazon S3 bucket.</p> </li> <li> <p> <code>S3_BUCKET_NOT_ACCESSIBLE</code> - The bucket policy doesn't allow AWS WAF to perform the <code>PutObject</code> action in the bucket.</p> </li> <li> <p> <code>S3_BUCKET_NOT_FOUND</code> - The S3 bucket doesn't exist. </p> </li> <li> <p> <code>S3_BUCKET_INVALID_REGION</code> - The S3 bucket is not in the same Region as the web ACL.</p> </li> <li> <p> <code>S3_INTERNAL_ERROR</code> - AWS WAF failed to create the template in the S3 bucket for another reason.</p> </li> </ul>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_web_acl_migration_stack_request.CreateWebACLMigrationStackRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_web_acl_migration_stack_response.CreateWebACLMigrationStackResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_web_acl_migration_stack

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_web_acl_migration_stack.async_create_web_acl_migration_stack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_web_acl_migration_stack_request.CreateWebACLMigrationStackRequest = {
            "web_acl_id": web_acl_id,
            "s3_bucket_name": s3_bucket_name,
            "ignore_unsupported_type": ignore_unsupported_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_xss_match_set(
        self,
        name: "capo_waf.types.resource_name.ResourceName",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.create_xss_match_set_response.CreateXssMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Creates an <a>XssMatchSet</a>, which you use to allow, block, or count requests that contain cross-site scripting attacks in the specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.</p> <p>To create and configure an <code>XssMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>CreateXssMatchSet</code> request.</p> </li> <li> <p>Submit a <code>CreateXssMatchSet</code> request.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateXssMatchSet</a> request.</p> </li> <li> <p>Submit an <a>UpdateXssMatchSet</a> request to specify the parts of web requests in which you want to allow, block, or count cross-site scripting attacks.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            name: <p>A friendly name or description for the <a>XssMatchSet</a> that you're creating. You can't change <code>Name</code> after you create the <code>XssMatchSet</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an XSS match set
            The following example creates an XSS match set named MySampleXssMatchSet.

            >>> await client.create_xss_match_set(name='MySampleXssMatchSet', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.create_xss_match_set_request.CreateXssMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.create_xss_match_set_response.CreateXssMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.create_xss_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.create_xss_match_set.async_create_xss_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.create_xss_match_set_request.CreateXssMatchSetRequest = {
            "name": name,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_byte_match_set(
        self,
        byte_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_byte_match_set_response.DeleteByteMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>ByteMatchSet</a>. You can't delete a <code>ByteMatchSet</code> if it's still used in any <code>Rules</code> or if it still includes any <a>ByteMatchTuple</a> objects (any filters).</p> <p>If you just want to remove a <code>ByteMatchSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete a <code>ByteMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Update the <code>ByteMatchSet</code> to remove filters, if any. For more information, see <a>UpdateByteMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteByteMatchSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteByteMatchSet</code> request.</p> </li> </ol>

        Args:
            byte_match_set_id: <p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to delete. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a byte match set
            The following example deletes a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.delete_byte_match_set(byte_match_set_id='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_byte_match_set_request.DeleteByteMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_byte_match_set_response.DeleteByteMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_byte_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_byte_match_set.async_delete_byte_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_byte_match_set_request.DeleteByteMatchSetRequest = {
            "byte_match_set_id": byte_match_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_geo_match_set(
        self,
        geo_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_geo_match_set_response.DeleteGeoMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>GeoMatchSet</a>. You can't delete a <code>GeoMatchSet</code> if it's still used in any <code>Rules</code> or if it still includes any countries.</p> <p>If you just want to remove a <code>GeoMatchSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete a <code>GeoMatchSet</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>GeoMatchSet</code> to remove any countries. For more information, see <a>UpdateGeoMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteGeoMatchSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteGeoMatchSet</code> request.</p> </li> </ol>

        Args:
            geo_match_set_id: <p>The <code>GeoMatchSetID</code> of the <a>GeoMatchSet</a> that you want to delete. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_geo_match_set_request.DeleteGeoMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_geo_match_set_response.DeleteGeoMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_geo_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_geo_match_set.async_delete_geo_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_geo_match_set_request.DeleteGeoMatchSetRequest = {
            "geo_match_set_id": geo_match_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ip_set(
        self,
        ip_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_ip_set_response.DeleteIPSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes an <a>IPSet</a>. You can't delete an <code>IPSet</code> if it's still used in any <code>Rules</code> or if it still includes any IP addresses.</p> <p>If you just want to remove an <code>IPSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete an <code>IPSet</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>IPSet</code> to remove IP address ranges, if any. For more information, see <a>UpdateIPSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteIPSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteIPSet</code> request.</p> </li> </ol>

        Args:
            ip_set_id: <p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to delete. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an IP set
            The following example deletes an IP match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.delete_ip_set(ip_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_ip_set_request.DeleteIPSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_ip_set_response.DeleteIPSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_ip_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_ip_set.async_delete_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_ip_set_request.DeleteIPSetRequest = {
            "ip_set_id": ip_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_logging_configuration(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_logging_configuration_response.DeleteLoggingConfigurationResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes the <a>LoggingConfiguration</a> from the specified web ACL.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web ACL from which you want to delete the <a>LoggingConfiguration</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_logging_configuration_response.DeleteLoggingConfigurationResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_logging_configuration

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_logging_configuration.async_delete_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_permission_policy(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_permission_policy_response.DeletePermissionPolicyResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes an IAM policy from the specified RuleGroup.</p> <p>The user making the request must be the owner of the RuleGroup.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the RuleGroup from which you want to delete the policy.</p> <p>The user making the request must be the owner of the RuleGroup.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_permission_policy_request.DeletePermissionPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_permission_policy_response.DeletePermissionPolicyResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_permission_policy

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_permission_policy.async_delete_permission_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_permission_policy_request.DeletePermissionPolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rate_based_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_rate_based_rule_response.DeleteRateBasedRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>RateBasedRule</a>. You can't delete a rule if it's still used in any <code>WebACL</code> objects or if it still includes any predicates, such as <code>ByteMatchSet</code> objects.</p> <p>If you just want to remove a rule from a <code>WebACL</code>, use <a>UpdateWebACL</a>.</p> <p>To permanently delete a <code>RateBasedRule</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>RateBasedRule</code> to remove predicates, if any. For more information, see <a>UpdateRateBasedRule</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteRateBasedRule</code> request.</p> </li> <li> <p>Submit a <code>DeleteRateBasedRule</code> request.</p> </li> </ol>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <a>RateBasedRule</a> that you want to delete. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_rate_based_rule_request.DeleteRateBasedRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_rate_based_rule_response.DeleteRateBasedRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_rate_based_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_rate_based_rule.async_delete_rate_based_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_rate_based_rule_request.DeleteRateBasedRuleRequest = {
            "rule_id": rule_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_regex_match_set(
        self,
        regex_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_regex_match_set_response.DeleteRegexMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>RegexMatchSet</a>. You can't delete a <code>RegexMatchSet</code> if it's still used in any <code>Rules</code> or if it still includes any <code>RegexMatchTuples</code> objects (any filters).</p> <p>If you just want to remove a <code>RegexMatchSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete a <code>RegexMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Update the <code>RegexMatchSet</code> to remove filters, if any. For more information, see <a>UpdateRegexMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteRegexMatchSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteRegexMatchSet</code> request.</p> </li> </ol>

        Args:
            regex_match_set_id: <p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to delete. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_regex_match_set_request.DeleteRegexMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_regex_match_set_response.DeleteRegexMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_regex_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_regex_match_set.async_delete_regex_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_regex_match_set_request.DeleteRegexMatchSetRequest = {
            "regex_match_set_id": regex_match_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_regex_pattern_set(
        self,
        regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> (
        "capo_waf.types.delete_regex_pattern_set_response.DeleteRegexPatternSetResponse"
    ):
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>RegexPatternSet</a>. You can't delete a <code>RegexPatternSet</code> if it's still used in any <code>RegexMatchSet</code> or if the <code>RegexPatternSet</code> is not empty. </p>

        Args:
            regex_pattern_set_id: <p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to delete. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_regex_pattern_set_request.DeleteRegexPatternSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_regex_pattern_set_response.DeleteRegexPatternSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_regex_pattern_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_regex_pattern_set.async_delete_regex_pattern_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_regex_pattern_set_request.DeleteRegexPatternSetRequest = {
            "regex_pattern_set_id": regex_pattern_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_rule_response.DeleteRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>Rule</a>. You can't delete a <code>Rule</code> if it's still used in any <code>WebACL</code> objects or if it still includes any predicates, such as <code>ByteMatchSet</code> objects.</p> <p>If you just want to remove a <code>Rule</code> from a <code>WebACL</code>, use <a>UpdateWebACL</a>.</p> <p>To permanently delete a <code>Rule</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>Rule</code> to remove predicates, if any. For more information, see <a>UpdateRule</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteRule</code> request.</p> </li> <li> <p>Submit a <code>DeleteRule</code> request.</p> </li> </ol>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <a>Rule</a> that you want to delete. <code>RuleId</code> is returned by <a>CreateRule</a> and by <a>ListRules</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a rule
            The following example deletes a rule with the ID WAFRule-1-Example.

            >>> await client.delete_rule(rule_id='WAFRule-1-Example', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_rule_request.DeleteRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_rule_request.DeleteRuleRequest = {
            "rule_id": rule_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule_group(
        self,
        rule_group_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_rule_group_response.DeleteRuleGroupResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>RuleGroup</a>. You can't delete a <code>RuleGroup</code> if it's still used in any <code>WebACL</code> objects or if it still includes any rules.</p> <p>If you just want to remove a <code>RuleGroup</code> from a <code>WebACL</code>, use <a>UpdateWebACL</a>.</p> <p>To permanently delete a <code>RuleGroup</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>RuleGroup</code> to remove rules, if any. For more information, see <a>UpdateRuleGroup</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteRuleGroup</code> request.</p> </li> <li> <p>Submit a <code>DeleteRuleGroup</code> request.</p> </li> </ol>

        Args:
            rule_group_id: <p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to delete. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_rule_group_request.DeleteRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_rule_group_response.DeleteRuleGroupResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_rule_group

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_rule_group.async_delete_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_rule_group_request.DeleteRuleGroupRequest = {
            "rule_group_id": rule_group_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_size_constraint_set(
        self,
        size_constraint_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_size_constraint_set_response.DeleteSizeConstraintSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>SizeConstraintSet</a>. You can't delete a <code>SizeConstraintSet</code> if it's still used in any <code>Rules</code> or if it still includes any <a>SizeConstraint</a> objects (any filters).</p> <p>If you just want to remove a <code>SizeConstraintSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete a <code>SizeConstraintSet</code>, perform the following steps:</p> <ol> <li> <p>Update the <code>SizeConstraintSet</code> to remove filters, if any. For more information, see <a>UpdateSizeConstraintSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteSizeConstraintSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteSizeConstraintSet</code> request.</p> </li> </ol>

        Args:
            size_constraint_set_id: <p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to delete. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a size constraint set
            The following example deletes a size constraint set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.delete_size_constraint_set(size_constraint_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_size_constraint_set_request.DeleteSizeConstraintSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_size_constraint_set_response.DeleteSizeConstraintSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_size_constraint_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_size_constraint_set.async_delete_size_constraint_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_size_constraint_set_request.DeleteSizeConstraintSetRequest = {
            "size_constraint_set_id": size_constraint_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sql_injection_match_set(
        self,
        sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_sql_injection_match_set_response.DeleteSqlInjectionMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>SqlInjectionMatchSet</a>. You can't delete a <code>SqlInjectionMatchSet</code> if it's still used in any <code>Rules</code> or if it still contains any <a>SqlInjectionMatchTuple</a> objects.</p> <p>If you just want to remove a <code>SqlInjectionMatchSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete a <code>SqlInjectionMatchSet</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>SqlInjectionMatchSet</code> to remove filters, if any. For more information, see <a>UpdateSqlInjectionMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteSqlInjectionMatchSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteSqlInjectionMatchSet</code> request.</p> </li> </ol>

        Args:
            sql_injection_match_set_id: <p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to delete. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a SQL injection match set
            The following example deletes a SQL injection match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.delete_sql_injection_match_set(sql_injection_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_sql_injection_match_set_request.DeleteSqlInjectionMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_sql_injection_match_set_response.DeleteSqlInjectionMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_sql_injection_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_sql_injection_match_set.async_delete_sql_injection_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_sql_injection_match_set_request.DeleteSqlInjectionMatchSetRequest = {
            "sql_injection_match_set_id": sql_injection_match_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_acl(
        self,
        web_acl_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_web_acl_response.DeleteWebACLResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes a <a>WebACL</a>. You can't delete a <code>WebACL</code> if it still contains any <code>Rules</code>.</p> <p>To delete a <code>WebACL</code>, perform the following steps:</p> <ol> <li> <p>Update the <code>WebACL</code> to remove <code>Rules</code>, if any. For more information, see <a>UpdateWebACL</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteWebACL</code> request.</p> </li> <li> <p>Submit a <code>DeleteWebACL</code> request.</p> </li> </ol>

        Args:
            web_acl_id: <p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to delete. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a web ACL
            The following example deletes a web ACL with the ID example-46da-4444-5555-example.

            >>> await client.delete_web_acl(web_acl_id='example-46da-4444-5555-example', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_web_acl_request.DeleteWebACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_web_acl_response.DeleteWebACLResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_web_acl

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_web_acl.async_delete_web_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_web_acl_request.DeleteWebACLRequest = {
            "web_acl_id": web_acl_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_xss_match_set(
        self,
        xss_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.delete_xss_match_set_response.DeleteXssMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Permanently deletes an <a>XssMatchSet</a>. You can't delete an <code>XssMatchSet</code> if it's still used in any <code>Rules</code> or if it still contains any <a>XssMatchTuple</a> objects.</p> <p>If you just want to remove an <code>XssMatchSet</code> from a <code>Rule</code>, use <a>UpdateRule</a>.</p> <p>To permanently delete an <code>XssMatchSet</code> from AWS WAF, perform the following steps:</p> <ol> <li> <p>Update the <code>XssMatchSet</code> to remove filters, if any. For more information, see <a>UpdateXssMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of a <code>DeleteXssMatchSet</code> request.</p> </li> <li> <p>Submit a <code>DeleteXssMatchSet</code> request.</p> </li> </ol>

        Args:
            xss_match_set_id: <p>The <code>XssMatchSetId</code> of the <a>XssMatchSet</a> that you want to delete. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_non_empty_entity_exception.WAFNonEmptyEntityException: <p>The operation failed because you tried to delete an object that isn't empty. For example:</p> <ul> <li> <p>You tried to delete a <code>WebACL</code> that still contains one or more <code>Rule</code> objects.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that still contains one or more <code>ByteMatchSet</code> objects or other predicates.</p> </li> <li> <p>You tried to delete a <code>ByteMatchSet</code> that contains one or more <code>ByteMatchTuple</code> objects.</p> </li> <li> <p>You tried to delete an <code>IPSet</code> that references one or more IP addresses.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an XSS match set
            The following example deletes an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.delete_xss_match_set(xss_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.delete_xss_match_set_request.DeleteXssMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.delete_xss_match_set_response.DeleteXssMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.delete_xss_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.delete_xss_match_set.async_delete_xss_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.delete_xss_match_set_request.DeleteXssMatchSetRequest = {
            "xss_match_set_id": xss_match_set_id,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_byte_match_set(
        self,
        byte_match_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_byte_match_set_response.GetByteMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>ByteMatchSet</a> specified by <code>ByteMatchSetId</code>.</p>

        Args:
            byte_match_set_id: <p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to get. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a byte match set
            The following example returns the details of a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_byte_match_set(byte_match_set_id='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_byte_match_set_request.GetByteMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_byte_match_set_response.GetByteMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_byte_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_byte_match_set.async_get_byte_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_byte_match_set_request.GetByteMatchSetRequest = {
            "byte_match_set_id": byte_match_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_change_token(
        self, *, config_overrides: Optional[AsyncWAFClientConfig] = None
    ) -> "capo_waf.types.get_change_token_response.GetChangeTokenResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn't submit conflicting requests to AWS WAF.</p> <p>Each create, update, or delete request must use a unique change token. If your application submits a <code>GetChangeToken</code> request and then submits a second <code>GetChangeToken</code> request before submitting a create, update, or delete request, the second <code>GetChangeToken</code> request returns the same value as the first <code>GetChangeToken</code> request.</p> <p>When you use a change token in a create, update, or delete request, the status of the change token changes to <code>PENDING</code>, which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use <code>GetChangeTokenStatus</code> to determine the status of your change token.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a change token
            The following example returns a change token to use for a create, update or delete operation.

            >>> await client.get_change_token()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_change_token_request.GetChangeTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_change_token_response.GetChangeTokenResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_change_token

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_change_token.async_get_change_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_change_token_request.GetChangeTokenRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_change_token_status(
        self,
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_change_token_status_response.GetChangeTokenStatusResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the status of a <code>ChangeToken</code> that you got by calling <a>GetChangeToken</a>. <code>ChangeTokenStatus</code> is one of the following values:</p> <ul> <li> <p> <code>PROVISIONED</code>: You requested the change token by calling <code>GetChangeToken</code>, but you haven't used it yet in a call to create, update, or delete an AWS WAF object.</p> </li> <li> <p> <code>PENDING</code>: AWS WAF is propagating the create, update, or delete request to all AWS WAF servers.</p> </li> <li> <p> <code>INSYNC</code>: Propagation is complete.</p> </li> </ul>

        Args:
            change_token: <p>The change token for which you want to get the status. This change token was previously returned in the <code>GetChangeToken</code> response.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the change token status
            The following example returns the status of a change token with the ID abcd12f2-46da-4fdb-b8d5-fbd4c466928f.

            >>> await client.get_change_token_status(change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_change_token_status_request.GetChangeTokenStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_change_token_status_response.GetChangeTokenStatusResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_change_token_status

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_change_token_status.async_get_change_token_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_change_token_status_request.GetChangeTokenStatusRequest = {
            "change_token": change_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_geo_match_set(
        self,
        geo_match_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_geo_match_set_response.GetGeoMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>GeoMatchSet</a> that is specified by <code>GeoMatchSetId</code>.</p>

        Args:
            geo_match_set_id: <p>The <code>GeoMatchSetId</code> of the <a>GeoMatchSet</a> that you want to get. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_geo_match_set_request.GetGeoMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_geo_match_set_response.GetGeoMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_geo_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_geo_match_set.async_get_geo_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_geo_match_set_request.GetGeoMatchSetRequest = {
            "geo_match_set_id": geo_match_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ip_set(
        self,
        ip_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_ip_set_response.GetIPSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>IPSet</a> that is specified by <code>IPSetId</code>.</p>

        Args:
            ip_set_id: <p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to get. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an IP set
            The following example returns the details of an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_ip_set(ip_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_ip_set_request.GetIPSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_ip_set_response.GetIPSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_ip_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_ip_set.async_get_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_ip_set_request.GetIPSetRequest = {
            "ip_set_id": ip_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_logging_configuration(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_logging_configuration_response.GetLoggingConfigurationResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>LoggingConfiguration</a> for the specified web ACL.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web ACL for which you want to get the <a>LoggingConfiguration</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_logging_configuration_request.GetLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_logging_configuration_response.GetLoggingConfigurationResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_logging_configuration

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_logging_configuration.async_get_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_logging_configuration_request.GetLoggingConfigurationRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_permission_policy(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_permission_policy_response.GetPermissionPolicyResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the IAM policy attached to the RuleGroup.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_permission_policy_request.GetPermissionPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_permission_policy_response.GetPermissionPolicyResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_permission_policy

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_permission_policy.async_get_permission_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_permission_policy_request.GetPermissionPolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rate_based_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_rate_based_rule_response.GetRateBasedRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>RateBasedRule</a> that is specified by the <code>RuleId</code> that you included in the <code>GetRateBasedRule</code> request.</p>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <a>RateBasedRule</a> that you want to get. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_rate_based_rule_request.GetRateBasedRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_rate_based_rule_response.GetRateBasedRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_rate_based_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_rate_based_rule.async_get_rate_based_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_rate_based_rule_request.GetRateBasedRuleRequest = {
            "rule_id": rule_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rate_based_rule_managed_keys(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
    ) -> "capo_waf.types.get_rate_based_rule_managed_keys_response.GetRateBasedRuleManagedKeysResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of IP addresses currently being blocked by the <a>RateBasedRule</a> that is specified by the <code>RuleId</code>. The maximum number of managed keys that will be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the 10,000 addresses with the highest rates will be blocked.</p>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <a>RateBasedRule</a> for which you want to get a list of <code>ManagedKeys</code>. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>
            next_marker: <p>A null value and not currently used. Do not include this in your request.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_rate_based_rule_managed_keys_request.GetRateBasedRuleManagedKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_rate_based_rule_managed_keys_response.GetRateBasedRuleManagedKeysResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_rate_based_rule_managed_keys

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_rate_based_rule_managed_keys.async_get_rate_based_rule_managed_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_rate_based_rule_managed_keys_request.GetRateBasedRuleManagedKeysRequest = {
            "rule_id": rule_id
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_regex_match_set(
        self,
        regex_match_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_regex_match_set_response.GetRegexMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>RegexMatchSet</a> specified by <code>RegexMatchSetId</code>.</p>

        Args:
            regex_match_set_id: <p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to get. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_regex_match_set_request.GetRegexMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_regex_match_set_response.GetRegexMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_regex_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_regex_match_set.async_get_regex_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_regex_match_set_request.GetRegexMatchSetRequest = {
            "regex_match_set_id": regex_match_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_regex_pattern_set(
        self,
        regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_regex_pattern_set_response.GetRegexPatternSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>RegexPatternSet</a> specified by <code>RegexPatternSetId</code>.</p>

        Args:
            regex_pattern_set_id: <p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to get. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_regex_pattern_set_request.GetRegexPatternSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_regex_pattern_set_response.GetRegexPatternSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_regex_pattern_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_regex_pattern_set.async_get_regex_pattern_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_regex_pattern_set_request.GetRegexPatternSetRequest = {
            "regex_pattern_set_id": regex_pattern_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_rule_response.GetRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>Rule</a> that is specified by the <code>RuleId</code> that you included in the <code>GetRule</code> request.</p>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <a>Rule</a> that you want to get. <code>RuleId</code> is returned by <a>CreateRule</a> and by <a>ListRules</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a rule
            The following example returns the details of a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_rule(rule_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_rule_request.GetRuleRequest]",
        ) -> AsyncOperationResponse["capo_waf.types.get_rule_response.GetRuleResponse"]:
            import capo_waf._operations.awswaf_20150824.get_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_rule_request.GetRuleRequest = {"rule_id": rule_id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rule_group(
        self,
        rule_group_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_rule_group_response.GetRuleGroupResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>RuleGroup</a> that is specified by the <code>RuleGroupId</code> that you included in the <code>GetRuleGroup</code> request.</p> <p>To view the rules in a rule group, use <a>ListActivatedRulesInRuleGroup</a>.</p>

        Args:
            rule_group_id: <p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to get. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_rule_group_request.GetRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_rule_group_response.GetRuleGroupResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_rule_group

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_rule_group.async_get_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_rule_group_request.GetRuleGroupRequest = {
            "rule_group_id": rule_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sampled_requests(
        self,
        web_acl_id: "capo_waf.types.resource_id.ResourceId",
        rule_id: "capo_waf.types.resource_id.ResourceId",
        time_window: "capo_waf.types.time_window.TimeWindow",
        max_items: "capo_waf.types.get_sampled_requests_max_items.GetSampledRequestsMaxItems",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_sampled_requests_response.GetSampledRequestsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.</p> <p> <code>GetSampledRequests</code> returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, <code>GetSampledRequests</code> returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.</p>

        Args:
            web_acl_id: <p>The <code>WebACLId</code> of the <code>WebACL</code> for which you want <code>GetSampledRequests</code> to return a sample of requests.</p>
            rule_id: <p> <code>RuleId</code> is one of three values:</p> <ul> <li> <p>The <code>RuleId</code> of the <code>Rule</code> or the <code>RuleGroupId</code> of the <code>RuleGroup</code> for which you want <code>GetSampledRequests</code> to return a sample of requests.</p> </li> <li> <p> <code>Default_Action</code>, which causes <code>GetSampledRequests</code> to return a sample of the requests that didn't match any of the rules in the specified <code>WebACL</code>.</p> </li> </ul>
            time_window: <p>The start date and time and the end date and time of the range for which you want <code>GetSampledRequests</code> to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours.</p>
            max_items: <p>The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of <code>MaxItems</code>, <code>GetSampledRequests</code> returns information about all of them. </p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_sampled_requests_request.GetSampledRequestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_sampled_requests_response.GetSampledRequestsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_sampled_requests

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_sampled_requests.async_get_sampled_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_sampled_requests_request.GetSampledRequestsRequest = {
            "web_acl_id": web_acl_id,
            "rule_id": rule_id,
            "time_window": time_window,
            "max_items": max_items,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_size_constraint_set(
        self,
        size_constraint_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_size_constraint_set_response.GetSizeConstraintSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>SizeConstraintSet</a> specified by <code>SizeConstraintSetId</code>.</p>

        Args:
            size_constraint_set_id: <p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to get. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a size constraint set
            The following example returns the details of a size constraint match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_size_constraint_set(size_constraint_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_size_constraint_set_request.GetSizeConstraintSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_size_constraint_set_response.GetSizeConstraintSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_size_constraint_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_size_constraint_set.async_get_size_constraint_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_size_constraint_set_request.GetSizeConstraintSetRequest = {
            "size_constraint_set_id": size_constraint_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sql_injection_match_set(
        self,
        sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_sql_injection_match_set_response.GetSqlInjectionMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>SqlInjectionMatchSet</a> that is specified by <code>SqlInjectionMatchSetId</code>.</p>

        Args:
            sql_injection_match_set_id: <p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to get. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a SQL injection match set
            The following example returns the details of a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_sql_injection_match_set(sql_injection_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_sql_injection_match_set_request.GetSqlInjectionMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_sql_injection_match_set_response.GetSqlInjectionMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_sql_injection_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_sql_injection_match_set.async_get_sql_injection_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_sql_injection_match_set_request.GetSqlInjectionMatchSetRequest = {
            "sql_injection_match_set_id": sql_injection_match_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_acl(
        self,
        web_acl_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_web_acl_response.GetWebACLResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>WebACL</a> that is specified by <code>WebACLId</code>.</p>

        Args:
            web_acl_id: <p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to get. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a web ACL
            The following example returns the details of a web ACL with the ID createwebacl-1472061481310.

            >>> await client.get_web_acl(web_acl_id='createwebacl-1472061481310')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_web_acl_request.GetWebACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_web_acl_response.GetWebACLResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_web_acl

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_web_acl.async_get_web_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_web_acl_request.GetWebACLRequest = {
            "web_acl_id": web_acl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_xss_match_set(
        self,
        xss_match_set_id: "capo_waf.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.get_xss_match_set_response.GetXssMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns the <a>XssMatchSet</a> that is specified by <code>XssMatchSetId</code>.</p>

        Args:
            xss_match_set_id: <p>The <code>XssMatchSetId</code> of the <a>XssMatchSet</a> that you want to get. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an XSS match set
            The following example returns the details of an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.get_xss_match_set(xss_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.get_xss_match_set_request.GetXssMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.get_xss_match_set_response.GetXssMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.get_xss_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.get_xss_match_set.async_get_xss_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.get_xss_match_set_request.GetXssMatchSetRequest = {
            "xss_match_set_id": xss_match_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_activated_rules_in_rule_group(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        rule_group_id: Optional["capo_waf.types.resource_id.ResourceId"] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_activated_rules_in_rule_group_response.ListActivatedRulesInRuleGroupResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>ActivatedRule</a> objects.</p>

        Args:
            rule_group_id: <p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> for which you want to get a list of <a>ActivatedRule</a> objects.</p>
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>ActivatedRules</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>ActivatedRules</code>. For the second and subsequent <code>ListActivatedRulesInRuleGroup</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>ActivatedRules</code>.</p>
            limit: <p>Specifies the number of <code>ActivatedRules</code> that you want AWS WAF to return for this request. If you have more <code>ActivatedRules</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>ActivatedRules</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_activated_rules_in_rule_group_request.ListActivatedRulesInRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_activated_rules_in_rule_group_response.ListActivatedRulesInRuleGroupResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_activated_rules_in_rule_group

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_activated_rules_in_rule_group.async_list_activated_rules_in_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_activated_rules_in_rule_group_request.ListActivatedRulesInRuleGroupRequest = {}
        if rule_group_id is not None:
            input_["rule_group_id"] = rule_group_id
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_byte_match_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_byte_match_sets_response.ListByteMatchSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>ByteMatchSetSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>ByteMatchSets</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>ByteMatchSets</code>. For the second and subsequent <code>ListByteMatchSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>ByteMatchSets</code>.</p>
            limit: <p>Specifies the number of <code>ByteMatchSet</code> objects that you want AWS WAF to return for this request. If you have more <code>ByteMatchSets</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>ByteMatchSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_byte_match_sets_request.ListByteMatchSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_byte_match_sets_response.ListByteMatchSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_byte_match_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_byte_match_sets.async_list_byte_match_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_byte_match_sets_request.ListByteMatchSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_geo_match_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_geo_match_sets_response.ListGeoMatchSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>GeoMatchSetSummary</a> objects in the response.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>GeoMatchSet</code>s than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>GeoMatchSet</code> objects. For the second and subsequent <code>ListGeoMatchSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>GeoMatchSet</code> objects.</p>
            limit: <p>Specifies the number of <code>GeoMatchSet</code> objects that you want AWS WAF to return for this request. If you have more <code>GeoMatchSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>GeoMatchSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_geo_match_sets_request.ListGeoMatchSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_geo_match_sets_response.ListGeoMatchSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_geo_match_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_geo_match_sets.async_list_geo_match_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_geo_match_sets_request.ListGeoMatchSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ip_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_ip_sets_response.ListIPSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>IPSetSummary</a> objects in the response.</p>

        Args:
            next_marker: <p>AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>IPSets</code>. For the second and subsequent <code>ListIPSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>IPSets</code>.</p>
            limit: <p>Specifies the number of <code>IPSet</code> objects that you want AWS WAF to return for this request. If you have more <code>IPSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>IPSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list IP sets
            The following example returns an array of up to 100 IP match sets.

            >>> await client.list_ip_sets(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_ip_sets_request.ListIPSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_ip_sets_response.ListIPSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_ip_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_ip_sets.async_list_ip_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_ip_sets_request.ListIPSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_logging_configurations(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_logging_configurations_response.ListLoggingConfigurationsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>LoggingConfiguration</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>LoggingConfigurations</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>LoggingConfigurations</code>. For the second and subsequent <code>ListLoggingConfigurations</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>ListLoggingConfigurations</code>.</p>
            limit: <p>Specifies the number of <code>LoggingConfigurations</code> that you want AWS WAF to return for this request. If you have more <code>LoggingConfigurations</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>LoggingConfigurations</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_logging_configurations_request.ListLoggingConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_logging_configurations_response.ListLoggingConfigurationsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_logging_configurations

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_logging_configurations.async_list_logging_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_logging_configurations_request.ListLoggingConfigurationsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rate_based_rules(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_rate_based_rules_response.ListRateBasedRulesResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RuleSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>Rules</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>Rules</code>. For the second and subsequent <code>ListRateBasedRules</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>Rules</code>.</p>
            limit: <p>Specifies the number of <code>Rules</code> that you want AWS WAF to return for this request. If you have more <code>Rules</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>Rules</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_rate_based_rules_request.ListRateBasedRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_rate_based_rules_response.ListRateBasedRulesResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_rate_based_rules

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_rate_based_rules.async_list_rate_based_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_rate_based_rules_request.ListRateBasedRulesRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_regex_match_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_regex_match_sets_response.ListRegexMatchSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RegexMatchSetSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>RegexMatchSet</code> objects than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>ByteMatchSets</code>. For the second and subsequent <code>ListRegexMatchSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>RegexMatchSet</code> objects.</p>
            limit: <p>Specifies the number of <code>RegexMatchSet</code> objects that you want AWS WAF to return for this request. If you have more <code>RegexMatchSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>RegexMatchSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_regex_match_sets_request.ListRegexMatchSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_regex_match_sets_response.ListRegexMatchSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_regex_match_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_regex_match_sets.async_list_regex_match_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_regex_match_sets_request.ListRegexMatchSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_regex_pattern_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_regex_pattern_sets_response.ListRegexPatternSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RegexPatternSetSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>RegexPatternSet</code> objects than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>RegexPatternSet</code> objects. For the second and subsequent <code>ListRegexPatternSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>RegexPatternSet</code> objects.</p>
            limit: <p>Specifies the number of <code>RegexPatternSet</code> objects that you want AWS WAF to return for this request. If you have more <code>RegexPatternSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>RegexPatternSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_regex_pattern_sets_request.ListRegexPatternSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_regex_pattern_sets_response.ListRegexPatternSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_regex_pattern_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_regex_pattern_sets.async_list_regex_pattern_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_regex_pattern_sets_request.ListRegexPatternSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rule_groups(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_rule_groups_response.ListRuleGroupsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RuleGroup</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>RuleGroups</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>RuleGroups</code>. For the second and subsequent <code>ListRuleGroups</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>RuleGroups</code>.</p>
            limit: <p>Specifies the number of <code>RuleGroups</code> that you want AWS WAF to return for this request. If you have more <code>RuleGroups</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>RuleGroups</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_rule_groups_request.ListRuleGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_rule_groups_response.ListRuleGroupsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_rule_groups

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_rule_groups.async_list_rule_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_rule_groups_request.ListRuleGroupsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rules(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_rules_response.ListRulesResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RuleSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>Rules</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>Rules</code>. For the second and subsequent <code>ListRules</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>Rules</code>.</p>
            limit: <p>Specifies the number of <code>Rules</code> that you want AWS WAF to return for this request. If you have more <code>Rules</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>Rules</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list rules
            The following example returns an array of up to 100 rules.

            >>> await client.list_rules(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_rules

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_rules_request.ListRulesRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_size_constraint_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_size_constraint_sets_response.ListSizeConstraintSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>SizeConstraintSetSummary</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>SizeConstraintSets</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>SizeConstraintSets</code>. For the second and subsequent <code>ListSizeConstraintSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>SizeConstraintSets</code>.</p>
            limit: <p>Specifies the number of <code>SizeConstraintSet</code> objects that you want AWS WAF to return for this request. If you have more <code>SizeConstraintSets</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>SizeConstraintSet</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list a size constraint sets
            The following example returns an array of up to 100 size contraint match sets.

            >>> await client.list_size_constraint_sets(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_size_constraint_sets_request.ListSizeConstraintSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_size_constraint_sets_response.ListSizeConstraintSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_size_constraint_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_size_constraint_sets.async_list_size_constraint_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_size_constraint_sets_request.ListSizeConstraintSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sql_injection_match_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_sql_injection_match_sets_response.ListSqlInjectionMatchSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>SqlInjectionMatchSet</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <a>SqlInjectionMatchSet</a> objects than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>SqlInjectionMatchSets</code>. For the second and subsequent <code>ListSqlInjectionMatchSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>SqlInjectionMatchSets</code>.</p>
            limit: <p>Specifies the number of <a>SqlInjectionMatchSet</a> objects that you want AWS WAF to return for this request. If you have more <code>SqlInjectionMatchSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>Rules</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list SQL injection match sets
            The following example returns an array of up to 100 SQL injection match sets.

            >>> await client.list_sql_injection_match_sets(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_sql_injection_match_sets_request.ListSqlInjectionMatchSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_sql_injection_match_sets_response.ListSqlInjectionMatchSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_sql_injection_match_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_sql_injection_match_sets.async_list_sql_injection_match_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_sql_injection_match_sets_request.ListSqlInjectionMatchSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_subscribed_rule_groups(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_subscribed_rule_groups_response.ListSubscribedRuleGroupsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>RuleGroup</a> objects that you are subscribed to.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>ByteMatchSets</code>subscribed rule groups than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of subscribed rule groups. For the second and subsequent <code>ListSubscribedRuleGroupsRequest</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of subscribed rule groups.</p>
            limit: <p>Specifies the number of subscribed rule groups that you want AWS WAF to return for this request. If you have more objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_subscribed_rule_groups_request.ListSubscribedRuleGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_subscribed_rule_groups_response.ListSubscribedRuleGroupsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_subscribed_rule_groups

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_subscribed_rule_groups.async_list_subscribed_rule_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_subscribed_rule_groups_request.ListSubscribedRuleGroupsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Retrieves the tags associated with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.</p> <p>Tagging is only available through the API, SDKs, and CLI. You can't manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules. </p>

        Args:
            next_marker: <p></p>
            limit: <p></p>
            resource_arn: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_web_ac_ls(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_web_ac_ls_response.ListWebACLsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>WebACLSummary</a> objects in the response.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <code>WebACL</code> objects than the number that you specify for <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>WebACL</code> objects. For the second and subsequent <code>ListWebACLs</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>WebACL</code> objects.</p>
            limit: <p>Specifies the number of <code>WebACL</code> objects that you want AWS WAF to return for this request. If you have more <code>WebACL</code> objects than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>WebACL</code> objects.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list Web ACLs
            The following example returns an array of up to 100 web ACLs.

            >>> await client.list_web_ac_ls(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_web_ac_ls_request.ListWebACLsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_web_ac_ls_response.ListWebACLsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_web_ac_ls

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_web_ac_ls.async_list_web_ac_ls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_web_ac_ls_request.ListWebACLsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_xss_match_sets(
        self,
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        next_marker: Optional["capo_waf.types.next_marker.NextMarker"] = None,
        limit: Optional["capo_waf.types.pagination_limit.PaginationLimit"] = None,
    ) -> "capo_waf.types.list_xss_match_sets_response.ListXssMatchSetsResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Returns an array of <a>XssMatchSet</a> objects.</p>

        Args:
            next_marker: <p>If you specify a value for <code>Limit</code> and you have more <a>XssMatchSet</a> objects than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>XssMatchSets</code>. For the second and subsequent <code>ListXssMatchSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>XssMatchSets</code>.</p>
            limit: <p>Specifies the number of <a>XssMatchSet</a> objects that you want AWS WAF to return for this request. If you have more <code>XssMatchSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>Rules</code>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list XSS match sets
            The following example returns an array of up to 100 XSS match sets.

            >>> await client.list_xss_match_sets(limit=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.list_xss_match_sets_request.ListXssMatchSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.list_xss_match_sets_response.ListXssMatchSetsResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.list_xss_match_sets

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.list_xss_match_sets.async_list_xss_match_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.list_xss_match_sets_request.ListXssMatchSetsRequest = {}
        if next_marker is not None:
            input_["next_marker"] = next_marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_logging_configuration(
        self,
        logging_configuration: "capo_waf.types.logging_configuration.LoggingConfiguration",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.put_logging_configuration_response.PutLoggingConfigurationResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Associates a <a>LoggingConfiguration</a> with a specified web ACL.</p> <p>You can access information about all traffic that AWS WAF inspects using the following steps:</p> <ol> <li> <p>Create an Amazon Kinesis Data Firehose. </p> <p>Create the data firehose with a PUT source and in the region that you are operating. However, if you are capturing logs for Amazon CloudFront, always create the firehose in US East (N. Virginia). </p> <note> <p>Do not create the data firehose using a <code>Kinesis stream</code> as your source.</p> </note> </li> <li> <p>Associate that firehose to your web ACL using a <code>PutLoggingConfiguration</code> request.</p> </li> </ol> <p>When you successfully enable logging using a <code>PutLoggingConfiguration</code> request, AWS WAF will create a service linked role with the necessary permissions to write logs to the Amazon Kinesis Data Firehose. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging.html">Logging Web ACL Traffic Information</a> in the <i>AWS WAF Developer Guide</i>.</p>

        Args:
            logging_configuration: <p>The Amazon Kinesis Data Firehose that contains the inspected traffic information, the redacted fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.</p> <note> <p>When specifying <code>Type</code> in <code>RedactedFields</code>, you must use one of the following values: <code>URI</code>, <code>QUERY_STRING</code>, <code>HEADER</code>, or <code>METHOD</code>.</p> </note>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_service_linked_role_error_exception.WAFServiceLinkedRoleErrorException: <p>AWS WAF is not able to access the service linked role. This can be caused by a previous <code>PutLoggingConfiguration</code> request, which can lock the service linked role for about 20 seconds. Please try your request again. The service linked role can also be locked by a previous <code>DeleteServiceLinkedRole</code> request, which can lock the role for 15 minutes or more. If you recently made a <code>DeleteServiceLinkedRole</code>, wait at least 15 minutes and try the request again. If you receive this same exception again, you will have to wait additional time until the role is unlocked.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.put_logging_configuration_request.PutLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.put_logging_configuration_response.PutLoggingConfigurationResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.put_logging_configuration

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.put_logging_configuration.async_put_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.put_logging_configuration_request.PutLoggingConfigurationRequest = {
            "logging_configuration": logging_configuration
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_permission_policy(
        self,
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        policy: "capo_waf.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.put_permission_policy_response.PutPermissionPolicyResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Attaches an IAM policy to the specified resource. The only supported use for this action is to share a RuleGroup across accounts.</p> <p>The <code>PutPermissionPolicy</code> is subject to the following restrictions:</p> <ul> <li> <p>You can attach only one policy with each <code>PutPermissionPolicy</code> request.</p> </li> <li> <p>The policy must include an <code>Effect</code>, <code>Action</code> and <code>Principal</code>. </p> </li> <li> <p> <code>Effect</code> must specify <code>Allow</code>.</p> </li> <li> <p>The <code>Action</code> in the policy must be <code>waf:UpdateWebACL</code>, <code>waf-regional:UpdateWebACL</code>, <code>waf:GetRuleGroup</code> and <code>waf-regional:GetRuleGroup</code> . Any extra or wildcard actions in the policy will be rejected.</p> </li> <li> <p>The policy cannot include a <code>Resource</code> parameter.</p> </li> <li> <p>The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.</p> </li> <li> <p>The user making the request must be the owner of the RuleGroup.</p> </li> <li> <p>Your policy must be composed using IAM Policy version 2012-10-17.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM Policies</a>. </p> <p>An example of a valid policy parameter is shown in the Examples section below.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.</p>
            policy: <p>The policy to attach to the specified RuleGroup.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_permission_policy_exception.WAFInvalidPermissionPolicyException: <p>The operation failed because the specified policy is not in the proper format. </p> <p>The policy is subject to the following restrictions:</p> <ul> <li> <p>You can attach only one policy with each <code>PutPermissionPolicy</code> request.</p> </li> <li> <p>The policy must include an <code>Effect</code>, <code>Action</code> and <code>Principal</code>. </p> </li> <li> <p> <code>Effect</code> must specify <code>Allow</code>.</p> </li> <li> <p>The <code>Action</code> in the policy must be <code>waf:UpdateWebACL</code>, <code>waf-regional:UpdateWebACL</code>, <code>waf:GetRuleGroup</code> and <code>waf-regional:GetRuleGroup</code> . Any extra or wildcard actions in the policy will be rejected.</p> </li> <li> <p>The policy cannot include a <code>Resource</code> parameter.</p> </li> <li> <p>The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.</p> </li> <li> <p>The user making the request must be the owner of the RuleGroup.</p> </li> <li> <p>Your policy must be composed using IAM Policy version 2012-10-17.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.put_permission_policy_request.PutPermissionPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.put_permission_policy_response.PutPermissionPolicyResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.put_permission_policy

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.put_permission_policy.async_put_permission_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.put_permission_policy_request.PutPermissionPolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
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
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        tags: "capo_waf.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.tag_resource_response.TagResourceResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Associates tags with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.</p> <p>Tagging is only available through the API, SDKs, and CLI. You can't manage or view tags through the AWS WAF Classic console. You can use this action to tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules. </p>

        Args:
            resource_arn: <p></p>
            tags: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.tag_resource

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_waf.types.resource_arn.ResourceArn",
        tag_keys: "capo_waf.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.untag_resource_response.UntagResourceResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p></p>

        Args:
            resource_arn: <p></p>
            tag_keys: <p></p>

        Raises:
            capo_waf.errors.waf_bad_request_exception.WAFBadRequestException: <p></p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_tag_operation_exception.WAFTagOperationException: <p></p>
            capo_waf.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException: <p></p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.untag_resource

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_byte_match_set(
        self,
        byte_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.byte_match_set_updates.ByteMatchSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_byte_match_set_response.UpdateByteMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>ByteMatchTuple</a> objects (filters) in a <a>ByteMatchSet</a>. For each <code>ByteMatchTuple</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the object from the array. If you want to change a <code>ByteMatchSetUpdate</code> object, you delete the existing object and add a new one.</p> </li> <li> <p>The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the <code>User-Agent</code> header. </p> </li> <li> <p>The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to look for. For more information, including how you specify the values for the AWS WAF API and the AWS CLI or SDKs, see <code>TargetString</code> in the <a>ByteMatchTuple</a> data type. </p> </li> <li> <p>Where to look, such as at the beginning or the end of a query string.</p> </li> <li> <p>Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.</p> </li> </ul> <p>For example, you can add a <code>ByteMatchSetUpdate</code> object that matches web requests in which <code>User-Agent</code> headers contain the string <code>BadBot</code>. You can then configure AWS WAF to block those requests.</p> <p>To create and configure a <code>ByteMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Create a <code>ByteMatchSet.</code> For more information, see <a>CreateByteMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateByteMatchSet</code> request.</p> </li> <li> <p>Submit an <code>UpdateByteMatchSet</code> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            byte_match_set_id: <p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to update. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>ByteMatchSetUpdate</code> objects that you want to insert into or delete from a <a>ByteMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>ByteMatchSetUpdate</a>: Contains <code>Action</code> and <code>ByteMatchTuple</code> </p> </li> <li> <p> <a>ByteMatchTuple</a>: Contains <code>FieldToMatch</code>, <code>PositionalConstraint</code>, <code>TargetString</code>, and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a byte match set
            The following example deletes a ByteMatchTuple object (filters) in an byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_byte_match_set(byte_match_set_id='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'ByteMatchTuple': {'FieldToMatch': {'Data': 'referer', 'Type': 'HEADER'}, 'PositionalConstraint': 'CONTAINS', 'TargetString': 'badrefer1', 'TextTransformation': 'NONE'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_byte_match_set_request.UpdateByteMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_byte_match_set_response.UpdateByteMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_byte_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_byte_match_set.async_update_byte_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_byte_match_set_request.UpdateByteMatchSetRequest = {
            "byte_match_set_id": byte_match_set_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_geo_match_set(
        self,
        geo_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.geo_match_set_updates.GeoMatchSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_geo_match_set_response.UpdateGeoMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>GeoMatchConstraint</a> objects in an <code>GeoMatchSet</code>. For each <code>GeoMatchConstraint</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the object from the array. If you want to change an <code>GeoMatchConstraint</code> object, you delete the existing object and add a new one.</p> </li> <li> <p>The <code>Type</code>. The only valid value for <code>Type</code> is <code>Country</code>.</p> </li> <li> <p>The <code>Value</code>, which is a two character code for the country to add to the <code>GeoMatchConstraint</code> object. Valid codes are listed in <a>GeoMatchConstraint$Value</a>.</p> </li> </ul> <p>To create and configure an <code>GeoMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Submit a <a>CreateGeoMatchSet</a> request.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateGeoMatchSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateGeoMatchSet</code> request to specify the country that you want AWS WAF to watch for.</p> </li> </ol> <p>When you update an <code>GeoMatchSet</code>, you specify the country that you want to add and/or the country that you want to delete. If you want to change a country, you delete the existing country and add the new one.</p> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            geo_match_set_id: <p>The <code>GeoMatchSetId</code> of the <a>GeoMatchSet</a> that you want to update. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>GeoMatchSetUpdate</code> objects that you want to insert into or delete from an <a>GeoMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>GeoMatchSetUpdate</a>: Contains <code>Action</code> and <code>GeoMatchConstraint</code> </p> </li> <li> <p> <a>GeoMatchConstraint</a>: Contains <code>Type</code> and <code>Value</code> </p> <p>You can have only one <code>Type</code> and <code>Value</code> per <code>GeoMatchConstraint</code>. To add multiple countries, include multiple <code>GeoMatchSetUpdate</code> objects in your request.</p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_geo_match_set_request.UpdateGeoMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_geo_match_set_response.UpdateGeoMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_geo_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_geo_match_set.async_update_geo_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_geo_match_set_request.UpdateGeoMatchSetRequest = {
            "geo_match_set_id": geo_match_set_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ip_set(
        self,
        ip_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.ip_set_updates.IPSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_ip_set_response.UpdateIPSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>IPSetDescriptor</a> objects in an <code>IPSet</code>. For each <code>IPSetDescriptor</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the object from the array. If you want to change an <code>IPSetDescriptor</code> object, you delete the existing object and add a new one.</p> </li> <li> <p>The IP address version, <code>IPv4</code> or <code>IPv6</code>. </p> </li> <li> <p>The IP address in CIDR notation, for example, <code>192.0.2.0/24</code> (for the range of IP addresses from <code>192.0.2.0</code> to <code>192.0.2.255</code>) or <code>192.0.2.44/32</code> (for the individual IP address <code>192.0.2.44</code>). </p> </li> </ul> <p>AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p> <p>IPv6 addresses can be represented using any of the following formats:</p> <ul> <li> <p>1111:0000:0000:0000:0000:0000:0000:0111/128</p> </li> <li> <p>1111:0:0:0:0:0:0:0111/128</p> </li> <li> <p>1111::0111/128</p> </li> <li> <p>1111::111/128</p> </li> </ul> <p>You use an <code>IPSet</code> to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you're receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an <code>IPSet</code> that specifies those IP addresses, and then configure AWS WAF to block the requests. </p> <p>To create and configure an <code>IPSet</code>, perform the following steps:</p> <ol> <li> <p>Submit a <a>CreateIPSet</a> request.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateIPSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateIPSet</code> request to specify the IP addresses that you want AWS WAF to watch for.</p> </li> </ol> <p>When you update an <code>IPSet</code>, you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.</p> <p>You can insert a maximum of 1000 addresses in a single request.</p> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            ip_set_id: <p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to update. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>IPSetUpdate</code> objects that you want to insert into or delete from an <a>IPSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>IPSetUpdate</a>: Contains <code>Action</code> and <code>IPSetDescriptor</code> </p> </li> <li> <p> <a>IPSetDescriptor</a>: Contains <code>Type</code> and <code>Value</code> </p> </li> </ul> <p>You can insert a maximum of 1000 addresses in a single request.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an IP set
            The following example deletes an IPSetDescriptor object in an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_ip_set(ip_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'IPSetDescriptor': {'Type': 'IPV4', 'Value': '192.0.2.44/32'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_ip_set_request.UpdateIPSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_ip_set_response.UpdateIPSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_ip_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_ip_set.async_update_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_ip_set_request.UpdateIPSetRequest = {
            "ip_set_id": ip_set_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rate_based_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.rule_updates.RuleUpdates",
        rate_limit: "capo_waf.types.rate_limit.RateLimit",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_rate_based_rule_response.UpdateRateBasedRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>Predicate</a> objects in a rule and updates the <code>RateLimit</code> in the rule. </p> <p>Each <code>Predicate</code> object identifies a predicate, such as a <a>ByteMatchSet</a> or an <a>IPSet</a>, that specifies the web requests that you want to block or count. The <code>RateLimit</code> specifies the number of requests every five minutes that triggers the rule.</p> <p>If you add more than one predicate to a <code>RateBasedRule</code>, a request must match all the predicates and exceed the <code>RateLimit</code> to be counted or blocked. For example, suppose you add the following to a <code>RateBasedRule</code>:</p> <ul> <li> <p>An <code>IPSet</code> that matches the IP address <code>192.0.2.44/32</code> </p> </li> <li> <p>A <code>ByteMatchSet</code> that matches <code>BadBot</code> in the <code>User-Agent</code> header</p> </li> </ul> <p>Further, you specify a <code>RateLimit</code> of 1,000.</p> <p>You then add the <code>RateBasedRule</code> to a <code>WebACL</code> and specify that you want to block requests that satisfy the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 <i>and</i> the <code>User-Agent</code> header in the request must contain the value <code>BadBot</code>. Further, requests that match these two conditions much be received at a rate of more than 1,000 every five minutes. If the rate drops below this limit, AWS WAF no longer blocks the requests.</p> <p>As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a <code>RateBasedRule</code>:</p> <ul> <li> <p>A <code>ByteMatchSet</code> with <code>FieldToMatch</code> of <code>URI</code> </p> </li> <li> <p>A <code>PositionalConstraint</code> of <code>STARTS_WITH</code> </p> </li> <li> <p>A <code>TargetString</code> of <code>login</code> </p> </li> </ul> <p>Further, you specify a <code>RateLimit</code> of 1,000.</p> <p>By adding this <code>RateBasedRule</code> to a <code>WebACL</code>, you could limit requests to your login page without affecting the rest of your site.</p>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <code>RateBasedRule</code> that you want to update. <code>RuleId</code> is returned by <code>CreateRateBasedRule</code> and by <a>ListRateBasedRules</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>RuleUpdate</code> objects that you want to insert into or delete from a <a>RateBasedRule</a>. </p>
            rate_limit: <p>The maximum number of requests, which have an identical value in the field specified by the <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_rate_based_rule_request.UpdateRateBasedRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_rate_based_rule_response.UpdateRateBasedRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_rate_based_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_rate_based_rule.async_update_rate_based_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_rate_based_rule_request.UpdateRateBasedRuleRequest = {
            "rule_id": rule_id,
            "change_token": change_token,
            "updates": updates,
            "rate_limit": rate_limit,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_regex_match_set(
        self,
        regex_match_set_id: "capo_waf.types.resource_id.ResourceId",
        updates: "capo_waf.types.regex_match_set_updates.RegexMatchSetUpdates",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_regex_match_set_response.UpdateRegexMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>RegexMatchTuple</a> objects (filters) in a <a>RegexMatchSet</a>. For each <code>RegexMatchSetUpdate</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the object from the array. If you want to change a <code>RegexMatchSetUpdate</code> object, you delete the existing object and add a new one.</p> </li> <li> <p>The part of a web request that you want AWS WAF to inspectupdate, such as a query string or the value of the <code>User-Agent</code> header. </p> </li> <li> <p>The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see <a>RegexPatternSet</a>. </p> </li> <li> <p>Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.</p> </li> </ul> <p> For example, you can create a <code>RegexPatternSet</code> that matches any requests with <code>User-Agent</code> headers that contain the string <code>B[a@]dB[o0]t</code>. You can then configure AWS WAF to reject those requests.</p> <p>To create and configure a <code>RegexMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Create a <code>RegexMatchSet.</code> For more information, see <a>CreateRegexMatchSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateRegexMatchSet</code> request.</p> </li> <li> <p>Submit an <code>UpdateRegexMatchSet</code> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the identifier of the <code>RegexPatternSet</code> that contain the regular expression patters you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            regex_match_set_id: <p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to update. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>
            updates: <p>An array of <code>RegexMatchSetUpdate</code> objects that you want to insert into or delete from a <a>RegexMatchSet</a>. For more information, see <a>RegexMatchTuple</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_disallowed_name_exception.WAFDisallowedNameException: <p>The name specified is invalid.</p>
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_regex_match_set_request.UpdateRegexMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_regex_match_set_response.UpdateRegexMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_regex_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_regex_match_set.async_update_regex_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_regex_match_set_request.UpdateRegexMatchSetRequest = {
            "regex_match_set_id": regex_match_set_id,
            "updates": updates,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_regex_pattern_set(
        self,
        regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId",
        updates: "capo_waf.types.regex_pattern_set_updates.RegexPatternSetUpdates",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> (
        "capo_waf.types.update_regex_pattern_set_response.UpdateRegexPatternSetResponse"
    ):
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <code>RegexPatternString</code> objects in a <a>RegexPatternSet</a>. For each <code>RegexPatternString</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the <code>RegexPatternString</code>.</p> </li> <li> <p>The regular expression pattern that you want to insert or delete. For more information, see <a>RegexPatternSet</a>. </p> </li> </ul> <p> For example, you can create a <code>RegexPatternString</code> such as <code>B[a@]dB[o0]t</code>. AWS WAF will match this <code>RegexPatternString</code> to:</p> <ul> <li> <p>BadBot</p> </li> <li> <p>BadB0t</p> </li> <li> <p>B@dBot</p> </li> <li> <p>B@dB0t</p> </li> </ul> <p>To create and configure a <code>RegexPatternSet</code>, perform the following steps:</p> <ol> <li> <p>Create a <code>RegexPatternSet.</code> For more information, see <a>CreateRegexPatternSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateRegexPatternSet</code> request.</p> </li> <li> <p>Submit an <code>UpdateRegexPatternSet</code> request to specify the regular expression pattern that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            regex_pattern_set_id: <p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to update. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>
            updates: <p>An array of <code>RegexPatternSetUpdate</code> objects that you want to insert into or delete from a <a>RegexPatternSet</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_regex_pattern_exception.WAFInvalidRegexPatternException: <p>The regular expression (regex) you specified in <code>RegexPatternString</code> is invalid.</p>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_regex_pattern_set_request.UpdateRegexPatternSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_regex_pattern_set_response.UpdateRegexPatternSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_regex_pattern_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_regex_pattern_set.async_update_regex_pattern_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_regex_pattern_set_request.UpdateRegexPatternSetRequest = {
            "regex_pattern_set_id": regex_pattern_set_id,
            "updates": updates,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rule(
        self,
        rule_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.rule_updates.RuleUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_rule_response.UpdateRuleResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>Predicate</a> objects in a <code>Rule</code>. Each <code>Predicate</code> object identifies a predicate, such as a <a>ByteMatchSet</a> or an <a>IPSet</a>, that specifies the web requests that you want to allow, block, or count. If you add more than one predicate to a <code>Rule</code>, a request must match all of the specifications to be allowed, blocked, or counted. For example, suppose that you add the following to a <code>Rule</code>: </p> <ul> <li> <p>A <code>ByteMatchSet</code> that matches the value <code>BadBot</code> in the <code>User-Agent</code> header</p> </li> <li> <p>An <code>IPSet</code> that matches the IP address <code>192.0.2.44</code> </p> </li> </ul> <p>You then add the <code>Rule</code> to a <code>WebACL</code> and specify that you want to block requests that satisfy the <code>Rule</code>. For a request to be blocked, the <code>User-Agent</code> header in the request must contain the value <code>BadBot</code> <i>and</i> the request must originate from the IP address 192.0.2.44.</p> <p>To create and configure a <code>Rule</code>, perform the following steps:</p> <ol> <li> <p>Create and update the predicates that you want to include in the <code>Rule</code>.</p> </li> <li> <p>Create the <code>Rule</code>. See <a>CreateRule</a>.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateRule</a> request.</p> </li> <li> <p>Submit an <code>UpdateRule</code> request to add predicates to the <code>Rule</code>.</p> </li> <li> <p>Create and update a <code>WebACL</code> that contains the <code>Rule</code>. See <a>CreateWebACL</a>.</p> </li> </ol> <p>If you want to replace one <code>ByteMatchSet</code> or <code>IPSet</code> with another, you delete the existing one and add the new one.</p> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            rule_id: <p>The <code>RuleId</code> of the <code>Rule</code> that you want to update. <code>RuleId</code> is returned by <code>CreateRule</code> and by <a>ListRules</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>RuleUpdate</code> objects that you want to insert into or delete from a <a>Rule</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>RuleUpdate</a>: Contains <code>Action</code> and <code>Predicate</code> </p> </li> <li> <p> <a>Predicate</a>: Contains <code>DataId</code>, <code>Negated</code>, and <code>Type</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a rule
            The following example deletes a Predicate object in a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_rule(rule_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'Predicate': {'DataId': 'MyByteMatchSetID', 'Negated': False, 'Type': 'ByteMatch'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_rule_request.UpdateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_rule_response.UpdateRuleResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_rule

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_rule_request.UpdateRuleRequest = {
            "rule_id": rule_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rule_group(
        self,
        rule_group_id: "capo_waf.types.resource_id.ResourceId",
        updates: "capo_waf.types.rule_group_updates.RuleGroupUpdates",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_rule_group_response.UpdateRuleGroupResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>ActivatedRule</a> objects in a <code>RuleGroup</code>.</p> <p>You can only insert <code>REGULAR</code> rules into a rule group.</p> <p>You can have a maximum of ten rules per rule group.</p> <p>To create and configure a <code>RuleGroup</code>, perform the following steps:</p> <ol> <li> <p>Create and update the <code>Rules</code> that you want to include in the <code>RuleGroup</code>. See <a>CreateRule</a>.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateRuleGroup</a> request.</p> </li> <li> <p>Submit an <code>UpdateRuleGroup</code> request to add <code>Rules</code> to the <code>RuleGroup</code>.</p> </li> <li> <p>Create and update a <code>WebACL</code> that contains the <code>RuleGroup</code>. See <a>CreateWebACL</a>.</p> </li> </ol> <p>If you want to replace one <code>Rule</code> with another, you delete the existing one and add the new one.</p> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            rule_group_id: <p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to update. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>
            updates: <p>An array of <code>RuleGroupUpdate</code> objects that you want to insert into or delete from a <a>RuleGroup</a>.</p> <p>You can only insert <code>REGULAR</code> rules into a rule group.</p> <p> <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_rule_group_request.UpdateRuleGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_rule_group_response.UpdateRuleGroupResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_rule_group

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_rule_group.async_update_rule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_rule_group_request.UpdateRuleGroupRequest = {
            "rule_group_id": rule_group_id,
            "updates": updates,
            "change_token": change_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_size_constraint_set(
        self,
        size_constraint_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.size_constraint_set_updates.SizeConstraintSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_size_constraint_set_response.UpdateSizeConstraintSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>SizeConstraint</a> objects (filters) in a <a>SizeConstraintSet</a>. For each <code>SizeConstraint</code> object, you specify the following values: </p> <ul> <li> <p>Whether to insert or delete the object from the array. If you want to change a <code>SizeConstraintSetUpdate</code> object, you delete the existing object and add a new one.</p> </li> <li> <p>The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the <code>User-Agent</code> header.</p> </li> <li> <p>Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first <code>8192</code> bytes of your request to AWS WAF.</p> <p>You can only specify a single type of TextTransformation.</p> </li> <li> <p>A <code>ComparisonOperator</code> used for evaluating the selected part of the request against the specified <code>Size</code>, such as equals, greater than, less than, and so on.</p> </li> <li> <p>The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation.</p> </li> </ul> <p>For example, you can add a <code>SizeConstraintSetUpdate</code> object that matches web requests in which the length of the <code>User-Agent</code> header is greater than 100 bytes. You can then configure AWS WAF to block those requests.</p> <p>To create and configure a <code>SizeConstraintSet</code>, perform the following steps:</p> <ol> <li> <p>Create a <code>SizeConstraintSet.</code> For more information, see <a>CreateSizeConstraintSet</a>.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <code>UpdateSizeConstraintSet</code> request.</p> </li> <li> <p>Submit an <code>UpdateSizeConstraintSet</code> request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            size_constraint_set_id: <p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to update. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>SizeConstraintSetUpdate</code> objects that you want to insert into or delete from a <a>SizeConstraintSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>SizeConstraintSetUpdate</a>: Contains <code>Action</code> and <code>SizeConstraint</code> </p> </li> <li> <p> <a>SizeConstraint</a>: Contains <code>FieldToMatch</code>, <code>TextTransformation</code>, <code>ComparisonOperator</code>, and <code>Size</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a size constraint set
            The following example deletes a SizeConstraint object (filters) in a size constraint set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_size_constraint_set(size_constraint_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'SizeConstraint': {'ComparisonOperator': 'GT', 'FieldToMatch': {'Type': 'QUERY_STRING'}, 'Size': 0, 'TextTransformation': 'NONE'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_size_constraint_set_request.UpdateSizeConstraintSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_size_constraint_set_response.UpdateSizeConstraintSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_size_constraint_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_size_constraint_set.async_update_size_constraint_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_size_constraint_set_request.UpdateSizeConstraintSetRequest = {
            "size_constraint_set_id": size_constraint_set_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sql_injection_match_set(
        self,
        sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.sql_injection_match_set_updates.SqlInjectionMatchSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_sql_injection_match_set_response.UpdateSqlInjectionMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>SqlInjectionMatchTuple</a> objects (filters) in a <a>SqlInjectionMatchSet</a>. For each <code>SqlInjectionMatchTuple</code> object, you specify the following values:</p> <ul> <li> <p> <code>Action</code>: Whether to insert the object into or delete the object from the array. To change a <code>SqlInjectionMatchTuple</code>, you delete the existing object and add a new one.</p> </li> <li> <p> <code>FieldToMatch</code>: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.</p> </li> <li> <p> <code>TextTransformation</code>: Which text transformation, if any, to perform on the web request before inspecting the request for snippets of malicious SQL code.</p> <p>You can only specify a single type of TextTransformation.</p> </li> </ul> <p>You use <code>SqlInjectionMatchSet</code> objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you're receiving requests that contain snippets of SQL code in the query string and you want to block the requests, you can create a <code>SqlInjectionMatchSet</code> with the applicable settings, and then configure AWS WAF to block the requests. </p> <p>To create and configure a <code>SqlInjectionMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Submit a <a>CreateSqlInjectionMatchSet</a> request.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateIPSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateSqlInjectionMatchSet</code> request to specify the parts of web requests that you want AWS WAF to inspect for snippets of SQL code.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            sql_injection_match_set_id: <p>The <code>SqlInjectionMatchSetId</code> of the <code>SqlInjectionMatchSet</code> that you want to update. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>SqlInjectionMatchSetUpdate</code> objects that you want to insert into or delete from a <a>SqlInjectionMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>SqlInjectionMatchSetUpdate</a>: Contains <code>Action</code> and <code>SqlInjectionMatchTuple</code> </p> </li> <li> <p> <a>SqlInjectionMatchTuple</a>: Contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a SQL injection match set
            The following example deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_sql_injection_match_set(sql_injection_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'SqlInjectionMatchTuple': {'FieldToMatch': {'Type': 'QUERY_STRING'}, 'TextTransformation': 'URL_DECODE'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_sql_injection_match_set_request.UpdateSqlInjectionMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_sql_injection_match_set_response.UpdateSqlInjectionMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_sql_injection_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_sql_injection_match_set.async_update_sql_injection_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_sql_injection_match_set_request.UpdateSqlInjectionMatchSetRequest = {
            "sql_injection_match_set_id": sql_injection_match_set_id,
            "change_token": change_token,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_web_acl(
        self,
        web_acl_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
        updates: Optional["capo_waf.types.web_acl_updates.WebACLUpdates"] = None,
        default_action: Optional["capo_waf.types.waf_action.WafAction"] = None,
    ) -> "capo_waf.types.update_web_acl_response.UpdateWebACLResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>ActivatedRule</a> objects in a <code>WebACL</code>. Each <code>Rule</code> identifies web requests that you want to allow, block, or count. When you update a <code>WebACL</code>, you specify the following values:</p> <ul> <li> <p>A default action for the <code>WebACL</code>, either <code>ALLOW</code> or <code>BLOCK</code>. AWS WAF performs the default action if a request doesn't match the criteria in any of the <code>Rules</code> in a <code>WebACL</code>.</p> </li> <li> <p>The <code>Rules</code> that you want to add or delete. If you want to replace one <code>Rule</code> with another, you delete the existing <code>Rule</code> and add the new one.</p> </li> <li> <p>For each <code>Rule</code>, whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the <code>Rule</code>.</p> </li> <li> <p>The order in which you want AWS WAF to evaluate the <code>Rules</code> in a <code>WebACL</code>. If you add more than one <code>Rule</code> to a <code>WebACL</code>, AWS WAF evaluates each request against the <code>Rules</code> in order based on the value of <code>Priority</code>. (The <code>Rule</code> that has the lowest value for <code>Priority</code> is evaluated first.) When a web request matches all the predicates (such as <code>ByteMatchSets</code> and <code>IPSets</code>) in a <code>Rule</code>, AWS WAF immediately takes the corresponding action, allow or block, and doesn't evaluate the request against the remaining <code>Rules</code> in the <code>WebACL</code>, if any. </p> </li> </ul> <p>To create and configure a <code>WebACL</code>, perform the following steps:</p> <ol> <li> <p>Create and update the predicates that you want to include in <code>Rules</code>. For more information, see <a>CreateByteMatchSet</a>, <a>UpdateByteMatchSet</a>, <a>CreateIPSet</a>, <a>UpdateIPSet</a>, <a>CreateSqlInjectionMatchSet</a>, and <a>UpdateSqlInjectionMatchSet</a>.</p> </li> <li> <p>Create and update the <code>Rules</code> that you want to include in the <code>WebACL</code>. For more information, see <a>CreateRule</a> and <a>UpdateRule</a>.</p> </li> <li> <p>Create a <code>WebACL</code>. See <a>CreateWebACL</a>.</p> </li> <li> <p>Use <code>GetChangeToken</code> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateWebACL</a> request.</p> </li> <li> <p>Submit an <code>UpdateWebACL</code> request to specify the <code>Rules</code> that you want to include in the <code>WebACL</code>, to specify the default action, and to associate the <code>WebACL</code> with a CloudFront distribution. </p> <p>The <code>ActivatedRule</code> can be a rule group. If you specify a rule group as your <code>ActivatedRule</code> , you can exclude specific rules from that rule group.</p> <p>If you already have a rule group associated with a web ACL and want to submit an <code>UpdateWebACL</code> request to exclude certain rules from that rule group, you must first remove the rule group from the web ACL, the re-insert it again, specifying the excluded rules. For details, see <a>ActivatedRule$ExcludedRules</a> . </p> </li> </ol> <p>Be aware that if you try to add a RATE_BASED rule to a web ACL without setting the rule type when first creating the rule, the <a>UpdateWebACL</a> request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist. </p> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            web_acl_id: <p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to update. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of updates to make to the <a>WebACL</a>.</p> <p>An array of <code>WebACLUpdate</code> objects that you want to insert into or delete from a <a>WebACL</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>WebACLUpdate</a>: Contains <code>Action</code> and <code>ActivatedRule</code> </p> </li> <li> <p> <a>ActivatedRule</a>: Contains <code>Action</code>, <code>OverrideAction</code>, <code>Priority</code>, <code>RuleId</code>, and <code>Type</code>. <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case, you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>. </p> </li> <li> <p> <a>WafAction</a>: Contains <code>Type</code> </p> </li> </ul>
            default_action: <p>A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesn't match the criteria in any of the rules in a web ACL.</p>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_referenced_item_exception.WAFReferencedItemException: <p>The operation failed because you tried to delete an object that is still in use. For example:</p> <ul> <li> <p>You tried to delete a <code>ByteMatchSet</code> that is still referenced by a <code>Rule</code>.</p> </li> <li> <p>You tried to delete a <code>Rule</code> that is still referenced by a <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException: <p>The specified subscription does not exist.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Web ACL
            The following example deletes an ActivatedRule object in a WebACL with the ID webacl-1472061481310.

            >>> await client.update_web_acl(web_acl_id='webacl-1472061481310', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'ActivatedRule': {'Action': {'Type': 'ALLOW'}, 'Priority': 1, 'RuleId': 'WAFRule-1-Example'}}], default_action={'Type': 'ALLOW'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_web_acl_request.UpdateWebACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_web_acl_response.UpdateWebACLResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_web_acl

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_web_acl.async_update_web_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_web_acl_request.UpdateWebACLRequest = {
            "web_acl_id": web_acl_id,
            "change_token": change_token,
        }
        if updates is not None:
            input_["updates"] = updates
        if default_action is not None:
            input_["default_action"] = default_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_xss_match_set(
        self,
        xss_match_set_id: "capo_waf.types.resource_id.ResourceId",
        change_token: "capo_waf.types.change_token.ChangeToken",
        updates: "capo_waf.types.xss_match_set_updates.XssMatchSetUpdates",
        *,
        config_overrides: Optional[AsyncWAFClientConfig] = None,
    ) -> "capo_waf.types.update_xss_match_set_response.UpdateXssMatchSetResponse":
        """<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>Inserts or deletes <a>XssMatchTuple</a> objects (filters) in an <a>XssMatchSet</a>. For each <code>XssMatchTuple</code> object, you specify the following values:</p> <ul> <li> <p> <code>Action</code>: Whether to insert the object into or delete the object from the array. To change an <code>XssMatchTuple</code>, you delete the existing object and add a new one.</p> </li> <li> <p> <code>FieldToMatch</code>: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.</p> </li> <li> <p> <code>TextTransformation</code>: Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.</p> <p>You can only specify a single type of TextTransformation.</p> </li> </ul> <p>You use <code>XssMatchSet</code> objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you're receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an <code>XssMatchSet</code> with the applicable settings, and then configure AWS WAF to block the requests. </p> <p>To create and configure an <code>XssMatchSet</code>, perform the following steps:</p> <ol> <li> <p>Submit a <a>CreateXssMatchSet</a> request.</p> </li> <li> <p>Use <a>GetChangeToken</a> to get the change token that you provide in the <code>ChangeToken</code> parameter of an <a>UpdateIPSet</a> request.</p> </li> <li> <p>Submit an <code>UpdateXssMatchSet</code> request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.</p> </li> </ol> <p>For more information about how to use the AWS WAF API to allow or block HTTP requests, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/">AWS WAF Developer Guide</a>.</p>

        Args:
            xss_match_set_id: <p>The <code>XssMatchSetId</code> of the <code>XssMatchSet</code> that you want to update. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>
            change_token: <p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>
            updates: <p>An array of <code>XssMatchSetUpdate</code> objects that you want to insert into or delete from an <a>XssMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>XssMatchSetUpdate</a>: Contains <code>Action</code> and <code>XssMatchTuple</code> </p> </li> <li> <p> <a>XssMatchTuple</a>: Contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>

        Raises:
            capo_waf.errors.waf_internal_error_exception.WAFInternalErrorException: <p>The operation failed because of a system problem, even though the request was valid. Retry your request.</p>
            capo_waf.errors.waf_invalid_account_exception.WAFInvalidAccountException: <p>The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.</p>
            capo_waf.errors.waf_invalid_operation_exception.WAFInvalidOperationException: <p>The operation failed because there was nothing to do. For example:</p> <ul> <li> <p>You tried to remove a <code>Rule</code> from a <code>WebACL</code>, but the <code>Rule</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to remove an IP address from an <code>IPSet</code>, but the IP address isn't in the specified <code>IPSet</code>.</p> </li> <li> <p>You tried to remove a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> isn't in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>Rule</code> to a <code>WebACL</code>, but the <code>Rule</code> already exists in the specified <code>WebACL</code>.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to a <code>ByteMatchSet</code>, but the <code>ByteMatchTuple</code> already exists in the specified <code>WebACL</code>.</p> </li> </ul>
            capo_waf.errors.waf_invalid_parameter_exception.WAFInvalidParameterException: <p>The operation failed because AWS WAF didn't recognize a parameter in the request. For example:</p> <ul> <li> <p>You specified an invalid parameter name.</p> </li> <li> <p>You specified an invalid value.</p> </li> <li> <p>You tried to update an object (<code>ByteMatchSet</code>, <code>IPSet</code>, <code>Rule</code>, or <code>WebACL</code>) using an action other than <code>INSERT</code> or <code>DELETE</code>.</p> </li> <li> <p>You tried to create a <code>WebACL</code> with a <code>DefaultAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to create a <code>RateBasedRule</code> with a <code>RateKey</code> value other than <code>IP</code>.</p> </li> <li> <p>You tried to update a <code>WebACL</code> with a <code>WafAction</code> <code>Type</code> other than <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>FieldToMatch</code> <code>Type</code> other than HEADER, METHOD, QUERY_STRING, URI, or BODY.</p> </li> <li> <p>You tried to update a <code>ByteMatchSet</code> with a <code>Field</code> of <code>HEADER</code> but no value for <code>Data</code>.</p> </li> <li> <p>Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.</p> </li> </ul>
            capo_waf.errors.waf_limits_exceeded_exception.WAFLimitsExceededException: <p>The operation exceeds a resource limit, for example, the maximum number of <code>WebACL</code> objects that you can create for an AWS account. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">Limits</a> in the <i>AWS WAF Developer Guide</i>.</p>
            capo_waf.errors.waf_nonexistent_container_exception.WAFNonexistentContainerException: <p>The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:</p> <ul> <li> <p>You tried to add a <code>Rule</code> to or delete a <code>Rule</code> from a <code>WebACL</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchSet</code> to or delete a <code>ByteMatchSet</code> from a <code>Rule</code> that doesn't exist.</p> </li> <li> <p>You tried to add an IP address to or delete an IP address from an <code>IPSet</code> that doesn't exist.</p> </li> <li> <p>You tried to add a <code>ByteMatchTuple</code> to or delete a <code>ByteMatchTuple</code> from a <code>ByteMatchSet</code> that doesn't exist.</p> </li> </ul>
            capo_waf.errors.waf_nonexistent_item_exception.WAFNonexistentItemException: <p>The operation failed because the referenced object doesn't exist.</p>
            capo_waf.errors.waf_stale_data_exception.WAFStaleDataException: <p>The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.</p>
            capo_waf.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an XSS match set
            The following example deletes an XssMatchTuple object (filters) in an XssMatchSet with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.

            >>> await client.update_xss_match_set(xss_match_set_id='example1ds3t-46da-4fdb-b8d5-abc321j569j5', change_token='abcd12f2-46da-4fdb-b8d5-fbd4c466928f', updates=[{'Action': 'DELETE', 'XssMatchTuple': {'FieldToMatch': {'Type': 'QUERY_STRING'}, 'TextTransformation': 'URL_DECODE'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_waf.types.update_xss_match_set_request.UpdateXssMatchSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_waf.types.update_xss_match_set_response.UpdateXssMatchSetResponse"
        ]:
            import capo_waf._operations.awswaf_20150824.update_xss_match_set

            (
                output,
                http_response,
            ) = await capo_waf._operations.awswaf_20150824.update_xss_match_set.async_update_xss_match_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_waf.types.update_xss_match_set_request.UpdateXssMatchSetRequest = {
            "xss_match_set_id": xss_match_set_id,
            "change_token": change_token,
            "updates": updates,
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
