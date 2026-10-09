"""Generated from Smithy shape ``com.amazonaws.apigateway#BackplaneControlService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_api_gateway._auth._signers
import capo_api_gateway._auth._sigv4
from capo_api_gateway._auth._identity import Credentials
from capo_api_gateway._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_api_gateway._auth._zapros_handler import AuthMiddleware
from capo_api_gateway._pagination import resolve_path as _resolve_path
from capo_api_gateway._services._aws_config import aws_config
from capo_api_gateway._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_api_gateway.types.access_association_source_type
    import capo_api_gateway.types.account
    import capo_api_gateway.types.api_key
    import capo_api_gateway.types.api_key_ids
    import capo_api_gateway.types.api_key_source_type
    import capo_api_gateway.types.api_keys
    import capo_api_gateway.types.api_keys_format
    import capo_api_gateway.types.authorizer
    import capo_api_gateway.types.authorizer_type
    import capo_api_gateway.types.authorizers
    import capo_api_gateway.types.base_path_mapping
    import capo_api_gateway.types.base_path_mappings
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.cache_cluster_size
    import capo_api_gateway.types.canary_settings
    import capo_api_gateway.types.client_certificate
    import capo_api_gateway.types.client_certificates
    import capo_api_gateway.types.connection_type
    import capo_api_gateway.types.content_handling_strategy
    import capo_api_gateway.types.create_api_key_request
    import capo_api_gateway.types.create_authorizer_request
    import capo_api_gateway.types.create_base_path_mapping_request
    import capo_api_gateway.types.create_deployment_request
    import capo_api_gateway.types.create_documentation_part_request
    import capo_api_gateway.types.create_documentation_version_request
    import capo_api_gateway.types.create_domain_name_access_association_request
    import capo_api_gateway.types.create_domain_name_request
    import capo_api_gateway.types.create_model_request
    import capo_api_gateway.types.create_request_validator_request
    import capo_api_gateway.types.create_resource_request
    import capo_api_gateway.types.create_rest_api_request
    import capo_api_gateway.types.create_stage_request
    import capo_api_gateway.types.create_usage_plan_key_request
    import capo_api_gateway.types.create_usage_plan_request
    import capo_api_gateway.types.create_vpc_link_request
    import capo_api_gateway.types.delete_api_key_request
    import capo_api_gateway.types.delete_authorizer_request
    import capo_api_gateway.types.delete_base_path_mapping_request
    import capo_api_gateway.types.delete_client_certificate_request
    import capo_api_gateway.types.delete_deployment_request
    import capo_api_gateway.types.delete_documentation_part_request
    import capo_api_gateway.types.delete_documentation_version_request
    import capo_api_gateway.types.delete_domain_name_access_association_request
    import capo_api_gateway.types.delete_domain_name_request
    import capo_api_gateway.types.delete_gateway_response_request
    import capo_api_gateway.types.delete_integration_request
    import capo_api_gateway.types.delete_integration_response_request
    import capo_api_gateway.types.delete_method_request
    import capo_api_gateway.types.delete_method_response_request
    import capo_api_gateway.types.delete_model_request
    import capo_api_gateway.types.delete_request_validator_request
    import capo_api_gateway.types.delete_resource_request
    import capo_api_gateway.types.delete_rest_api_request
    import capo_api_gateway.types.delete_stage_request
    import capo_api_gateway.types.delete_usage_plan_key_request
    import capo_api_gateway.types.delete_usage_plan_request
    import capo_api_gateway.types.delete_vpc_link_request
    import capo_api_gateway.types.deployment
    import capo_api_gateway.types.deployment_canary_settings
    import capo_api_gateway.types.deployments
    import capo_api_gateway.types.documentation_part
    import capo_api_gateway.types.documentation_part_ids
    import capo_api_gateway.types.documentation_part_location
    import capo_api_gateway.types.documentation_part_type
    import capo_api_gateway.types.documentation_parts
    import capo_api_gateway.types.documentation_version
    import capo_api_gateway.types.documentation_versions
    import capo_api_gateway.types.domain_name
    import capo_api_gateway.types.domain_name_access_association
    import capo_api_gateway.types.domain_name_access_associations
    import capo_api_gateway.types.domain_names
    import capo_api_gateway.types.endpoint_access_mode
    import capo_api_gateway.types.endpoint_configuration
    import capo_api_gateway.types.export_response
    import capo_api_gateway.types.flush_stage_authorizers_cache_request
    import capo_api_gateway.types.flush_stage_cache_request
    import capo_api_gateway.types.gateway_response
    import capo_api_gateway.types.gateway_response_type
    import capo_api_gateway.types.gateway_responses
    import capo_api_gateway.types.generate_client_certificate_request
    import capo_api_gateway.types.get_account_request
    import capo_api_gateway.types.get_api_key_request
    import capo_api_gateway.types.get_api_keys_request
    import capo_api_gateway.types.get_authorizer_request
    import capo_api_gateway.types.get_authorizers_request
    import capo_api_gateway.types.get_base_path_mapping_request
    import capo_api_gateway.types.get_base_path_mappings_request
    import capo_api_gateway.types.get_client_certificate_request
    import capo_api_gateway.types.get_client_certificates_request
    import capo_api_gateway.types.get_deployment_request
    import capo_api_gateway.types.get_deployments_request
    import capo_api_gateway.types.get_documentation_part_request
    import capo_api_gateway.types.get_documentation_parts_request
    import capo_api_gateway.types.get_documentation_version_request
    import capo_api_gateway.types.get_documentation_versions_request
    import capo_api_gateway.types.get_domain_name_access_associations_request
    import capo_api_gateway.types.get_domain_name_request
    import capo_api_gateway.types.get_domain_names_request
    import capo_api_gateway.types.get_export_request
    import capo_api_gateway.types.get_gateway_response_request
    import capo_api_gateway.types.get_gateway_responses_request
    import capo_api_gateway.types.get_integration_request
    import capo_api_gateway.types.get_integration_response_request
    import capo_api_gateway.types.get_method_request
    import capo_api_gateway.types.get_method_response_request
    import capo_api_gateway.types.get_model_request
    import capo_api_gateway.types.get_model_template_request
    import capo_api_gateway.types.get_models_request
    import capo_api_gateway.types.get_request_validator_request
    import capo_api_gateway.types.get_request_validators_request
    import capo_api_gateway.types.get_resource_request
    import capo_api_gateway.types.get_resources_request
    import capo_api_gateway.types.get_rest_api_request
    import capo_api_gateway.types.get_rest_apis_request
    import capo_api_gateway.types.get_sdk_request
    import capo_api_gateway.types.get_sdk_type_request
    import capo_api_gateway.types.get_sdk_types_request
    import capo_api_gateway.types.get_stage_request
    import capo_api_gateway.types.get_stages_request
    import capo_api_gateway.types.get_tags_request
    import capo_api_gateway.types.get_usage_plan_key_request
    import capo_api_gateway.types.get_usage_plan_keys_request
    import capo_api_gateway.types.get_usage_plan_request
    import capo_api_gateway.types.get_usage_plans_request
    import capo_api_gateway.types.get_usage_request
    import capo_api_gateway.types.get_vpc_link_request
    import capo_api_gateway.types.get_vpc_links_request
    import capo_api_gateway.types.import_api_keys_request
    import capo_api_gateway.types.import_documentation_parts_request
    import capo_api_gateway.types.import_rest_api_request
    import capo_api_gateway.types.integration
    import capo_api_gateway.types.integration_response
    import capo_api_gateway.types.integration_type
    import capo_api_gateway.types.list_of_api_stage
    import capo_api_gateway.types.list_of_ar_ns
    import capo_api_gateway.types.list_of_patch_operation
    import capo_api_gateway.types.list_of_stage_keys
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.list_of_usage
    import capo_api_gateway.types.location_status_type
    import capo_api_gateway.types.map_of_string_to_boolean
    import capo_api_gateway.types.map_of_string_to_list
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.method
    import capo_api_gateway.types.method_response
    import capo_api_gateway.types.model
    import capo_api_gateway.types.models
    import capo_api_gateway.types.mutual_tls_authentication_input
    import capo_api_gateway.types.nullable_boolean
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.put_gateway_response_request
    import capo_api_gateway.types.put_integration_request
    import capo_api_gateway.types.put_integration_response_request
    import capo_api_gateway.types.put_method_request
    import capo_api_gateway.types.put_method_response_request
    import capo_api_gateway.types.put_mode
    import capo_api_gateway.types.put_rest_api_request
    import capo_api_gateway.types.quota_settings
    import capo_api_gateway.types.reject_domain_name_access_association_request
    import capo_api_gateway.types.request_validator
    import capo_api_gateway.types.request_validators
    import capo_api_gateway.types.resource
    import capo_api_gateway.types.resource_owner
    import capo_api_gateway.types.resources
    import capo_api_gateway.types.response_transfer_mode
    import capo_api_gateway.types.rest_api
    import capo_api_gateway.types.rest_apis
    import capo_api_gateway.types.routing_mode
    import capo_api_gateway.types.sdk_response
    import capo_api_gateway.types.sdk_type
    import capo_api_gateway.types.sdk_types
    import capo_api_gateway.types.security_policy
    import capo_api_gateway.types.stage
    import capo_api_gateway.types.stages
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string
    import capo_api_gateway.types.tag_resource_request
    import capo_api_gateway.types.tags
    import capo_api_gateway.types.template
    import capo_api_gateway.types.test_invoke_authorizer_request
    import capo_api_gateway.types.test_invoke_authorizer_response
    import capo_api_gateway.types.test_invoke_method_request
    import capo_api_gateway.types.test_invoke_method_response
    import capo_api_gateway.types.throttle_settings
    import capo_api_gateway.types.tls_config
    import capo_api_gateway.types.untag_resource_request
    import capo_api_gateway.types.update_account_request
    import capo_api_gateway.types.update_api_key_request
    import capo_api_gateway.types.update_authorizer_request
    import capo_api_gateway.types.update_base_path_mapping_request
    import capo_api_gateway.types.update_client_certificate_request
    import capo_api_gateway.types.update_deployment_request
    import capo_api_gateway.types.update_documentation_part_request
    import capo_api_gateway.types.update_documentation_version_request
    import capo_api_gateway.types.update_domain_name_request
    import capo_api_gateway.types.update_gateway_response_request
    import capo_api_gateway.types.update_integration_request
    import capo_api_gateway.types.update_integration_response_request
    import capo_api_gateway.types.update_method_request
    import capo_api_gateway.types.update_method_response_request
    import capo_api_gateway.types.update_model_request
    import capo_api_gateway.types.update_request_validator_request
    import capo_api_gateway.types.update_resource_request
    import capo_api_gateway.types.update_rest_api_request
    import capo_api_gateway.types.update_stage_request
    import capo_api_gateway.types.update_usage_plan_request
    import capo_api_gateway.types.update_usage_request
    import capo_api_gateway.types.update_vpc_link_request
    import capo_api_gateway.types.usage
    import capo_api_gateway.types.usage_plan
    import capo_api_gateway.types.usage_plan_key
    import capo_api_gateway.types.usage_plan_keys
    import capo_api_gateway.types.usage_plans
    import capo_api_gateway.types.vpc_link
    import capo_api_gateway.types.vpc_links


class APIGatewayClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class APIGatewayClient:
    """A client for the ``APIGateway`` service.

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
        self._config = APIGatewayClientConfig(
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
        self, config_overrides: Optional[APIGatewayClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: APIGatewayClientConfig = config_overrides or {}
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

    def create_api_key(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        name: Optional["capo_api_gateway.types.string.String"] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        enabled: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        generate_distinct_id: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        value: Optional["capo_api_gateway.types.string.String"] = None,
        stage_keys: Optional[
            "capo_api_gateway.types.list_of_stage_keys.ListOfStageKeys"
        ] = None,
        customer_id: Optional["capo_api_gateway.types.string.String"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.api_key.ApiKey":
        """<p>Create an ApiKey resource. </p>

        Args:
            name: <p>The name of the ApiKey.</p>
            description: <p>The description of the ApiKey.</p>
            enabled: <p>Specifies whether the ApiKey can be used by callers.</p>
            generate_distinct_id: <p>Specifies whether (<code>true</code>) or not (<code>false</code>) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</p>
            value: <p>Specifies a value of the API key.</p>
            stage_keys: <p>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</p>
            customer_id: <p>An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_api_key_request.CreateApiKeyRequest]",
        ) -> OperationResponse["capo_api_gateway.types.api_key.ApiKey"]:
            import capo_api_gateway._operations.backplane_control_service.create_api_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_api_key.create_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_api_key_request.CreateApiKeyRequest = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if enabled is not None:
            input_["enabled"] = enabled
        if generate_distinct_id is not None:
            input_["generate_distinct_id"] = generate_distinct_id
        if value is not None:
            input_["value"] = value
        if stage_keys is not None:
            input_["stage_keys"] = stage_keys
        if customer_id is not None:
            input_["customer_id"] = customer_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_authorizer(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        name: "capo_api_gateway.types.string.String",
        type: "capo_api_gateway.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        provider_ar_ns: Optional[
            "capo_api_gateway.types.list_of_ar_ns.ListOfARNs"
        ] = None,
        auth_type: Optional["capo_api_gateway.types.string.String"] = None,
        authorizer_uri: Optional["capo_api_gateway.types.string.String"] = None,
        authorizer_credentials: Optional["capo_api_gateway.types.string.String"] = None,
        identity_source: Optional["capo_api_gateway.types.string.String"] = None,
        identity_validation_expression: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        authorizer_result_ttl_in_seconds: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.authorizer.Authorizer":
        """<p>Adds a new Authorizer resource to an existing RestApi resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            name: <p>The name of the authorizer.</p>
            type: <p>The authorizer type. Valid values are <code>TOKEN</code> for a Lambda function using a single authorization token submitted in a custom header, <code>REQUEST</code> for a Lambda function using incoming request parameters, and <code>COGNITO_USER_POOLS</code> for using an Amazon Cognito user pool.</p>
            provider_ar_ns: <p>A list of the Amazon Cognito user pool ARNs for the <code>COGNITO_USER_POOLS</code> authorizer. Each element is of this format: <code>arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</code>. For a <code>TOKEN</code> or <code>REQUEST</code> authorizer, this is not defined. </p>
            auth_type: <p>Optional customer-defined field, used in OpenAPI imports and exports without functional impact.</p>
            authorizer_uri: <p>Specifies the authorizer's Uniform Resource Identifier (URI). For <code>TOKEN</code> or <code>REQUEST</code> authorizers, this must be a well-formed Lambda function URI, for example, <code>arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations</code>. In general, the URI has this form <code>arn:aws:apigateway:{region}:lambda:path/{service_api}</code>, where <code>{region}</code> is the same as the region hosting the Lambda function, <code>path</code> indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial <code>/</code>. For Lambda functions, this is usually of the form <code>/2015-03-31/functions/[FunctionARN]/invocations</code>.</p>
            authorizer_credentials: <p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.</p>
            identity_source: <p>The identity source for which authorization is requested. For a <code>TOKEN</code> or <code>COGNITO_USER_POOLS</code> authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is <code>Auth</code>, the header mapping expression is <code>method.request.header.Auth</code>. For the <code>REQUEST</code> authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an <code>Auth</code> header, a <code>Name</code> query string parameter are defined as identity sources, this value is <code>method.request.header.Auth, method.request.querystring.Name</code>. These parameters will be used to derive the authorization caching key and to perform runtime validation of the <code>REQUEST</code> authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.</p>
            identity_validation_expression: <p>A validation expression for the incoming identity token. For <code>TOKEN</code> authorizers, this value is a regular expression. For <code>COGNITO_USER_POOLS</code> authorizers, API Gateway will match the <code>aud</code> field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the <code>REQUEST</code> authorizer.</p>
            authorizer_result_ttl_in_seconds: <p>The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_authorizer_request.CreateAuthorizerRequest]",
        ) -> OperationResponse["capo_api_gateway.types.authorizer.Authorizer"]:
            import capo_api_gateway._operations.backplane_control_service.create_authorizer

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_authorizer.create_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_authorizer_request.CreateAuthorizerRequest = {
            "rest_api_id": rest_api_id,
            "name": name,
            "type": type,
        }
        if provider_ar_ns is not None:
            input_["provider_ar_ns"] = provider_ar_ns
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if authorizer_uri is not None:
            input_["authorizer_uri"] = authorizer_uri
        if authorizer_credentials is not None:
            input_["authorizer_credentials"] = authorizer_credentials
        if identity_source is not None:
            input_["identity_source"] = identity_source
        if identity_validation_expression is not None:
            input_["identity_validation_expression"] = identity_validation_expression
        if authorizer_result_ttl_in_seconds is not None:
            input_["authorizer_result_ttl_in_seconds"] = (
                authorizer_result_ttl_in_seconds
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_base_path_mapping(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
        base_path: Optional["capo_api_gateway.types.string.String"] = None,
        stage: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.base_path_mapping.BasePathMapping":
        """<p>Creates a new BasePathMapping resource.</p>

        Args:
            domain_name: <p>The domain name of the BasePathMapping resource to create.</p>
            domain_name_id: <p>The identifier for the domain name resource. Required for private custom domain names.</p>
            base_path: <p>The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify a base path name after the domain name.</p>
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage: <p>The name of the API's stage that you want to use for this mapping. Specify '(none)' if you want callers to explicitly specify the stage name after any base path name.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_base_path_mapping_request.CreateBasePathMappingRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.base_path_mapping.BasePathMapping"
        ]:
            import capo_api_gateway._operations.backplane_control_service.create_base_path_mapping

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_base_path_mapping.create_base_path_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_base_path_mapping_request.CreateBasePathMappingRequest = {
            "domain_name": domain_name,
            "rest_api_id": rest_api_id,
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if base_path is not None:
            input_["base_path"] = base_path
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        stage_name: Optional["capo_api_gateway.types.string.String"] = None,
        stage_description: Optional["capo_api_gateway.types.string.String"] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        cache_cluster_enabled: Optional[
            "capo_api_gateway.types.nullable_boolean.NullableBoolean"
        ] = None,
        cache_cluster_size: Optional[
            "capo_api_gateway.types.cache_cluster_size.CacheClusterSize"
        ] = None,
        variables: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        canary_settings: Optional[
            "capo_api_gateway.types.deployment_canary_settings.DeploymentCanarySettings"
        ] = None,
        tracing_enabled: Optional[
            "capo_api_gateway.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_api_gateway.types.deployment.Deployment":
        """<p>Creates a Deployment resource, which makes a specified RestApi callable over the internet.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage resource for the Deployment resource to create.</p>
            stage_description: <p>The description of the Stage resource for the Deployment resource to create.</p>
            description: <p>The description for the Deployment resource to create.</p>
            cache_cluster_enabled: <p>Enables a cache cluster for the Stage resource specified in the input.</p>
            cache_cluster_size: <p>The stage's cache capacity in GB. For more information about choosing a cache size, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html">Enabling API caching to enhance responsiveness</a>.</p>
            variables: <p>A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9-._~:/?#&=,]+</code>.</p>
            canary_settings: <p>The input configuration for the canary deployment when the deployment is a canary release deployment. </p>
            tracing_enabled: <p>Specifies whether active tracing with X-ray is enabled for the Stage.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is not available. For details see the accompanying error message. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> OperationResponse["capo_api_gateway.types.deployment.Deployment"]:
            import capo_api_gateway._operations.backplane_control_service.create_deployment

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_deployment_request.CreateDeploymentRequest = {
            "rest_api_id": rest_api_id
        }
        if stage_name is not None:
            input_["stage_name"] = stage_name
        if stage_description is not None:
            input_["stage_description"] = stage_description
        if description is not None:
            input_["description"] = description
        if cache_cluster_enabled is not None:
            input_["cache_cluster_enabled"] = cache_cluster_enabled
        if cache_cluster_size is not None:
            input_["cache_cluster_size"] = cache_cluster_size
        if variables is not None:
            input_["variables"] = variables
        if canary_settings is not None:
            input_["canary_settings"] = canary_settings
        if tracing_enabled is not None:
            input_["tracing_enabled"] = tracing_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_documentation_part(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        location: "capo_api_gateway.types.documentation_part_location.DocumentationPartLocation",
        properties: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.documentation_part.DocumentationPart":
        """<p>Creates a documentation part.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            location: <p>The location of the targeted API entity of the to-be-created documentation part.</p>
            properties: <p>The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_documentation_part_request.CreateDocumentationPartRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_part.DocumentationPart"
        ]:
            import capo_api_gateway._operations.backplane_control_service.create_documentation_part

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_documentation_part.create_documentation_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_documentation_part_request.CreateDocumentationPartRequest = {
            "rest_api_id": rest_api_id,
            "location": location,
            "properties": properties,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_documentation_version(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_version: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        stage_name: Optional["capo_api_gateway.types.string.String"] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.documentation_version.DocumentationVersion":
        """<p>Creates a documentation version</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_version: <p>The version identifier of the new snapshot.</p>
            stage_name: <p>The stage name to be associated with the new documentation snapshot.</p>
            description: <p>A description about the new documentation snapshot.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_documentation_version_request.CreateDocumentationVersionRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_version.DocumentationVersion"
        ]:
            import capo_api_gateway._operations.backplane_control_service.create_documentation_version

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_documentation_version.create_documentation_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_documentation_version_request.CreateDocumentationVersionRequest = {
            "rest_api_id": rest_api_id,
            "documentation_version": documentation_version,
        }
        if stage_name is not None:
            input_["stage_name"] = stage_name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain_name(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        certificate_name: Optional["capo_api_gateway.types.string.String"] = None,
        certificate_body: Optional["capo_api_gateway.types.string.String"] = None,
        certificate_private_key: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        certificate_chain: Optional["capo_api_gateway.types.string.String"] = None,
        certificate_arn: Optional["capo_api_gateway.types.string.String"] = None,
        regional_certificate_name: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        regional_certificate_arn: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        endpoint_configuration: Optional[
            "capo_api_gateway.types.endpoint_configuration.EndpointConfiguration"
        ] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        security_policy: Optional[
            "capo_api_gateway.types.security_policy.SecurityPolicy"
        ] = None,
        endpoint_access_mode: Optional[
            "capo_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
        ] = None,
        mutual_tls_authentication: Optional[
            "capo_api_gateway.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
        ] = None,
        ownership_verification_certificate_arn: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        policy: Optional["capo_api_gateway.types.string.String"] = None,
        routing_mode: Optional[
            "capo_api_gateway.types.routing_mode.RoutingMode"
        ] = None,
    ) -> "capo_api_gateway.types.domain_name.DomainName":
        """<p>Creates a new domain name.</p>

        Args:
            domain_name: <p>The name of the DomainName resource.</p>
            certificate_name: <p>The user-friendly name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.</p>
            certificate_body: <p>[Deprecated] The body of the server certificate that will be used by edge-optimized endpoint or private endpoint for this domain name provided by your certificate authority.</p>
            certificate_private_key: <p>[Deprecated] Your edge-optimized endpoint's domain name certificate's private key.</p>
            certificate_chain: <p>[Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines, used by an edge-optimized endpoint for this domain name. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.</p>
            certificate_arn: <p>The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. Certificate Manager is the only supported source.</p>
            regional_certificate_name: <p>The user-friendly name of the certificate that will be used by regional endpoint for this domain name.</p>
            regional_certificate_arn: <p>The reference to an Amazon Web Services-managed certificate that will be used by regional endpoint for this domain name. Certificate Manager is the only supported source.</p>
            endpoint_configuration: <p>The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name. </p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>
            security_policy: <p>The Transport Layer Security (TLS) version + cipher suite for this DomainName.</p>
            endpoint_access_mode: <p> The endpoint access mode of the DomainName. Only available for DomainNames that use security policies that start with <code>SecurityPolicy_</code>. </p>
            ownership_verification_certificate_arn: <p>The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.</p>
            policy: <p>A stringified JSON policy document that applies to the <code>execute-api</code> service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.</p>
            routing_mode: <p> The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your private APIs. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_domain_name_request.CreateDomainNameRequest]",
        ) -> OperationResponse["capo_api_gateway.types.domain_name.DomainName"]:
            import capo_api_gateway._operations.backplane_control_service.create_domain_name

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_domain_name.create_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_domain_name_request.CreateDomainNameRequest = {
            "domain_name": domain_name
        }
        if certificate_name is not None:
            input_["certificate_name"] = certificate_name
        if certificate_body is not None:
            input_["certificate_body"] = certificate_body
        if certificate_private_key is not None:
            input_["certificate_private_key"] = certificate_private_key
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if regional_certificate_name is not None:
            input_["regional_certificate_name"] = regional_certificate_name
        if regional_certificate_arn is not None:
            input_["regional_certificate_arn"] = regional_certificate_arn
        if endpoint_configuration is not None:
            input_["endpoint_configuration"] = endpoint_configuration
        if tags is not None:
            input_["tags"] = tags
        if security_policy is not None:
            input_["security_policy"] = security_policy
        if endpoint_access_mode is not None:
            input_["endpoint_access_mode"] = endpoint_access_mode
        if mutual_tls_authentication is not None:
            input_["mutual_tls_authentication"] = mutual_tls_authentication
        if ownership_verification_certificate_arn is not None:
            input_["ownership_verification_certificate_arn"] = (
                ownership_verification_certificate_arn
            )
        if policy is not None:
            input_["policy"] = policy
        if routing_mode is not None:
            input_["routing_mode"] = routing_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain_name_access_association(
        self,
        domain_name_arn: "capo_api_gateway.types.string.String",
        access_association_source_type: "capo_api_gateway.types.access_association_source_type.AccessAssociationSourceType",
        access_association_source: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.domain_name_access_association.DomainNameAccessAssociation":
        """<p> Creates a domain name access association resource between an access association source and a private custom domain name.</p>

        Args:
            domain_name_arn: <p> The ARN of the domain name. </p>
            access_association_source_type: <p> The type of the domain name access association source. </p>
            access_association_source: <p> The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID. </p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_domain_name_access_association_request.CreateDomainNameAccessAssociationRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.domain_name_access_association.DomainNameAccessAssociation"
        ]:
            import capo_api_gateway._operations.backplane_control_service.create_domain_name_access_association

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_domain_name_access_association.create_domain_name_access_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_domain_name_access_association_request.CreateDomainNameAccessAssociationRequest = {
            "domain_name_arn": domain_name_arn,
            "access_association_source_type": access_association_source_type,
            "access_association_source": access_association_source,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_model(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        name: "capo_api_gateway.types.string.String",
        content_type: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        schema: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.model.Model":
        """<p>Adds a new Model resource to an existing RestApi resource.</p>

        Args:
            rest_api_id: <p>The RestApi identifier under which the Model will be created.</p>
            name: <p>The name of the model. Must be alphanumeric.</p>
            description: <p>The description of the model.</p>
            schema: <p>The schema for the model. For <code>application/json</code> models, this should be JSON schema draft 4 model. The maximum size of the model is 400 KB.</p>
            content_type: <p>The content-type for the model.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_model_request.CreateModelRequest]",
        ) -> OperationResponse["capo_api_gateway.types.model.Model"]:
            import capo_api_gateway._operations.backplane_control_service.create_model

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_model.create_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_model_request.CreateModelRequest = {
            "rest_api_id": rest_api_id,
            "name": name,
            "content_type": content_type,
        }
        if description is not None:
            input_["description"] = description
        if schema is not None:
            input_["schema"] = schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_request_validator(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        name: Optional["capo_api_gateway.types.string.String"] = None,
        validate_request_body: Optional[
            "capo_api_gateway.types.boolean.Boolean"
        ] = None,
        validate_request_parameters: Optional[
            "capo_api_gateway.types.boolean.Boolean"
        ] = None,
    ) -> "capo_api_gateway.types.request_validator.RequestValidator":
        """<p>Creates a RequestValidator of a given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            name: <p>The name of the to-be-created RequestValidator.</p>
            validate_request_body: <p>A Boolean flag to indicate whether to validate request body according to the configured model schema for the method (<code>true</code>) or not (<code>false</code>).</p>
            validate_request_parameters: <p>A Boolean flag to indicate whether to validate request parameters, <code>true</code>, or not <code>false</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_request_validator_request.CreateRequestValidatorRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.request_validator.RequestValidator"
        ]:
            import capo_api_gateway._operations.backplane_control_service.create_request_validator

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_request_validator.create_request_validator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_request_validator_request.CreateRequestValidatorRequest = {
            "rest_api_id": rest_api_id
        }
        if name is not None:
            input_["name"] = name
        if validate_request_body is not None:
            input_["validate_request_body"] = validate_request_body
        if validate_request_parameters is not None:
            input_["validate_request_parameters"] = validate_request_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resource(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        parent_id: "capo_api_gateway.types.string.String",
        path_part: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.resource.Resource":
        """<p>Creates a Resource resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            parent_id: <p>The parent resource's identifier.</p>
            path_part: <p>The last path segment for this resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_resource_request.CreateResourceRequest]",
        ) -> OperationResponse["capo_api_gateway.types.resource.Resource"]:
            import capo_api_gateway._operations.backplane_control_service.create_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_resource.create_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_resource_request.CreateResourceRequest = {
            "rest_api_id": rest_api_id,
            "parent_id": parent_id,
            "path_part": path_part,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rest_api(
        self,
        name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        version: Optional["capo_api_gateway.types.string.String"] = None,
        clone_from: Optional["capo_api_gateway.types.string.String"] = None,
        binary_media_types: Optional[
            "capo_api_gateway.types.list_of_string.ListOfString"
        ] = None,
        minimum_compression_size: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        api_key_source: Optional[
            "capo_api_gateway.types.api_key_source_type.ApiKeySourceType"
        ] = None,
        endpoint_configuration: Optional[
            "capo_api_gateway.types.endpoint_configuration.EndpointConfiguration"
        ] = None,
        policy: Optional["capo_api_gateway.types.string.String"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        disable_execute_api_endpoint: Optional[
            "capo_api_gateway.types.boolean.Boolean"
        ] = None,
        security_policy: Optional[
            "capo_api_gateway.types.security_policy.SecurityPolicy"
        ] = None,
        endpoint_access_mode: Optional[
            "capo_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
        ] = None,
    ) -> "capo_api_gateway.types.rest_api.RestApi":
        """<p>Creates a new RestApi resource.</p>

        Args:
            name: <p>The name of the RestApi.</p>
            description: <p>The description of the RestApi.</p>
            version: <p>A version identifier for the API.</p>
            clone_from: <p>The ID of the RestApi that you want to clone from.</p>
            binary_media_types: <p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>
            minimum_compression_size: <p>A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.</p>
            api_key_source: <p>The source of the API key for metering requests according to a usage plan. Valid values are: <code>HEADER</code> to read the API key from the <code>X-API-Key</code> header of a request. <code>AUTHORIZER</code> to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.</p>
            endpoint_configuration: <p>The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API. </p>
            policy: <p>A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>
            disable_execute_api_endpoint: <p>Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default <code>https://{api_id}.execute-api.{region}.amazonaws.com</code> endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint</p>
            security_policy: <p> The Transport Layer Security (TLS) version + cipher suite for this RestApi. </p>
            endpoint_access_mode: <p> The endpoint access mode of the RestApi. Only available for RestApis that use security policies that start with <code>SecurityPolicy_</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_rest_api_request.CreateRestApiRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_api.RestApi"]:
            import capo_api_gateway._operations.backplane_control_service.create_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_rest_api.create_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_rest_api_request.CreateRestApiRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if version is not None:
            input_["version"] = version
        if clone_from is not None:
            input_["clone_from"] = clone_from
        if binary_media_types is not None:
            input_["binary_media_types"] = binary_media_types
        if minimum_compression_size is not None:
            input_["minimum_compression_size"] = minimum_compression_size
        if api_key_source is not None:
            input_["api_key_source"] = api_key_source
        if endpoint_configuration is not None:
            input_["endpoint_configuration"] = endpoint_configuration
        if policy is not None:
            input_["policy"] = policy
        if tags is not None:
            input_["tags"] = tags
        if disable_execute_api_endpoint is not None:
            input_["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if security_policy is not None:
            input_["security_policy"] = security_policy
        if endpoint_access_mode is not None:
            input_["endpoint_access_mode"] = endpoint_access_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stage(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        deployment_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        cache_cluster_enabled: Optional[
            "capo_api_gateway.types.boolean.Boolean"
        ] = None,
        cache_cluster_size: Optional[
            "capo_api_gateway.types.cache_cluster_size.CacheClusterSize"
        ] = None,
        variables: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        documentation_version: Optional["capo_api_gateway.types.string.String"] = None,
        canary_settings: Optional[
            "capo_api_gateway.types.canary_settings.CanarySettings"
        ] = None,
        tracing_enabled: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.stage.Stage":
        """<p>Creates a new Stage resource that references a pre-existing Deployment for the API. </p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>
            deployment_id: <p>The identifier of the Deployment resource for the Stage resource.</p>
            description: <p>The description of the Stage resource.</p>
            cache_cluster_enabled: <p>Whether cache clustering is enabled for the stage.</p>
            cache_cluster_size: <p>The stage's cache capacity in GB. For more information about choosing a cache size, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html">Enabling API caching to enhance responsiveness</a>.</p>
            variables: <p>A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9-._~:/?#&=,]+</code>.</p>
            documentation_version: <p>The version of the associated API documentation.</p>
            canary_settings: <p>The canary deployment settings of this stage.</p>
            tracing_enabled: <p>Specifies whether active tracing with X-ray is enabled for the Stage.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_stage_request.CreateStageRequest]",
        ) -> OperationResponse["capo_api_gateway.types.stage.Stage"]:
            import capo_api_gateway._operations.backplane_control_service.create_stage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_stage.create_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_stage_request.CreateStageRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
            "deployment_id": deployment_id,
        }
        if description is not None:
            input_["description"] = description
        if cache_cluster_enabled is not None:
            input_["cache_cluster_enabled"] = cache_cluster_enabled
        if cache_cluster_size is not None:
            input_["cache_cluster_size"] = cache_cluster_size
        if variables is not None:
            input_["variables"] = variables
        if documentation_version is not None:
            input_["documentation_version"] = documentation_version
        if canary_settings is not None:
            input_["canary_settings"] = canary_settings
        if tracing_enabled is not None:
            input_["tracing_enabled"] = tracing_enabled
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_usage_plan(
        self,
        name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        api_stages: Optional[
            "capo_api_gateway.types.list_of_api_stage.ListOfApiStage"
        ] = None,
        throttle: Optional[
            "capo_api_gateway.types.throttle_settings.ThrottleSettings"
        ] = None,
        quota: Optional["capo_api_gateway.types.quota_settings.QuotaSettings"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.usage_plan.UsagePlan":
        """<p>Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload. </p>

        Args:
            name: <p>The name of the usage plan.</p>
            description: <p>The description of the usage plan.</p>
            api_stages: <p>The associated API stages of the usage plan.</p>
            throttle: <p>The throttling limits of the usage plan.</p>
            quota: <p>The quota of the usage plan.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_usage_plan_request.CreateUsagePlanRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan.UsagePlan"]:
            import capo_api_gateway._operations.backplane_control_service.create_usage_plan

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_usage_plan.create_usage_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_usage_plan_request.CreateUsagePlanRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if api_stages is not None:
            input_["api_stages"] = api_stages
        if throttle is not None:
            input_["throttle"] = throttle
        if quota is not None:
            input_["quota"] = quota
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_usage_plan_key(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        key_id: "capo_api_gateway.types.string.String",
        key_type: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.usage_plan_key.UsagePlanKey":
        """<p>Creates a usage plan key for adding an existing API key to a usage plan.</p>

        Args:
            usage_plan_id: <p>The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.</p>
            key_id: <p>The identifier of a UsagePlanKey resource for a plan customer.</p>
            key_type: <p>The type of a UsagePlanKey resource for a plan customer.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_usage_plan_key_request.CreateUsagePlanKeyRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan_key.UsagePlanKey"]:
            import capo_api_gateway._operations.backplane_control_service.create_usage_plan_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_usage_plan_key.create_usage_plan_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_usage_plan_key_request.CreateUsagePlanKeyRequest = {
            "usage_plan_id": usage_plan_id,
            "key_id": key_id,
            "key_type": key_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_link(
        self,
        name: "capo_api_gateway.types.string.String",
        target_arns: "capo_api_gateway.types.list_of_string.ListOfString",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.vpc_link.VpcLink":
        """<p>Creates a VPC link, under the caller's account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.</p>

        Args:
            name: <p>The name used to label and identify the VPC link.</p>
            description: <p>The description of the VPC link.</p>
            target_arns: <p>The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.create_vpc_link_request.CreateVpcLinkRequest]",
        ) -> OperationResponse["capo_api_gateway.types.vpc_link.VpcLink"]:
            import capo_api_gateway._operations.backplane_control_service.create_vpc_link

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.create_vpc_link.create_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.create_vpc_link_request.CreateVpcLinkRequest = {
            "name": name,
            "target_arns": target_arns,
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

    def delete_api_key(
        self,
        api_key: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes the ApiKey resource.</p>

        Args:
            api_key: <p>The identifier of the ApiKey resource to be deleted.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_api_key_request.DeleteApiKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_api_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_api_key.delete_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_api_key_request.DeleteApiKeyRequest = {
            "api_key": api_key
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_authorizer(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        authorizer_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes an existing Authorizer resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            authorizer_id: <p>The identifier of the Authorizer resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_authorizer_request.DeleteAuthorizerRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_authorizer

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_authorizer.delete_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_authorizer_request.DeleteAuthorizerRequest = {
            "rest_api_id": rest_api_id,
            "authorizer_id": authorizer_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_base_path_mapping(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        base_path: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> None:
        """<p>Deletes the BasePathMapping resource.</p>

        Args:
            domain_name: <p>The domain name of the BasePathMapping resource to delete.</p>
            domain_name_id: <p> The identifier for the domain name resource. Supported only for private custom domain names. </p>
            base_path: <p>The base path name of the BasePathMapping resource to delete.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_base_path_mapping_request.DeleteBasePathMappingRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_base_path_mapping

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_base_path_mapping.delete_base_path_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_base_path_mapping_request.DeleteBasePathMappingRequest = {
            "domain_name": domain_name,
            "base_path": base_path,
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_client_certificate(
        self,
        client_certificate_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes the ClientCertificate resource.</p>

        Args:
            client_certificate_id: <p>The identifier of the ClientCertificate resource to be deleted.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_client_certificate_request.DeleteClientCertificateRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_client_certificate

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_client_certificate.delete_client_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_client_certificate_request.DeleteClientCertificateRequest = {
            "client_certificate_id": client_certificate_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_deployment(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        deployment_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a Deployment resource. Deleting a deployment will only succeed if there are no Stage resources associated with it.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            deployment_id: <p>The identifier of the Deployment resource to delete.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_deployment_request.DeleteDeploymentRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_deployment

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_deployment_request.DeleteDeploymentRequest = {
            "rest_api_id": rest_api_id,
            "deployment_id": deployment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_documentation_part(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_part_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a documentation part</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_part_id: <p>The identifier of the to-be-deleted documentation part.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_documentation_part_request.DeleteDocumentationPartRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_documentation_part

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_documentation_part.delete_documentation_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_documentation_part_request.DeleteDocumentationPartRequest = {
            "rest_api_id": rest_api_id,
            "documentation_part_id": documentation_part_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_documentation_version(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_version: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a documentation version.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_version: <p>The version identifier of a to-be-deleted documentation snapshot.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_documentation_version_request.DeleteDocumentationVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_documentation_version

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_documentation_version.delete_documentation_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_documentation_version_request.DeleteDocumentationVersionRequest = {
            "rest_api_id": rest_api_id,
            "documentation_version": documentation_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_name(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> None:
        """<p>Deletes the DomainName resource.</p>

        Args:
            domain_name: <p>The name of the DomainName resource to be deleted.</p>
            domain_name_id: <p> The identifier for the domain name resource. Supported only for private custom domain names. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_domain_name_request.DeleteDomainNameRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_domain_name

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_domain_name.delete_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_domain_name_request.DeleteDomainNameRequest = {
            "domain_name": domain_name
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_name_access_association(
        self,
        domain_name_access_association_arn: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p> Deletes the DomainNameAccessAssociation resource.</p> <p>Only the AWS account that created the DomainNameAccessAssociation resource can delete it. To stop an access association source in another AWS account from accessing your private custom domain name, use the RejectDomainNameAccessAssociation operation.</p>

        Args:
            domain_name_access_association_arn: <p> The ARN of the domain name access association resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_domain_name_access_association_request.DeleteDomainNameAccessAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_domain_name_access_association

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_domain_name_access_association.delete_domain_name_access_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_domain_name_access_association_request.DeleteDomainNameAccessAssociationRequest = {
            "domain_name_access_association_arn": domain_name_access_association_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Clears any customization of a GatewayResponse of a specified response type on the given RestApi and resets it with the default settings.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            response_type: <p>The response type of the associated GatewayResponse.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_gateway_response_request.DeleteGatewayResponseRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_gateway_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_gateway_response.delete_gateway_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_gateway_response_request.DeleteGatewayResponseRequest = {
            "rest_api_id": rest_api_id,
            "response_type": response_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_integration(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Represents a delete integration.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a delete integration request's resource identifier.</p>
            http_method: <p>Specifies a delete integration request's HTTP method.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_integration

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_integration_request.DeleteIntegrationRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_integration_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Represents a delete integration response.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a delete integration response request's resource identifier.</p>
            http_method: <p>Specifies a delete integration response request's HTTP method.</p>
            status_code: <p>Specifies a delete integration response request's status code.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_integration_response_request.DeleteIntegrationResponseRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_integration_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_integration_response.delete_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_integration_response_request.DeleteIntegrationResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_method(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes an existing Method resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the Method resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>

        Raises:
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_method_request.DeleteMethodRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_method

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_method.delete_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_method_request.DeleteMethodRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_method_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes an existing MethodResponse resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the MethodResponse resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>
            status_code: <p>The status code identifier for the MethodResponse resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_method_response_request.DeleteMethodResponseRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_method_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_method_response.delete_method_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_method_response_request.DeleteMethodResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_model(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        model_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a model.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            model_name: <p>The name of the model to delete.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_model_request.DeleteModelRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_model

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_model.delete_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_model_request.DeleteModelRequest = {
            "rest_api_id": rest_api_id,
            "model_name": model_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_request_validator(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        request_validator_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a RequestValidator of a given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            request_validator_id: <p>The identifier of the RequestValidator to be deleted.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_request_validator_request.DeleteRequestValidatorRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_request_validator

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_request_validator.delete_request_validator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_request_validator_request.DeleteRequestValidatorRequest = {
            "rest_api_id": rest_api_id,
            "request_validator_id": request_validator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a Resource resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The identifier of the Resource resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_resource_request.DeleteResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_resource.delete_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_resource_request.DeleteResourceRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rest_api(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified API.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_rest_api_request.DeleteRestApiRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_rest_api.delete_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_rest_api_request.DeleteRestApiRequest = {
            "rest_api_id": rest_api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stage(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a Stage resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage resource to delete.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_stage_request.DeleteStageRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_stage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_stage.delete_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_stage_request.DeleteStageRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_usage_plan(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a usage plan of a given plan Id.</p>

        Args:
            usage_plan_id: <p>The Id of the to-be-deleted usage plan.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_usage_plan_request.DeleteUsagePlanRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_usage_plan

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_usage_plan.delete_usage_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_usage_plan_request.DeleteUsagePlanRequest = {
            "usage_plan_id": usage_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_usage_plan_key(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        key_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes a usage plan key and remove the underlying API key from the associated usage plan.</p>

        Args:
            usage_plan_id: <p>The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.</p>
            key_id: <p>The Id of the UsagePlanKey resource to be deleted.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_usage_plan_key_request.DeleteUsagePlanKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_usage_plan_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_usage_plan_key.delete_usage_plan_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_usage_plan_key_request.DeleteUsagePlanKeyRequest = {
            "usage_plan_id": usage_plan_id,
            "key_id": key_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_link(
        self,
        vpc_link_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Deletes an existing VpcLink of a specified identifier.</p>

        Args:
            vpc_link_id: <p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.delete_vpc_link_request.DeleteVpcLinkRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.delete_vpc_link

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.delete_vpc_link.delete_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.delete_vpc_link_request.DeleteVpcLinkRequest = {
            "vpc_link_id": vpc_link_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def flush_stage_authorizers_cache(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Flushes all authorizer cache entries on a stage.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the stage to flush.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.flush_stage_authorizers_cache_request.FlushStageAuthorizersCacheRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.flush_stage_authorizers_cache

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.flush_stage_authorizers_cache.flush_stage_authorizers_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.flush_stage_authorizers_cache_request.FlushStageAuthorizersCacheRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def flush_stage_cache(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Flushes a stage's cache.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the stage to flush its cache.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.flush_stage_cache_request.FlushStageCacheRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.flush_stage_cache

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.flush_stage_cache.flush_stage_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.flush_stage_cache_request.FlushStageCacheRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_client_certificate(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        description: Optional["capo_api_gateway.types.string.String"] = None,
        tags: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.client_certificate.ClientCertificate":
        """<p>Generates a ClientCertificate resource.</p>

        Args:
            description: <p>The description of the ClientCertificate.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.generate_client_certificate_request.GenerateClientCertificateRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.client_certificate.ClientCertificate"
        ]:
            import capo_api_gateway._operations.backplane_control_service.generate_client_certificate

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.generate_client_certificate.generate_client_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.generate_client_certificate_request.GenerateClientCertificateRequest = {}
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

    def get_account(
        self, *, config_overrides: Optional[APIGatewayClientConfig] = None
    ) -> "capo_api_gateway.types.account.Account":
        """<p>Gets information about the current Account resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_account_request.GetAccountRequest]",
        ) -> OperationResponse["capo_api_gateway.types.account.Account"]:
            import capo_api_gateway._operations.backplane_control_service.get_account

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_account.get_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_account_request.GetAccountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_key(
        self,
        api_key: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        include_value: Optional[
            "capo_api_gateway.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_api_gateway.types.api_key.ApiKey":
        """<p>Gets information about the current ApiKey resource.</p>

        Args:
            api_key: <p>The identifier of the ApiKey resource.</p>
            include_value: <p>A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains the key value.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_api_key_request.GetApiKeyRequest]",
        ) -> OperationResponse["capo_api_gateway.types.api_key.ApiKey"]:
            import capo_api_gateway._operations.backplane_control_service.get_api_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_api_key.get_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_api_key_request.GetApiKeyRequest = {
            "api_key": api_key
        }
        if include_value is not None:
            input_["include_value"] = include_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_keys(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        name_query: Optional["capo_api_gateway.types.string.String"] = None,
        customer_id: Optional["capo_api_gateway.types.string.String"] = None,
        include_values: Optional[
            "capo_api_gateway.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_api_gateway.types.api_keys.ApiKeys":
        """<p>Gets information about the current ApiKeys resource.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>
            name_query: <p>The name of queried API keys.</p>
            customer_id: <p>The identifier of a customer in Amazon Web Services Marketplace or an external system, such as a developer portal.</p>
            include_values: <p>A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains key values.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_api_keys_request.GetApiKeysRequest]",
        ) -> OperationResponse["capo_api_gateway.types.api_keys.ApiKeys"]:
            import capo_api_gateway._operations.backplane_control_service.get_api_keys

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_api_keys.get_api_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_api_keys_request.GetApiKeysRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if name_query is not None:
            input_["name_query"] = name_query
        if customer_id is not None:
            input_["customer_id"] = customer_id
        if include_values is not None:
            input_["include_values"] = include_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_api_keys(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        name_query: Optional["capo_api_gateway.types.string.String"] = None,
        customer_id: Optional["capo_api_gateway.types.string.String"] = None,
        include_values: Optional[
            "capo_api_gateway.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.api_key.ApiKey]":
        _token = position
        while True:
            _response = self.get_api_keys(
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
                name_query=name_query,
                customer_id=customer_id,
                include_values=include_values,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_authorizer(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        authorizer_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.authorizer.Authorizer":
        """<p>Describe an existing Authorizer resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            authorizer_id: <p>The identifier of the Authorizer resource.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_authorizer_request.GetAuthorizerRequest]",
        ) -> OperationResponse["capo_api_gateway.types.authorizer.Authorizer"]:
            import capo_api_gateway._operations.backplane_control_service.get_authorizer

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_authorizer.get_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_authorizer_request.GetAuthorizerRequest = {
            "rest_api_id": rest_api_id,
            "authorizer_id": authorizer_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_authorizers(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.authorizers.Authorizers":
        """<p>Describe an existing Authorizers resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_authorizers_request.GetAuthorizersRequest]",
        ) -> OperationResponse["capo_api_gateway.types.authorizers.Authorizers"]:
            import capo_api_gateway._operations.backplane_control_service.get_authorizers

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_authorizers.get_authorizers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_authorizers_request.GetAuthorizersRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_base_path_mapping(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        base_path: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.base_path_mapping.BasePathMapping":
        """<p>Describe a BasePathMapping resource.</p>

        Args:
            domain_name: <p>The domain name of the BasePathMapping resource to be described.</p>
            domain_name_id: <p>The identifier for the domain name resource. Supported only for private custom domain names. </p>
            base_path: <p>The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify any base path name after the domain name.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_base_path_mapping_request.GetBasePathMappingRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.base_path_mapping.BasePathMapping"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_base_path_mapping

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_base_path_mapping.get_base_path_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_base_path_mapping_request.GetBasePathMappingRequest = {
            "domain_name": domain_name,
            "base_path": base_path,
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_base_path_mappings(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.base_path_mappings.BasePathMappings":
        """<p>Represents a collection of BasePathMapping resources.</p>

        Args:
            domain_name: <p>The domain name of a BasePathMapping resource.</p>
            domain_name_id: <p> The identifier for the domain name resource. Supported only for private custom domain names. </p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_base_path_mappings_request.GetBasePathMappingsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.base_path_mappings.BasePathMappings"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_base_path_mappings

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_base_path_mappings.get_base_path_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_base_path_mappings_request.GetBasePathMappingsRequest = {
            "domain_name": domain_name
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_base_path_mappings(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.base_path_mapping.BasePathMapping]":
        _token = position
        while True:
            _response = self.get_base_path_mappings(
                domain_name,
                config_overrides=config_overrides,
                domain_name_id=domain_name_id,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_client_certificate(
        self,
        client_certificate_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.client_certificate.ClientCertificate":
        """<p>Gets information about the current ClientCertificate resource.</p>

        Args:
            client_certificate_id: <p>The identifier of the ClientCertificate resource to be described.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_client_certificate_request.GetClientCertificateRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.client_certificate.ClientCertificate"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_client_certificate

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_client_certificate.get_client_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_client_certificate_request.GetClientCertificateRequest = {
            "client_certificate_id": client_certificate_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_client_certificates(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.client_certificates.ClientCertificates":
        """<p>Gets a collection of ClientCertificate resources.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_client_certificates_request.GetClientCertificatesRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.client_certificates.ClientCertificates"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_client_certificates

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_client_certificates.get_client_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_client_certificates_request.GetClientCertificatesRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_client_certificates(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.client_certificate.ClientCertificate]":
        _token = position
        while True:
            _response = self.get_client_certificates(
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_deployment(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        deployment_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        embed: Optional["capo_api_gateway.types.list_of_string.ListOfString"] = None,
    ) -> "capo_api_gateway.types.deployment.Deployment":
        """<p>Gets information about a Deployment resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            deployment_id: <p>The identifier of the Deployment resource to get information about.</p>
            embed: <p>A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this <code>embed</code> parameter value is a list of comma-separated strings, as in <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2</code>. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the <code>"apisummary"</code> string. For example, <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is not available. For details see the accompanying error message. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_deployment_request.GetDeploymentRequest]",
        ) -> OperationResponse["capo_api_gateway.types.deployment.Deployment"]:
            import capo_api_gateway._operations.backplane_control_service.get_deployment

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_deployment_request.GetDeploymentRequest = {
            "rest_api_id": rest_api_id,
            "deployment_id": deployment_id,
        }
        if embed is not None:
            input_["embed"] = embed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployments(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.deployments.Deployments":
        """<p>Gets information about a Deployments collection.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is not available. For details see the accompanying error message. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_deployments_request.GetDeploymentsRequest]",
        ) -> OperationResponse["capo_api_gateway.types.deployments.Deployments"]:
            import capo_api_gateway._operations.backplane_control_service.get_deployments

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_deployments.get_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_deployments_request.GetDeploymentsRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_deployments(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.deployment.Deployment]":
        _token = position
        while True:
            _response = self.get_deployments(
                rest_api_id,
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_documentation_part(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_part_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.documentation_part.DocumentationPart":
        """<p>Gets a documentation part.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_part_id: <p>The string identifier of the associated RestApi.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_documentation_part_request.GetDocumentationPartRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_part.DocumentationPart"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_documentation_part

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_documentation_part.get_documentation_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_documentation_part_request.GetDocumentationPartRequest = {
            "rest_api_id": rest_api_id,
            "documentation_part_id": documentation_part_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_documentation_parts(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        type: Optional[
            "capo_api_gateway.types.documentation_part_type.DocumentationPartType"
        ] = None,
        name_query: Optional["capo_api_gateway.types.string.String"] = None,
        path: Optional["capo_api_gateway.types.string.String"] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        location_status: Optional[
            "capo_api_gateway.types.location_status_type.LocationStatusType"
        ] = None,
    ) -> "capo_api_gateway.types.documentation_parts.DocumentationParts":
        """<p>Gets documentation parts.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            type: <p>The type of API entities of the to-be-retrieved documentation parts. </p>
            name_query: <p>The name of API entities of the to-be-retrieved documentation parts.</p>
            path: <p>The path of API entities of the to-be-retrieved documentation parts.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>
            location_status: <p>The status of the API documentation parts to retrieve. Valid values are <code>DOCUMENTED</code> for retrieving DocumentationPart resources with content and <code>UNDOCUMENTED</code> for DocumentationPart resources without content.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_documentation_parts_request.GetDocumentationPartsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_parts.DocumentationParts"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_documentation_parts

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_documentation_parts.get_documentation_parts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_documentation_parts_request.GetDocumentationPartsRequest = {
            "rest_api_id": rest_api_id
        }
        if type is not None:
            input_["type"] = type
        if name_query is not None:
            input_["name_query"] = name_query
        if path is not None:
            input_["path"] = path
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if location_status is not None:
            input_["location_status"] = location_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_documentation_version(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_version: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.documentation_version.DocumentationVersion":
        """<p>Gets a documentation version.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_version: <p>The version identifier of the to-be-retrieved documentation snapshot.</p>

        Raises:
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_documentation_version_request.GetDocumentationVersionRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_version.DocumentationVersion"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_documentation_version

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_documentation_version.get_documentation_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_documentation_version_request.GetDocumentationVersionRequest = {
            "rest_api_id": rest_api_id,
            "documentation_version": documentation_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_documentation_versions(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.documentation_versions.DocumentationVersions":
        """<p>Gets documentation versions.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_documentation_versions_request.GetDocumentationVersionsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_versions.DocumentationVersions"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_documentation_versions

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_documentation_versions.get_documentation_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_documentation_versions_request.GetDocumentationVersionsRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_name(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.domain_name.DomainName":
        """<p>Represents a domain name that is contained in a simpler, more intuitive URL that can be called.</p>

        Args:
            domain_name: <p>The name of the DomainName resource.</p>
            domain_name_id: <p> The identifier for the domain name resource. Required for private custom domain names. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_domain_name_request.GetDomainNameRequest]",
        ) -> OperationResponse["capo_api_gateway.types.domain_name.DomainName"]:
            import capo_api_gateway._operations.backplane_control_service.get_domain_name

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_domain_name.get_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_domain_name_request.GetDomainNameRequest = {
            "domain_name": domain_name
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_name_access_associations(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        resource_owner: Optional[
            "capo_api_gateway.types.resource_owner.ResourceOwner"
        ] = None,
    ) -> "capo_api_gateway.types.domain_name_access_associations.DomainNameAccessAssociations":
        """<p>Represents a collection on DomainNameAccessAssociations resources.</p>

        Args:
            position: <p>The current pagination position in the paged result set. </p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500. </p>
            resource_owner: <p> The owner of the domain name access association. Use <code>SELF</code> to only list the domain name access associations owned by your own account. Use <code>OTHER_ACCOUNTS</code> to list the domain name access associations with your private custom domain names that are owned by other AWS accounts.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_domain_name_access_associations_request.GetDomainNameAccessAssociationsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.domain_name_access_associations.DomainNameAccessAssociations"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_domain_name_access_associations

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_domain_name_access_associations.get_domain_name_access_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_domain_name_access_associations_request.GetDomainNameAccessAssociationsRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_names(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        resource_owner: Optional[
            "capo_api_gateway.types.resource_owner.ResourceOwner"
        ] = None,
    ) -> "capo_api_gateway.types.domain_names.DomainNames":
        """<p>Represents a collection of DomainName resources.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>
            resource_owner: <p>The owner of the domain name access association. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_domain_names_request.GetDomainNamesRequest]",
        ) -> OperationResponse["capo_api_gateway.types.domain_names.DomainNames"]:
            import capo_api_gateway._operations.backplane_control_service.get_domain_names

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_domain_names.get_domain_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_domain_names_request.GetDomainNamesRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_domain_names(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        resource_owner: Optional[
            "capo_api_gateway.types.resource_owner.ResourceOwner"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.domain_name.DomainName]":
        _token = position
        while True:
            _response = self.get_domain_names(
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
                resource_owner=resource_owner,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_export(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        export_type: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        accepts: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.export_response.ExportResponse":
        """<p>Exports a deployed version of a RestApi in a specified format.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage that will be exported.</p>
            export_type: <p>The type of export. Acceptable values are 'oas30' for OpenAPI 3.0.x and 'swagger' for Swagger/OpenAPI 2.0.</p>
            parameters: <p>A key-value map of query string parameters that specify properties of the export, depending on the requested <code>exportType</code>. For <code>exportType</code> <code>oas30</code> and <code>swagger</code>, any combination of the following parameters are supported: <code>extensions='integrations'</code> or <code>extensions='apigateway'</code> will export the API with x-amazon-apigateway-integration extensions. <code>extensions='authorizers'</code> will export the API with x-amazon-apigateway-authorizer extensions. <code>postman</code> will export the API with Postman extensions, allowing for import to the Postman tool</p>
            accepts: <p>The content-type of the export, for example <code>application/json</code>. Currently <code>application/json</code> and <code>application/yaml</code> are supported for <code>exportType</code> of<code>oas30</code> and <code>swagger</code>. This should be specified in the <code>Accept</code> header for direct API requests.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_export_request.GetExportRequest]",
        ) -> OperationResponse["capo_api_gateway.types.export_response.ExportResponse"]:
            import capo_api_gateway._operations.backplane_control_service.get_export

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_export.get_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_export_request.GetExportRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
            "export_type": export_type,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if accepts is not None:
            input_["accepts"] = accepts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.gateway_response.GatewayResponse":
        """<p>Gets a GatewayResponse of a specified response type on the given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            response_type: <p>The response type of the associated GatewayResponse.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_gateway_response_request.GetGatewayResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.gateway_response.GatewayResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_gateway_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_gateway_response.get_gateway_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_gateway_response_request.GetGatewayResponseRequest = {
            "rest_api_id": rest_api_id,
            "response_type": response_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_responses(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.gateway_responses.GatewayResponses":
        """<p>Gets the GatewayResponses collection on the given RestApi. If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default GatewayResponses collection for the supported response types.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_gateway_responses_request.GetGatewayResponsesRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.gateway_responses.GatewayResponses"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_gateway_responses

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_gateway_responses.get_gateway_responses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_gateway_responses_request.GetGatewayResponsesRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.integration.Integration":
        """<p>Get the integration settings.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a get integration request's resource identifier</p>
            http_method: <p>Specifies a get integration request's HTTP method.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_integration_request.GetIntegrationRequest]",
        ) -> OperationResponse["capo_api_gateway.types.integration.Integration"]:
            import capo_api_gateway._operations.backplane_control_service.get_integration

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_integration_request.GetIntegrationRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.integration_response.IntegrationResponse":
        """<p>Represents a get integration response.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a get integration response request's resource identifier.</p>
            http_method: <p>Specifies a get integration response request's HTTP method.</p>
            status_code: <p>Specifies a get integration response request's status code.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_integration_response_request.GetIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.integration_response.IntegrationResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_integration_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_integration_response.get_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_integration_response_request.GetIntegrationResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_method(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.method.Method":
        """<p>Describe an existing Method resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the Method resource.</p>
            http_method: <p>Specifies the method request's HTTP method type.</p>

        Raises:
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_method_request.GetMethodRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method.Method"]:
            import capo_api_gateway._operations.backplane_control_service.get_method

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_method.get_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_method_request.GetMethodRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_method_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.method_response.MethodResponse":
        """<p>Describes a MethodResponse resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the MethodResponse resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>
            status_code: <p>The status code for the MethodResponse resource.</p>

        Raises:
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_method_response_request.GetMethodResponseRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method_response.MethodResponse"]:
            import capo_api_gateway._operations.backplane_control_service.get_method_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_method_response.get_method_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_method_response_request.GetMethodResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        model_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        flatten: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_api_gateway.types.model.Model":
        """<p>Describes an existing model defined for a RestApi resource.</p>

        Args:
            rest_api_id: <p>The RestApi identifier under which the Model exists.</p>
            model_name: <p>The name of the model as an identifier.</p>
            flatten: <p>A query parameter of a Boolean value to resolve (<code>true</code>) all external model references and returns a flattened model schema or not (<code>false</code>) The default is <code>false</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_model_request.GetModelRequest]",
        ) -> OperationResponse["capo_api_gateway.types.model.Model"]:
            import capo_api_gateway._operations.backplane_control_service.get_model

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_model.get_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_model_request.GetModelRequest = {
            "rest_api_id": rest_api_id,
            "model_name": model_name,
        }
        if flatten is not None:
            input_["flatten"] = flatten

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_models(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.models.Models":
        """<p>Describes existing Models defined for a RestApi resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_models_request.GetModelsRequest]",
        ) -> OperationResponse["capo_api_gateway.types.models.Models"]:
            import capo_api_gateway._operations.backplane_control_service.get_models

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_models.get_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_models_request.GetModelsRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_models(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.model.Model]":
        _token = position
        while True:
            _response = self.get_models(
                rest_api_id,
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_model_template(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        model_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.template.Template":
        """<p>Generates a sample mapping template that can be used to transform a payload into the structure of a model.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            model_name: <p>The name of the model for which to generate a template.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_model_template_request.GetModelTemplateRequest]",
        ) -> OperationResponse["capo_api_gateway.types.template.Template"]:
            import capo_api_gateway._operations.backplane_control_service.get_model_template

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_model_template.get_model_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_model_template_request.GetModelTemplateRequest = {
            "rest_api_id": rest_api_id,
            "model_name": model_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_request_validator(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        request_validator_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.request_validator.RequestValidator":
        """<p>Gets a RequestValidator of a given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            request_validator_id: <p>The identifier of the RequestValidator to be retrieved.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_request_validator_request.GetRequestValidatorRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.request_validator.RequestValidator"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_request_validator

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_request_validator.get_request_validator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_request_validator_request.GetRequestValidatorRequest = {
            "rest_api_id": rest_api_id,
            "request_validator_id": request_validator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_request_validators(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.request_validators.RequestValidators":
        """<p>Gets the RequestValidators collection of a given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_request_validators_request.GetRequestValidatorsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.request_validators.RequestValidators"
        ]:
            import capo_api_gateway._operations.backplane_control_service.get_request_validators

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_request_validators.get_request_validators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_request_validators_request.GetRequestValidatorsRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        embed: Optional["capo_api_gateway.types.list_of_string.ListOfString"] = None,
    ) -> "capo_api_gateway.types.resource.Resource":
        """<p>Lists information about a resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The identifier for the Resource resource.</p>
            embed: <p>A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>"methods"</code> string. For example, <code>GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods</code>.</p>

        Raises:
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_resource_request.GetResourceRequest]",
        ) -> OperationResponse["capo_api_gateway.types.resource.Resource"]:
            import capo_api_gateway._operations.backplane_control_service.get_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_resource.get_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_resource_request.GetResourceRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
        }
        if embed is not None:
            input_["embed"] = embed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resources(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        embed: Optional["capo_api_gateway.types.list_of_string.ListOfString"] = None,
    ) -> "capo_api_gateway.types.resources.Resources":
        """<p>Lists information about a collection of Resource resources.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>
            embed: <p>A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>"methods"</code> string. For example, <code>GET /restapis/{restapi_id}/resources?embed=methods</code>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_resources_request.GetResourcesRequest]",
        ) -> OperationResponse["capo_api_gateway.types.resources.Resources"]:
            import capo_api_gateway._operations.backplane_control_service.get_resources

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_resources.get_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_resources_request.GetResourcesRequest = {
            "rest_api_id": rest_api_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if embed is not None:
            input_["embed"] = embed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_resources(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        embed: Optional["capo_api_gateway.types.list_of_string.ListOfString"] = None,
    ) -> "Iterator[capo_api_gateway.types.resource.Resource]":
        _token = position
        while True:
            _response = self.get_resources(
                rest_api_id,
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
                embed=embed,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_rest_api(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.rest_api.RestApi":
        """<p>Lists the RestApi resource in the collection.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_rest_api_request.GetRestApiRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_api.RestApi"]:
            import capo_api_gateway._operations.backplane_control_service.get_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_rest_api.get_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_rest_api_request.GetRestApiRequest = {
            "rest_api_id": rest_api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rest_apis(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.rest_apis.RestApis":
        """<p>Lists the RestApis resources for your collection.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_rest_apis_request.GetRestApisRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_apis.RestApis"]:
            import capo_api_gateway._operations.backplane_control_service.get_rest_apis

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_rest_apis.get_rest_apis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_rest_apis_request.GetRestApisRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_rest_apis(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.rest_api.RestApi]":
        _token = position
        while True:
            _response = self.get_rest_apis(
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_sdk(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        sdk_type: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.sdk_response.SdkResponse":
        """<p>Generates a client SDK for a RestApi and Stage.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage that the SDK will use.</p>
            sdk_type: <p>The language for the generated SDK. Currently <code>java</code>, <code>javascript</code>, <code>android</code>, <code>objectivec</code> (for iOS), <code>swift</code> (for iOS), and <code>ruby</code> are supported.</p>
            parameters: <p>A string-to-string key-value map of query parameters <code>sdkType</code>-dependent properties of the SDK. For <code>sdkType</code> of <code>objectivec</code> or <code>swift</code>, a parameter named <code>classPrefix</code> is required. For <code>sdkType</code> of <code>android</code>, parameters named <code>groupId</code>, <code>artifactId</code>, <code>artifactVersion</code>, and <code>invokerPackage</code> are required. For <code>sdkType</code> of <code>java</code>, parameters named <code>serviceName</code> and <code>javaPackageName</code> are required. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_sdk_request.GetSdkRequest]",
        ) -> OperationResponse["capo_api_gateway.types.sdk_response.SdkResponse"]:
            import capo_api_gateway._operations.backplane_control_service.get_sdk

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_sdk.get_sdk(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_sdk_request.GetSdkRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
            "sdk_type": sdk_type,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sdk_type(
        self,
        id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.sdk_type.SdkType":
        """<p>Gets an SDK type.</p>

        Args:
            id: <p>The identifier of the queried SdkType instance.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_sdk_type_request.GetSdkTypeRequest]",
        ) -> OperationResponse["capo_api_gateway.types.sdk_type.SdkType"]:
            import capo_api_gateway._operations.backplane_control_service.get_sdk_type

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_sdk_type.get_sdk_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_sdk_type_request.GetSdkTypeRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sdk_types(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.sdk_types.SdkTypes":
        """<p>Gets SDK types</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_sdk_types_request.GetSdkTypesRequest]",
        ) -> OperationResponse["capo_api_gateway.types.sdk_types.SdkTypes"]:
            import capo_api_gateway._operations.backplane_control_service.get_sdk_types

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_sdk_types.get_sdk_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_sdk_types_request.GetSdkTypesRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stage(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.stage.Stage":
        """<p>Gets information about a Stage resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage resource to get information about.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_stage_request.GetStageRequest]",
        ) -> OperationResponse["capo_api_gateway.types.stage.Stage"]:
            import capo_api_gateway._operations.backplane_control_service.get_stage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_stage.get_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_stage_request.GetStageRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stages(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        deployment_id: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.stages.Stages":
        """<p>Gets information about one or more Stage resources.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            deployment_id: <p>The stages' deployment identifiers.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_stages_request.GetStagesRequest]",
        ) -> OperationResponse["capo_api_gateway.types.stages.Stages"]:
            import capo_api_gateway._operations.backplane_control_service.get_stages

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_stages.get_stages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_stages_request.GetStagesRequest = {
            "rest_api_id": rest_api_id
        }
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_tags(
        self,
        resource_arn: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.tags.Tags":
        """<p>Gets the Tags collection for a given resource.</p>

        Args:
            resource_arn: <p>The ARN of a resource that can be tagged.</p>
            position: <p>(Not currently supported) The current pagination position in the paged result set.</p>
            limit: <p>(Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_tags_request.GetTagsRequest]",
        ) -> OperationResponse["capo_api_gateway.types.tags.Tags"]:
            import capo_api_gateway._operations.backplane_control_service.get_tags

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_tags.get_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_tags_request.GetTagsRequest = {
            "resource_arn": resource_arn
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_usage(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        start_date: "capo_api_gateway.types.string.String",
        end_date: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        key_id: Optional["capo_api_gateway.types.string.String"] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.usage.Usage":
        """<p>Gets the usage data of a usage plan in a specified time interval.</p>

        Args:
            usage_plan_id: <p>The Id of the usage plan associated with the usage data.</p>
            key_id: <p>The Id of the API key associated with the resultant usage data.</p>
            start_date: <p>The starting date (e.g., 2016-01-01) of the usage data.</p>
            end_date: <p>The ending date (e.g., 2016-12-31) of the usage data.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_usage_request.GetUsageRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage.Usage"]:
            import capo_api_gateway._operations.backplane_control_service.get_usage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_usage.get_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_usage_request.GetUsageRequest = {
            "usage_plan_id": usage_plan_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        if key_id is not None:
            input_["key_id"] = key_id
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_usage(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        start_date: "capo_api_gateway.types.string.String",
        end_date: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        key_id: Optional["capo_api_gateway.types.string.String"] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[tuple[capo_api_gateway.types.string.String, capo_api_gateway.types.list_of_usage.ListOfUsage]]":
        _token = position
        while True:
            _response = self.get_usage(
                usage_plan_id,
                start_date,
                end_date,
                config_overrides=config_overrides,
                key_id=key_id,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _k, _v in (_page or {}).items():
                yield (_k, _v)
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_usage_plan(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.usage_plan.UsagePlan":
        """<p>Gets a usage plan of a given plan identifier.</p>

        Args:
            usage_plan_id: <p>The identifier of the UsagePlan resource to be retrieved.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_usage_plan_request.GetUsagePlanRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan.UsagePlan"]:
            import capo_api_gateway._operations.backplane_control_service.get_usage_plan

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_usage_plan.get_usage_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_usage_plan_request.GetUsagePlanRequest = {
            "usage_plan_id": usage_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_usage_plan_key(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        key_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.usage_plan_key.UsagePlanKey":
        """<p>Gets a usage plan key of a given key identifier.</p>

        Args:
            usage_plan_id: <p>The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>
            key_id: <p>The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_usage_plan_key_request.GetUsagePlanKeyRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan_key.UsagePlanKey"]:
            import capo_api_gateway._operations.backplane_control_service.get_usage_plan_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_usage_plan_key.get_usage_plan_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_usage_plan_key_request.GetUsagePlanKeyRequest = {
            "usage_plan_id": usage_plan_id,
            "key_id": key_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_usage_plan_keys(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        name_query: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.usage_plan_keys.UsagePlanKeys":
        """<p>Gets all the usage plan keys representing the API keys added to a specified usage plan.</p>

        Args:
            usage_plan_id: <p>The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>
            name_query: <p>A query parameter specifying the name of the to-be-returned usage plan keys.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_usage_plan_keys_request.GetUsagePlanKeysRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan_keys.UsagePlanKeys"]:
            import capo_api_gateway._operations.backplane_control_service.get_usage_plan_keys

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_usage_plan_keys.get_usage_plan_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_usage_plan_keys_request.GetUsagePlanKeysRequest = {
            "usage_plan_id": usage_plan_id
        }
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit
        if name_query is not None:
            input_["name_query"] = name_query

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_usage_plan_keys(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        name_query: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "Iterator[capo_api_gateway.types.usage_plan_key.UsagePlanKey]":
        _token = position
        while True:
            _response = self.get_usage_plan_keys(
                usage_plan_id,
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
                name_query=name_query,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_usage_plans(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        key_id: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.usage_plans.UsagePlans":
        """<p>Gets all the usage plans of the caller's account.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            key_id: <p>The identifier of the API key associated with the usage plans.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_usage_plans_request.GetUsagePlansRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plans.UsagePlans"]:
            import capo_api_gateway._operations.backplane_control_service.get_usage_plans

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_usage_plans.get_usage_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_usage_plans_request.GetUsagePlansRequest = {}
        if position is not None:
            input_["position"] = position
        if key_id is not None:
            input_["key_id"] = key_id
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_usage_plans(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        key_id: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.usage_plan.UsagePlan]":
        _token = position
        while True:
            _response = self.get_usage_plans(
                config_overrides=config_overrides,
                position=_token,
                key_id=key_id,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def get_vpc_link(
        self,
        vpc_link_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> "capo_api_gateway.types.vpc_link.VpcLink":
        """<p>Gets a specified VPC link under the caller's account in a region.</p>

        Args:
            vpc_link_id: <p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_vpc_link_request.GetVpcLinkRequest]",
        ) -> OperationResponse["capo_api_gateway.types.vpc_link.VpcLink"]:
            import capo_api_gateway._operations.backplane_control_service.get_vpc_link

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_vpc_link.get_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_vpc_link_request.GetVpcLinkRequest = {
            "vpc_link_id": vpc_link_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_links(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "capo_api_gateway.types.vpc_links.VpcLinks":
        """<p>Gets the VpcLinks collection under the caller's account in a selected region.</p>

        Args:
            position: <p>The current pagination position in the paged result set.</p>
            limit: <p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.get_vpc_links_request.GetVpcLinksRequest]",
        ) -> OperationResponse["capo_api_gateway.types.vpc_links.VpcLinks"]:
            import capo_api_gateway._operations.backplane_control_service.get_vpc_links

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.get_vpc_links.get_vpc_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.get_vpc_links_request.GetVpcLinksRequest = {}
        if position is not None:
            input_["position"] = position
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_vpc_links(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        position: Optional["capo_api_gateway.types.string.String"] = None,
        limit: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "Iterator[capo_api_gateway.types.vpc_link.VpcLink]":
        _token = position
        while True:
            _response = self.get_vpc_links(
                config_overrides=config_overrides,
                position=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("position",))
            if not _token:
                break

    def import_api_keys(
        self,
        body: "capo_api_gateway.types.blob.Blob",
        format: "capo_api_gateway.types.api_keys_format.ApiKeysFormat",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        fail_on_warnings: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_api_gateway.types.api_key_ids.ApiKeyIds":
        """<p>Import API keys from an external source, such as a CSV-formatted file.</p>

        Args:
            body: <p>The payload of the POST request to import API keys. For the payload format, see API Key File Format.</p>
            format: <p>A query parameter to specify the input format to imported API keys. Currently, only the <code>csv</code> format is supported.</p>
            fail_on_warnings: <p>A query parameter to indicate whether to rollback ApiKey importation (<code>true</code>) or not (<code>false</code>) when error is encountered.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.import_api_keys_request.ImportApiKeysRequest]",
        ) -> OperationResponse["capo_api_gateway.types.api_key_ids.ApiKeyIds"]:
            import capo_api_gateway._operations.backplane_control_service.import_api_keys

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.import_api_keys.import_api_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.import_api_keys_request.ImportApiKeysRequest = {
            "body": body,
            "format": format,
        }
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_documentation_parts(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        body: "capo_api_gateway.types.blob.Blob",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        mode: Optional["capo_api_gateway.types.put_mode.PutMode"] = None,
        fail_on_warnings: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
    ) -> "capo_api_gateway.types.documentation_part_ids.DocumentationPartIds":
        """<p>Imports documentation parts</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            mode: <p>A query parameter to indicate whether to overwrite (<code>overwrite</code>) any existing DocumentationParts definition or to merge (<code>merge</code>) the new definition into the existing one. The default value is <code>merge</code>.</p>
            fail_on_warnings: <p>A query parameter to specify whether to rollback the documentation importation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>
            body: <p>Raw byte array representing the to-be-imported documentation parts. To import from an OpenAPI file, this is a JSON object.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.import_documentation_parts_request.ImportDocumentationPartsRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_part_ids.DocumentationPartIds"
        ]:
            import capo_api_gateway._operations.backplane_control_service.import_documentation_parts

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.import_documentation_parts.import_documentation_parts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.import_documentation_parts_request.ImportDocumentationPartsRequest = {
            "rest_api_id": rest_api_id,
            "body": body,
        }
        if mode is not None:
            input_["mode"] = mode
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_rest_api(
        self,
        body: "capo_api_gateway.types.blob.Blob",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        fail_on_warnings: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.rest_api.RestApi":
        """<p>A feature of the API Gateway control service for creating a new API from an external API definition file.</p>

        Args:
            fail_on_warnings: <p>A query parameter to indicate whether to rollback the API creation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>
            parameters: <p>A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.</p> <p> To exclude DocumentationParts from the import, set <code>parameters</code> as <code>ignore=documentation</code>.</p> <p> To configure the endpoint type, set <code>parameters</code> as <code>endpointConfigurationTypes=EDGE</code>, <code>endpointConfigurationTypes=REGIONAL</code>, or <code>endpointConfigurationTypes=PRIVATE</code>. The default endpoint type is <code>EDGE</code>.</p> <p> To handle imported <code>basepath</code>, set <code>parameters</code> as <code>basepath=ignore</code>, <code>basepath=prepend</code> or <code>basepath=split</code>.</p>
            body: <p>The POST request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.import_rest_api_request.ImportRestApiRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_api.RestApi"]:
            import capo_api_gateway._operations.backplane_control_service.import_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.import_rest_api.import_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.import_rest_api_request.ImportRestApiRequest = {
            "body": body
        }
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_gateway_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        status_code: Optional["capo_api_gateway.types.status_code.StatusCode"] = None,
        response_parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        response_templates: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.gateway_response.GatewayResponse":
        """<p>Creates a customization of a GatewayResponse of a specified response type and status code on the given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            response_type: <p>The response type of the associated GatewayResponse</p>
            status_code: <p>The HTTP status code of the GatewayResponse.</p>
            response_parameters: <p>Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs.</p>
            response_templates: <p>Response templates of the GatewayResponse as a string-to-string map of key-value pairs.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_gateway_response_request.PutGatewayResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.gateway_response.GatewayResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.put_gateway_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_gateway_response.put_gateway_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_gateway_response_request.PutGatewayResponseRequest = {
            "rest_api_id": rest_api_id,
            "response_type": response_type,
        }
        if status_code is not None:
            input_["status_code"] = status_code
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if response_templates is not None:
            input_["response_templates"] = response_templates

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_integration(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        type: "capo_api_gateway.types.integration_type.IntegrationType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        integration_http_method: Optional[
            "capo_api_gateway.types.string.String"
        ] = None,
        uri: Optional["capo_api_gateway.types.string.String"] = None,
        connection_type: Optional[
            "capo_api_gateway.types.connection_type.ConnectionType"
        ] = None,
        connection_id: Optional["capo_api_gateway.types.string.String"] = None,
        credentials: Optional["capo_api_gateway.types.string.String"] = None,
        request_parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        request_templates: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        passthrough_behavior: Optional["capo_api_gateway.types.string.String"] = None,
        cache_namespace: Optional["capo_api_gateway.types.string.String"] = None,
        cache_key_parameters: Optional[
            "capo_api_gateway.types.list_of_string.ListOfString"
        ] = None,
        content_handling: Optional[
            "capo_api_gateway.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        timeout_in_millis: Optional[
            "capo_api_gateway.types.nullable_integer.NullableInteger"
        ] = None,
        tls_config: Optional["capo_api_gateway.types.tls_config.TlsConfig"] = None,
        response_transfer_mode: Optional[
            "capo_api_gateway.types.response_transfer_mode.ResponseTransferMode"
        ] = None,
        integration_target: Optional["capo_api_gateway.types.string.String"] = None,
    ) -> "capo_api_gateway.types.integration.Integration":
        """<p>Sets up a method's integration.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a put integration request's resource ID.</p>
            http_method: <p>Specifies the HTTP method for the integration.</p>
            type: <p>Specifies a put integration input's type.</p>
            integration_http_method: <p>The HTTP method for the integration.</p>
            uri: <p>Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or <code>HTTP_PROXY</code> integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification, for either standard integration, where <code>connectionType</code> is not <code>VPC_LINK</code>, or private integration, where <code>connectionType</code> is <code>VPC_LINK</code>. For a private HTTP integration, the URI is not used for routing. For <code>AWS</code> or <code>AWS_PROXY</code> integrations, the URI is of the form <code>arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api</code>}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated Amazon Web Services service (e.g., s3); and {subdomain} is a designated subdomain supported by certain Amazon Web Services service for fast host-name lookup. action can be used for an Amazon Web Services service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an Amazon Web Services service path-based API. The ensuing service_api refers to the path to an Amazon Web Services service resource, including the region of the integrated Amazon Web Services service, if applicable. For example, for integration with the S3 API of <code>GetObject</code>, the <code>uri</code> can be either <code>arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}</code> or <code>arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}</code>.</p>
            connection_type: <p>The type of the network connection to the integration endpoint. The valid value is <code>INTERNET</code> for connections through the public routable internet or <code>VPC_LINK</code> for private connections between API Gateway and a network load balancer in a VPC. The default value is <code>INTERNET</code>.</p>
            connection_id: <p>The ID of the VpcLink used for the integration. Specify this value only if you specify <code>VPC_LINK</code> as the connection type.</p>
            credentials: <p>Specifies whether credentials are required for a put integration.</p>
            request_parameters: <p>A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of <code>method.request.{location}.{name}</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> must be a valid and unique method request parameter name.</p>
            request_templates: <p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.</p>
            passthrough_behavior: <p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code>requestTemplates</code> property on the Integration resource. There are three valid values: <code>WHEN_NO_MATCH</code>, <code>WHEN_NO_TEMPLATES</code>, and <code>NEVER</code>. </p>
            cache_namespace: <p>Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the <code>cacheNamespace</code>. You can specify the same <code>cacheNamespace</code> across resources to return the same cached data for requests to different resources.</p>
            cache_key_parameters: <p>A list of request parameters whose values API Gateway caches. To be valid values for <code>cacheKeyParameters</code>, these parameters must also be specified for Method <code>requestParameters</code>.</p>
            content_handling: <p>Specifies how to handle request payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:</p> <p>If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the <code>passthroughBehavior</code> is configured to support payload pass-through.</p>
            timeout_in_millis: <p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. You can increase the default value to longer than 29 seconds for Regional or private APIs only.</p>
            response_transfer_mode: <p> The response transfer mode of the integration. </p>
            integration_target: <p> The ALB or NLB listener to send the request to. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_integration_request.PutIntegrationRequest]",
        ) -> OperationResponse["capo_api_gateway.types.integration.Integration"]:
            import capo_api_gateway._operations.backplane_control_service.put_integration

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_integration.put_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_integration_request.PutIntegrationRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "type": type,
        }
        if integration_http_method is not None:
            input_["integration_http_method"] = integration_http_method
        if uri is not None:
            input_["uri"] = uri
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if credentials is not None:
            input_["credentials"] = credentials
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if request_templates is not None:
            input_["request_templates"] = request_templates
        if passthrough_behavior is not None:
            input_["passthrough_behavior"] = passthrough_behavior
        if cache_namespace is not None:
            input_["cache_namespace"] = cache_namespace
        if cache_key_parameters is not None:
            input_["cache_key_parameters"] = cache_key_parameters
        if content_handling is not None:
            input_["content_handling"] = content_handling
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            input_["tls_config"] = tls_config
        if response_transfer_mode is not None:
            input_["response_transfer_mode"] = response_transfer_mode
        if integration_target is not None:
            input_["integration_target"] = integration_target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_integration_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        selection_pattern: Optional["capo_api_gateway.types.string.String"] = None,
        response_parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        response_templates: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        content_handling: Optional[
            "capo_api_gateway.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
    ) -> "capo_api_gateway.types.integration_response.IntegrationResponse":
        """<p>Represents a put integration.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a put integration response request's resource identifier.</p>
            http_method: <p>Specifies a put integration response request's HTTP method.</p>
            status_code: <p>Specifies the status code that is used to map the integration response to an existing MethodResponse.</p>
            selection_pattern: <p>Specifies the selection pattern of a put integration response.</p>
            response_parameters: <p>A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of <code>method.response.header.{name}</code>, where <code>name</code> is a valid and unique header name. The mapped non-static value must match the pattern of <code>integration.response.header.{name}</code> or <code>integration.response.body.{JSON-expression}</code>, where <code>name</code> must be a valid and unique response header name and <code>JSON-expression</code> a valid JSON expression without the <code>$</code> prefix.</p>
            response_templates: <p>Specifies a put integration response's templates.</p>
            content_handling: <p>Specifies how to handle response payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_integration_response_request.PutIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.integration_response.IntegrationResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.put_integration_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_integration_response.put_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_integration_response_request.PutIntegrationResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }
        if selection_pattern is not None:
            input_["selection_pattern"] = selection_pattern
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if response_templates is not None:
            input_["response_templates"] = response_templates
        if content_handling is not None:
            input_["content_handling"] = content_handling

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_method(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        authorization_type: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        authorizer_id: Optional["capo_api_gateway.types.string.String"] = None,
        api_key_required: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        operation_name: Optional["capo_api_gateway.types.string.String"] = None,
        request_parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_boolean.MapOfStringToBoolean"
        ] = None,
        request_models: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        request_validator_id: Optional["capo_api_gateway.types.string.String"] = None,
        authorization_scopes: Optional[
            "capo_api_gateway.types.list_of_string.ListOfString"
        ] = None,
    ) -> "capo_api_gateway.types.method.Method":
        """<p>Add a method to an existing Resource resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the new Method resource.</p>
            http_method: <p>Specifies the method request's HTTP method type.</p>
            authorization_type: <p>The method's authorization type. Valid values are <code>NONE</code> for open access, <code>AWS_IAM</code> for using AWS IAM permissions, <code>CUSTOM</code> for using a custom authorizer, or <code>COGNITO_USER_POOLS</code> for using a Cognito user pool.</p>
            authorizer_id: <p>Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM or COGNITO_USER_POOLS. The authorizer identifier is generated by API Gateway when you created the authorizer.</p>
            api_key_required: <p>Specifies whether the method required a valid ApiKey.</p>
            operation_name: <p>A human-friendly operation identifier for the method. For example, you can assign the <code>operationName</code> of <code>ListPets</code> for the <code>GET /pets</code> method in the <code>PetStore</code> example.</p>
            request_parameters: <p>A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key defines a method request parameter name matching the pattern of <code>method.request.{location}.{name}</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (<code>true</code>) or optional (<code>false</code>). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or body-mapping templates.</p>
            request_models: <p>Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value.</p>
            request_validator_id: <p>The identifier of a RequestValidator for validating the method request.</p>
            authorization_scopes: <p>A list of authorization scopes configured on the method. The scopes are used with a <code>COGNITO_USER_POOLS</code> authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_method_request.PutMethodRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method.Method"]:
            import capo_api_gateway._operations.backplane_control_service.put_method

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_method.put_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_method_request.PutMethodRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "authorization_type": authorization_type,
        }
        if authorizer_id is not None:
            input_["authorizer_id"] = authorizer_id
        if api_key_required is not None:
            input_["api_key_required"] = api_key_required
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if request_models is not None:
            input_["request_models"] = request_models
        if request_validator_id is not None:
            input_["request_validator_id"] = request_validator_id
        if authorization_scopes is not None:
            input_["authorization_scopes"] = authorization_scopes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_method_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        response_parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_boolean.MapOfStringToBoolean"
        ] = None,
        response_models: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.method_response.MethodResponse":
        """<p>Adds a MethodResponse to an existing Method resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the Method resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>
            status_code: <p>The method response's status code.</p>
            response_parameters: <p>A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of <code>method.response.header.{name}</code>, where <code>name</code> is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in <code>integration.response.header.{name}</code>, a static value enclosed within a pair of single quotes (e.g., <code>'application/json'</code>), or a JSON expression from the back-end response payload in the form of <code>integration.response.body.{JSON-expression}</code>, where <code>JSON-expression</code> is a valid JSON expression without the <code>$</code> prefix.)</p>
            response_models: <p>Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_method_response_request.PutMethodResponseRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method_response.MethodResponse"]:
            import capo_api_gateway._operations.backplane_control_service.put_method_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_method_response.put_method_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_method_response_request.PutMethodResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if response_models is not None:
            input_["response_models"] = response_models

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_rest_api(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        body: "capo_api_gateway.types.blob.Blob",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        mode: Optional["capo_api_gateway.types.put_mode.PutMode"] = None,
        fail_on_warnings: Optional["capo_api_gateway.types.boolean.Boolean"] = None,
        parameters: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.rest_api.RestApi":
        """<p>A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            mode: <p>The <code>mode</code> query parameter to specify the update mode. Valid values are "merge" and "overwrite". By default, the update mode is "merge".</p>
            fail_on_warnings: <p>A query parameter to indicate whether to rollback the API update (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>
            parameters: <p>Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set <code>ignore=documentation</code> as a <code>parameters</code> value, as in the AWS CLI command of <code>aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'</code>.</p>
            body: <p>The PUT request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.put_rest_api_request.PutRestApiRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_api.RestApi"]:
            import capo_api_gateway._operations.backplane_control_service.put_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.put_rest_api.put_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.put_rest_api_request.PutRestApiRequest = {
            "rest_api_id": rest_api_id,
            "body": body,
        }
        if mode is not None:
            input_["mode"] = mode
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_domain_name_access_association(
        self,
        domain_name_access_association_arn: "capo_api_gateway.types.string.String",
        domain_name_arn: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Rejects a domain name access association with a private custom domain name.</p> <p>To reject a domain name access association with an access association source in another AWS account, use this operation. To remove a domain name access association with an access association source in your own account, use the DeleteDomainNameAccessAssociation operation.</p>

        Args:
            domain_name_access_association_arn: <p>The ARN of the domain name access association resource. </p>
            domain_name_arn: <p> The ARN of the domain name. </p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.reject_domain_name_access_association_request.RejectDomainNameAccessAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.reject_domain_name_access_association

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.reject_domain_name_access_association.reject_domain_name_access_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.reject_domain_name_access_association_request.RejectDomainNameAccessAssociationRequest = {
            "domain_name_access_association_arn": domain_name_access_association_arn,
            "domain_name_arn": domain_name_arn,
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
        resource_arn: "capo_api_gateway.types.string.String",
        tags: "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Adds or updates a tag on a given resource.</p>

        Args:
            resource_arn: <p>The ARN of a resource that can be tagged.</p>
            tags: <p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.tag_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.tag_resource_request.TagResourceRequest = {
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

    def test_invoke_authorizer(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        authorizer_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        headers: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        multi_value_headers: Optional[
            "capo_api_gateway.types.map_of_string_to_list.MapOfStringToList"
        ] = None,
        path_with_query_string: Optional["capo_api_gateway.types.string.String"] = None,
        body: Optional["capo_api_gateway.types.string.String"] = None,
        stage_variables: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        additional_context: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.test_invoke_authorizer_response.TestInvokeAuthorizerResponse":
        """<p>Simulate the execution of an Authorizer in your RestApi with headers, parameters, and an incoming request body.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            authorizer_id: <p>Specifies a test invoke authorizer request's Authorizer ID.</p>
            headers: <p>A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified.</p>
            multi_value_headers: <p>The headers as a map from string to list of values to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, may be specified.</p>
            path_with_query_string: <p>The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.</p>
            body: <p>The simulated request body of an incoming invocation request.</p>
            stage_variables: <p>A key-value map of stage variables to simulate an invocation on a deployed Stage.</p>
            additional_context: <p>A key-value map of additional context variables.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.test_invoke_authorizer_request.TestInvokeAuthorizerRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.test_invoke_authorizer_response.TestInvokeAuthorizerResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.test_invoke_authorizer

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.test_invoke_authorizer.test_invoke_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.test_invoke_authorizer_request.TestInvokeAuthorizerRequest = {
            "rest_api_id": rest_api_id,
            "authorizer_id": authorizer_id,
        }
        if headers is not None:
            input_["headers"] = headers
        if multi_value_headers is not None:
            input_["multi_value_headers"] = multi_value_headers
        if path_with_query_string is not None:
            input_["path_with_query_string"] = path_with_query_string
        if body is not None:
            input_["body"] = body
        if stage_variables is not None:
            input_["stage_variables"] = stage_variables
        if additional_context is not None:
            input_["additional_context"] = additional_context

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_invoke_method(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        path_with_query_string: Optional["capo_api_gateway.types.string.String"] = None,
        body: Optional["capo_api_gateway.types.string.String"] = None,
        headers: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
        multi_value_headers: Optional[
            "capo_api_gateway.types.map_of_string_to_list.MapOfStringToList"
        ] = None,
        client_certificate_id: Optional["capo_api_gateway.types.string.String"] = None,
        stage_variables: Optional[
            "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
        ] = None,
    ) -> "capo_api_gateway.types.test_invoke_method_response.TestInvokeMethodResponse":
        """<p>Simulate the invocation of a Method in your RestApi with headers, parameters, and an incoming request body.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies a test invoke method request's resource ID.</p>
            http_method: <p>Specifies a test invoke method request's HTTP method.</p>
            path_with_query_string: <p>The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.</p>
            body: <p>The simulated request body of an incoming invocation request.</p>
            headers: <p>A key-value map of headers to simulate an incoming invocation request.</p>
            multi_value_headers: <p>The headers as a map from string to list of values to simulate an incoming invocation request.</p>
            client_certificate_id: <p>A ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint.</p>
            stage_variables: <p>A key-value map of stage variables to simulate an invocation on a deployed Stage.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.test_invoke_method_request.TestInvokeMethodRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.test_invoke_method_response.TestInvokeMethodResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.test_invoke_method

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.test_invoke_method.test_invoke_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.test_invoke_method_request.TestInvokeMethodRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }
        if path_with_query_string is not None:
            input_["path_with_query_string"] = path_with_query_string
        if body is not None:
            input_["body"] = body
        if headers is not None:
            input_["headers"] = headers
        if multi_value_headers is not None:
            input_["multi_value_headers"] = multi_value_headers
        if client_certificate_id is not None:
            input_["client_certificate_id"] = client_certificate_id
        if stage_variables is not None:
            input_["stage_variables"] = stage_variables

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_api_gateway.types.string.String",
        tag_keys: "capo_api_gateway.types.list_of_string.ListOfString",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a given resource.</p>

        Args:
            resource_arn: <p>The ARN of a resource that can be tagged.</p>
            tag_keys: <p>The Tag keys to delete.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_api_gateway._operations.backplane_control_service.untag_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.untag_resource_request.UntagResourceRequest = {
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

    def update_account(
        self,
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.account.Account":
        """<p>Changes information about the current Account resource.</p>

        Args:
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_account_request.UpdateAccountRequest]",
        ) -> OperationResponse["capo_api_gateway.types.account.Account"]:
            import capo_api_gateway._operations.backplane_control_service.update_account

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_account.update_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_account_request.UpdateAccountRequest = {}
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api_key(
        self,
        api_key: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.api_key.ApiKey":
        """<p>Changes information about an ApiKey resource.</p>

        Args:
            api_key: <p>The identifier of the ApiKey resource to be updated.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_api_key_request.UpdateApiKeyRequest]",
        ) -> OperationResponse["capo_api_gateway.types.api_key.ApiKey"]:
            import capo_api_gateway._operations.backplane_control_service.update_api_key

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_api_key.update_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_api_key_request.UpdateApiKeyRequest = {
            "api_key": api_key
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_authorizer(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        authorizer_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.authorizer.Authorizer":
        """<p>Updates an existing Authorizer resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            authorizer_id: <p>The identifier of the Authorizer resource.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_authorizer_request.UpdateAuthorizerRequest]",
        ) -> OperationResponse["capo_api_gateway.types.authorizer.Authorizer"]:
            import capo_api_gateway._operations.backplane_control_service.update_authorizer

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_authorizer.update_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_authorizer_request.UpdateAuthorizerRequest = {
            "rest_api_id": rest_api_id,
            "authorizer_id": authorizer_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_base_path_mapping(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        base_path: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.base_path_mapping.BasePathMapping":
        """<p>Changes information about the BasePathMapping resource.</p>

        Args:
            domain_name: <p>The domain name of the BasePathMapping resource to change.</p>
            domain_name_id: <p> The identifier for the domain name resource. Supported only for private custom domain names. </p>
            base_path: <p>The base path of the BasePathMapping resource to change.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_base_path_mapping_request.UpdateBasePathMappingRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.base_path_mapping.BasePathMapping"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_base_path_mapping

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_base_path_mapping.update_base_path_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_base_path_mapping_request.UpdateBasePathMappingRequest = {
            "domain_name": domain_name,
            "base_path": base_path,
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_client_certificate(
        self,
        client_certificate_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.client_certificate.ClientCertificate":
        """<p>Changes information about an ClientCertificate resource.</p>

        Args:
            client_certificate_id: <p>The identifier of the ClientCertificate resource to be updated.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_client_certificate_request.UpdateClientCertificateRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.client_certificate.ClientCertificate"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_client_certificate

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_client_certificate.update_client_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_client_certificate_request.UpdateClientCertificateRequest = {
            "client_certificate_id": client_certificate_id
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_deployment(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        deployment_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.deployment.Deployment":
        """<p>Changes information about a Deployment resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            deployment_id: <p>The replacement identifier for the Deployment resource to change information about.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is not available. For details see the accompanying error message. Retry after the specified time period.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_deployment_request.UpdateDeploymentRequest]",
        ) -> OperationResponse["capo_api_gateway.types.deployment.Deployment"]:
            import capo_api_gateway._operations.backplane_control_service.update_deployment

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_deployment.update_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_deployment_request.UpdateDeploymentRequest = {
            "rest_api_id": rest_api_id,
            "deployment_id": deployment_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_documentation_part(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_part_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.documentation_part.DocumentationPart":
        """<p>Updates a documentation part.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_part_id: <p>The identifier of the to-be-updated documentation part.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_documentation_part_request.UpdateDocumentationPartRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_part.DocumentationPart"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_documentation_part

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_documentation_part.update_documentation_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_documentation_part_request.UpdateDocumentationPartRequest = {
            "rest_api_id": rest_api_id,
            "documentation_part_id": documentation_part_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_documentation_version(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        documentation_version: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.documentation_version.DocumentationVersion":
        """<p>Updates a documentation version.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            documentation_version: <p>The version identifier of the to-be-updated documentation version.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_documentation_version_request.UpdateDocumentationVersionRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.documentation_version.DocumentationVersion"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_documentation_version

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_documentation_version.update_documentation_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_documentation_version_request.UpdateDocumentationVersionRequest = {
            "rest_api_id": rest_api_id,
            "documentation_version": documentation_version,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain_name(
        self,
        domain_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        domain_name_id: Optional["capo_api_gateway.types.string.String"] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.domain_name.DomainName":
        """<p>Changes information about the DomainName resource.</p>

        Args:
            domain_name: <p>The name of the DomainName resource to be changed.</p>
            domain_name_id: <p> The identifier for the domain name resource. Supported only for private custom domain names. </p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_domain_name_request.UpdateDomainNameRequest]",
        ) -> OperationResponse["capo_api_gateway.types.domain_name.DomainName"]:
            import capo_api_gateway._operations.backplane_control_service.update_domain_name

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_domain_name.update_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_domain_name_request.UpdateDomainNameRequest = {
            "domain_name": domain_name
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.gateway_response.GatewayResponse":
        """<p>Updates a GatewayResponse of a specified response type on the given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            response_type: <p>The response type of the associated GatewayResponse.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_gateway_response_request.UpdateGatewayResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.gateway_response.GatewayResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_gateway_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_gateway_response.update_gateway_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_gateway_response_request.UpdateGatewayResponseRequest = {
            "rest_api_id": rest_api_id,
            "response_type": response_type,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_integration(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.integration.Integration":
        """<p>Represents an update integration.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Represents an update integration request's resource identifier.</p>
            http_method: <p>Represents an update integration request's HTTP method.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_integration_request.UpdateIntegrationRequest]",
        ) -> OperationResponse["capo_api_gateway.types.integration.Integration"]:
            import capo_api_gateway._operations.backplane_control_service.update_integration

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_integration_request.UpdateIntegrationRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_integration_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.integration_response.IntegrationResponse":
        """<p>Represents an update integration response.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>Specifies an update integration response request's resource identifier.</p>
            http_method: <p>Specifies an update integration response request's HTTP method.</p>
            status_code: <p>Specifies an update integration response request's status code.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_integration_response_request.UpdateIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.integration_response.IntegrationResponse"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_integration_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_integration_response.update_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_integration_response_request.UpdateIntegrationResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_method(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.method.Method":
        """<p>Updates an existing Method resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the Method resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_method_request.UpdateMethodRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method.Method"]:
            import capo_api_gateway._operations.backplane_control_service.update_method

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_method.update_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_method_request.UpdateMethodRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_method_response(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        http_method: "capo_api_gateway.types.string.String",
        status_code: "capo_api_gateway.types.status_code.StatusCode",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.method_response.MethodResponse":
        """<p>Updates an existing MethodResponse resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The Resource identifier for the MethodResponse resource.</p>
            http_method: <p>The HTTP verb of the Method resource.</p>
            status_code: <p>The status code for the MethodResponse resource.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_method_response_request.UpdateMethodResponseRequest]",
        ) -> OperationResponse["capo_api_gateway.types.method_response.MethodResponse"]:
            import capo_api_gateway._operations.backplane_control_service.update_method_response

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_method_response.update_method_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_method_response_request.UpdateMethodResponseRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
            "http_method": http_method,
            "status_code": status_code,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_model(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        model_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.model.Model":
        """<p>Changes information about a model. The maximum size of the model is 400 KB.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            model_name: <p>The name of the model to update.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_model_request.UpdateModelRequest]",
        ) -> OperationResponse["capo_api_gateway.types.model.Model"]:
            import capo_api_gateway._operations.backplane_control_service.update_model

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_model.update_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_model_request.UpdateModelRequest = {
            "rest_api_id": rest_api_id,
            "model_name": model_name,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_request_validator(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        request_validator_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.request_validator.RequestValidator":
        """<p>Updates a RequestValidator of a given RestApi.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            request_validator_id: <p>The identifier of RequestValidator to be updated.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_request_validator_request.UpdateRequestValidatorRequest]",
        ) -> OperationResponse[
            "capo_api_gateway.types.request_validator.RequestValidator"
        ]:
            import capo_api_gateway._operations.backplane_control_service.update_request_validator

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_request_validator.update_request_validator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_request_validator_request.UpdateRequestValidatorRequest = {
            "rest_api_id": rest_api_id,
            "request_validator_id": request_validator_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        resource_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.resource.Resource":
        """<p>Changes information about a Resource resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            resource_id: <p>The identifier of the Resource resource.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_resource_request.UpdateResourceRequest]",
        ) -> OperationResponse["capo_api_gateway.types.resource.Resource"]:
            import capo_api_gateway._operations.backplane_control_service.update_resource

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_resource.update_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_resource_request.UpdateResourceRequest = {
            "rest_api_id": rest_api_id,
            "resource_id": resource_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rest_api(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.rest_api.RestApi":
        """<p>Changes information about the specified API.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_rest_api_request.UpdateRestApiRequest]",
        ) -> OperationResponse["capo_api_gateway.types.rest_api.RestApi"]:
            import capo_api_gateway._operations.backplane_control_service.update_rest_api

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_rest_api.update_rest_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_rest_api_request.UpdateRestApiRequest = {
            "rest_api_id": rest_api_id
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stage(
        self,
        rest_api_id: "capo_api_gateway.types.string.String",
        stage_name: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.stage.Stage":
        """<p>Changes information about a Stage resource.</p>

        Args:
            rest_api_id: <p>The string identifier of the associated RestApi.</p>
            stage_name: <p>The name of the Stage resource to change information about.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_stage_request.UpdateStageRequest]",
        ) -> OperationResponse["capo_api_gateway.types.stage.Stage"]:
            import capo_api_gateway._operations.backplane_control_service.update_stage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_stage.update_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_stage_request.UpdateStageRequest = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_usage(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        key_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.usage.Usage":
        """<p>Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.</p>

        Args:
            usage_plan_id: <p>The Id of the usage plan associated with the usage data.</p>
            key_id: <p>The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_usage_request.UpdateUsageRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage.Usage"]:
            import capo_api_gateway._operations.backplane_control_service.update_usage

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_usage.update_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_usage_request.UpdateUsageRequest = {
            "usage_plan_id": usage_plan_id,
            "key_id": key_id,
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_usage_plan(
        self,
        usage_plan_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.usage_plan.UsagePlan":
        """<p>Updates a usage plan of a given plan Id.</p>

        Args:
            usage_plan_id: <p>The Id of the to-be-updated usage plan.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_usage_plan_request.UpdateUsagePlanRequest]",
        ) -> OperationResponse["capo_api_gateway.types.usage_plan.UsagePlan"]:
            import capo_api_gateway._operations.backplane_control_service.update_usage_plan

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_usage_plan.update_usage_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_usage_plan_request.UpdateUsagePlanRequest = {
            "usage_plan_id": usage_plan_id
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_link(
        self,
        vpc_link_id: "capo_api_gateway.types.string.String",
        *,
        config_overrides: Optional[APIGatewayClientConfig] = None,
        patch_operations: Optional[
            "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
        ] = None,
    ) -> "capo_api_gateway.types.vpc_link.VpcLink":
        """<p>Updates an existing VpcLink of a specified identifier.</p>

        Args:
            vpc_link_id: <p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>
            patch_operations: <p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>

        Raises:
            capo_api_gateway.errors.bad_request_exception.BadRequestException: <p>The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_api_gateway.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded the rate limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.not_found_exception.NotFoundException: <p>The requested resource is not found. Make sure that the request URI is correct.</p>
            capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException: <p>The request has reached its throttling limit. Retry after the specified time period.</p>
            capo_api_gateway.errors.unauthorized_exception.UnauthorizedException: <p>The request is denied because the caller has insufficient permissions.</p>
            capo_api_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_api_gateway.types.update_vpc_link_request.UpdateVpcLinkRequest]",
        ) -> OperationResponse["capo_api_gateway.types.vpc_link.VpcLink"]:
            import capo_api_gateway._operations.backplane_control_service.update_vpc_link

            output, http_response = (
                capo_api_gateway._operations.backplane_control_service.update_vpc_link.update_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_api_gateway.types.update_vpc_link_request.UpdateVpcLinkRequest = {
            "vpc_link_id": vpc_link_id
        }
        if patch_operations is not None:
            input_["patch_operations"] = patch_operations

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
